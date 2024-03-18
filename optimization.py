# --------------------------------------------------------------------------------------------------
# import librairies 
# --------------------------------------------------------------------------------------------------
import numpy as np
import warnings


# --------------------------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------------------------
def SCM(X):  
    """ A function that computes the ML Estimator for covariance matrix estimation for gaussian data
        Inputs:
            * 𝐗 = a matrix of size p*N with each observation along column dimension
        Outputs:
            * sigma_mle = the ML estimate"""
    p = X.shape[0]
    n = X.shape[1] 

    # initialization
    sigma_mle = np.zeros((p, p)) 
  
    sigma_mle = (X@X.conj().T) / n 
return sigma_mle
