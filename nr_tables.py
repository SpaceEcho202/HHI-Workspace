import matplotlib.pyplot as plt
import numpy.matlib as np
from enum import Enum, auto, IntEnum
import math
class NR_Table(Enum):
    '''
    This class is used to select readable NR table index
    '''
    CQI_TABLE_2 = "Cqi-Table2"
    MCS_TABLE_1 = "Mcs-Table1"
    MCS_TABLE_2 = "Mcs-Table2"
class ModulationOrder(Enum):
    '''
    This class is used to select readable modulation order
    '''
    QPSK    = 4
    QAM_16  = 16
    QAM_64  = 64
    QAM_256 = 256  
class IndexName(Enum):
    '''
    This class is used to assign readable index
    '''
    LEVEL_INDEX      = 0
    MODULATION_ORDER = 1
    CODE_RATE        = 2
class NrParameterForCqiTable2(Enum):
    '''
    This class is used to store NR Parameter for CQI2
    '''
   #LEVEL-----Index---Modulationorder-------Coderate
    LEVEL_01 = (1, ModulationOrder.QPSK,    78/1024) 
    LEVEL_02 = (2, ModulationOrder.QPSK,   193/1024)
    LEVEL_03 = (3, ModulationOrder.QPSK,   449/1024)
    LEVEL_04 = (4, ModulationOrder.QAM_16, 378/1024)
    LEVEL_05 = (5, ModulationOrder.QAM_16, 490/1024)
    LEVEL_06 = (6, ModulationOrder.QAM_16, 616/1024)
    LEVEL_07 = (7, ModulationOrder.QAM_64, 466/1024)
    LEVEL_08 = (8, ModulationOrder.QAM_64, 567/1024)
    LEVEL_09 = (9, ModulationOrder.QAM_64, 666/1024)
    LEVEL_10 = (10,ModulationOrder.QAM_64, 772/1024)
    LEVEL_11 = (11,ModulationOrder.QAM_64, 873/1024)
    LEVEL_12 = (12,ModulationOrder.QAM_256,711/1024)
    LEVEL_13 = (13,ModulationOrder.QAM_256,797/1024)
    LEVEL_14 = (14,ModulationOrder.QAM_256,797/1024)
    LEVEL_15 = (15,ModulationOrder.QAM_256,948/1024)
class NrParameterForMcsTable1(Enum): 
    '''
    This class is used to store NR Parameter for MCS1
    '''
   #LEVEL-----Index---Modulationorder------Coderate
    LEVEL_00 = (0, ModulationOrder.QPSK,  120/1024)
    LEVEL_01 = (1, ModulationOrder.QPSK,  157/1024)
    LEVEL_02 = (2, ModulationOrder.QPSK,  193/1024)
    LEVEL_03 = (3, ModulationOrder.QPSK,  251/1024)
    LEVEL_04 = (4, ModulationOrder.QPSK,  308/1024)
    LEVEL_05 = (5, ModulationOrder.QPSK,  379/1024)
    LEVEL_06 = (6, ModulationOrder.QPSK,  449/1024)
    LEVEL_07 = (7, ModulationOrder.QPSK,  526/1024)
    LEVEL_08 = (8, ModulationOrder.QPSK,  602/1024)
    LEVEL_09 = (9, ModulationOrder.QPSK,  679/1024)
    LEVEL_10 = (10,ModulationOrder.QAM_16,340/1024)
    LEVEL_11 = (11,ModulationOrder.QAM_16,378/1024)
    LEVEL_12 = (12,ModulationOrder.QAM_16,434/1024)
    LEVEL_13 = (13,ModulationOrder.QAM_16,490/1024)
    LEVEL_14 = (14,ModulationOrder.QAM_16,553/1024)
    LEVEL_15 = (15,ModulationOrder.QAM_16,616/1024)
    LEVEL_16 = (16,ModulationOrder.QAM_16,658/1024)
    LEVEL_17 = (17,ModulationOrder.QAM_64,438/1024)
    LEVEL_18 = (18,ModulationOrder.QAM_64,466/1024)
    LEVEL_19 = (19,ModulationOrder.QAM_64,517/1024)
    LEVEL_20 = (20,ModulationOrder.QAM_64,567/1024)
    LEVEL_21 = (21,ModulationOrder.QAM_64,616/1024)
    LEVEL_22 = (22,ModulationOrder.QAM_64,666/1024)
    LEVEL_23 = (23,ModulationOrder.QAM_64,719/1024)
    LEVEL_24 = (24,ModulationOrder.QAM_64,772/1024)
    LEVEL_25 = (25,ModulationOrder.QAM_64,822/1024)
    LEVEL_26 = (26,ModulationOrder.QAM_64,873/1024)
    LEVEL_27 = (27,ModulationOrder.QAM_64,910/1024)
    LEVEL_28 = (28,ModulationOrder.QAM_64,948/1024)
class NrParameterForMcsTable2(Enum):
    '''
    This class is used to store NR Parameter for MCS1
    '''
   #LEVEL-----Index---Modulationorder-------Coderate
    LEVEL_00 = (0, ModulationOrder.QPSK,     120/1024)
    LEVEL_01 = (1, ModulationOrder.QPSK,     193/1024)
    LEVEL_02 = (2, ModulationOrder.QPSK,     308/1024)
    LEVEL_03 = (3, ModulationOrder.QPSK,     449/1024)
    LEVEL_04 = (4, ModulationOrder.QPSK,     602/1024)
    LEVEL_05 = (5, ModulationOrder.QAM_16,   378/1024)
    LEVEL_06 = (6, ModulationOrder.QAM_16,   434/1024)
    LEVEL_07 = (7, ModulationOrder.QAM_16,   490/1024)
    LEVEL_08 = (8, ModulationOrder.QAM_16,   553/1024)
    LEVEL_09 = (9, ModulationOrder.QAM_16,   616/1024)
    LEVEL_10 = (10,ModulationOrder.QAM_16,   658/1024)
    LEVEL_11 = (11,ModulationOrder.QAM_64,   466/1024)
    LEVEL_12 = (12,ModulationOrder.QAM_64,   517/1024)
    LEVEL_13 = (13,ModulationOrder.QAM_64,   567/1024)
    LEVEL_14 = (14,ModulationOrder.QAM_64,   616/1024)
    LEVEL_15 = (15,ModulationOrder.QAM_64,   666/1024)
    LEVEL_16 = (16,ModulationOrder.QAM_64,   719/1024)
    LEVEL_17 = (17,ModulationOrder.QAM_64,   772/1024)
    LEVEL_18 = (18,ModulationOrder.QAM_64,   822/1024)
    LEVEL_19 = (19,ModulationOrder.QAM_64,   873/1024)
    LEVEL_20 = (20,ModulationOrder.QAM_256,682.5/1024)
    LEVEL_21 = (21,ModulationOrder.QAM_256,  711/1024)
    LEVEL_22 = (22,ModulationOrder.QAM_256,  754/1024)
    LEVEL_23 = (23,ModulationOrder.QAM_256,  797/1024)
    LEVEL_24 = (24,ModulationOrder.QAM_256,  841/1024)
    LEVEL_25 = (25,ModulationOrder.QAM_256,  885/1024)
    LEVEL_26 = (26,ModulationOrder.QAM_256,916.5/1024)
    LEVEL_27 = (27,ModulationOrder.QAM_256,  948/1024)

def getStringIndexLevel(DedicatedTable):
    '''
    This 
    '''
    if DedicatedTable is NR_Table.CQI_TABLE_2: return [Level.name for Level in NrParameterForCqiTable2]
    if DedicatedTable is NR_Table.MCS_TABLE_1: return [Level.name for Level in NrParameterForMcsTable1]
    if DedicatedTable is NR_Table.MCS_TABLE_2: return [Level.name for Level in NrParameterForMcsTable2]

def getCodeRate(DedicatedTable):
    if DedicatedTable is NR_Table.CQI_TABLE_2: return [CodeRate.value[IndexName.CODE_RATE.value] for CodeRate in NrParameterForCqiTable2]
    if DedicatedTable is NR_Table.MCS_TABLE_1: return [CodeRate.value[IndexName.CODE_RATE.value] for CodeRate in NrParameterForMcsTable1]
    if DedicatedTable is NR_Table.MCS_TABLE_2: return [CodeRate.value[IndexName.CODE_RATE.value] for CodeRate in NrParameterForMcsTable2]

def getStringModulationOrder(DedicatedTable):
    if  DedicatedTable is NR_Table.CQI_TABLE_2:
        Parameter =  [Parameter.value[IndexName.MODULATION_ORDER.value] for Parameter in NrParameterForCqiTable2]
        return [Modulation.name for Modulation in Parameter]
    if  DedicatedTable is NR_Table.MCS_TABLE_1: 
        Parameter =  [Parameter.value[IndexName.MODULATION_ORDER.value] for Parameter in NrParameterForMcsTable1]
        return [Modulation.name for Modulation in Parameter]
    if  DedicatedTable is NR_Table.MCS_TABLE_2: 
        Parameter =  [Parameter.value[IndexName.MODULATION_ORDER.value] for Parameter in NrParameterForMcsTable2]
        return [Modulation.name for Modulation in Parameter]

def getMinAndMaxLevelIndices(DedicatedTable):
    if DedicatedTable is NR_Table.CQI_TABLE_2: return [NrParameterForCqiTable2.LEVEL_01.value[IndexName.LEVEL_INDEX.value], NrParameterForCqiTable2.LEVEL_15.value[IndexName.LEVEL_INDEX.value]] 
    if DedicatedTable is NR_Table.MCS_TABLE_1: return [NrParameterForMcsTable1.LEVEL_00.value[IndexName.LEVEL_INDEX.value], NrParameterForMcsTable1.LEVEL_28.value[IndexName.LEVEL_INDEX.value]]
    if DedicatedTable is NR_Table.MCS_TABLE_2: return [NrParameterForMcsTable2.LEVEL_00.value[IndexName.LEVEL_INDEX.value], NrParameterForMcsTable2.LEVEL_27.value[IndexName.LEVEL_INDEX.value]]

def getCurveParameterForCqiTable2():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForCqiTable2.LEVEL_01.value[IndexName.CODE_RATE.value]],    
                      [-6.5395, 0.5280, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForCqiTable2.LEVEL_02.value[IndexName.CODE_RATE.value]],  
                      [-5.7642, 0.4753, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForCqiTable2.LEVEL_03.value[IndexName.CODE_RATE.value]],  
                      [-4.6814, 0.4310, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForCqiTable2.LEVEL_04.value[IndexName.CODE_RATE.value]],  
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForCqiTable2.LEVEL_05.value[IndexName.CODE_RATE.value]],  
                      [-2.4033, 0.3888, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForCqiTable2.LEVEL_06.value[IndexName.CODE_RATE.value]],  
                      [-1.7048, 0.3381, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForCqiTable2.LEVEL_07.value[IndexName.CODE_RATE.value]],  
                      [-0.8264, 0.3169, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForCqiTable2.LEVEL_08.value[IndexName.CODE_RATE.value]],  
                      [-0.1311, 0.2991, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForCqiTable2.LEVEL_09.value[IndexName.CODE_RATE.value]],  
                      [ 0.7615, 0.2834, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForCqiTable2.LEVEL_10.value[IndexName.CODE_RATE.value]],  
                      [ 1.4570, 0.2554, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForCqiTable2.LEVEL_11.value[IndexName.CODE_RATE.value]],  
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_256.value) * NrParameterForCqiTable2.LEVEL_12.value[IndexName.CODE_RATE.value]],  
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_256.value) * NrParameterForCqiTable2.LEVEL_13.value[IndexName.CODE_RATE.value]],  
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_256.value) * NrParameterForCqiTable2.LEVEL_14.value[IndexName.CODE_RATE.value]],  
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_256.value) * NrParameterForCqiTable2.LEVEL_15.value[IndexName.CODE_RATE.value]]))
    return curve
    
def getCurveParameterForMcsTable1():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_00.value[IndexName.CODE_RATE.value]],  
                      [-6.5395, 0.5280, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_01.value[IndexName.CODE_RATE.value]],  
                      [-5.7642, 0.4753, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_02.value[IndexName.CODE_RATE.value]],  
                      [-4.6814, 0.4310, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_03.value[IndexName.CODE_RATE.value]],  
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_04.value[IndexName.CODE_RATE.value]],  
                      [-2.4033, 0.3888, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_05.value[IndexName.CODE_RATE.value]],  
                      [-1.7048, 0.3381, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_06.value[IndexName.CODE_RATE.value]],  
                      [-0.8264, 0.3169, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_07.value[IndexName.CODE_RATE.value]],  
                      [-0.1311, 0.2991, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_08.value[IndexName.CODE_RATE.value]],  
                      [ 0.7615, 0.2834, math.log2(ModulationOrder.QPSK.value  ) * NrParameterForMcsTable1.LEVEL_09.value[IndexName.CODE_RATE.value]],  
                      [ 1.4570, 0.2554, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_10.value[IndexName.CODE_RATE.value]],  
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_11.value[IndexName.CODE_RATE.value]],  
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_12.value[IndexName.CODE_RATE.value]],  
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_13.value[IndexName.CODE_RATE.value]],  
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_14.value[IndexName.CODE_RATE.value]],  
                      [ 5.2822, 0.2459, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_15.value[IndexName.CODE_RATE.value]],  
                      [ 5.6121, 0.2710, math.log2(ModulationOrder.QAM_16.value) * NrParameterForMcsTable1.LEVEL_16.value[IndexName.CODE_RATE.value]],  
                      [ 6.4676, 0.2470, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_17.value[IndexName.CODE_RATE.value]],  
                      [ 7.0153, 0.2413, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_18.value[IndexName.CODE_RATE.value]],  
                      [ 7.8056, 0.2244, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_19.value[IndexName.CODE_RATE.value]],  
                      [ 8.5042, 0.2136, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_20.value[IndexName.CODE_RATE.value]],  
                      [ 9.4141, 0.1955, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_21.value[IndexName.CODE_RATE.value]],  
                      [10.0140, 0.1923, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_22.value[IndexName.CODE_RATE.value]],  
                      [10.6933, 0.2222, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_23.value[IndexName.CODE_RATE.value]],  
                      [11.5429, 0.2131, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_24.value[IndexName.CODE_RATE.value]],  
                      [12.2963, 0.1829, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_25.value[IndexName.CODE_RATE.value]],  
                      [12.7529, 0.1979, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_26.value[IndexName.CODE_RATE.value]],  
                      [13.1731, 0.1966, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_27.value[IndexName.CODE_RATE.value]],  
                      [15.3686, 0.1883, math.log2(ModulationOrder.QAM_64.value) * NrParameterForMcsTable1.LEVEL_28.value[IndexName.CODE_RATE.value]])) 
    return curve

def getCurveParameterForMcsTable2():
    curve = np.array(([-7.8269, 0.5938, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForMcsTable2.LEVEL_00.value[IndexName.CODE_RATE.value]],
                      [-5.7977, 0.4928, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForMcsTable2.LEVEL_01.value[IndexName.CODE_RATE.value]],
                      [-3.6457, 0.3797, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForMcsTable2.LEVEL_02.value[IndexName.CODE_RATE.value]],
                      [-1.7048, 0.3380, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForMcsTable2.LEVEL_03.value[IndexName.CODE_RATE.value]],
                      [-0.1310, 0.2990, math.log2(ModulationOrder.QPSK.value   ) * NrParameterForMcsTable2.LEVEL_04.value[IndexName.CODE_RATE.value]],
                      [ 2.1853, 0.2702, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_05.value[IndexName.CODE_RATE.value]],
                      [ 2.8850, 0.2522, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_06.value[IndexName.CODE_RATE.value]],
                      [ 3.6101, 0.2457, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_07.value[IndexName.CODE_RATE.value]],
                      [ 4.5008, 0.2592, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_08.value[IndexName.CODE_RATE.value]],
                      [ 5.2822, 0.2459, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_09.value[IndexName.CODE_RATE.value]],
                      [ 5.6121, 0.2710, math.log2(ModulationOrder.QAM_16.value ) * NrParameterForMcsTable2.LEVEL_10.value[IndexName.CODE_RATE.value]],
                      [ 7.0153, 0.2413, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_11.value[IndexName.CODE_RATE.value]],
                      [ 7.8057, 0.2244, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_12.value[IndexName.CODE_RATE.value]],
                      [ 8.5041, 0.2136, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_13.value[IndexName.CODE_RATE.value]],
                      [ 9.4141, 0.1955, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_14.value[IndexName.CODE_RATE.value]],
                      [10.0140, 0.1923, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_15.value[IndexName.CODE_RATE.value]],
                      [10.6932, 0.2222, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_16.value[IndexName.CODE_RATE.value]],
                      [11.5429, 0.2131, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_17.value[IndexName.CODE_RATE.value]],
                      [12.2963, 0.1830, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_18.value[IndexName.CODE_RATE.value]],
                      [12.7529, 0.1979, math.log2(ModulationOrder.QAM_64.value ) * NrParameterForMcsTable2.LEVEL_19.value[IndexName.CODE_RATE.value]],
                      [14.0043, 0.1826, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_20.value[IndexName.CODE_RATE.value]],
                      [14.8284, 0.1824, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_21.value[IndexName.CODE_RATE.value]],
                      [15.5706, 0.1683, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_22.value[IndexName.CODE_RATE.value]],
                      [15.9361, 0.1720, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_23.value[IndexName.CODE_RATE.value]],
                      [17.0696, 0.1859, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_24.value[IndexName.CODE_RATE.value]],
                      [17.6402, 0.1742, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_25.value[IndexName.CODE_RATE.value]],
                      [18.0284, 0.2569, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_26.value[IndexName.CODE_RATE.value]],
                      [20.8035, 0.1957, math.log2(ModulationOrder.QAM_256.value) * NrParameterForMcsTable2.LEVEL_27.value[IndexName.CODE_RATE.value]]))
    return curve