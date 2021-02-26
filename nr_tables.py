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

        getTableCqiB()

        getTableMcsA()

        getTableMcsB()      
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
        MoudulationOrderCqiB = [( 4,  "QPSK", "lvl-0"),    
                                ( 4,  "QPSK", "lvl-1"),    ( 4,  "QPSK", "lvl-2"),
                                (16,  "QAM-16", "lvl-3"),  (16,  "QAM-16", "lvl-4"),   (16,  "QAM-16", "lvl-5"),
                                (64,  "QAM-64", "lvl-6"),  (64,  "QAM-64", "lvl-7"),   (64,  "QAM-64", "lvl-8"),   (64,  "QAM-64", "lvl-9"),  (64, "QAM-64", "lvl-10"),
                                (256, "QAM-256", "lvl-11"),(256, "QAM-256", "lvl-12"), (256, "QAM-256", "lvl-13"), (256, "QAM-256", "lvl-14")]

        MoudulationOrderMcsA = [( 4,  "QPSK", "lvl-1"),    ( 4,  "QPSK", "lvl-2"),     ( 4,  "QPSK", "lvl-3"),     ( 4,  "QPSK", "lvl-4"),   
                                ( 4,  "QPSK", "lvl-5"),    ( 4,  "QPSK", "lvl-6"),     ( 4,  "QPSK", "lvl-7"),     ( 4,  "QPSK", "lvl-8"),     ( 4,  "QPSK", "lvl-9"),   ( 4,  "QPSK", "lvl-10"), 
                                (16,  "QAM-16", "lvl-11"), (16,  "QAM-16", "lvl-12"),  (16,  "QAM-16", "lvl-12"),  (16,  "QAM-16", "lvl-13"),  (16,  "QAM-16", "lvl-14"), 
                                (16,  "QAM-16", "lvl-15"), (16,  "QAM-16", "lvl-16"),  (64,  "QAM-64", "lvl-17"),  (64,  "QAM-64", "lvl-18"),  (64,  "QAM-64", "lvl-19"),
                                (64,  "QAM-64", "lvl-20"),  (64,  "QAM-64", "lvl-20"), (64,  "QAM-64", "lvl-21"), (64,  "QAM-64", "lvl-22"),   (64,  "QAM-64", "lvl-23"), (64,  "QAM-64", "lvl-24"),  
                                (64,  "QAM-64", "lvl-25"),  (64,  "QAM-64", "lvl-26"),  (64,  "QAM-64", "lvl-27")]
                                
        MoudulationOrderMcsB = [( 4,  "QPSK", "lvl-1"),    ( 4,  "QPSK", "lvl-2"),     ( 4,  "QPSK", "lvl-3"),     ( 4,  "QPSK", "lvl-4"),     ( 4,  "QPSK", "lvl-5"), 
                                (16,  "QAM-16", "lvl-6"),  (16,  "QAM-16", "lvl-7"),   (16,  "QAM-16", "lvl-8"),   (16,  "QAM-16", "lvl-9"),   (16,  "QAM-16", "lvl-10"),  (16,  "QAM-16", "lvl-10"),
                                (64,  "QAM-64", "lvl-11"), (64,  "QAM-64", "lvl-12"),  (64,  "QAM-64", "lvl-13"),  (64,  "QAM-64", "lvl-14"),  (64,  "QAM-64", "lvl-15"),  
                                (64,  "QAM-64", "lvl-16"),  (64,  "QAM-64", "lvl-17"),  (64,  "QAM-64", "lvl-18"),  (64,  "QAM-64", "lvl-19"),
                                (256, "QAM-256", "lvl-20"),(256, "QAM-256", "lvl-21"), (256, "QAM-256", "lvl-22"), (256, "QAM-256", "lvl-23"), (256, "QAM-256", "lvl-24"), 
                                (256, "QAM-256", "lvl-25"), (256, "QAM-256", "lvl-26"), (256, "QAM-256", "lvl-27")]                     
        
        if ModulationOrderIn == "MoudulationOrderCqiB":
            ModulationOut = MoudulationOrderCqiB
        elif ModulationOrderIn == "MoudulationOrderMcsA":
            ModulationOut = MoudulationOrderMcsA
        elif ModulationOrderIn == "MoudulationOrderMcsB":
            ModulationOut = MoudulationOrderMcsB
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
        CoderRateCqiB = [78/1024,  193/1024,  449/1024,  
                         378/1024, 490/1024,  616/1024,
                         466/1024, 567/1024,  666/1024, 
                         772/1024, 873/1024,  711/1024, 
                         797/1024, 885/1024,  948/1024]

        CoderRateMcsA = [120/1024, 157/1024, 193/1024, 251/1024,
                         308/1024, 379/1024, 449/1024, 526/1024, 
                         602/1024, 679/1024, 340/1024, 378/1024, 
                         434/1024, 490/1024, 553/1024, 616/1024, 
                         658/1024, 438/1024, 466/1024, 517/1024, 
                         567/1024, 616/1024, 666/1024, 719/1024, 
                         772/1024, 822/1024, 873/1024, 910/1024, 
                         948/1024]

        CoderRateMcsB = [120/1024, 193/1024, 308/1024, 449/1024, 602/1024,
                         378/1024, 434/1024, 490/1024, 553/1024, 616/1024, 
                         658/1024, 466/1024, 517/1024, 567/1024, 616/1024, 
                         666/1024, 719/1024, 772/1024, 822/1024, 873/1024,
                         682.5/1024, 711/1024, 754/1024, 797/1024, 841/1024, 
                         885/1024, 916.5/1024, 948/1024]

        if CoderRateIn == "CoderRateCqiB":
            CodeRateOut = CoderRateCqiB
        elif CoderRateIn == "CoderRateMcsA":
            CodeRateOut = CoderRateMcsA
        elif CoderRateIn == "CoderRateMcsB":
            CodeRateOut = CoderRateMcsB
        else:
            CodeRateOut = []
        return CodeRateOut

    def getTableCqiB(self):
        '''
        This method is used to calculate BLER or Efficiency -> CqiB

        '''
        curve = np.array(([-8.5162,  0.6088, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 0][0])) * self.getCodeRate("CoderRateCqiB")[ 0]],  # lvl  1 
                          [-4.5634,  0.4267, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 1][0])) * self.getCodeRate("CoderRateCqiB")[ 1]],  # lvl  2
                          [-0.1623,  0.3134, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 2][0])) * self.getCodeRate("CoderRateCqiB")[ 2]],  # lvl  3
                          [ 3.6090,  0.2637, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 3][0])) * self.getCodeRate("CoderRateCqiB")[ 3]],  # lvl  4
                          [ 5.3871,  5.3871, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 4][0])) * self.getCodeRate("CoderRateCqiB")[ 4]],  # lvl  5
                          [ 7.3848,  0.1707, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 5][0])) * self.getCodeRate("CoderRateCqiB")[ 5]],  # lvl  6
                          [ 9.1271,  0.1685, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 6][0])) * self.getCodeRate("CoderRateCqiB")[ 6]],  # lvl  7
                          [11.0547,  0.1914, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 7][0])) * self.getCodeRate("CoderRateCqiB")[ 7]],  # lvl  8
                          [12.9193,  0.1699, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 8][0])) * self.getCodeRate("CoderRateCqiB")[ 8]],  # lvl  9
                          [14.9239,  0.1678, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 9][0])) * self.getCodeRate("CoderRateCqiB")[ 9]],  # lvl 10
                          [16.9465,  0.1677, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[10][0])) * self.getCodeRate("CoderRateCqiB")[10]],  # lvl 11
                          [18.4697,  0.1721, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[11][0])) * self.getCodeRate("CoderRateCqiB")[11]],  # lvl 12
                          [20.4287,  0.2035, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[12][0])) * self.getCodeRate("CoderRateCqiB")[12]],  # lvl 13
                          [22.5588,  0.1625, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[13][0])) * self.getCodeRate("CoderRateCqiB")[13]],  # lvl 14
                          [24.5320,  0.1957, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[14][0])) * self.getCodeRate("CoderRateCqiB")[14]]))  # lvl 15
        return curve

    def getTableMcsA(self):
        '''
        This method is used to calculate BLER or Efficiency -> McsA

        '''
        curve = np.array(([-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 0][0])) * self.getCodeRate("CoderRateMcsA")[ 0]],  # lvl  0
                          [-6.5395, 0.5280, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 1][0])) * self.getCodeRate("CoderRateMcsA")[ 1]],  # lvl  1
                          [-5.7642, 0.4753, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 2][0])) * self.getCodeRate("CoderRateMcsA")[ 2]],  # lvl  2
                          [-4.6814, 0.4310, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 3][0])) * self.getCodeRate("CoderRateMcsA")[ 3]],  # lvl  3
                          [-3.6457, 0.3797, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 4][0])) * self.getCodeRate("CoderRateMcsA")[ 4]],  # lvl  4
                          [-2.4033, 0.3888, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 5][0])) * self.getCodeRate("CoderRateMcsA")[ 5]],  # lvl  5
                          [-1.7048, 0.3381, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 6][0])) * self.getCodeRate("CoderRateMcsA")[ 6]],  # lvl  6
                          [-0.8264, 0.3169, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 7][0])) * self.getCodeRate("CoderRateMcsA")[ 7]],  # lvl  7
                          [-0.1311, 0.2991, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 8][0])) * self.getCodeRate("CoderRateMcsA")[ 8]],  # lvl  8
                          [ 0.7615, 0.2834, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 9][0])) * self.getCodeRate("CoderRateMcsA")[ 9]],  # lvl  9
                          [ 1.4570, 0.2554, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[10][0])) * self.getCodeRate("CoderRateMcsA")[10]],  # lvl 10
                          [ 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[11][0])) * self.getCodeRate("CoderRateMcsA")[11]],  # lvl 11
                          [ 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[12][0])) * self.getCodeRate("CoderRateMcsA")[12]],  # lvl 12
                          [ 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[13][0])) * self.getCodeRate("CoderRateMcsA")[13]],  # lvl 13
                          [ 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[14][0])) * self.getCodeRate("CoderRateMcsA")[14]],  # lvl 14
                          [ 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[15][0])) * self.getCodeRate("CoderRateMcsA")[15]],  # lvl 15
                          [ 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[16][0])) * self.getCodeRate("CoderRateMcsA")[16]],  # lvl 16
                          [ 6.4676, 0.2470, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[17][0])) * self.getCodeRate("CoderRateMcsA")[17]],  # lvl 17
                          [ 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[18][0])) * self.getCodeRate("CoderRateMcsA")[18]],  # lvl 18
                          [ 7.8056, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[19][0])) * self.getCodeRate("CoderRateMcsA")[19]],  # lvl 19
                          [ 8.5042, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[20][0])) * self.getCodeRate("CoderRateMcsA")[20]],  # lvl 20
                          [ 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[21][0])) * self.getCodeRate("CoderRateMcsA")[21]],  # lvl 21
                          [10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[22][0])) * self.getCodeRate("CoderRateMcsA")[22]],  # lvl 22
                          [10.6933, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[23][0])) * self.getCodeRate("CoderRateMcsA")[23]],  # lvl 23
                          [11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[24][0])) * self.getCodeRate("CoderRateMcsA")[24]],  # lvl 24
                          [12.2963, 0.1829, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[25][0])) * self.getCodeRate("CoderRateMcsA")[25]],  # lvl 25
                          [12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[26][0])) * self.getCodeRate("CoderRateMcsA")[26]],  # lvl 26
                          [13.1731, 0.1966, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[27][0])) * self.getCodeRate("CoderRateMcsA")[27]],  # lvl 27
                          [15.3686, 0.1883, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[28][0])) * self.getCodeRate("CoderRateMcsA")[28]]))  # lvl 28
        return curve    

    def getTableMcsB(self):
        '''
        This method is used to calculate BLER or Efficiency -> McsB

        '''
        curve = np.array(([-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 0][0])) * self.getCodeRate("CoderRateMcsB")[ 0]],  # lvl  0
                          [-5.7977, 0.4928, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 1][0])) * self.getCodeRate("CoderRateMcsB")[ 1]],  # lvl  2
                          [-3.6457, 0.3797, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 2][0])) * self.getCodeRate("CoderRateMcsB")[ 2]],  # lvl  2
                          [-1.7048, 0.3380, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 3][0])) * self.getCodeRate("CoderRateMcsB")[ 3]],  # lvl  3
                          [-0.1310, 0.2990, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 4][0])) * self.getCodeRate("CoderRateMcsB")[ 4]],  # lvl  4
                          [ 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 5][0])) * self.getCodeRate("CoderRateMcsB")[ 5]],  # lvl  5
                          [ 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 6][0])) * self.getCodeRate("CoderRateMcsB")[ 6]],  # lvl  6
                          [ 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 7][0])) * self.getCodeRate("CoderRateMcsB")[ 7]],  # lvl  7
                          [ 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 8][0])) * self.getCodeRate("CoderRateMcsB")[ 8]],  # lvl  8
                          [ 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 9][0])) * self.getCodeRate("CoderRateMcsB")[ 9]],  # lvl  9
                          [ 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[10][0])) * self.getCodeRate("CoderRateMcsB")[10]],  # lvl 10
                          [ 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[11][0])) * self.getCodeRate("CoderRateMcsB")[11]],  # lvl 11
                          [ 7.8057, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[12][0])) * self.getCodeRate("CoderRateMcsB")[12]],  # lvl 12
                          [ 8.5041, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[13][0])) * self.getCodeRate("CoderRateMcsB")[13]],  # lvl 13
                          [ 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[14][0])) * self.getCodeRate("CoderRateMcsB")[14]],  # lvl 14
                          [10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[15][0])) * self.getCodeRate("CoderRateMcsB")[15]],  # lvl 15
                          [10.6932, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[16][0])) * self.getCodeRate("CoderRateMcsB")[16]],  # lvl 16
                          [11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[17][0])) * self.getCodeRate("CoderRateMcsB")[17]],  # lvl 17
                          [12.2963, 0.1830, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[18][0])) * self.getCodeRate("CoderRateMcsB")[18]],  # lvl 18
                          [12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[19][0])) * self.getCodeRate("CoderRateMcsB")[19]],  # lvl 19
                          [14.0043, 0.1826, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[20][0])) * self.getCodeRate("CoderRateMcsB")[20]],  # lvl 20
                          [14.8284, 0.1824, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[21][0])) * self.getCodeRate("CoderRateMcsB")[21]],  # lvl 21
                          [15.5706, 0.1683, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[22][0])) * self.getCodeRate("CoderRateMcsB")[22]],  # lvl 22
                          [15.9361, 0.1720, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[23][0])) * self.getCodeRate("CoderRateMcsB")[23]],  # lvl 23
                          [17.0696, 0.1859, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[24][0])) * self.getCodeRate("CoderRateMcsB")[24]],  # lvl 24
                          [17.6402, 0.1742, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[25][0])) * self.getCodeRate("CoderRateMcsB")[25]],  # lvl 25
                          [18.0284, 0.2569, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[26][0])) * self.getCodeRate("CoderRateMcsB")[26]],  # lvl 26
                          [20.8035, 0.1957, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[27][0])) * self.getCodeRate("CoderRateMcsB")[27]]))  # lvl 27
        return curve
