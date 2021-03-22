import matplotlib.pyplot as plt
from nr_tables import Tables
import numpy as np
import scipy.special
import numpy.matlib
import math

def PlotBlerforCqiTable2(self, SnrVectorOrScalar, LevelIndex, StyleParameter):
    

def SnrVectorCreator(SnrStart, SnrEnd, SnrResolutionInDezibel):
    if np.isscalar(SnrResolutionInDezibel):
        SnrVector = np.linspace(SnrStart, SnrEnd, int(abs(SnrStart-SnrEnd)+1/SnrResolutionInDezibel))
    return[SnrVector]

SNR = SnrVectorCreator(-10, 10, 1)
Test = 1