from nr_tables import getCurveParameter
from nr_tables import getMinAndMaxLevelIndices
from nr_tables import getStringIndexLevel
from nr_tables import getCodeRate
from nr_tables import NR_Table
import matplotlib.pyplot as plt
from enum import Enum, auto
import scipy.special
import numpy.matlib
import numpy as np
import math
class StyleParameter():
    SnrStart        = -10
    SnrEnd          = 20 
    SnrResolution   = 0.1
    FigSave         = False
    CscSave         = False
    MinorGrid       = True
    MajaorGrid      = True
    LineStyle       = 'solid'
    LineWidth       = 1
    Label           = []
    YScale          = 'linear'

def MyPlotFunction(PlottingData, styleParameter, DedicatedTable):
    plt.grid(b=True, which='major', color='#666666', linestyle='-') if StyleParameter.MajaorGrid else None
    plt.minorticks_on(), plt.grid(b=True, which='minor',color='#999999', linestyle='-', alpha=0.2) if StyleParameter.MinorGrid else None 

    for n in range(len(PlottingData[0])):
        plt.plot(PlottingData[0][n], PlottingData[1][n],
        label     = StyleParameter.Label[n], 
        linestyle = StyleParameter.LineStyle,
        linewidth = StyleParameter.LineWidth)

    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize='x-small', fancybox=True)
    plt.show()

def LabelStringForPlotFunction(LevelVector, DedicatedTable):
    for n in LevelVector:
        StyleParameter.Label = np.append(StyleParameter.Label, r"{} - $R = {:.2f}".
        format(getStringIndexLevel(DedicatedTable)[n], getCodeRate(DedicatedTable)[n]))
    print(StyleParameter.Label)

def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    LabelStringForPlotFunction(LevelVector, NR_Table.CQI_TABLE_2)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), styleParameter, NR_Table.CQI_TABLE_2)

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), styleParameter, NR_Table.MCS_TABLE_1)

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter), styleParameter)

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.CQI_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), styleParameter)

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_1)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), styleParameter)

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar, styleParameter):
    [LevelVector, SnrVector, CurveParameter] = CreateValidDataForPlot(LevelIndex, SnrVectorOrScalar, NR_Table.MCS_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter), styleParameter)

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
    CurveParameter = getCurveParameter(DedicatedTable)
    [MinIndice, MaxIndice] = getMinAndMaxLevelIndices(DedicatedTable)
    [LevelVector, MinLevel, MaxLevel] = LevelVectorCreator(LevelIndex, DedicatedTable)
    if MinLevel < MinIndice or MaxLevel > MaxIndice: raise NotImplementedError("Data not found")
    SnrVector = SnrVectorCreator(SnrVectorOrScalar)
    return [LevelVector, SnrVector, CurveParameter]

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
    ScaleSnr = [((SnrInDecibel)-SnrFactor[i])
                / math.sqrt(2.0) / CodeRateFactor[i] for i in range(len(SnrFactor))]
    return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

def getEfficiency(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    Bler = np.array(
        getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate))
    return [((1.0 - Bler[i]) * MaximumRate[i]) for i in range(len(MaximumRate))]

PlotBlerforCqiTable2([1, 12, 15], [], 0)
