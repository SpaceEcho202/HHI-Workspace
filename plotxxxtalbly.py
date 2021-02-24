import matplotlib.pyplot as plt
from nr_tables import Tables
import time
import numpy as np
import numpy.matlib
import math
import scipy.special
from time import process_time as clock

class PlotTable:
        #Method which creates BLER vector depending on the previous specified Snr & nr_table -> "CQI, MCS"       
        def __init__(self, dictionary):
            self.grid          = dictionary.get('grid'            , "True"  )
            self.gridMinor     = dictionary.get('gridMinor'       , "True"  )
            self.xscale        = dictionary.get('xscale'          , 'linear')
            self.lineSytle     = dictionary.get('lineStyle'       , 'solid')
            self.linewidth     = dictionary.get('linewidth'       , 1)
            self.plotType      = dictionary.get('PlotType'        , "Unknown")
            self.plotTable     = dictionary.get('PlotTable'       , "Unknown")
            self.xlabel        = dictionary.get('xlabel'          , "SNR [dB]")
            self.title         = dictionary.get('title'           , str.upper(self.plotType) + " for " + str.upper(self.plotTable))
            self.SnrMax        = dictionary.get('SnrMax'          , 10)
            self.SnrMin        = dictionary.get('SnrMin'          ,-10)
            self.SnrResolution = dictionary.get('SnrResolution[dB]'   , 0.1)
            self.Save          = dictionary.get('Save'            , 'Yes')
            self.xlim          = dictionary.get('xlim'            , (self.SnrMin, self.SnrMax))
            if self.plotType == "Bler":
                self.ylim      = dictionary.get('ylim'            , (10e-6, 1))
                self.yscale    = dictionary.get('yscale'          , 'log')
                self.ylabel    = dictionary.get('ylabel'          , str.upper(self.plotType))
            elif self.plotType == "Efficiency":

                #ylim is determind by the max&min value in Y-vector if not predefined
                self.ylim      = dictionary.get('ylim', (np.min((self.CreateCurveDataEfficiency
                                                        (self.plotTable, self.SnrMin, self.SnrMax,
                                                         self.SnrResolution))[1]), 
                                                        (np.max((self.CreateCurveDataEfficiency(self.plotTable,
                                                         self.SnrMin, self.SnrMax, self.SnrResolution))[1]))))
                self.yscale    = dictionary.get('yscale'          , 'linear')
                self.ylabel    = dictionary.get('ylabel'          , "Spectral " + self.plotType + " in [bit/s/Hz]")

        def PlotCurve(self):
            plt.xlim(self.xlim)
            plt.ylim(self.ylim)
            plt.title(self.title)
            plt.xlabel(self.xlabel)
            plt.ylabel(self.ylabel)
            plt.xscale(self.xscale)
            plt.yscale(self.yscale)

            #sets grid Major if not predefined  
            if self.grid == 'True':
                plt.grid(b=True, which='major', color='#666666', linestyle='-')

            #sets grid Minor if not predefined  
            if self.gridMinor == 'True':
                plt.minorticks_on()
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

            #Sets labels "CqiB, McsA & McsB"
            if self.plotTable == "CqiB":
                self.label = ((Tables().getModulationOrder("MoudulationOrderCqiB"),Tables().getTableCqiB()),
                (Tables().getCodeRate("CoderRateCqiB")))
            elif self.plotTable == "McsA":
                self.label = ((Tables().getModulationOrder("MoudulationOrderMcsA"),Tables().getTableMcsA()),
                (Tables().getCodeRate("CoderRateMcsA")))
            elif self.plotTable == "McsB":
                self.label = ((Tables().getModulationOrder("MoudulationOrderMcsB"),Tables().getTableMcsB()),
                (Tables().getCodeRate("CoderRateMcsB")))
            else:
                self.legend = "Unknown"

            #Creates BLER curve 
            if self.plotType == "Bler":
                TempPlot = (self.CreateCurveDataBler(self.plotTable, self.SnrMin, self.SnrMax, self.SnrResolution))

                for n in range(len(TempPlot[0])):
                    plt.plot(TempPlot[0][n],
                        TempPlot[1][n],
                        label = str(self.label[0][0][n][1]) + " " +str(self.label[0][0][n][2])+ " Coderate" + str(round(self.label[1][n],2)),
                        linestyle = self.lineSytle,
                        linewidth = self.linewidth ) 

                plt.legend(bbox_to_anchor=(1,1), loc="upper left")
                #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                #ncol=2, mode="expand", borderaxespad=0.)
                if self.Save == "Yes":
                    #Sets figure size can be changed to fit for different screens
                    fig = plt.gcf()
                    fig.set_size_inches(17, 8)
                    plt.savefig('Plot' + self.plotTable + 'Table' + self.plotType, bbox_inches='tight')
                    print("\t Process finished --- %s seconds ---" % (clock() - start_time))
                    plt.show()

                else:
                    print("\t Process finished --- %s seconds ---" % (clock() - start_time))

                    #Sets figure size can be changed to fit for different screens
                    fig = plt.gcf()
                    fig.set_size_inches(17, 8)
                    plt.show()

            # Creates efficiency curve    
            elif self.plotType == "Efficiency":
                TempPlot = (self.CreateCurveDataEfficiency(self.plotTable, self.SnrMin, self.SnrMax, self.SnrResolution))
                for n in range(len(TempPlot[0])):
                    plt.plot(TempPlot[0][n],
                        TempPlot[1][n],
                        label = str(self.label[0][0][n][1]) + " <" +str(self.label[0][0][n][2])+ "> Coderate: " + str(round(self.label[1][n],2)),
                        linestyle = self.lineSytle,
                        linewidth = self.linewidth)

                plt.legend(bbox_to_anchor=(1,1), loc="upper left")
                #plt.legend(bbox_to_anchor=(0., -0.25, 1., 1.02), loc='lower left',
                #ncol=4, mode="expand", borderaxespad=0.)
                if self.Save == "Yes":
                    #Sets figure size can be changed to fit for different screens
                    fig = plt.gcf()
                    fig.set_size_inches(17, 8)
                    plt.savefig('Plot' + self.plotTable + 'Table' + self.plotType, bbox_inches='tight')
                    print("\t Process finished --- %s seconds ---" % (clock() - start_time))
                    plt.show()

                else:
                    print("\t Process finished --- %s seconds ---" % (clock() - start_time))
                    #Sets figure size can be changed to fit for different screens 
                    fig = plt.gcf()
                    fig.set_size_inches(17, 8)
                    plt.show()

        def CreateCurveDataBler(self, TableType, SnrMin, SnrMax, Resolution):
            
            TempResolution = int((abs(SnrMin)+SnrMax)/Resolution)
            self.SnrVector = np.linspace(SnrMin, SnrMax, TempResolution)

            if TableType == "CqiB":     
               TempSnrFactor   = (Tables().getTableCqiB())[:, 0]
               TempCodeRate    = (Tables().getTableCqiB())[:, 1]
               TempMaximumRate = (Tables().getTableCqiB())[:, 2]
               DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetBler(self.SnrVector ))

            if TableType == "McsA":     
                TempSnrFactor   = (Tables().getTableMcsA())[:, 0]
                TempCodeRate    = (Tables().getTableMcsA())[:, 1]
                TempMaximumRate = (Tables().getTableMcsA())[:, 2]
                DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetBler(self.SnrVector ))

            if TableType == "McsB":     
                TempSnrFactor   = (Tables().getTableMcsB())[:, 0]
                TempCodeRate    = (Tables().getTableMcsB())[:, 1]
                TempMaximumRate = (Tables().getTableMcsB())[:, 2]
                DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetBler(self.SnrVector ))
            return [np.matlib.repmat(self.SnrVector, len(DataY), 1), DataY]

        def CreateCurveDataEfficiency(self, TableType, SnrMin, SnrMax, Resolution):

            TempResolution = int((abs(SnrMin)+SnrMax)/Resolution)
            self.SnrVector = np.linspace(SnrMin, SnrMax, TempResolution)

            if TableType == "CqiB":     
                TempSnrFactor   = (Tables().getTableCqiB())[:, 0]
                TempCodeRate    = (Tables().getTableCqiB())[:, 1]
                TempMaximumRate = (Tables().getTableCqiB())[:, 2]
                DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetEfficiency(self.SnrVector ))

            if TableType == "McsA":     
                TempSnrFactor   = (Tables().getTableMcsA())[:, 0]
                TempCodeRate    = (Tables().getTableMcsA())[:, 1]
                TempMaximumRate = (Tables().getTableMcsA())[:, 2]
                DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetEfficiency(self.SnrVector ))

            if TableType == "McsB":     
                TempSnrFactor   = (Tables().getTableMcsB())[:, 0]
                TempCodeRate    = (Tables().getTableMcsB())[:, 1]
                TempMaximumRate = (Tables().getTableMcsB())[:, 2]
                DataY           = (FastCalculationBlerEfficiency
                                 (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                 .GetEfficiency(self.SnrVector ))
            return [np.matlib.repmat(self.SnrVector, len(DataY), 1), DataY]
class FastCalculationBlerEfficiency:
        def __init__(self, SnrFactor=1.0, CodeRateFactor=1.0, MaximumRate=1.0):
            self.SnrFactor      = SnrFactor
            self.CodeRateFactor = CodeRateFactor
            self.MaximumRate    = MaximumRate
 
        def GetBler(self, SnrInDecibel):
            ScaleSnr = [((SnrInDecibel)-self.SnrFactor[i])\
                / math.sqrt(2.0) / self.CodeRateFactor[i] for i in range(len(self.SnrFactor))]
            return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

        def GetEfficiency(self, SnrInDecibel):
            Bler = np.array(self.GetBler(SnrInDecibel))
            return [((1.0 - Bler[i]) * self.MaximumRate[i]) for i in range(len(self.MaximumRate))]

start_time = clock()
PlotTable({'PlotType': "Efficiency", 'PlotTable': "McsB", 'SnrMax': 20, 'SnrMin': -10
          ,'SnrResolution[dB]': 0.01}).PlotCurve()