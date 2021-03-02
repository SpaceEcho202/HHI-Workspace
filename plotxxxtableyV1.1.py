import matplotlib.pyplot as plt
from nr_tables import Tables
import numpy as np
import scipy.special
import numpy.matlib
import math

# Implementation is not fully done. Do not return the hole Matrix of calculation 

class PlotTable:
    """
    A class for plotting awgn curves for passed tables

    ...

    Methods
    -------
        PlotBlerCqiB(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMcsA(TableData: int, SNR: int, SytleParameter: dict)

        PlotBlerMcsB(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyCqiB(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyMcsA(TableData: int, SNR: int, SytleParameter: dict)

        PlotEfficiencyMcsB(TableData: int, SNR: int, SytleParameter: dict)
    """
    def __init__(self, TableData: int, SNR: int, StyleParameter: dict):
        """
        Parameters
        ----------
        TableData : int

            Vector or Scalar //if Scalar plots only dedicated curve TableData CqiB: 0-14 McsA: 0-28, McsB: 0-27
        SNR : float

            Vector or Scalar //if Scalar -10 dB to passed argument in 0.1 dB steps
        StyleParameter : dict

            dictionary or empty //if empty {} uses default StyleParameters 
        
        Returns
        -------
        CurveData[0] : float

            Vector with all calculated BLER or Efficiency data
        CurveData[1] : float

            Vector with all dedicated SNR values
        """
        self.SNR               = SNR
        self.StyleParameter    = StyleParameter
        self.TableData         = np.array(TableData).astype(int)
        self.ToTable           = int(np.max(self.TableData)+1)
        self.IsScalarSNR       = True if np.isscalar(self.SNR) else False
        self.IsScalarTableData = True if np.isscalar(self.TableData) else False
    
        SNR_Resolution         = self.StyleParameter.get('SNR_Resolution',0.1)
        # Check if passed scalar value is larger then zero
        if self.IsScalarSNR and self.SNR < 0: 
            raise ValueError("SNR needs to be larger then zero")
        elif self.IsScalarSNR:
             self.SNR = np.linspace(-10,self.SNR,int(abs(-10)+self.SNR/SNR_Resolution))
        # Removes dublicates in TableData Vector
        if not self.IsScalarTableData:
            self.TableData = np.unique(self.TableData)           
            # Converts a Vector with single entry to Scalar
            if len(self.TableData) == 1:
                print("change from Vector to Scalar")
                self.IsScalarTableData = True
                self.TableData         = int(self.TableData[0])
          
    def BlerCqiB(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> CqiB- Table 
        '''
        if self.ToTable > len(Tables().getTableCqiB()):
            raise NotImplementedError("No data for dedicated curve")    
        
        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableCqiB())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableCqiB())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableCqiB())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableCqiB())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableCqiB())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableCqiB())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('BLER', 'CqiB')
        self.__PlotCurve('CqiB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMcsA(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> McsA- Table
        '''
        if self.ToTable > len(Tables().getTableMcsA()):
            raise NotImplementedError("No data for dedicated curve")    

        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableMcsA())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableMcsA())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableMcsA())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableMcsA())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableMcsA())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableMcsA())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('BLER', 'McsA')
        self.__PlotCurve('McsA')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def BlerMcsB(self):
        '''
        This method creates SNR- Vector & BLER- Vector for the dedicated-> McsB- Table
        '''
        if self.ToTable > len(Tables().getTableMcsB()):
            raise NotImplementedError("No data for dedicated curve")    

        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableMcsB())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableMcsB())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableMcsB())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableMcsB())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableMcsB())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableMcsB())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetBler(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('BLER', 'McsB')
        self.__PlotCurve('McsB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyCqiB(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> CqiB- Table
        '''
        if self.ToTable > len(Tables().getTableCqiB()):
            raise NotImplementedError("No data for dedicated curve")    

        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableCqiB())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableCqiB())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableCqiB())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableCqiB())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableCqiB())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableCqiB())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('Efficiency', 'CqiB')
        self.__PlotCurve('CqiB')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMcsA(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> McsA- Table 
        '''
        if self.ToTable > len(Tables().getTableMcsA()):
            raise NotImplementedError("No data for dedicated curve")    

        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableMcsA())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableMcsA())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableMcsA())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableMcsA())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableMcsA())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableMcsA())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('Efficiency', 'McsA')
        self.__PlotCurve('McsA')
        return [self.CurveData[0][:], self.CurveData[1][:]]

    def EfficiencyMcsB(self):
        '''
        This method creates SNR- Vector & Efficiency- Vector for the dedicated-> McsB- Table 
        '''
        if self.ToTable > len(Tables().getTableMcsB()):
            raise NotImplementedError("No data for dedicated curve")    

        if self.IsScalarTableData:
            TempSnrFactor   = (Tables().getTableMcsB())[self.TableData, 0]
            TempCodeRate    = (Tables().getTableMcsB())[self.TableData, 1]
            TempMaximumRate = (Tables().getTableMcsB())[self.TableData, 2]
            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [self.SNR, DataY]
        else:
            TempSnrFactor, TempCodeRate, TempMaximumRate = [],[],[]
            for n in self.TableData:
                TempSnrFactor   = np.append(TempSnrFactor,   (Tables().getTableMcsB())[n, 0])
                TempCodeRate    = np.append(TempCodeRate ,   (Tables().getTableMcsB())[n, 1])
                TempMaximumRate = np.append(TempMaximumRate, (Tables().getTableMcsB())[n, 2])

            DataY           = (FastCalculationBlerEfficiency
                              (TempSnrFactor, TempCodeRate, TempMaximumRate)
                              .GetEfficiency(self.SNR))
            self.CurveData  = [np.matlib.repmat(self.SNR, len(DataY), 1), DataY]

        self.__setAxisLabelTitleScale('Efficiency', 'McsA')
        self.__PlotCurve('McsB')
        return [self.CurveData[0][:], self.CurveData[1][:]]
    
    def __setAxisLabelTitleScale(self, Type, Table):
        '''
        This method creates alle labels, titels & scales -> can not be seen 
        '''      
        if Type == 'BLER':
            self.Yscale    = 'log'
            self.ylabel    = 'BLER'
            self.ylim      = 10e-6
        else: 
            self.Yscale = 'linear'
            self.ylabel = 'Spectral Efficiency in [bit/s/Hz]'
            self.ylim   = (0,     np.max(self.CurveData[1]))
        self.title     = Type + " for " + Table
        self.SaveTitle = 'Plot' + Type + 'table' + Table
        self.xlimMin   = np.min(self.SNR)
        self.xlimMax   = np.max(self.SNR)
              
    def __PlotCurve(self, Table):       
        '''
        This method creates a plot for the dedicated table & type -> can not be seen 
        '''
        # Dictionary compare and set style parameter
        gridMajor     = self.StyleParameter.get('grid',       "True"  )
        gridMinor     = self.StyleParameter.get('gridMinor',  "True"  )
        linestyle     = self.StyleParameter.get('linestyle',   'solid')
        linewidth     = self.StyleParameter.get('linewidth',         1)
        plotSave      = self.StyleParameter.get('Save',          'Yes')
        # Sets style parameter plt.plot method
        plt.title(self.StyleParameter.get('title',                 self.title))
        plt.xlabel(self.StyleParameter.get('xlabel',            'SNR in [dB]'))
        plt.ylabel(self.StyleParameter.get('ylabel',              self.ylabel))
        plt.yscale(self.StyleParameter.get('yscale',              self.Yscale))
        plt.ylim(self.StyleParameter.get('ylim',                    self.ylim))
        plt.xlim(self.StyleParameter.get('xlim', (self.xlimMin, self.xlimMax)))
            
        #sets grid Major if not predefined  
        if gridMajor == 'True':
            plt.grid(b=True, which='major', color='#666666', linestyle='-')
        #sets grid Minor if not predefined
        if gridMinor == 'True':
                plt.minorticks_on()
                plt.grid(b=True, which='minor', color='#999999',
                         linestyle='-', alpha=0.2)

        #Sets labels "CqiB, McsA & McsB"
        if Table == "CqiB":
            self.label = ((Tables().getModulationOrder("MoudulationOrderCqiB"), Tables().getTableCqiB()),
                          (Tables().getCodeRate("CoderRateCqiB")))
        elif Table == "McsA":
            self.label = ((Tables().getModulationOrder("MoudulationOrderMcsA"), Tables().getTableMcsA()),
                          (Tables().getCodeRate("CoderRateMcsA")))
        elif Table == "McsB":
            self.label = ((Tables().getModulationOrder("MoudulationOrderMcsB"), Tables().getTableMcsB()),
                          (Tables().getCodeRate("CoderRateMcsB")))
        else:
            self.label = "Unknown"
        if self.IsScalarTableData:
            plt.plot(self.CurveData[0],self.CurveData[1],    
                    label     = str(self.label[0][0][self.TableData][1])+ " " + 
                                str(self.label[0][0][self.TableData][2])+ " Coderate " + 
                                str(round(self.label[1][self.TableData],2)),
                    linestyle = linestyle,
                    linewidth = linewidth)
        else:
            for n in range(len(self.TableData)):
                TempData = self.TableData[n]
                plt.plot(self.CurveData[0][n],self.CurveData[1][n],    
                    label     = str(self.label[0][0][TempData][1])+ " " + 
                                str(self.label[0][0][TempData][2])+ " Coderate " + 
                                str(round(self.label[1][TempData],2)),
                    linestyle = linestyle,
                    linewidth = linewidth)
        plt.legend(bbox_to_anchor=(1,1), loc="upper left")

        if str.upper(plotSave) == "YES":
            #Sets figure size can be changed to fit for different screens
            fig = plt.gcf()
            fig.set_size_inches(17, 8)
            plt.savefig(self.SaveTitle, bbox_inches='tight')
            plt.show()
        else:
            plt.show()
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

            Vector or Scalar //if Scalar calculates only dedicated value
        CodeRateFactor : float or int

            Vector or Scalar //if Scalar calculates only dedicated value // has to be positive
        MaximumRate : float or int

            dictionary or empty //if Scalar calculates only dedicated value // has to be larger then zero

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

PlotTable([0, 1, 15, 25], 20, {'Save': 'No'}).BlerMcsA()
