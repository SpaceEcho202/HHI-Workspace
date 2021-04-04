from nr_tables import getCurveParameterForCqiTable2
from nr_tables import getCurveParameterForMcsTable1
from nr_tables import getCurveParameterForMcsTable2
from nr_tables import getStringModulationOrder
from nr_tables import getMinAndMaxLevelIndices
from nr_tables import getStringIndexLevel
from nr_tables import getCodeRate
from nr_tables import NR_Table
from enum import Enum, auto

import matplotlib.pyplot as plt
import scipy.special
import numpy.matlib
import numpy as np
import math

class PlotType(Enum):
    '''
    This class is used to provide axis labels 
    '''
    BLER       = "Block Error Rate"
    EFFICIENCY = "Spectral efficiency in [bit's/Hz]"
    SNR        = "SNR[dB]"
class AxisIndex(Enum):
    '''
    This class is used to assign readable indexes
    '''
    X_VECTOR = 0
    Y_VECTOR = 1
class StyleParameter():
    '''
    This class is used for the standard parameterization of the MyPlotFunction. 
    '''
    def __init__(self):
        self.SnrStart        = -10
        self.SnrEnd          = 20 
        self.SnrResolution   = 0.1
        self.FigSave         = True
        self.CsvSave         = True
        self.MinorGrid       = True
        self.MajaorGrid      = True
        self.LineStyle       = 'solid'
        self.LineWidth       = 1
        self.Label           = []
        self.YScale          = 'linear'
        self.Ylim            = None
        self.YLabel          = None
        self.Xlabel          = None
        self.Xlim            = None
        self.FigTitle        = 'generic'     
        self.FigSaveTitle    = 'generic'  

def MyPlotFunction(DataX, DataY, *args):
    '''
    This method is used to generate a plot based on the transferred X & Y vector. 
    In addition, a style parameter object can be transferred, e.g. to insert axis labels.
    When the implemented NR tables and the associated level indexes are transferred, 
    the style parameters are generated automatically 

    Parameter
    ---------
    DataX: float or int

        Pass Vector or Matrix of your dedicated x-axis vector or matrix
    DataY: float or int

        Pass Vector or Matrix of your dedicated y-axis vector or matrix
    args* = {exact description in PlotBlerCqiB etc.}

        All optionally passed arguments are used exclusively for displaying BLER 
        and Efficiency Awgn curves of nr_tables
    '''
    if len(args) > 2 and isinstance(args[2], NR_Table):
        # Will only be executed for NR_Tables
        PlotData = DataX, DataY
        styleParameter, LevelVector, DedicatedTable, DedicatedPlotType = args 
        getPlotLabelsForDedicatedTable(styleParameter, LevelVector, DedicatedTable)
        getCsvFile(styleParameter, LevelVector, PlotData, DedicatedTable, DedicatedPlotType)
        AxisScaleAndTitleCreator(styleParameter, PlotData, DedicatedPlotType, DedicatedTable)
    else:
        # Is used for standard representations
        styleParameter = getStyleParameter(args)
        PlotData = np.matlib.repmat(DataX, 1, 1), np.matlib.repmat(DataY, 1, 1)
        print(len(PlotData[AxisIndex.X_VECTOR.value]))
        styleParameter.Label = str((np.linspace(1, len(PlotData[AxisIndex.Y_VECTOR.value]), 
        len(PlotData[AxisIndex.Y_VECTOR.value])))) if len(styleParameter.Label) == 0 else styleParameter.Label
    
    Height, Width, Dpi = GetFigureSize(len(PlotData[AxisIndex.Y_VECTOR.value]) > 20)
    # Will be used to scale labels and set grid styles
    plt.figure(figsize = (Height, Width), dpi = Dpi)    
    plt.grid(b = True, which = 'major', color = '#666666', linestyle = '-') if styleParameter.MajaorGrid else None
    plt.minorticks_on(), plt.grid(b=True,which='minor',color='#999999',linestyle='-',alpha=0.2) if styleParameter.MinorGrid else None 
    # Used to arange plotdata 
    for LevelIndex in range(len(PlotData[AxisIndex.X_VECTOR.value])):
        plt.plot(PlotData[AxisIndex.X_VECTOR.value][LevelIndex], 
        PlotData[AxisIndex.Y_VECTOR.value][LevelIndex],
        label     = styleParameter.Label[LevelIndex], 
        linestyle = styleParameter.LineStyle,
        linewidth = styleParameter.LineWidth)
    # Set dedicated styleparameter for figure
    plt.title(styleParameter.FigTitle), plt.yscale(styleParameter.YScale), plt.ylim(styleParameter.Ylim)
    plt.ylabel(styleParameter.YLabel), plt.xlim(styleParameter.Xlim), plt.xlabel(styleParameter.Xlabel)     
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", fancybox=True)
    plt.subplots_adjust(right=0.7)    
    fig = plt.gcf()
    fig.set_size_inches(17, 8)
    # Save is located in EXECUTED DIRECTORY
    if styleParameter.FigSave:plt.savefig(styleParameter.FigSaveTitle, bbox_inches = 'tight')
    plt.show()
    styleParameter.Label = []

def getPlotLabelsForDedicatedTable(styleParameter ,LevelVector, DedicatedTable):
    '''
    This method is used to create plot labels based on the selected levels from 
    the desired NR table  e.g. cqi_table2, mcs_table1, .....

    Parameter
    ---------
    styleParameter: object

        Is object of the styleParameter class
    LevelVector: float or int

        Is index for dedicated table e.g. []
    DedicatedTable: class

        Is Enum class to verifiy which table is dedicated e.g NR_Table.CQI_TABLE_2 
    '''
    for LevelIndex in LevelVector:
        styleParameter.Label = np.append(styleParameter.Label, r"{} - {} - $R = {:.2f}$".
        format(getStringIndexLevel(DedicatedTable)[LevelIndex], 
               getStringModulationOrder(DedicatedTable)[LevelIndex],
               getCodeRate(DedicatedTable)[LevelIndex]))

def getCsvFile(styleParameter, LevelVector, PlotData, DedicatedTable, DedicatedPlotType):
    '''
    This method is used to save figure data in a csv file. 

    Parameter
    ---------
    styleParameter: object

        Is object of the styleParameter class
    LevelVector: scalar or vector

        Is level index for dedicated table e.g. []
    PlotData: float matrix

        Is a matrix and contains x-axis and y-axis values for dedicated plot
    DedicatedTable: class

        Is Enum class to verify which table is dedicated e.g NR_Table.CQI_TABLE_2 
    DedicatedPlotType: class

        Is Enum class to verify which Type is dedicated e.g PlotType.BLER or 
        PlotType.EFFICIENCY
    '''
    if styleParameter.CsvSave:
        for (LevelIndex, CurveIndex) in zip(LevelVector ,range(len(PlotData[AxisIndex.Y_VECTOR.value]))):
            CsvHeader = r"SnrInDezibel;{};".format(DedicatedPlotType.name)
            CsvTitle = str.lower(r"{}_{}_{}".format(DedicatedTable.name, 
            DedicatedPlotType.name, getStringIndexLevel(DedicatedTable)[LevelIndex]))
            CsvFile = open(CsvTitle+".csv","w")
            CsvFile.write(CsvHeader+"\n")
            for DataIndex in range(len(PlotData[AxisIndex.X_VECTOR.value][CurveIndex])):
                CsvData = r"{:f};{:f}".format(PlotData[AxisIndex.X_VECTOR.value][CurveIndex][DataIndex],
                PlotData[AxisIndex.Y_VECTOR.value][CurveIndex][DataIndex])    
                CsvFile.write(CsvData+"\n")
            CsvFile.close()
                
def AxisScaleAndTitleCreator(styleParameter ,PlotData, DedicatedPlotType, DedicatedTable):
    '''
    This method is used to create the axis labeling, axis scaling and the figure title 
    
    Parameter
    ---------
    styleParameter: object

        Is object of the styleParameter class
    PlotData: float matrix 

        Is a matrix and contains x-axis and y-axis values for dedicated plot
    DedicatedTable: class

        Is Enum class to verify which table is dedicated e.g NR_Table.CQI_TABLE_2 
    DedicatedPlotType: class

        Is Enum class to verify which Type is dedicated e.g PlotType.BLER or 
        PlotType.EFFICIENCY
    '''
    if DedicatedPlotType is PlotType.BLER:
        styleParameter.YLabel, styleParameter.Ylim, styleParameter.YScale = (r"{}".format(PlotType.BLER.name), (10e-6, 1), 'log')
    if DedicatedPlotType is PlotType.EFFICIENCY: 
        styleParameter.YLabel, styleParameter.Ylim, styleParameter.YScale = (r"{}".format(PlotType.EFFICIENCY.value), 
        (0, np.ceil(np.max(PlotData[AxisIndex.Y_VECTOR.value]))), 'linear')
    styleParameter.Xlabel = r"{}".format(PlotType.SNR.value)
    styleParameter.Xlim = (np.min(PlotData[AxisIndex.X_VECTOR.value]), np.max(PlotData[AxisIndex.X_VECTOR.value]))
    styleParameter.FigTitle = r"{}-{}".format(DedicatedTable.value, DedicatedPlotType.name)
    styleParameter.FigSaveTitle = str.lower(r"{}_{}".format(DedicatedTable.name, DedicatedPlotType.name))

def GetFigureSize(IsManyCurves):
    '''
    This method defines the height, width and dpi

    Parameter
    ---------
    IsMannyCurves: bool

        If the number of plots displayed at the same time exceeds 20,
        the figure will be resized
    '''
    Dpi = 96
    Height = 600 / Dpi
    Width = 1100 / Dpi
    if IsManyCurves == True:
         Height = 700 / Dpi
    return Width, Height, Dpi

def getStyleParameter(DedicatedStyle):
    '''
    This method is used to create an object of the StyleParameter class 
    if it was not passed before. The standard parameters can be taken 
    from the style parameter class 

    Parameter
    ---------
    DedicatedStyle: object
        overridden object of the style parameter class. Contains 
        styleParameters for the desired plot
    '''
    if len(DedicatedStyle) > 0:
        if isinstance(DedicatedStyle[0], StyleParameter):
            styleParameter = DedicatedStyle[0]
    else: styleParameter = StyleParameter()
    return styleParameter

def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar, *args):
    '''
    This method is used to generate a plot of the block error rate in the range of the desired SNR's 
    for NR table Cqi2

    Parameter
    ---------
    LevelIndex: int

        Is index for dedicated table e.g. 0 or np.linspace(0,3,4)
    SnrVectorOrScalar: float or int

        If a scalar is passed, it is used as the end value of the Snr vector. 
        For more information see getSnrVector
    args: StyleParameter object

        see description getStyleParameter

    '''
    styleParameter = getStyleParameter(args)
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForCqiTable2())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.CQI_TABLE_2, PlotType.BLER)

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar, *args):
    '''
    This method is used to generate a BLER plot in the range of the desired SNR's for dedicated levels in
    NR table MCS1
    
    Parameter
    ---------
    See description PlotBlerForCqiTable2
    '''
    styleParameter = getStyleParameter(args)
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable1())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.MCS_TABLE_1, PlotType.BLER)

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar, *args):
    '''
    This method is used to generate a BLER plot in the range of the desired SNR's for dedicated levels in
    NR table MCS2

    Parameter
    ---------
    See description PlotBlerForCqiTable2
    '''
    styleParameter = getStyleParameter(args)
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable2())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.MCS_TABLE_2, PlotType.BLER)

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar, *args):
    '''
    This method is used to generate a efficiency plot in the range of the desired SNR's for dedicated levels in
    NR table CQI2

    Parameter
    ---------
    See description PlotBlerForCqiTable2
    '''
    styleParameter = getStyleParameter(args)
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForCqiTable2())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.CQI_TABLE_2, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar, *args):   
    '''
    This method is used to generate a efficiency plot in the range of the desired SNR's for dedicated levels in
    NR table MCS1

    Parameter
    ---------
    See description PlotBlerForCqiTable2
    '''
    styleParameter = getStyleParameter(args) 
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable1())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.MCS_TABLE_1, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar, *args):
    '''
    This method is used to generate a efficiency plot in the range of the desired SNR's for dedicated levels in 
    NR table MCS2

    Parameter
    ---------
    See description PlotBlerForCqiTable2
    '''
    styleParameter = getStyleParameter(args) 
    LevelVector, SnrVector = CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable2())
    MyPlotFunction(DataX, DataY, styleParameter, LevelVector ,NR_Table.MCS_TABLE_2, PlotType.EFFICIENCY)

def CalculateEfficiency(LevelVector, SnrVector, CurveParameter):
    '''
    This method is used to calculate the efficiency of the NR tables. 

    Parameter
    ---------
    LevelVector: int

        Is a vector with the desired levels of the used NR table
    SnrVector: float or int

        Is a vector with the disired SNR values for efficiency calculation 
    '''
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for LevelIndex in LevelVector:
        SnrFactor = np.append(SnrFactor, CurveParameter[LevelIndex, 0])
        CodeRate = np.append(CodeRate, CurveParameter[LevelIndex, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[LevelIndex, 2])
    DataY = getEfficiency(SnrVector, CodeRate, SnrFactor, MaximumRate)
    DataX = np.matlib.repmat(SnrVector, len(DataY), 1)
    return DataX, DataY 

def CalculateBler(LevelVector, SnrVector, CurveParameter):
    '''
    This method is used to calculate the BLER of the NR tables. 

    Parameter
    ---------
    LevelVector: int

        Is a vector with the desired levels of the used NR table
    SnrVector: float or int

        Is a vector with the disired SNR values for BLER calculation 
    '''
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for LevelIndex in LevelVector:
        SnrFactor = np.append(SnrFactor, CurveParameter[LevelIndex, 0])
        CodeRate = np.append(CodeRate, CurveParameter[LevelIndex, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[LevelIndex, 2])
    DataY = getBler(SnrVector, CodeRate, SnrFactor, MaximumRate)
    DataX = np.matlib.repmat(SnrVector, len(DataY), 1)
    return DataX, DataY

def CreateValidDataForPlot(styleParameter, LevelIndex, SnrVectorOrScalar, DedicatedTable):
    '''
    This method checks if the passed levels and SNR values are correct
    to create plot data & labels 

    styleParameter: object

        Is object of the styleParameter class
    LevelVector: int

        Is a vector with the desired levels of the used NR table
    SnrVector: float or int

        Is a vector with the disired SNR values for BLER calculatio
    DedicatedTable: class

        Is Enum class to verify which table is dedicated e.g NR_Table.CQI_TABLE_2 
    '''
    MinIndice, MaxIndice = getMinAndMaxLevelIndices(DedicatedTable)
    LevelVector, MinLevel, MaxLevel = LevelVectorCreator(LevelIndex, DedicatedTable)
    if MinLevel < MinIndice or MaxLevel > MaxIndice: raise NotImplementedError("Data not found")
    SnrVector = getSnrVector(styleParameter, SnrVectorOrScalar)
    return LevelVector, SnrVector

def getSnrVector(styleParameter ,SnrVectorOrScalar):
    '''
    This method generates an SNR vector. If a scalar is passed, the vector is generated 
    based on the styleParameter, the scalar serves as the end value. The SNR resolution is 
    defined in the Styleparameter.

    Parameter
    ---------
    styleParameter: object 

        Is object of the styleParameter class
    SnrVectorOrScalar: float or int

        Is a scalar or vector for dedicated SNR values
    '''
    if np.isscalar(SnrVectorOrScalar):
        SnrVector = np.linspace(styleParameter.SnrStart, SnrVectorOrScalar,
                    int(abs(styleParameter.SnrStart - SnrVectorOrScalar) /
                    styleParameter.SnrResolution + 1))
    elif len(SnrVectorOrScalar) == 0 :
        SnrVector = np.linspace(styleParameter.SnrStart, styleParameter.SnrEnd,
                    int(abs(styleParameter.SnrStart - styleParameter.SnrEnd) /
                    styleParameter.SnrResolution + 1))
    else:
        SnrVector = np.array(SnrVectorOrScalar)
    return SnrVector

def LevelVectorCreator(LevelIndex, DedicatedTable):
    '''
    This method creates an index vector. If a scalar is passed, it is also built up as an array 

    Parameter 
    ---------

    LevelIndex: int

        Is index for dedicated table e.g. 0 or np.linspace(0,3,4)
    DedicatedTable: class

        Is Enum class to verify which table is dedicated e.g NR_Table.CQI_TABLE_2
    '''
    LevelIndex = np.array(LevelIndex)
    LevelIndexMin,LevelIndexMax = np.min(LevelIndex), np.max(LevelIndex)
    if DedicatedTable is NR_Table.CQI_TABLE_2: LevelIndex = np.array(LevelIndex) - 1 
    return LevelIndex.astype(int), LevelIndexMin, LevelIndexMax

def getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    '''
    This method is used for fast BLER  calculation 

    Parameters
    ----------
    SnrFactor : float or int

    Vector or Scalar //if Scalar is passed calculates only dedicated value
        CodeRateFactor : float or int

    Vector or Scalar //if Scalar is passed calculates only dedicated value // has to be positive
        MaximumRate : float or int

        dictionary or empty //if Scalar is passed calculates only dedicated value // has to be larger then zero

    '''
    ScaleSnr = [((SnrInDecibel)-SnrFactor[i])/ math.sqrt(2.0) / CodeRateFactor[i] for i in range(len(SnrFactor))]
    return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

def getEfficiency(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    '''
    This method is used for fast Efficiency calculation 

    Parameters
    ----------
    see getBler
    '''
    Bler = np.array(getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate))
    return [((1.0 - Bler[i]) * MaximumRate[i]) for i in range(len(MaximumRate))]

 
#Example override some parameter if you like so
FigOption1           = StyleParameter()
FigOption1.LineStyle = 'solid'
FigOption1.CsvSave   = True
FigOption1.FigSave   = True
#Call methods to create plots for your dedicated NR table 
PlotBlerforCqiTable2([1, 2 ,10], np.linspace(-10,20,100))
PlotEfficiencyforCqiTable2(np.linspace(1,15,15), np.linspace(-10,20,100))
PlotBlerforMcsTable1([0, 2 ,15], np.linspace(-10,20,100))
PlotEfficiencyforMcsTable1(np.linspace(0,28,29), np.linspace(-10,20,100))
PlotBlerforMcsTable2(np.linspace(0,27,28), np.linspace(-10,20,100))
PlotEfficiencyforMcsTable2(np.linspace(0,27,28), np.linspace(-10,20,100))

FigOption2 = StyleParameter()
FigOption2.Label = ['Test_1', 'Test_2']

A = [[1,2,3,4],[1,2,3,4]]
B = [[1,2,3,4],[1,2,3,4]]
MyPlotFunction(A, B, FigOption2)