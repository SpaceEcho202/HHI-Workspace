import matplotlib.pyplot as plt
from nr_tables import Tables
import numpy as np
import scipy.special
import numpy.matlib
import math
class PlotTable:
    """
    A class for plotting awgn curves for passed tables

    ...

    Methods
    -------
        PlotBlerCQI_2(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMCS_1(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMCS_2(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyCQI_2(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyMCS_1(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyMCS_2(TableData: int, SNR: int, SytleParameter: dict)
    """
    def __init__(self, TableData: int, SNR: int, StyleParameter: dict):
        """
        Parameters
        ----------
        TableData : int

            Vector or Scalar //if Scalar is passed plots only dedicated curve. The following tables are currently implemented:
            CQI_2: 1-14 MCS_1: 0-28, MCS_2: 0-27
        SNR : float

            Vector or Scalar //if Scalar is used then from -10 dB to passed argument in 0.1 dB steps or dedicated step size
        StyleParameter : dict

            dictionary //if dictonary is empty pass {} to argument then class is initialised with the following default parameters:
            {yscale:'log' for BLER and 'linear' for Efficiency, title:'Table' and 'Type', xlabel:'SNR', ylabel:'Type', 
            linewidth: 1, linestyle: 'solid', girdMajor: 'TRUE',gridMinor: 'TRUE',Save: 'NO', ResoSNR: 0.1}
            //else define your own parameters.
            
        Returns
        -------
        CurveData[0] : float

            Vector or Matrix with calculated BLER or Efficiency data
        CurveData[1] : float

            Vector or Matrix with all dedicated SNR values

        Examples
        -------
        1.) Call the class PlotTable.

        2.) Select the desired lvl, e.g. as Scalar e.g. MCS_2 0, 1, ...N or as Vector [0,2]

        3.) Pass a scalar e.g. 20 or as a vector np.linspace(-10, 20, 100)

        4.) Pass an empty dictionary e.g. {} or set own parameters {'xlabel': Test, 'Save': Yes, ...}

        5.) Call method for graphical representation of the desired curve e.g. BlerMCS_1(), EfficiencyMCS_1() 

        DataBlerMCS_1 = PlotTable([0, 1], 20, {}).BlerMCS_1() or

        DataBlerCQI_2 = PlotTable(0, np.linspace(-10, 20, 1e3), {'Save':Yes}).BlerCQI_2()
        """
        self.SNR               = SNR
        self.StyleParameter    = StyleParameter
        self.TableData         = np.array(TableData).astype(int)
        self.FromTable         = int(np.min(self.TableData))
        self.ToTable           = int(np.max(self.TableData) +1 )
        self.IsScalarSNR       = True if np.isscalar(self.SNR) else False
        self.IsScalarTableData = True if np.isscalar(self.TableData) else False
    
        ResoSNR         = self.StyleParameter.get('ResoSNR',0.1)
        # Check if passed scalar value is larger then zero
        if self.IsScalarSNR and self.SNR < 0: 
            raise ValueError("SNR needs to be larger then zero")
        elif self.IsScalarSNR:
             self.SNR = np.linspace(-10,self.SNR,int(abs(-10)+self.SNR/ResoSNR))
        # Removes dublicates in TableData Vector
        if not self.IsScalarTableData:
            self.TableData = np.unique(self.TableData)           
            # Converts a Vector with single entry to Scalar
            if len(self.TableData) == 1:
                print("change from Vector to Scalar")
                self.IsScalarTableData = True
                self.TableData         = int(self.TableData[0])
          
    def BlerCQI_2(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> CQI_2- Table 
        '''
        self.TableData = self.TableData - 1
        if self.ToTable -1 > len(Tables().getTableCQI_2()) or self.FromTable <= 0:
            raise NotImplementedError("No data for dedicated curve")    

        self.__getBlerOrEfficiency('BLER', 'CQI_2')
        self.__setAxisLabelTitleScale('BLER', 'CQI Table 2')
        self.__PlotCurve('CQI_2')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMCS_1(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> MCS_1- Table
        '''
        if self.ToTable > len(Tables().getTableMCS_1()) or self.FromTable < 0:
            raise NotImplementedError("No data for dedicated curve")    

        self.__getBlerOrEfficiency('BLER', 'MCS_1')
        self.__setAxisLabelTitleScale('BLER', 'MCS Table 1')
        self.__PlotCurve('MCS_1')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMCS_2(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> MCS_2- Table
        '''
        if self.ToTable > len(Tables().getTableMCS_2()) or self.FromTable < 0:
            raise NotImplementedError("No data for dedicated curve")    
        self.__getBlerOrEfficiency('BLER', 'MCS_2')
        self.__setAxisLabelTitleScale('BLER', 'MCS Table 2')
        self.__PlotCurve('MCS_2')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyCQI_2(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> CQI_2- Table
        '''
        self.TableData = self.TableData - 1
        if self.ToTable -1 > len(Tables().getTableCQI_2()) or self.FromTable <= 0:
            raise NotImplementedError("No data for dedicated curve")      
        self.__getBlerOrEfficiency('Efficiency', 'CQI_2')
        self.__setAxisLabelTitleScale('Efficiency', 'CQI Table 2')
        self.__PlotCurve('CQI_2')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMCS_1(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> MCS_1- Table 
        '''
        if self.ToTable > len(Tables().getTableMCS_1()) or self.FromTable < 0:
            raise NotImplementedError("No data for dedicated curve")    
        self.__getBlerOrEfficiency('Efficiency', 'MCS_1')    
        self.__setAxisLabelTitleScale('Efficiency', 'MCS Table 1')
        self.__PlotCurve('MCS_1')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMCS_2(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> MCS_2- Table 
        '''
        if self.ToTable > len(Tables().getTableMCS_2()) or self.FromTable < 0:
            raise NotImplementedError("No data for dedicated curve")  
        self.__getBlerOrEfficiency('Efficiency', 'MCS_2') 
        self.__setAxisLabelTitleScale('Efficiency', 'MCS Table 2')
        self.__PlotCurve('MCS_2')
        return [self.CurveData[0][:], self.CurveData[1][:]]
            

    def __getBlerOrEfficiency(self, Table, Type):
        if Type == 'CQI_2':
            TempTable = (Tables().getTableCQI_2())
        if Type == 'MCS_1':    
            TempTable = (Tables().getTableMCS_1())
        if Type == 'MCS_2':
            TempTable = (Tables().getTableMCS_2())
        # More tables can be added here
        if self.IsScalarTableData:
            TempSnrFactor   = TempTable[self.TableData, 0]
            TempCodeRate    = TempTable[self.TableData, 1]
            TempMaximumRate = TempTable[self.TableData, 2]

            if Type == 'Efficiency':
                DataY           = (FastCalculationBlerEfficiency
                                  (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                  .GetEfficiency(self.SNR))
            else:
                DataY           = (FastCalculationBlerEfficiency
                                  (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                  .GetBler(self.SNR))

            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   TempTable[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   TempTable[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, TempTable[n, 2])

            if Type == 'Efficiency':                  
                DataY           = (FastCalculationBlerEfficiency
                                  (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                  .GetEfficiency(self.SNR))
            else:
                DataY           = (FastCalculationBlerEfficiency
                                  (TempSnrFactor, TempCodeRate, TempMaximumRate)
                                  .GetBler(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]
       
    def __setAxisLabelTitleScale(self, Type, Table):
        '''
        This method creates alle labels, titels & scales -> can not be seen 
        '''      
        if Type == 'BLER':
            self.Yscale    = 'log'
            self.ylabel    = 'BLER'
            self.ylim      = (10e-6, 1)
        else: 
            self.Yscale = 'linear'
            self.ylabel = 'Spectral Efficiency in [bit/s/Hz]'
            self.ylim   = (0,     np.ceil(np.max(self.CurveData[1])))
        self.type   = Type
        self.table  = Table
        self.title     = r"{} for {}".format(Type, Table)
        self.SaveTitle = r"plot_{}_table_{}_{}".format(str.lower(self.table[0:3]),
                         self.table[10],str.lower(self.type))
        self.xlimMin   = np.min(self.SNR)
        self.xlimMax   = np.max(self.SNR)

    def __GetFigureSize(self, IsManyCurves):
        Dpi     = 96
        Height  = 600 / Dpi
        Width   = 1100 / Dpi

        if IsManyCurves == True:
            Height = 700 / Dpi    

        return [Width, Height, Dpi]

    def __SaveCSV(self):
        '''
        This method creates a CSV- file for the dedicated tables & types -> can not be seen 
        '''
        if self.IsScalarTableData:
            FileName = r"{}_table_{}_{}_{}".format(
                str.lower(self.table[0:3]), self.table[10], 
                self.label[0][0][self.TableData][2], 
                str.lower(self.type))
            f = open(FileName+".csv","w")

            Header = r"SnrInDezibel; {}".format(str(self.type))
            f.write(Header+ ";\n")

            for i in range(len(self.CurveData[0])):
                Results = r"{:d}; {}; {}".format(
                    i, self.CurveData[0][i], 
                    self.CurveData[1][i])
                f.write(Results+"\n")
                
            f.close() 

        else:
            for n in range(len(self.TableData)):
                FileName = r"{}_table_{}_{}_{}".format(
                    str.lower(self.table[0:3]), self.table[10], 
                    self.label[0][0][self.TableData[n]][2],
                    str.lower(self.type))
                f = open(FileName+".csv","w")

                Header = r"SnrInDezibel; {}".format(str(self.type))
                f.write(Header+ ";\n")

                for i in range(len(self.CurveData[0][0])):
                    Results = r"{:d}; {}; {}".format(
                        i, self.CurveData[0][n][i],
                        self.CurveData[1][n][i])
                    f.write(Results+"\n")

                f.close()     

    def __PlotCurve(self, Table):       
        '''
        This method creates a plot for the dedicated table & type -> can not be seen 
        '''
        # Dictionary compare and set style parameter
        gridMajor     = self.StyleParameter.get('grid',         "True")
        gridMinor     = self.StyleParameter.get('gridMinor',    "True")
        linestyle     = self.StyleParameter.get('linestyle',   'solid')
        linewidth     = self.StyleParameter.get('linewidth',         1)
        SaveFig       = self.StyleParameter.get('SaveFig',       'Yes')
        SaveCsv       = self.StyleParameter.get('SaveCsv',       'Yes')
        # Sets style parameter plt.plot method
        
        if not self.IsScalarTableData: 
            Height, Width, Dpi = self.__GetFigureSize(len(self.TableData) > 20)
            plt.figure(figsize=(Height, Width), dpi = Dpi)

        plt.title(self.StyleParameter.get('title',                 self.title))
        plt.xlabel(self.StyleParameter.get('xlabel',            'SNR in [dB]'))
        plt.ylabel(self.StyleParameter.get('ylabel',              self.ylabel))
        plt.yscale(self.StyleParameter.get('yscale',              self.Yscale))
        plt.ylim(self.StyleParameter.get('ylim',                    self.ylim))
        plt.xlim(self.StyleParameter.get('xlim', (self.xlimMin, self.xlimMax)))
            
        #sets grid Major if not predefined  
        if gridMajor == 'True':
            plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.4)
        #sets grid Minor if not predefined
        if gridMinor == 'True':
                plt.minorticks_on()
                plt.grid(b=True, which='minor', color='#999999',
                         linestyle='-', alpha=0.2)

        #Sets labels "CQI_2, MCS_1 & MCS_2"
        if Table == "CQI_2":
            self.label = ((Tables().getModulationOrder("MoudulationOrderCQI_2"), Tables().getTableCQI_2()),
                          (Tables().getCodeRate("CoderRateCQI_2")))
        elif Table == "MCS_1":
            self.label = ((Tables().getModulationOrder("MoudulationOrderMCS_1"), Tables().getTableMCS_1()),
                          (Tables().getCodeRate("CoderRateMCS_1")))
        elif Table == "MCS_2":
            self.label = ((Tables().getModulationOrder("MoudulationOrderMCS_2"), Tables().getTableMCS_2()),
                          (Tables().getCodeRate("CoderRateMCS_2")))
        else:
            self.label = "Unknown"
        if self.IsScalarTableData:
            TempData = self.TableData
            LabelString = r"{} - {} - $R = {:.2f}$".format(
                self.label[0][0][TempData][2], self.label[0][0][TempData][1], (self.label[1][TempData]))

            plt.plot(self.CurveData[0],self.CurveData[1],    
                    label     = LabelString,
                    linestyle = linestyle,
                    linewidth = linewidth)
        else:
            for n in range(len(self.TableData)):
                TempData = self.TableData[n]

                LabelString = r"{} - {} - $R = {:.2f}$".format(
                    self.label[0][0][TempData][2], self.label[0][0][TempData][1], (self.label[1][TempData]))

                plt.plot(self.CurveData[0][n],self.CurveData[1][n],    
                    label     = LabelString,
                    linestyle = linestyle,
                    linewidth = linewidth)
        plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", fancybox=True)
        plt.subplots_adjust(right=0.7)

        if str.upper(SaveFig) == "YES":
            #Sets figure size can be changed to fit for different screens
            fig = plt.gcf()
            fig.set_size_inches(17, 8)
            plt.savefig(self.SaveTitle, bbox_inches='tight')
            plt.show()
        else:
            plt.show()

        if str.upper(SaveCsv) == "YES":
            self.__SaveCSV()

class FastCalculationBlerEfficiency:
    """
    A class for fast BLER & Efficiency calculation 

    ...

    Methods
    -------
        GetBler(self, SnrInDecibel)

        GetEfficiency(self, SnrInDecibel)

    """
    def __init__(self, SnrFactor:float = 1.0, CodeRateFactor: float = 1.0, MaximumRate: float = 1.0):
        """
        Parameters
        ----------
        SnrFactor : float or int

            Vector or Scalar //if Scalar is passed calculates only dedicated value
        CodeRateFactor : float or int

            Vector or Scalar //if Scalar is passed calculates only dedicated value // has to be positive
        MaximumRate : float or int

            dictionary or empty //if Scalar is passed calculates only dedicated value // has to be larger then zero

        """
        self.SnrFactor      = SnrFactor
        self.CodeRateFactor = CodeRateFactor
        self.MaximumRate    = MaximumRate
        self.IsScalar       = True if np.isscalar(CodeRateFactor) else False

        if self.IsScalar:
            if CodeRateFactor < 0:
                raise ValueError("Code rate factor has to be positive")
            if MaximumRate <= 0:
                    raise ValueError("Maximum rate has to be larger then zero")
        else:
            if all (x < 0 for x in CodeRateFactor):
                raise ValueError("Code rate factor has to be positive")
            if all (x <= 0 for x in MaximumRate):
                raise ValueError("Maximum rate has to be larger then zero")

    def GetBler(self, SnrInDecibel):
        if self.IsScalar:
            ScaleSnr = ((SnrInDecibel)-self.SnrFactor)\
            / math.sqrt(2.0) / self.CodeRateFactor
        else:
            ScaleSnr = [((SnrInDecibel)-self.SnrFactor[i])\
            / math.sqrt(2.0) / self.CodeRateFactor[i] for i in range(len(self.SnrFactor))]

        return [(0.5*(1-(scipy.special.erf(v)))) for v in ScaleSnr]

    def GetEfficiency(self, SnrInDecibel):
        Bler = np.array(self.GetBler(SnrInDecibel))
        if self.IsScalar:
            return ((1.0 - Bler) * self.MaximumRate)
        else:
            return [((1.0 - Bler[i]) * self.MaximumRate[i]) for i in range(len(self.MaximumRate))]

PlotTable([1], np.linspace(-10,20,1000), {'SaveFig':'Yes', 'SaveCsv':'Yes'}).BlerMCS_1()
