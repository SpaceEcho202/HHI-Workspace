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
    BLER = "Block Error Rate"
    EFFICIENCY = "Spectral efficiency in [bit's/Hz]"
class StyleParameter():
    SnrStart        = -10
    SnrEnd          = 20 
    SnrResolution   = 0.1
    FigSave         = False
    CscSave         = True
    MinorGrid       = True
    MajaorGrid      = True
    LineStyle       = 'solid'
    LineWidth       = 1
    Label           = []
    YScale          = 'linear'
    Ylim            = None
    YLabel          = None
    Xlabel          = None

def MyPlotFunction(PlottingData, DedicatedTable, DedicatedPlotType):
    plt.grid(b=True, which='major', color='#666666', linestyle='-') if StyleParameter.MajaorGrid else None
    plt.minorticks_on(), plt.grid(b=True, which='minor',color='#999999', linestyle='-', alpha=0.2) if StyleParameter.MinorGrid else None 
    print(len(PlottingData[0]))
    for levelIndex in range(len(PlottingData[0])):
        plt.plot(PlottingData[0][levelIndex], PlottingData[1][levelIndex],
        label     = StyleParameter.Label[levelIndex], 
        linestyle = StyleParameter.LineStyle,
        linewidth = StyleParameter.LineWidth)

    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize='x-small', fancybox=True)
    plt.show()

def LabelStringForPlotFunction(LevelVector, DedicatedTable):
    for labelIndex in LevelVector:
        StyleParameter.Label = np.append(StyleParameter.Label, r"{} - {} = {:.2f}".
        format(getStringIndexLevel(DedicatedTable)[labelIndex], 
               getStringModulationOrder(DedicatedTable)[labelIndex],
               getCodeRate(DedicatedTable)[labelIndex]))

def CsvCreator(LevelVector, PlottingData, DedicatedTable, DedicatedPlotType):
    if StyleParameter.CscSave: 
        for labelIndex in LevelVector:
            CsvTitle = str.lower(r"{}_{}_{}".format(DedicatedTable.name, 
            DedicatedPlotType.name, getStringIndexLevel(DedicatedTable)[labelIndex]))
            CsvHeader = r"SnrInDezibel;{};".format(DedicatedPlotType.name)
            f = open(CsvTitle+".csv","w")
            f.write(CsvHeader+"\n")
            for DataIndex in range(len(PlottingData[0][labelIndex])):
                CsvData = r"{:f};{:f}".format(PlottingData[0][labelIndex][DataIndex],
                PlottingData[1][labelIndex][DataIndex])    
                f.write(CsvData+"\n")
        f.close()

                
def AxisScaleAndTitleCreator(DedicatedPlotType, DedicatedTable):
    if DedicatedPlotType is PlotType.BLER: [StyleParameter.YLabel, StyleParameter.Ylim] = r"{}".format(PlotType.BLER), (10e-6, 0)
    if DedicatedPlotType is PlotType.EFFICIENCY: StyleParameter.YLabel = r"{}".format(PlotType.EFFICIENCY.name)
    StyleParameter.Title = r"{}".format(DedicatedTable)

def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForCqiTable2()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    LabelStringForPlotFunction(LevelVector, NR_Table.CQI_TABLE_2)
    CsvCreator(LevelVector ,CalculateBler(LevelVector, SnrVector, CurveParameter), NR_Table.CQI_TABLE_2, PlotType.BLER)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), NR_Table.CQI_TABLE_2, PlotType.BLER)

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForMcsTable1()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    LabelStringForPlotFunction(LevelVector, NR_Table.MCS_TABLE_1)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), NR_Table.MCS_TABLE_1, PlotType.BLER)

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForMcsTable2()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    LabelStringForPlotFunction(LevelVector, NR_Table.MCS_TABLE_2)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), NR_Table.MCS_TABLE_2, PlotType.BLER)

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForCqiTable2()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    LabelStringForPlotFunction(LevelVector, NR_Table.CQI_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), NR_Table.CQI_TABLE_2, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForCqiTable2()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    LabelStringForPlotFunction(LevelVector, NR_Table.MCS_TABLE_1)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), NR_Table.MCS_TABLE_1, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar):
    CurveParameter = getCurveParameterForCqiTable2()
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    LabelStringForPlotFunction(LevelVector, NR_Table.MCS_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), NR_Table.MCS_TABLE_2, PlotType.EFFICIENCY)

def CalculateEfficiency(LevelIndex, SnrVector, CurveParameter):
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for n in LevelIndex:
        SnrFactor = np.append(SnrFactor, CurveParameter[n, 0])
        CodeRate = np.append(CodeRate, CurveParameter[n, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[n, 2])
    DataY = getEfficiency(SnrVector, CodeRate, SnrFactor, MaximumRate)
    return [np.matlib.repmat(SnrVector, len(DataY), 1), DataY] 

def CalculateBler(LevelIndex, SnrVector, CurveParameter):
    SnrFactor, CodeRate, MaximumRate = [], [], []
    for n in LevelIndex:
        SnrFactor = np.append(SnrFactor, CurveParameter[n, 0])
        CodeRate = np.append(CodeRate, CurveParameter[n, 1])
        MaximumRate = np.append(MaximumRate, CurveParameter[n, 2])
    DataY = getBler(SnrVector, CodeRate, SnrFactor, MaximumRate)
    return [np.matlib.repmat(SnrVector, len(DataY), 1), DataY]

def CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, DedicatedTable):
    [MinIndice, MaxIndice] = getMinAndMaxLevelIndices(DedicatedTable)
    [LevelVector, MinLevel, MaxLevel] = LevelVectorCreator(LevelIndex, DedicatedTable)
    if MinLevel < MinIndice or MaxLevel > MaxIndice: raise NotImplementedError("Data not found")
    SnrVector = SnrVectorCreator(SnrVectorOrScalar)
    return [LevelVector, SnrVector]

def SnrVectorCreator(SnrVectorOrScalar):
    if np.isscalar(SnrVectorOrScalar) or SnrVectorOrScalar == []:
        SnrVector = np.linspace(StyleParameter.SnrStart, StyleParameter.SnrEnd,
                    int(abs(StyleParameter.SnrStart - StyleParameter.SnrEnd) /
                    StyleParameter.SnrResolution + 1))
    else:
        SnrVector = np.array(SnrVectorOrScalar)
    return SnrVector

def LevelVectorCreator(LevelIndex, DedicatedTable):
    np.array(LevelIndex) if np.isscalar(LevelIndex) else LevelIndex
    [LevelIndexMin,LevelIndexMax] = [np.min(LevelIndex), np.max(LevelIndex)]
    if DedicatedTable is NR_Table.CQI_TABLE_2: LevelIndex = np.array(LevelIndex) - 1 
    return [LevelIndex, LevelIndexMin, LevelIndexMax]

def getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    ScaleSnr = [((SnrInDecibel)-SnrFactor[i])/ math.sqrt(2.0) / CodeRateFactor[i] for i in range(len(SnrFactor))]
    return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

def getEfficiency(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    Bler = np.array(getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate))
    return [((1.0 - Bler[i]) * MaximumRate[i]) for i in range(len(MaximumRate))]

PlotBlerforCqiTable2([1, 2], [])
