from nr_tables import NR_Tables
from nr_tables import getCurveParameterForCqiTable2
from nr_tables import getCurveParameterForMcsTable1
from nr_tables import getCurveParameterForMcsTable2

import matplotlib.pyplot as plt
from enum import Enum, auto
import scipy.special
import numpy.matlib
import numpy as np
import math
class StyleParameter():
    SnrStart = -10
    SnrEnd = 20
    SnrResolution = 0.1
    FigSave = False
    CscSave = False

def MyPlotFunction(PlottingData, StyleParameter):
    for n in range(len(PlottingData[0])):
        plt.plot(PlottingData[0][n], PlottingData[1][n])
    plt.show()

def PlotBlerforCqiTable2(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.CQI_TABLE_2)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter, StyleParameter))

def PlotBlerforMcsTable1(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.MCS_TABLE_1)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter, StyleParameter))

def PlotBlerforMcsTable2(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.MCS_TABLE_2)
    MyPlotFunction(CalculateBler(LevelVector, SnrVector, CurveParameter, StyleParameter))

def PlotEfficiencyforCqiTable2(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.CQI_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter, StyleParameter))

def PlotEfficiencyforMcsTable1(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.MCS_TABLE_1)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter, StyleParameter))

def PlotEfficiencyforMcsTable2(LevelIndex, SnrVectorOrScalar, StyleParameter):
    [LevelVector, SnrVector, CurveParameter] = CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, NR_Tables.MCS_TABLE_2)
    MyPlotFunction(CalculateEfficiency(LevelVector, SnrVector, CurveParameter, StyleParameter))

def getCurveParameter(TableType):
    if TableType is NR_Tables.CQI_TABLE_2: CurveParameter = getCurveParameterForCqiTable2()
    if TableType is NR_Tables.MCS_TABLE_1: CurveParameter = getCurveParameterForMcsTable1()
    if TableType is NR_Tables.MCS_TABLE_2: CurveParameter = getCurveParameterForMcsTable2()
    return CurveParameter

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

def CheckArgumentsForSnrAndLevel(LevelIndex, SnrVectorOrScalar, DedicatedTable):
    LevelVector = LevelVectorCreator(LevelIndex)
    SnrVector = SnrVectorCreator(SnrVectorOrScalar)
    CurveParameter = getCurveParameter(DedicatedTable)
    if np.max(LevelVector) > np.max(getLevelIndex(DedicatedTable)) or np.min(LevelVector) < np.min(getLevelIndex(DedicatedTable)):
         raise NotImplementedError('No data found') 
    return [LevelVector, SnrVector, CurveParameter]

def SnrVectorCreator(SnrVectorOrScalar):
    if np.isscalar(SnrVectorOrScalar) or SnrVectorOrScalar == []:
        SnrVector = np.linspace(StyleParameter.SnrStart, StyleParameter.SnrEnd,
                    int(abs(StyleParameter.SnrStart - StyleParameter.SnrEnd) /
                    StyleParameter.SnrResolution + 1))
    else:
        SnrVector = np.array(SnrVectorOrScalar)
    return SnrVector

def LevelVectorCreator(LevelIndex):
    np.array(LevelIndex) if np.isscalar(LevelIndex) else LevelIndex
    return LevelIndex

def getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    ScaleSnr = [((SnrInDecibel)-SnrFactor[i])
                / math.sqrt(2.0) / CodeRateFactor[i] for i in range(len(SnrFactor))]
    return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

def getEfficiency(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate):
    Bler = np.array(
        getBler(SnrInDecibel, CodeRateFactor, SnrFactor, MaximumRate))
    return [((1.0 - Bler[i]) * MaximumRate[i]) for i in range(len(MaximumRate))]


PlotBlerforCqiTable2([10, 12], [], 0)
