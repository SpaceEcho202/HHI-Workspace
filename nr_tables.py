import matplotlib.pyplot as plt
import numpy as np
import math

class Tables:
    '''
    A class to store all table data
    ...

    Methods
    -------
        getModulationOrder(ModulationOrderIn: string)

        getCodeRate(CoderRateIn: string)

        getTableCQI_2()

        getTableMCS_1()

        getTableMCS_2()      
    '''
    def getModulationOrder(self, ModulationOrderIn):
        '''
        This method returns a dedicated modulation order & level
        
        ...

        Parameters
        ----------
        ModulationOrderIn: string

        pass string to get dedicated modulation order & level 

        '''
        MoudulationOrderCQI_2 = [( 4,  "QPSK", "level_1"),    
                                ( 4,  "QPSK", "level_2"),    ( 4,  "QPSK", "level_3"),
                                (16,  "QAM-16", "level_4"),  (16,  "QAM-16", "level_5"),   (16,  "QAM-16", "level_6"),
                                (64,  "QAM-64", "level_7"),  (64,  "QAM-64", "level_8"),   (64,  "QAM-64", "level_9"),   (64,  "QAM-64", "level_10"),  (64, "QAM-64", "level_11"),
                                (256, "QAM-256", "level_12"),(256, "QAM-256", "level_13"), (256, "QAM-256", "level_14"), (256, "QAM-256", "level_15")]

        MoudulationOrderMCS_1 = [( 4,  "QPSK", "level_0"),    ( 4,  "QPSK", "level_1"),     ( 4,  "QPSK", "level_2"),     ( 4,  "QPSK", "level_3"),   
                                ( 4,  "QPSK", "level_4"),    ( 4,  "QPSK", "level_5"),     ( 4,  "QPSK", "level_6"),     ( 4,  "QPSK", "level_7"),     ( 4,  "QPSK", "level_8"),   ( 4,  "QPSK", "level_9"), 
                                (16,  "QAM-16", "level_10"), (16,  "QAM-16", "level_11"),  (16,  "QAM-16", "level_12"),  (16,  "QAM-16", "level_13"),  (16,  "QAM-16", "level_14"), 
                                (16,  "QAM-16", "level_15"), (16,  "QAM-16", "level_16"),  (64,  "QAM-64", "level_17"),  (64,  "QAM-64", "level_18"),  (64,  "QAM-64", "level_19"),
                                (64,  "QAM-64", "level_20"),  (64,  "QAM-64", "level_21"), (64,  "QAM-64", "level_22"), (64,  "QAM-64", "level_23"),   (64,  "QAM-64", "level_24"), (64,  "QAM-64", "level_25"),  
                                (64,  "QAM-64", "level_26"),  (64,  "QAM-64", "level_27"),  (64,  "QAM-64", "level_28")]
                                
        MoudulationOrderMCS_2 = [( 4,  "QPSK", "level_0"),    ( 4,  "QPSK", "level_1"),     ( 4,  "QPSK", "level_2"),     ( 4,  "QPSK", "level_3"),     ( 4,  "QPSK", "level_4"), 
                                (16,  "QAM-16", "level_5"),  (16,  "QAM-16", "level_6"),   (16,  "QAM-16", "level_7"),   (16,  "QAM-16", "level_8"),   (16,  "QAM-16", "level_9"),  (16,  "QAM-16", "level_10"),
                                (64,  "QAM-64", "level_11"), (64,  "QAM-64", "level_12"),  (64,  "QAM-64", "level_13"),  (64,  "QAM-64", "level_14"),  (64,  "QAM-64", "level_15"),  
                                (64,  "QAM-64", "level_16"),  (64,  "QAM-64", "level_17"),  (64,  "QAM-64", "level_18"),  (64,  "QAM-64", "level_19"),
                                (256, "QAM-256", "level_20"),(256, "QAM-256", "level_21"), (256, "QAM-256", "level_22"), (256, "QAM-256", "level_23"), (256, "QAM-256", "level_24"), 
                                (256, "QAM-256", "level_25"), (256, "QAM-256", "level_26"), (256, "QAM-256", "level_27")]                     
        
        if ModulationOrderIn == "MoudulationOrderCQI_2":
            ModulationOut = MoudulationOrderCQI_2
        elif ModulationOrderIn == "MoudulationOrderMCS_1":
            ModulationOut = MoudulationOrderMCS_1
        elif ModulationOrderIn == "MoudulationOrderMCS_2":
            ModulationOut = MoudulationOrderMCS_2
        else:
            ModulationOut = []
        return ModulationOut

    def getCodeRate(self, CoderRateIn):
        '''
        This method returns a dedicated coderate
        ...

        Parameters
        ----------
        ModulationOrderIn: string

        pass string to get dedicated coderate

        '''
        CoderRateCQI_2 = [78/1024,  193/1024,  449/1024,  
                         378/1024, 490/1024,  616/1024,
                         466/1024, 567/1024,  666/1024, 
                         772/1024, 873/1024,  711/1024, 
                         797/1024, 885/1024,  948/1024]

        CoderRateMCS_1 = [120/1024, 157/1024, 193/1024, 251/1024,
                         308/1024, 379/1024, 449/1024, 526/1024, 
                         602/1024, 679/1024, 340/1024, 378/1024, 
                         434/1024, 490/1024, 553/1024, 616/1024, 
                         658/1024, 438/1024, 466/1024, 517/1024, 
                         567/1024, 616/1024, 666/1024, 719/1024, 
                         772/1024, 822/1024, 873/1024, 910/1024, 
                         948/1024]

        CoderRateMCS_2 = [120/1024, 193/1024, 308/1024, 449/1024, 602/1024,
                         378/1024, 434/1024, 490/1024, 553/1024, 616/1024, 
                         658/1024, 466/1024, 517/1024, 567/1024, 616/1024, 
                         666/1024, 719/1024, 772/1024, 822/1024, 873/1024,
                         682.5/1024, 711/1024, 754/1024, 797/1024, 841/1024, 
                         885/1024, 916.5/1024, 948/1024]

        if CoderRateIn == "CoderRateCQI_2":
            CodeRateOut = CoderRateCQI_2
        elif CoderRateIn == "CoderRateMCS_1":
            CodeRateOut = CoderRateMCS_1
        elif CoderRateIn == "CoderRateMCS_2":
            CodeRateOut = CoderRateMCS_2
        else:
            CodeRateOut = []
        return CodeRateOut

    def getTableCQI_2(self):
        '''
        This method is used to calculate BLER or Efficiency -> CQI_2

        '''
        curve = np.array(([-8.5162,  0.6088, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 0][0])) * self.getCodeRate("CoderRateCQI_2")[ 0]],  # level  1 
                          [-4.5634,  0.4267, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 1][0])) * self.getCodeRate("CoderRateCQI_2")[ 1]],  # level  2
                          [-0.1623,  0.3134, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 2][0])) * self.getCodeRate("CoderRateCQI_2")[ 2]],  # level  3
                          [ 3.6090,  0.2637, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 3][0])) * self.getCodeRate("CoderRateCQI_2")[ 3]],  # level  4
                          [ 5.3871,  0.2319, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 4][0])) * self.getCodeRate("CoderRateCQI_2")[ 4]],  # level  5
                          [ 7.3848,  0.1707, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 5][0])) * self.getCodeRate("CoderRateCQI_2")[ 5]],  # level  6
                          [ 9.1271,  0.1685, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 6][0])) * self.getCodeRate("CoderRateCQI_2")[ 6]],  # level  7
                          [11.0547,  0.1914, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 7][0])) * self.getCodeRate("CoderRateCQI_2")[ 7]],  # level  8
                          [12.9193,  0.1699, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 8][0])) * self.getCodeRate("CoderRateCQI_2")[ 8]],  # level  9
                          [14.9239,  0.1678, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[ 9][0])) * self.getCodeRate("CoderRateCQI_2")[ 9]],  # level 10
                          [16.9465,  0.1677, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[10][0])) * self.getCodeRate("CoderRateCQI_2")[10]],  # level 11
                          [18.4697,  0.1721, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[11][0])) * self.getCodeRate("CoderRateCQI_2")[11]],  # level 12
                          [20.4287,  0.2035, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[12][0])) * self.getCodeRate("CoderRateCQI_2")[12]],  # level 13
                          [22.5588,  0.1625, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[13][0])) * self.getCodeRate("CoderRateCQI_2")[13]],  # level 14
                          [24.5320,  0.1957, math.log2((self.getModulationOrder("MoudulationOrderCQI_2")[14][0])) * self.getCodeRate("CoderRateCQI_2")[14]]))  # level 15
        return curve

    def getTableMCS_1(self):
        '''
        This method is used to calculate BLER or Efficiency -> MCS_1

        '''
        curve = np.array(([-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 0][0])) * self.getCodeRate("CoderRateMCS_1")[ 0]],  # level  0
                          [-6.5395, 0.5280, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 1][0])) * self.getCodeRate("CoderRateMCS_1")[ 1]],  # level  1
                          [-5.7642, 0.4753, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 2][0])) * self.getCodeRate("CoderRateMCS_1")[ 2]],  # level  2
                          [-4.6814, 0.4310, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 3][0])) * self.getCodeRate("CoderRateMCS_1")[ 3]],  # level  3
                          [-3.6457, 0.3797, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 4][0])) * self.getCodeRate("CoderRateMCS_1")[ 4]],  # level  4
                          [-2.4033, 0.3888, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 5][0])) * self.getCodeRate("CoderRateMCS_1")[ 5]],  # level  5
                          [-1.7048, 0.3381, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 6][0])) * self.getCodeRate("CoderRateMCS_1")[ 6]],  # level  6
                          [-0.8264, 0.3169, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 7][0])) * self.getCodeRate("CoderRateMCS_1")[ 7]],  # level  7
                          [-0.1311, 0.2991, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 8][0])) * self.getCodeRate("CoderRateMCS_1")[ 8]],  # level  8
                          [ 0.7615, 0.2834, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[ 9][0])) * self.getCodeRate("CoderRateMCS_1")[ 9]],  # level  9
                          [ 1.4570, 0.2554, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[10][0])) * self.getCodeRate("CoderRateMCS_1")[10]],  # level 10
                          [ 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[11][0])) * self.getCodeRate("CoderRateMCS_1")[11]],  # level 11
                          [ 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[12][0])) * self.getCodeRate("CoderRateMCS_1")[12]],  # level 12
                          [ 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[13][0])) * self.getCodeRate("CoderRateMCS_1")[13]],  # level 13
                          [ 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[14][0])) * self.getCodeRate("CoderRateMCS_1")[14]],  # level 14
                          [ 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[15][0])) * self.getCodeRate("CoderRateMCS_1")[15]],  # level 15
                          [ 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[16][0])) * self.getCodeRate("CoderRateMCS_1")[16]],  # level 16
                          [ 6.4676, 0.2470, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[17][0])) * self.getCodeRate("CoderRateMCS_1")[17]],  # level 17
                          [ 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[18][0])) * self.getCodeRate("CoderRateMCS_1")[18]],  # level 18
                          [ 7.8056, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[19][0])) * self.getCodeRate("CoderRateMCS_1")[19]],  # level 19
                          [ 8.5042, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[20][0])) * self.getCodeRate("CoderRateMCS_1")[20]],  # level 20
                          [ 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[21][0])) * self.getCodeRate("CoderRateMCS_1")[21]],  # level 21
                          [10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[22][0])) * self.getCodeRate("CoderRateMCS_1")[22]],  # level 22
                          [10.6933, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[23][0])) * self.getCodeRate("CoderRateMCS_1")[23]],  # level 23
                          [11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[24][0])) * self.getCodeRate("CoderRateMCS_1")[24]],  # level 24
                          [12.2963, 0.1829, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[25][0])) * self.getCodeRate("CoderRateMCS_1")[25]],  # level 25
                          [12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[26][0])) * self.getCodeRate("CoderRateMCS_1")[26]],  # level 26
                          [13.1731, 0.1966, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[27][0])) * self.getCodeRate("CoderRateMCS_1")[27]],  # level 27
                          [15.3686, 0.1883, math.log2((self.getModulationOrder("MoudulationOrderMCS_1")[28][0])) * self.getCodeRate("CoderRateMCS_1")[28]]))  # level 28
        return curve    

    def getTableMCS_2(self):
        '''
        This method is used to calculate BLER or Efficiency -> MCS_2

        '''
        curve = np.array(([-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 0][0])) * self.getCodeRate("CoderRateMCS_2")[ 0]],  # level  0
                          [-5.7977, 0.4928, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 1][0])) * self.getCodeRate("CoderRateMCS_2")[ 1]],  # level  2
                          [-3.6457, 0.3797, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 2][0])) * self.getCodeRate("CoderRateMCS_2")[ 2]],  # level  2
                          [-1.7048, 0.3380, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 3][0])) * self.getCodeRate("CoderRateMCS_2")[ 3]],  # level  3
                          [-0.1310, 0.2990, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 4][0])) * self.getCodeRate("CoderRateMCS_2")[ 4]],  # level  4
                          [ 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 5][0])) * self.getCodeRate("CoderRateMCS_2")[ 5]],  # level  5
                          [ 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 6][0])) * self.getCodeRate("CoderRateMCS_2")[ 6]],  # level  6
                          [ 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 7][0])) * self.getCodeRate("CoderRateMCS_2")[ 7]],  # level  7
                          [ 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 8][0])) * self.getCodeRate("CoderRateMCS_2")[ 8]],  # level  8
                          [ 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[ 9][0])) * self.getCodeRate("CoderRateMCS_2")[ 9]],  # level  9
                          [ 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[10][0])) * self.getCodeRate("CoderRateMCS_2")[10]],  # level 10
                          [ 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[11][0])) * self.getCodeRate("CoderRateMCS_2")[11]],  # level 11
                          [ 7.8057, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[12][0])) * self.getCodeRate("CoderRateMCS_2")[12]],  # level 12
                          [ 8.5041, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[13][0])) * self.getCodeRate("CoderRateMCS_2")[13]],  # level 13
                          [ 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[14][0])) * self.getCodeRate("CoderRateMCS_2")[14]],  # level 14
                          [10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[15][0])) * self.getCodeRate("CoderRateMCS_2")[15]],  # level 15
                          [10.6932, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[16][0])) * self.getCodeRate("CoderRateMCS_2")[16]],  # level 16
                          [11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[17][0])) * self.getCodeRate("CoderRateMCS_2")[17]],  # level 17
                          [12.2963, 0.1830, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[18][0])) * self.getCodeRate("CoderRateMCS_2")[18]],  # level 18
                          [12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[19][0])) * self.getCodeRate("CoderRateMCS_2")[19]],  # level 19
                          [14.0043, 0.1826, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[20][0])) * self.getCodeRate("CoderRateMCS_2")[20]],  # level 20
                          [14.8284, 0.1824, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[21][0])) * self.getCodeRate("CoderRateMCS_2")[21]],  # level 21
                          [15.5706, 0.1683, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[22][0])) * self.getCodeRate("CoderRateMCS_2")[22]],  # level 22
                          [15.9361, 0.1720, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[23][0])) * self.getCodeRate("CoderRateMCS_2")[23]],  # level 23
                          [17.0696, 0.1859, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[24][0])) * self.getCodeRate("CoderRateMCS_2")[24]],  # level 24
                          [17.6402, 0.1742, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[25][0])) * self.getCodeRate("CoderRateMCS_2")[25]],  # level 25
                          [18.0284, 0.2569, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[26][0])) * self.getCodeRate("CoderRateMCS_2")[26]],  # level 26
                          [20.8035, 0.1957, math.log2((self.getModulationOrder("MoudulationOrderMCS_2")[27][0])) * self.getCodeRate("CoderRateMCS_2")[27]]))  # level 27
        return curve
