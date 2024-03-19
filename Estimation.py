# --------------------------------------------------------------------------------------------------
# import librairies 
# --------------------------------------------------------------------------------------------------
import numpy as np

# --------------------------------------------------------------------------------------------------
# functions
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

def phasecorrection3(covmatrix): 
    """
    A function that corrects the phase of a covariance matrix to ensure phase alignment with the first element.
        Inputs:
            * covmatrix : Covariance matrix representing the phase information.
        Outputs:
            * phase_minus0 : corrected phases ensuring alignment with the phase of the first element. """
    phase = -np.angle(covmatrix[0,:])
    phase_minus0 = phase-phase[0]
    return phase_minus0

def phasecorrection4(covmatrix,sigmamatrix):
    """    
    A function that corrects the phase of a covariance matrix based on the sub-diagonal elements and sigma matrix.
        Inputs:
            * covmatrix : Covariance matrix 
            * sigmamatrix : Coherence matrix
        Outputs:
        * phase : corrected phases based on sub-diagonal elements and coherence matrix. """
    subdiagphase = np.zeros((sigmamatrix.shape[0]-1))
    phase = np.zeros((sigmamatrix.shape[0]))
    for i in range (sigmamatrix.shape[0]-1):
        subdiagphase[i] = ((np.angle(covmatrix[i,i+1])) +np.pi)%(2*np.pi)-np.pi
        phase[i+1] = (phase[i]+subdiagphase[i]+np.pi)%(2*np.pi)-np.pi
    return -phase
