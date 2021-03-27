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
    SNR = "SNR[dB]"
class AxisIndex(Enum):
    X_VECTOR = 0
    Y_VECTOR = 1
class StyleParameter():
    SnrStart        = -10
    SnrEnd          = 20 
    SnrResolution   = 0.1
    FigSave         = True
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
    Xlim            = None
    FigTitle        = None

def MyPlotFunction(LevelVector ,PlottingData, DedicatedTable, DedicatedPlotType):
    plt.grid(b=True, which='major', color='#666666', linestyle='-') if StyleParameter.MajaorGrid else None
    plt.minorticks_on(), plt.grid(b=True, which='minor',color='#999999', linestyle='-', alpha=0.2) if StyleParameter.MinorGrid else None 

    CsvCreator(LevelVector, PlottingData, DedicatedTable, DedicatedPlotType)
    LabelStringForPlotFunction(LevelVector, DedicatedTable)
    AxisScaleAndTitleCreator(PlottingData, DedicatedPlotType, DedicatedTable)
    
    for levelIndex in range(len(PlottingData[AxisIndex.X_VECTOR.value])):
        plt.plot(PlottingData[AxisIndex.X_VECTOR.value][levelIndex], PlottingData[AxisIndex.Y_VECTOR.value][levelIndex],
        label     = StyleParameter.Label[levelIndex], 
        linestyle = StyleParameter.LineStyle,
        linewidth = StyleParameter.LineWidth)

    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize='x-small', fancybox=True)
    if StyleParameter.FigSave: plt.savefig(str.lower(r"{}_{}".format(DedicatedTable.name, DedicatedPlotType.name)))
    plt.show()

def LabelStringForPlotFunction(LevelVector, DedicatedTable):
    for labelIndex in LevelVector:
        StyleParameter.Label = np.append(StyleParameter.Label, r"{} - {} = {:.2f}".
        format(getStringIndexLevel(DedicatedTable)[labelIndex], 
               getStringModulationOrder(DedicatedTable)[labelIndex],
               getCodeRate(DedicatedTable)[labelIndex]))

def CsvCreator(LevelVector, PlottingData, DedicatedTable, DedicatedPlotType):
    if StyleParameter.CscSave: 
        for (labelIndex, CurveIndex) in zip(LevelVector ,range(len(PlottingData[AxisIndex.Y_VECTOR.value]))):
            CsvTitle = str.lower(r"{}_{}_{}".format(DedicatedTable.name, DedicatedPlotType.name, getStringIndexLevel(DedicatedTable)[labelIndex]))
            CsvHeader = r"SnrInDezibel;{};".format(DedicatedPlotType.name)
            CsvFile = open(CsvTitle+".csv","w")
            CsvFile.write(CsvHeader+"\n")
            for DataIndex in range(len(PlottingData[AxisIndex.X_VECTOR.value][CurveIndex])):
                CsvData = r"{:f};{:f}".format(PlottingData[AxisIndex.X_VECTOR.value][CurveIndex][DataIndex],
                PlottingData[AxisIndex.Y_VECTOR.value][CurveIndex][DataIndex])    
                CsvFile.write(CsvData+"\n")
            CsvFile.close()
                
def AxisScaleAndTitleCreator(PlottingData, DedicatedPlotType, DedicatedTable):
    if DedicatedPlotType is PlotType.BLER: [StyleParameter.YLabel, StyleParameter.Ylim, StyleParameter.YScale] = (r"{}".format(PlotType.BLER.name), (10e-6, 1), 'log')
    if DedicatedPlotType is PlotType.EFFICIENCY: [StyleParameter.YLabel, StyleParameter.Ylim, StyleParameter.YScale] = (r"{}".format(PlotType.EFFICIENCY.value), 
    (0, np.ceil(np.max(PlottingData[AxisIndex.Y_VECTOR.value]))), 'linear')
    StyleParameter.Xlim = (np.min(PlottingData[AxisIndex.X_VECTOR.value]), np.max(PlottingData[AxisIndex.X_VECTOR.value]))
    StyleParameter.Xlabel = r"{}".format(PlotType.SNR.value)
    StyleParameter.FigTitle = r"{}".format(DedicatedTable.name)
    plt.title(StyleParameter.FigTitle), plt.yscale(StyleParameter.YScale), plt.ylim(StyleParameter.Ylim), plt.ylabel(StyleParameter.YLabel)
    plt.xlim(StyleParameter.Xlim), plt.xlabel(StyleParameter.Xlabel)


def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar):
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    MyPlotFunction(LevelVector ,CalculateBler(LevelVector, SnrVector, getCurveParameterForCqiTable2()), NR_Table.CQI_TABLE_2, PlotType.BLER)

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar):
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    MyPlotFunction(LevelVector ,CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable1()), NR_Table.MCS_TABLE_1, PlotType.BLER)

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar):
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    MyPlotFunction(LevelVector, CalculateBler(LevelVector, SnrVector, getCurveParameterForMcsTable2()), NR_Table.MCS_TABLE_2, PlotType.BLER)

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar):
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    MyPlotFunction(LevelVector, CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForCqiTable2()), NR_Table.CQI_TABLE_2, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar):    
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    MyPlotFunction(LevelVector, CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable1()), NR_Table.MCS_TABLE_1, PlotType.EFFICIENCY)

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar):
    [LevelVector, SnrVector] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    MyPlotFunction(LevelVector, CalculateEfficiency(LevelVector, SnrVector, getCurveParameterForMcsTable2()), NR_Table.MCS_TABLE_2, PlotType.EFFICIENCY)

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
    if np.isscalar(SnrVectorOrScalar):
        SnrVector = np.linspace(StyleParameter.SnrStart, SnrVectorOrScalar,
                    int(abs(StyleParameter.SnrStart - SnrVectorOrScalar) /
                    StyleParameter.SnrResolution + 1))
    elif SnrVectorOrScalar == []:
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

PlotBlerforCqiTable2([1, 2, 11, 13], 10)
PlotEfficiencyforMcsTable1([0, 2, 4, 5], [])
