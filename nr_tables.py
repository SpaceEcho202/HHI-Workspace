import matplotlib.pyplot as plt
import numpy as np
import math

class Tables:

    def getModulationOrder(self, ModulationOrderIn):
        MoudulationOrderCqiB = [4,    4,   4,
                                16,  16,  16,
                                64,  64,  64,  64, 64,
                                256, 256, 256, 256]
        MoudulationOrderMcsA = [4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
                                16, 16, 16, 16, 16, 16, 16,
                                64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64]
        MoudulationOrderMcsB = [4,   4,   4,   4,   4,
                                16,  16,  16,  16,  16,  16,
                                64,  64,  64,  64,  64,  64,  64,  64,  64,
                                256, 256, 256, 256, 256, 256, 256, 256]
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
        CoderRateCiqA = [4,  4,  4,  4,  4,  4,
                             16, 16, 16,
                             64, 64, 64, 64, 64, 64]
        CoderRateMcsA = [4,  4,  4,  4,  4,  4,  4,  4,  4,  4,
                             16, 16, 16, 16, 16, 16, 16,
                             64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64]
        CoderRateMcsB = [4,   4,   4,   4,   4,
                             16,  16,  16,  16,  16,  16,
                             64,  64,  64,  64,  64,  64,  64,  64,  64,
                             256, 256, 256, 256, 256, 256, 256, 256]
        if CoderRateIn == "CoderRateCiqA":
            CodeRateOut = CoderRateCiqA
        elif CoderRateIn == "CoderRateMcsA":
            CodeRateOut = CoderRateMcsA
        elif CoderRateIn == "CoderRateMcsB":
            CodeRateOut = CoderRateMcsB
        else:
            CodeRateOut = []
        return CodeRateOut

    def getTableCqiB(self):
        curve = [(-8.5162,  0.6088, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 0])) * self.getCodeRate("CoderRateCiqA")[ 0]),  # level  1 
                 (-4.5634,  0.4267, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 1])) * self.getCodeRate("CoderRateCiqA")[ 1]),  # level  2
                 (-0.1623,  0.3134, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 2])) * self.getCodeRate("CoderRateCiqA")[ 2]),  # level  3
                 ( 3.6090,  0.2637, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 3])) * self.getCodeRate("CoderRateCiqA")[ 3]),  # level  4
                 ( 5.3871,  5.3871, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 4])) * self.getCodeRate("CoderRateCiqA")[ 4]),  # level  5
                 ( 7.3848,  0.1707, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 5])) * self.getCodeRate("CoderRateCiqA")[ 5]),  # level  6
                 ( 9.1271,  0.1685, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 6])) * self.getCodeRate("CoderRateCiqA")[ 6]),  # level  7
                 (11.0547,  0.1914, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 7])) * self.getCodeRate("CoderRateCiqA")[ 7]),  # level  8
                 (12.9193,  0.1699, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 8])) * self.getCodeRate("CoderRateCiqA")[ 8]),  # level  9
                 (14.9239,  0.1678, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[ 9])) * self.getCodeRate("CoderRateCiqA")[ 9]),  # level 10
                 (16.9465,  0.1677, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[10])) * self.getCodeRate("CoderRateCiqA")[10]),  # level 11
                 (18.4697,  0.1721, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[11])) * self.getCodeRate("CoderRateCiqA")[11]),  # level 12
                 (20.4287,  0.2035, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[12])) * self.getCodeRate("CoderRateCiqA")[12]),  # level 13
                 (22.5588,  0.1625, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[13])) * self.getCodeRate("CoderRateCiqA")[13]),  # level 14
                 (24.5320,  0.1957, math.log2((self.getModulationOrder("MoudulationOrderCqiB")[14])) * self.getCodeRate("CoderRateCiqA")[14])]  # level 15
        return curve

    def getTableMcsA(self):
        curve = [(-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 0])) * self.getCodeRate("CoderRateMcsA")[ 0]),  # level  0
                 (-6.5395, 0.5280, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 1])) * self.getCodeRate("CoderRateMcsA")[ 1]),  # level  1
                 (-5.7642, 0.4753, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 2])) * self.getCodeRate("CoderRateMcsA")[ 2]),  # level  2
                 (-4.6814, 0.4310, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 3])) * self.getCodeRate("CoderRateMcsA")[ 3]),  # level  3
                 (-3.6457, 0.3797, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 4])) * self.getCodeRate("CoderRateMcsA")[ 4]),  # level  4
                 (-2.4033, 0.3888, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 5])) * self.getCodeRate("CoderRateMcsA")[ 5]),  # level  5
                 (-1.7048, 0.3381, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 6])) * self.getCodeRate("CoderRateMcsA")[ 6]),  # level  6
                 (-0.8264, 0.3169, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 7])) * self.getCodeRate("CoderRateMcsA")[ 7]),  # level  7
                 (-0.1311, 0.2991, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 8])) * self.getCodeRate("CoderRateMcsA")[ 8]),  # level  8
                 ( 0.7615, 0.2834, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[ 9])) * self.getCodeRate("CoderRateMcsA")[ 9]),  # level  9
                 ( 1.4570, 0.2554, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[10])) * self.getCodeRate("CoderRateMcsA")[10]),  # level 10
                 ( 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[11])) * self.getCodeRate("CoderRateMcsA")[11]),  # level 11
                 ( 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[12])) * self.getCodeRate("CoderRateMcsA")[12]),  # level 12
                 ( 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[13])) * self.getCodeRate("CoderRateMcsA")[13]),  # level 13
                 ( 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[14])) * self.getCodeRate("CoderRateMcsA")[14]),  # level 14
                 ( 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[15])) * self.getCodeRate("CoderRateMcsA")[15]),  # level 15
                 ( 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[16])) * self.getCodeRate("CoderRateMcsA")[16]),  # level 16
                 ( 6.4676, 0.2470, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[17])) * self.getCodeRate("CoderRateMcsA")[17]),  # level 17
                 ( 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[18])) * self.getCodeRate("CoderRateMcsA")[18]),  # level 18
                 ( 7.8056, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[19])) * self.getCodeRate("CoderRateMcsA")[19]),  # level 19
                 ( 8.5042, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[20])) * self.getCodeRate("CoderRateMcsA")[20]),  # level 20
                 ( 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[21])) * self.getCodeRate("CoderRateMcsA")[21]),  # level 21
                 (10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[22])) * self.getCodeRate("CoderRateMcsA")[22]),  # level 22
                 (10.6933, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[23])) * self.getCodeRate("CoderRateMcsA")[23]),  # level 23
                 (11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[24])) * self.getCodeRate("CoderRateMcsA")[24]),  # level 24
                 (12.2963, 0.1829, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[25])) * self.getCodeRate("CoderRateMcsA")[25]),  # level 25
                 (12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[26])) * self.getCodeRate("CoderRateMcsA")[26]),  # level 26
                 (13.1731, 0.1966, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[27])) * self.getCodeRate("CoderRateMcsA")[27]),  # level 27
                 (15.3686, 0.1883, math.log2((self.getModulationOrder("MoudulationOrderMcsA")[28])) * self.getCodeRate("CoderRateMcsA")[28])]  # level 28
        return curve    

    def getTableMcsB(self):
        curve = [(-7.8269, 0.5938, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 0])) * self.getCodeRate("CoderRateMcsB")[ 0]),  # level  0
                 (-5.7977, 0.4928, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 2])) * self.getCodeRate("CoderRateMcsB")[ 2]),  # level  2
                 (-1.7048, 0.3380, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 3])) * self.getCodeRate("CoderRateMcsB")[ 3]),  # level  3
                 (-0.1310, 0.2990, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 4])) * self.getCodeRate("CoderRateMcsB")[ 4]),  # level  4
                 ( 2.1853, 0.2702, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 5])) * self.getCodeRate("CoderRateMcsB")[ 5]),  # level  5
                 ( 2.8850, 0.2522, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 6])) * self.getCodeRate("CoderRateMcsB")[ 6]),  # level  6
                 ( 3.6101, 0.2457, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 7])) * self.getCodeRate("CoderRateMcsB")[ 7]),  # level  7
                 ( 4.5008, 0.2592, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 8])) * self.getCodeRate("CoderRateMcsB")[ 8]),  # level  8
                 ( 5.2822, 0.2459, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[ 9])) * self.getCodeRate("CoderRateMcsB")[ 9]),  # level  9
                 ( 5.6121, 0.2710, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[10])) * self.getCodeRate("CoderRateMcsB")[10]),  # level 10
                 ( 7.0153, 0.2413, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[11])) * self.getCodeRate("CoderRateMcsB")[11]),  # level 11
                 ( 7.8057, 0.2244, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[12])) * self.getCodeRate("CoderRateMcsB")[12]),  # level 12
                 ( 8.5041, 0.2136, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[13])) * self.getCodeRate("CoderRateMcsB")[13]),  # level 13
                 ( 9.4141, 0.1955, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[14])) * self.getCodeRate("CoderRateMcsB")[14]),  # level 14
                 (10.0140, 0.1923, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[15])) * self.getCodeRate("CoderRateMcsB")[15]),  # level 15
                 (10.6932, 0.2222, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[16])) * self.getCodeRate("CoderRateMcsB")[16]),  # level 16
                 (11.5429, 0.2131, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[17])) * self.getCodeRate("CoderRateMcsB")[17]),  # level 17
                 (12.2963, 0.1830, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[18])) * self.getCodeRate("CoderRateMcsB")[18]),  # level 18
                 (12.7529, 0.1979, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[19])) * self.getCodeRate("CoderRateMcsB")[19]),  # level 19
                 (14.0043, 0.1826, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[20])) * self.getCodeRate("CoderRateMcsB")[20]),  # level 20
                 (14.8284, 0.1824, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[21])) * self.getCodeRate("CoderRateMcsB")[21]),  # level 21
                 (15.5706, 0.1683, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[22])) * self.getCodeRate("CoderRateMcsB")[22]),  # level 22
                 (15.9361, 0.1720, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[23])) * self.getCodeRate("CoderRateMcsB")[23]),  # level 23
                 (17.0696, 0.1859, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[24])) * self.getCodeRate("CoderRateMcsB")[24]),  # level 24
                 (17.6402, 0.1742, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[25])) * self.getCodeRate("CoderRateMcsB")[25]),  # level 25
                 (18.0284, 0.2569, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[26])) * self.getCodeRate("CoderRateMcsB")[26]),  # level 26
                 (20.8035, 0.1957, math.log2((self.getModulationOrder("MoudulationOrderMcsB")[27])) * self.getCodeRate("CoderRateMcsB")[27])]  # level 27
        return curve