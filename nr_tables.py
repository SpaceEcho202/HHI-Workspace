import matplotlib.pyplot as plt
import numpy.matlib as np
from PlotAwgn import NR_Table
from enum import Enum, auto
import math
class ModulationOrder(Enum):
    QPSK = 4
    QAM_16 = 16
    QAM_64 = 64
    QAM_256 = 256  
class CodeRateForCqiTable2(Enum):
    [LEVEL_01, LEVEL_02, LEVEL_03, LEVEL_04, LEVEL_05,
     LEVEL_06, LEVEL_07, LEVEL_08, LEVEL_09, LEVEL_10,
     LEVEL_11, LEVEL_12, LEVEL_13, LEVEL_14, LEVEL_15
    ] = [ 78/1024, 193/1024, 449/1024, 378/1024,
         490/1024, 616/1024, 466/1024, 567/1024,
         666/1024, 772/1024, 873/1024, 711/1024, 
         797/1024, 885/1024, 948/1024]
class CodeRateForMcsTable1(Enum):
    [LEVEL_00, LEVEL_01, LEVEL_02, LEVEL_03, LEVEL_04,
     LEVEL_05, LEVEL_06, LEVEL_07, LEVEL_08, LEVEL_09,
     LEVEL_10, LEVEL_11, LEVEL_12, LEVEL_13, LEVEL_14,
     LEVEL_15, LEVEL_16, LEVEL_17, LEVEL_18, LEVEL_19,
     LEVEL_20, LEVEL_21, LEVEL_22, LEVEL_23, LEVEL_24,
     LEVEL_25, LEVEL_26, LEVEL_27, LEVEL_28
    ] = [120/1024, 157/1024, 193/1024, 251/1024,
         308/1024, 379/1024, 449/1024, 526/1024, 
         602/1024, 679/1024, 340/1024, 378/1024, 
         434/1024, 490/1024, 553/1024, 616/1024, 
         658/1024, 438/1024, 466/1024, 517/1024, 
         567/1024, 616/1024, 666/1024, 719/1024, 
         772/1024, 822/1024, 873/1024, 910/1024, 
         948/1024]
class CodeRateForMcsTable2(Enum):
    [LEVEL_00, LEVEL_01, LEVEL_02, LEVEL_03, LEVEL_04,
     LEVEL_05, LEVEL_06, LEVEL_07, LEVEL_08, LEVEL_09,
     LEVEL_10, LEVEL_11, LEVEL_12, LEVEL_13, LEVEL_14,
     LEVEL_15, LEVEL_16, LEVEL_17, LEVEL_18, LEVEL_19,
     LEVEL_20, LEVEL_21, LEVEL_22, LEVEL_23, LEVEL_24,
     LEVEL_25, LEVEL_26, LEVEL_27
    ] = [120/1024, 193/1024, 308/1024, 449/1024,
         602/1024, 378/1024, 434/1024, 490/1024, 
         553/1024, 616/1024, 658/1024, 466/1024, 
         517/1024, 567/1024, 616/1024, 666/1024, 
         719/1024, 772/1024, 822/1024, 873/1024,
         682.5/1024, 711/1024, 754/1024, 797/1024, 
         841/1024, 885/1024, 916.5/1024, 948/1024]

def getLevelIndex(TableType):
    if TableType is NR_Table.CQI_TABLE_2: return np.linspace(1,15,15)
    if TableType is NR_Table.MCS_TABLE_1: return np.linspace(0,28,29)
    if TableType is NR_Table.MCS_TABLE_2: return np.linspace(0,27,28)

def getCurveParameterForCqiTable2():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForCqiTable2.LEVEL_01.value],    
                      [-6.5395, 0.5280, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForCqiTable2.LEVEL_02.value],  
                      [-5.7642, 0.4753, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForCqiTable2.LEVEL_03.value],  
                      [-4.6814, 0.4310, math.log2(ModulationOrder.QAM_16.value) * CodeRateForCqiTable2.LEVEL_04.value],  
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QAM_16.value) * CodeRateForCqiTable2.LEVEL_05.value],  
                      [-2.4033, 0.3888, math.log2(ModulationOrder.QAM_16.value) * CodeRateForCqiTable2.LEVEL_06.value],  
                      [-1.7048, 0.3381, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_07.value],  
                      [-0.8264, 0.3169, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_08.value],  
                      [-0.1311, 0.2991, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_09.value],  
                      [ 0.7615, 0.2834, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_10.value],  
                      [ 1.4570, 0.2554, math.log2(ModulationOrder.QAM_16.value) * CodeRateForCqiTable2.LEVEL_11.value],  
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_12.value],  
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_13.value],  
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_14.value],  
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_64.value) * CodeRateForCqiTable2.LEVEL_15.value]))
    return curve
    
def getCurveParameterForMcsTable1():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_00.value],  
                      [-6.5395, 0.5280, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_01.value],  
                      [-5.7642, 0.4753, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_02.value],  
                      [-4.6814, 0.4310, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_03.value],  
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_04.value],  
                      [-2.4033, 0.3888, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_05.value],  
                      [-1.7048, 0.3381, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_06.value],  
                      [-0.8264, 0.3169, math.log2(ModulationOrder.QPSK.value  ) * CodeRateForMcsTable1.LEVEL_07.value],  
                      [-0.1311, 0.2991, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_08.value],  
                      [ 0.7615, 0.2834, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_09.value],  
                      [ 1.4570, 0.2554, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_10.value],  
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_11.value],  
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_12.value],  
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_13.value],  
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_14.value],  
                      [ 5.2822, 0.2459, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_15.value],  
                      [ 5.6121, 0.2710, math.log2(ModulationOrder.QAM_16.value) * CodeRateForMcsTable1.LEVEL_16.value],  
                      [ 6.4676, 0.2470, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_17.value],  
                      [ 7.0153, 0.2413, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_18.value],  
                      [ 7.8056, 0.2244, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_19.value],  
                      [ 8.5042, 0.2136, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_20.value],  
                      [ 9.4141, 0.1955, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_21.value],  
                      [10.0140, 0.1923, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_22.value],  
                      [10.6933, 0.2222, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_23.value],  
                      [11.5429, 0.2131, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_24.value],  
                      [12.2963, 0.1829, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_25.value],  
                      [12.7529, 0.1979, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_26.value],  
                      [13.1731, 0.1966, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_27.value],  
                      [15.3686, 0.1883, math.log2(ModulationOrder.QAM_64.value) * CodeRateForMcsTable1.LEVEL_28.value])) 
    return curve

def getCurveParameterForMcsTable2():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value   ) * CodeRateForMcsTable2.LEVEL_00.value],
                      [-5.7977, 0.4928, math.log2(ModulationOrder.QPSK.value   ) * CodeRateForMcsTable2.LEVEL_01.value],
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QPSK.value   ) * CodeRateForMcsTable2.LEVEL_02.value],
                      [-1.7048, 0.3380, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_03.value],
                      [-0.1310, 0.2990, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_04.value],
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_05.value],
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_06.value],
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_07.value],
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_08.value],
                      [ 5.2822, 0.2459, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_09.value],
                      [ 5.6121, 0.2710, math.log2(ModulationOrder.QAM_16.value ) * CodeRateForMcsTable2.LEVEL_10.value],
                      [ 7.0153, 0.2413, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_11.value],
                      [ 7.8057, 0.2244, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_12.value],
                      [ 8.5041, 0.2136, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_13.value],
                      [ 9.4141, 0.1955, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_14.value],
                      [10.0140, 0.1923, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_15.value],
                      [10.6932, 0.2222, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_16.value],
                      [11.5429, 0.2131, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_17.value],
                      [12.2963, 0.1830, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_18.value],
                      [12.7529, 0.1979, math.log2(ModulationOrder.QAM_64.value ) * CodeRateForMcsTable2.LEVEL_19.value],
                      [14.0043, 0.1826, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_20.value],
                      [14.8284, 0.1824, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_21.value],
                      [15.5706, 0.1683, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_22.value],
                      [15.9361, 0.1720, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_23.value],
                      [17.0696, 0.1859, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_24.value],
                      [17.6402, 0.1742, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_25.value],
                      [18.0284, 0.2569, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_26.value],
                      [20.8035, 0.1957, math.log2(ModulationOrder.QAM_256.value) * CodeRateForMcsTable2.LEVEL_27.value]))
    return curve