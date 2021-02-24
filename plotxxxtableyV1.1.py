from time import process_time as clock
import matplotlib.pyplot as plt
from nr_tables import Tables
import numpy as np
import scipy.special
import numpy.matlib
import math
import time


class PlotTableForAWGN:
    """
    A class for plotting awgn curves for passed tables

    ...

    Methods
    -------
        PlotBlerCqiB(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMcsA(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMcsB(TableData: int, SNR: int, SytleParameter: dict)
    """
    def __init__(self, TableData: int, SNR: int, StyleParameter: dict):
        """
        Parameters
        ----------
        TableData : int

            Vector or Scalar //if Scalar plots only dedicated curve
        SNR : float

            Vector or Scalar //if Scalar -10 dB to passed argument in 0.1 dB steps
        StyleParameter : dict

            dictionary or empty //if empty uses default StyleParameters

        """
        self.TableData      = TableData
        self.StyleParameter = StyleParameter
        self.SNR            = SNR

        if np.isscalar(self.SNR) and self.SNR < 0: 
            raise ValueError("SNR needs to be larger then zero")
        if np.isscalar(self.SNR):
            self.SNR = np.linspace(-10,self.SNR,int(abs(-10)+self.SNR/0.1))
    
    def BlerCqiB(self):
        if self.TableData > len(Tables().getTableCqiB()):
            raise NotImplementedError("No data for dedicated curve")    
        
        TempSnrFactor   = (Tables().getTableCqiB())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableCqiB())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableCqiB())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetBler(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('CqiB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMcsA(self):
        if self.TableData > len(Tables().getTableMcsA()):
            raise NotImplementedError("No data for dedicated curve")

        TempSnrFactor   = (Tables().getTableMcsA())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableMcsA())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableMcsA())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetBler(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('McsA')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMcsB(self):
        if self.TableData > len(Tables().getTableMcsB()):
            raise NotImplementedError("No data for dedicated curve")

        TempSnrFactor   = (Tables().getTableMcsB())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableMcsB())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableMcsB())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetBler(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('McsB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyCqiB(self):
        if self.TableData > len(Tables().getTableCqiB()):
            raise NotImplementedError("No data for dedicated curve")

        TempSnrFactor   = (Tables().getTableCqiB())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableCqiB())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableCqiB())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetEfficiency(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('CiqB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMscA(self):
        if self.TableData > len(Tables().getTableMcsA()):
            raise NotImplementedError("No data for dedicated curve")

        TempSnrFactor   = (Tables().getTableMcsA())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableMcsA())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableMcsA())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetEfficiency(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('McsA')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMcsB(self):
        if self.TableData > len(Tables().getTableMcsB()):
            raise NotImplementedError("No data for dedicated curve")

        TempSnrFactor   = (Tables().getTableMcsB())[0:self.TableData, 0]
        TempCodeRate    = (Tables().getTableMcsB())[0:self.TableData, 1]
        TempMaximumRate = (Tables().getTableMcsB())[0:self.TableData, 2]
        DataY           = (FastCalculationBlerEfficiency
                          (TempSnrFactor, TempCodeRate, TempMaximumRate)
                          .GetEfficiency(self.SNR))
        self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
        self.__PlotCurve('McsB')
        return [self.CurveData[0][:], self.CurveData[0][:]]
    
    def __PlotCurve(self, Table):
        #sets grid Major if not predefined  
        #    if self.grid == 'True':
        #        plt.grid(b=True, which='major', color='#666666', linestyle='-')
        #sets grid Minor if not predefined  
        #    if self.gridMinor == 'True':
        #        plt.minorticks_on()
        #        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        #Sets labels "CqiB, McsA & McsB"       
            if   Table == "CqiB":
                self.label = ((Tables().getModulationOrder("MoudulationOrderCqiB"),Tables().getTableCqiB()),
                (Tables().getCodeRate("CoderRateCqiB")))
            elif Table == "McsA":
                self.label = ((Tables().getModulationOrder("MoudulationOrderMcsA"),Tables().getTableMcsA()),
                (Tables().getCodeRate("CoderRateMcsA")))
            elif Table == "McsB":
                self.label = ((Tables().getModulationOrder("MoudulationOrderMcsB"),Tables().getTableMcsB()),
                (Tables().getCodeRate("CoderRateMcsB")))
            else:
                self.legend = "Unknown"
            if np.isscalar(self.TableData):
                plt.plot(self.CurveData[0],self.CurveData[1],    
                        label     = str(self.label[0][0][self.TableData][1]) + " " + 
                                    str(self.label[0][0][self.TableData][2])+ " Coderate" + 
                                    str(round(self.label[1][self.TableData],2)),
                        linestyle = 'solid',
                        linewidth = 1)
                plt.show()
            else:
                for n in range(np.min(self.TableData),np.max(self.TableData)):
                    plt.plot(self.CurveData[0][n],self.CurveData[0][n],    
                        label     = str(self.label[0][0][n][1]) + " " + 
                                    str(self.label[0][0][n][2])+ " Coderate" + 
                                    str(round(self.label[1][n],2)),
                        linestyle = self.lineSytle,
                        linewidth = self.linewidth)

class FastCalculationBlerEfficiency:
        def __init__(self, SnrFactor=1.0, CodeRateFactor=1.0, MaximumRate=1.0):
            self.SnrFactor      = SnrFactor
            self.CodeRateFactor = CodeRateFactor
            self.MaximumRate    = MaximumRate
            if all (x < 0 for x in CodeRateFactor):
                raise ValueError("Code rate factor has to be positive")
            if all (x <= 0 for x in MaximumRate):
                raise ValueError("Maximum rate has to be larger then zero")
 
        def GetBler(self, SnrInDecibel):
            ScaleSnr = [((SnrInDecibel)-self.SnrFactor[i])\
                / math.sqrt(2.0) / self.CodeRateFactor[i] for i in range(len(self.SnrFactor))]

            return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

        def GetEfficiency(self, SnrInDecibel):
            Bler = np.array(self.GetBler(SnrInDecibel))

            return [((1.0 - Bler[i]) * self.MaximumRate[i]) for i in range(len(self.MaximumRate))]

Test = PlotTableForAWGN(3,20,1).BlerCqiB();
Test1 = 1