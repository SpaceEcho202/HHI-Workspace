import matplotlib.pyplot as plt
from nr_tables import Tables
import time
import numpy as np
import numpy.matlib
import math
import scipy.special
from time import process_time as clock

def track_time (snr_res__var, scpy):
    #Call exception class
    class ValueTooSmallError(Exception):
        pass

    class ValueNegativeError(Exception):
        pass

    #Call class which is responsible for creating the curve and all required default settings
    class PlotTable:
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
            self.SnrResolution = dictionary.get('SnrResolution'   , 1100)
            self.Save          = dictionary.get('Save'            , 'Yes')
            self.xlim          = dictionary.get('xlim'            , (self.SnrMin, self.SnrMax))
            if self.plotType == "Bler":
                self.ylim      = dictionary.get('ylim'            , (10e-6, 1))
                self.yscale    = dictionary.get('yscale'          , 'log')
                self.ylabel    = dictionary.get('ylabel'          , str.upper(self.plotType))
            elif self.plotType == "Efficiency":

        #ylim is determind by the max&min value in Y-vector if not predefined
                self.ylim      = dictionary.get('ylim', (np.min((self.CreateCurveDataEfficiency
                                                        (self.plotTable, self.SnrMin, self.SnrMax, self.SnrResolution))[1]), 
                                                        (np.max((self.CreateCurveDataEfficiency(self.plotTable, self.SnrMin, self.SnrMax, self.SnrResolution))[1]))))
                self.yscale    = dictionary.get('yscale'          , 'linear')
                self.ylabel    = dictionary.get('ylabel'          , "Spectral " + self.plotType + " in [bit/s/Hz]")

        #Method that generates the curve and the associated plot
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
                self.label = (Tables().getModulationOrder("MoudulationOrderCqiB"),Tables().getTableCqiB())
            elif self.plotTable == "McsA":
                self.label = (Tables().getModulationOrder("MoudulationOrderMcsA"),Tables().getTableMcsA())
            elif self.plotTable == "McsB":
                self.label = (Tables().getModulationOrder("MoudulationOrderMcsB"),Tables().getTableMcsB())
            else:
                self.legend = "Unknown"

            #Creates BLER curve 
            if self.plotType == "Bler":
                TempPlot = (self.CreateCurveDataBler(self.plotTable, self.SnrMin, self.SnrMax, self.SnrResolution))

                for n in range(len(TempPlot[0])):
                    plt.plot(TempPlot[0][n],
                        TempPlot[1][n],
                        label = str(self.label[0][n][1]) + " " + str(self.label[1][n][3]),
                        linestyle = self.lineSytle,
                        linewidth = self.linewidth ) 

                plt.legend(bbox_to_anchor=(1,1), loc="upper left")

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
                        label = str(self.label[0][n][1]) + " " + str(self.label[1][n][3]),
                        linestyle = self.lineSytle,
                        linewidth = self.linewidth)

                plt.legend(bbox_to_anchor=(1,1), loc="upper left")

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


        #Method which creates BLER vector depending on the previous specified Snr & nr_table -> "CQI, MCS"       
        def CreateCurveDataBler(self, TableType, SnrMin, SnrMax, Resolution):
            DataY     = []
            TempDataY = []

            self.SnrVector = np.linspace(SnrMin, SnrMax, Resolution)

            if TableType == "CqiB":     
                for n in range(len(self.SnrVector)):
                    DataY.append(CalculationBlerEfficiency(
                        SnrFactor=(Tables().getTableCqiB())[0][0],
                        CodeRateFactor=(Tables().getTableCqiB())[0][1],
                        MaximumRate=(Tables().getTableCqiB())[0][2]).GetBler(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableCqiB())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableCqiB())[i][0],
                                CodeRateFactor=(Tables().getTableCqiB())[i][1],
                                MaximumRate=(Tables().getTableCqiB())[i][2]).GetBler(self.SnrVector[n]))

                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            elif TableType == "McsA":
                for n in range(len(self.SnrVector)):
                            DataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsA())[0][0],
                                CodeRateFactor=(Tables().getTableMcsA())[0][1],
                                MaximumRate=(Tables().getTableMcsA())[0][2]).GetBler(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableMcsA())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsA())[i][0],
                                CodeRateFactor=(Tables().getTableMcsA())[i][1],
                                MaximumRate=(Tables().getTableMcsA())[i][2]).GetBler(self.SnrVector[n]))

                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            elif TableType == "McsB":
                for n in range(len(self.SnrVector)):
                            DataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsB())[0][0],
                                CodeRateFactor=(Tables().getTableMcsB())[0][1],
                                MaximumRate=(Tables().getTableMcsB())[0][2]).GetBler(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableMcsB())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsB())[i][0],
                                CodeRateFactor=(Tables().getTableMcsB())[i][1],
                                MaximumRate=(Tables().getTableMcsB())[i][2]).GetBler(self.SnrVector[n]))

                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            return [np.matlib.repmat(self.SnrVector, len(DataY), 1), DataY]


        #Method which creates Efficiency Matrix depending on the previous specified Snr & nr_table -> "CQI, MCS" 
        def CreateCurveDataEfficiency(self, TableType, SnrMin, SnrMax, Resolution):
            DataY     = []
            TempDataY = []
            self.SnrVector = np.linspace(SnrMin, SnrMax, Resolution)

            if TableType == "CqiB":
                for n in range(len(self.SnrVector)):
                            DataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableCqiB())[0][0],
                                CodeRateFactor=(Tables().getTableCqiB())[0][1],
                                MaximumRate=(Tables().getTableCqiB())[0][2]).GetEfficiency(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableCqiB())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableCqiB())[i][0],
                                CodeRateFactor=(Tables().getTableCqiB())[i][1],
                                MaximumRate=(Tables().getTableCqiB())[i][2]).GetEfficiency(self.SnrVector[n]))
                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            elif TableType == "McsA":
                for n in range(len(self.SnrVector)):
                            DataY.append(CalculationBlerEfficiency(
                                (Tables().getTableMcsA())[0][0],
                                (Tables().getTableMcsA())[0][1],
                                (Tables().getTableMcsA())[0][2]).GetEfficiency(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableMcsA())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsA())[i][0],
                                CodeRateFactor=(Tables().getTableMcsA())[i][1],
                                MaximumRate=(Tables().getTableMcsA())[i][2]).GetEfficiency(self.SnrVector[n]))
                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            elif TableType == "McsB":
                for n in range(len(self.SnrVector)):
                            DataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsB())[0][0],
                                CodeRateFactor=(Tables().getTableMcsB())[0][1],
                                MaximumRate=(Tables().getTableMcsB())[0][2]).GetEfficiency(self.SnrVector[n]))

                for i in range(1, len(Tables().getTableMcsB())):
                        for n in range(len(self.SnrVector)):
                            TempDataY.append(CalculationBlerEfficiency(
                                SnrFactor=(Tables().getTableMcsB())[i][0],
                                CodeRateFactor=(Tables().getTableMcsB())[i][1],
                                MaximumRate=(Tables().getTableMcsB())[i][2]).GetEfficiency(self.SnrVector[n]))

                        DataY = np.row_stack((DataY, TempDataY))
                        TempDataY = []

            return [np.matlib.repmat(self.SnrVector, len(DataY), 1), DataY]


    #Method which creates the Bler || Efficiency vector            
    class CalculationBlerEfficiency:
        def __init__(self, SnrFactor=1.0, CodeRateFactor=1.0, MaximumRate=1.0):
            self.SnrFactor      = SnrFactor
            self.CodeRateFactor = CodeRateFactor
            self.MaximumRate    = MaximumRate

            #Exception call if the data does not meet the criteria description
            try:
                if self.CodeRateFactor < 0.0:
                    raise ValueNegativeError
                elif self.MaximumRate <= 0.0:
                    raise ValueTooSmallError
            except ValueNegativeError:
                print("Code rate factor has to be positive!")
            except ValueTooSmallError:
                print("Maximum rate has to be larger than zero!")

        def GetBler(self, SnrInDecibel):
            ScaleSnr = (SnrInDecibel-self.SnrFactor) / \
                math.sqrt(2.0) / self.CodeRateFactor
            if (scpy):
                return (0.5 * (1 - math.erf(ScaleSnr)))
            else:
                return (0.5 * (1 - scipy.special.erf(ScaleSnr)))

        def GetEfficiency(self, SnrInDecibel):
            Bler = self.GetBler(SnrInDecibel)
            return (1.0 - Bler) * self.MaximumRate

    #Calculates the time required to create the previously determined plot data
    start_time = clock()

    # Class call & method call to plot desired table "CqiB, McsA & McsB"
    PlotTable({'PlotType': "Efficiency", 'PlotTable': "McsA", 'SnrMax': 30, 'SnrMin': -10
                ,'SnrResolution': snr_res__var}).PlotCurve()



for i in [250]:
    print("\nSnr-Resolution: " + str(i) + ":")
    print("math.erf:")
    track_time(i, scpy=False)
    print("scipy.special.erf:")
    track_time(i, scpy=True)