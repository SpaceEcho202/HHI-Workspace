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
    BLER       = "Block Error Rate"
    EFFICIENCY = "Spectral efficiency in [bit's/Hz]"
    SNR        = "SNR[dB]"
class AxisIndex(Enum):
    X_VECTOR = 0
    Y_VECTOR = 1
class StyleParameter():  
    SnrStart        = -10
    SnrEnd          = 20 
    SnrResolution   = 0.1
    FigSave         = True
    CsvSave         = True
    MinorGrid       = True
    MajaorGrid      = True
    LineStyle       = 'solid'
    LineWidth       = 1
    Label           = []
    YScale          = 'linear'
    Ylim            = None
    YLabel          = None
    Xlabel          = None
    Xlim            = None
    FigTitle        = 'generic'     

def MyPlotFunction(DataX, DataY,  *args):
    styleParameter = StyleParameter
    if len(args) == 3: 
        PlottingData = DataX, DataY
        LevelVector, DedicatedTable, DedicatedPlotType = args 
        CsvCreator(LevelVector, PlottingData, DedicatedTable, DedicatedPlotType, styleParameter)
        AxisScaleAndTitleCreator(PlottingData, DedicatedPlotType, DedicatedTable)
        LabelStringForPlotFunction(LevelVector, DedicatedTable)
    else:
        PlottingData = np.matlib.repmat(DataX, 1, 1), np.matlib.repmat(DataY, 1, 1)
        StyleParameter.Label = np.linspace(1, len(PlottingData[0]), len(PlottingData[0]))

    Height, Width, Dpi = GetFigureSize(len(PlottingData[AxisIndex.Y_VECTOR.value]) > 20)
    plt.figure(figsize=(Height, Width), dpi = Dpi)    
    plt.grid(b=True, which='major', color='#666666', linestyle='-') if StyleParameter.MajaorGrid else None
    plt.minorticks_on(), plt.grid(b=True, which='minor',color='#999999', linestyle='-', alpha=0.2) if StyleParameter.MinorGrid else None 
    
    for LevelIndex in range(len(PlottingData[AxisIndex.X_VECTOR.value])):
        plt.plot(PlottingData[AxisIndex.X_VECTOR.value][LevelIndex], 
        PlottingData[AxisIndex.Y_VECTOR.value][LevelIndex],
        label     = StyleParameter.Label[LevelIndex], 
        linestyle = StyleParameter.LineStyle,
        linewidth = StyleParameter.LineWidth)
    
    plt.title(StyleParameter.FigTitle), plt.yscale(StyleParameter.YScale), plt.ylim(StyleParameter.Ylim)
    plt.ylabel(StyleParameter.YLabel), plt.xlim(StyleParameter.Xlim), plt.xlabel(StyleParameter.Xlabel)     
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", fancybox=True)
    plt.subplots_adjust(right=0.7)    
    fig = plt.gcf()
    fig.set_size_inches(17, 8)
    if StyleParameter.FigSave: plt.savefig(str.lower(StyleParameter.FigTitle), bbox_inches = 'tight')
    plt.show()

def LabelStringForPlotFunction(LevelVector, DedicatedTable):
    for LevelIndex in LevelVector:
        StyleParameter.Label = np.append(StyleParameter.Label, r"{} - {} - $R = {:.2f}$".
        format(getStringIndexLevel(DedicatedTable)[LevelIndex], 
               getStringModulationOrder(DedicatedTable)[LevelIndex],
               getCodeRate(DedicatedTable)[LevelIndex]))

def CsvCreator(LevelVector, PlottingData, DedicatedTable, DedicatedPlotType, styleParameter):
    if styleParameter.CsvSave:
        for (LevelIndex, CurveIndex) in zip(LevelVector ,range(len(PlottingData[AxisIndex.Y_VECTOR.value]))):
            CsvHeader = r"SnrInDezibel;{};".format(DedicatedPlotType.name)
            CsvTitle = str.lower(r"{}_{}_{}".format(DedicatedTable.name, 
            DedicatedPlotType.name, getStringIndexLevel(DedicatedTable)[LevelIndex]))
            CsvFile = open(CsvTitle+".csv","w")
            CsvFile.write(CsvHeader+"\n")

            for DataIndex in range(len(PlottingData[AxisIndex.X_VECTOR.value][CurveIndex])):
                CsvData = r"{:f};{:f}".format(PlottingData[AxisIndex.X_VECTOR.value][CurveIndex][DataIndex],
                PlottingData[AxisIndex.Y_VECTOR.value][CurveIndex][DataIndex])    
                CsvFile.write(CsvData+"\n")
            CsvFile.close()
                
def AxisScaleAndTitleCreator(PlottingData, DedicatedPlotType, DedicatedTable):
    if DedicatedPlotType is PlotType.BLER:
        StyleParameter.YLabel, StyleParameter.Ylim, StyleParameter.YScale = (r"{}".format(PlotType.BLER.name), (10e-6, 1), 'log')
    if DedicatedPlotType is PlotType.EFFICIENCY: 
        StyleParameter.YLabel, StyleParameter.Ylim, StyleParameter.YScale = (r"{}".format(PlotType.EFFICIENCY.value), 
        (0, np.ceil(np.max(PlottingData[AxisIndex.Y_VECTOR.value]))), 'linear')

    StyleParameter.Xlabel = r"{}".format(PlotType.SNR.value)
    StyleParameter.Xlim = (np.min(PlottingData[AxisIndex.X_VECTOR.value]), np.max(PlottingData[AxisIndex.X_VECTOR.value]))
    StyleParameter.FigTitle = r"{}_{}".format(DedicatedTable.name, DedicatedPlotType.name)

def GetFigureSize(IsManyCurves):
    Dpi = 96
    Height = 600 / Dpi
    Width = 1100 / Dpi
    if IsManyCurves == True:
         Height = 700 / Dpi
    return Width, Height, Dpi

def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar):
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForCqiTable2())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.CQI_TABLE_2, PlotType.BLER)

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar):
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable1())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.MCS_TABLE_1, PlotType.BLER)

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar):
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    DataX, DataY = CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable2())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.MCS_TABLE_2, PlotType.BLER)

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar):
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForCqiTable2())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.CQI_TABLE_2, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar):    
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable1())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.MCS_TABLE_1, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar):
    LevelVector, SnrVector = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    DataX, DataY = CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable2())
    MyPlotFunction(DataX, DataY, LevelVector ,NR_Table.MCS_TABLE_2, PlotType.EFFICIENCY)

def CalculateEfficiency(LevelVector, SnrVector, CurveParameter):
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for LevelIndex in LevelVector:
        SnrFactor = np.append(SnrFactor, CurveParameter[LevelIndex, 0])
        CodeRate = np.append(CodeRate, CurveParameter[LevelIndex, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[LevelIndex, 2])
    DataY = getEfficiency(SnrVector, CodeRate, SnrFactor, MaximumRate)
    DataX = np.matlib.repmat(SnrVector, len(DataY), 1)
    return DataX, DataY 

def CalculateBler(LevelVector, SnrVector, CurveParameter):
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for LevelIndex in LevelVector:
        SnrFactor = np.append(SnrFactor, CurveParameter[LevelIndex, 0])
        CodeRate = np.append(CodeRate, CurveParameter[LevelIndex, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[LevelIndex, 2])
    DataY = getBler(SnrVector, CodeRate, SnrFactor, MaximumRate)
    DataX = np.matlib.repmat(SnrVector, len(DataY), 1)
    return DataX, DataY

def CreateValidDataForPlot(Level, SnrVectorOrScalar, DedicatedTable):
    MinIndice, MaxIndice = getMinAndMaxLevelIndices(DedicatedTable)
    LevelVector, MinLevel, MaxLevel = LevelVectorCreator(Level, DedicatedTable)
    if MinLevel < MinIndice or MaxLevel > MaxIndice: raise NotImplementedError("Data not found")
    SnrVector = SnrVectorCreator(SnrVectorOrScalar)
    return LevelVector, SnrVector

def SnrVectorCreator(SnrVectorOrScalar):
    if np.isscalar(SnrVectorOrScalar):
        SnrVector = np.linspace(StyleParameter.SnrStart, SnrVectorOrScalar,
                    int(abs(StyleParameter.SnrStart - SnrVectorOrScalar) /
                    StyleParameter.SnrResolution + 1))
    elif len(SnrVectorOrScalar) == 0 :
        SnrVector = np.linspace(StyleParameter.SnrStart, StyleParameter.SnrEnd,
                    int(abs(StyleParameter.SnrStart - StyleParameter.SnrEnd) /
                    StyleParameter.SnrResolution + 1))
    else:
        SnrVector = np.array(SnrVectorOrScalar)
    return SnrVector

def LevelVectorCreator(LevelIndex, DedicatedTable):
    np.array(LevelIndex) if np.isscalar(LevelIndex) else LevelIndex
    LevelIndexMin,LevelIndexMax = np.min(LevelIndex), np.max(LevelIndex)
    if DedicatedTable is NR_Table.CQI_TABLE_2: LevelIndex = np.array(LevelIndex) - 1 
    return LevelIndex.astype(int), LevelIndexMin, LevelIndexMax

def getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    ScaleSnr = [((SnrInDecibel)-SnrFactor[i])/ math.sqrt(2.0) / CodeRateFactor[i] for i in range(len(SnrFactor))]
    return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

def getEfficiency(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    Bler = np.array(getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate))
    return [((1.0 - Bler[i]) * MaximumRate[i]) for i in range(len(MaximumRate))]


PlotBlerforCqiTable2(np.linspace(1,14,14), np.linspace(-10, 10, 100))
PlotEfficiencyforCqiTable2(np.linspace(1,14,14),np.linspace(-10, 10, 100))
PlotEfficiencyforMcsTable1(np.linspace(0,27,28), [])
MyPlotFunction(np.linspace(0,10,11), np.linspace(0,10,11))