import numpy as np
import pandas as pd
import scipy as sp
from scipy import fftpack
from scipy import signal


ARMS_thresh = 1.2
dA_thresh = 10
BAI_thresh = 100000

def ARMS(alpha):
    alpha1 = alpha/np.mean(alpha)
    return np.sqrt(np.mean(alpha1**2))

def BAI(alpha,beta,delta,theta):
    return np.abs((np.diff(alpha)+np.diff(theta))*np.diff(delta)-np.diff(beta))


def dARMS(alpha):
    return np.sqrt(np.mean(np.diff(alpha)**2))

def isDrowsy(alpha, beta, delta, theta):
    ARMS_drowsy = ARMS(alpha) > ARMS_thresh
    dA_drowsy = dARMS(alpha) > dA_thresh
    BAI_drowsy = BAI(alpha,beta,delta,theta) > BAI_thresh
    return (BAI_drowsy & dA_drowsy) | (BAI_drowsy & ARMS_drowsy) | (dA_drowsy & ARMS_drowsy)

#Returns a tuple containing a list of 1000 alpha values and a list of 1000 theta values
def getEEGBuffer(alpha_values, beta_values, theta_values, delta_values):
    return isDrowsy(alpha_values, beta_values, delta_values, theta_values)

def ready():
    return True

