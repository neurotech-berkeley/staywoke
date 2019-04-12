import numpy as np
from scipy import signal

#extract relative band powers (a float between 0 and 1)
theta_relative = '/muse/elements/theta_relative' #EDIT PATH TO MATCH YOUR OWN
alpha_relative = '/muse/elements/alpha_relative' #EDIT PATH TO MATCH YOUR OWN

#filter relative band powers using 4th order type II Chebyshev filter
#isolate slow waves

#for theta
rs_theta = '??' #minimum attenuation required in the stop band
Wn_theta = '??' #critical frequency after which the wave is no longer considered a "slow wave"
b_theta, a_theta = scipy.signal.cheby2(4, rs_theta, Wn_theta)

w_theta, h_theta = scipy.signal.freqz(b_theta, a_theta) #extract frequency response

#for alpha
rs_alpha = '??' #minimum attenuation required in the stop band
Wn_alpha = '??' #critical frequency after which the wave is no longer considered a "slow wave"
b_alpha, a_alpha = scipy.signal.cheby2(4, rs_alpha, Wn_alpha)

w_alpha, h_alpha = scipy.signal.freqz(b_alpha, a_theta) #extract frequency response


#STUCK ON HOW TO USE FREQUENCY RESPONSE TO FILTER OUR THETA/ALPHA WAVES INTO SLOW WAVES:
# 1) how to use the frequency response to filter the data?
# 2) how the relative band powers play into these calculations?

#sleep-onset detection rules: need to estimate optimal V, lambda parameters


import scipy as sp
from scipy import fftpack
import numpy as np

# Artifact Removal - used only on preprocessing of raw sleep data
#sp.signal.butter(..)

# Converts a signal from its original domain to a representation in the frequency domain -
# used only on preprocessing of raw sleep data

#fftpack.fft(..)

# Power Ratio Calculation
# Forth order type two Chebyshev filter
# scipy.signal.cheb2(N=4, ...)

# Final Cut (final step)

# Estimating optimal parameters V, lambda
def sign(x):
    return {
    if x > 0: 1,

    elif x == 0: 0,

    else -1 }[True]

def H(x):
    return 1 if x > 0 else 0

def grid_search(S_theta, S_alpha, N_1, N_2):
    err = float('inf')
    # ...
    return V, alpha

# Calculating emergy power ratio
def totalPS(data): #input transformed data (needs to have an x axis of frequency)
    Fmin = 0.3
    Fmax = 64
    return integrate.quad(data, Fmin, Fmax)

def PR(flow, fhigh, data):
    return (integrate.quad(data, flow, fhigh)) / totalPS(data)

def alpha_theta_PRs(data):
    PRalpha = PR(8, 12, data)
    PRtheta = PR(4, 8 data)
    return PRalpha, PRtheta

h = 1456

eeg1 = []
eeg2 = []
eeg3 = []
eeg4 = []

def getEEGBuffer(eegBuff):
    eeg1 += [eegBuff[0]]
    eeg2 += [eegBuff[1]]
    eeg3 += [eegBuff[2]]
    eeg4 += [eegBuff[3]]
    print(eegBuff)


