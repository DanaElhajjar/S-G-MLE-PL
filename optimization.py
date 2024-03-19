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

def Gaussian_complex_theta_recursif(X, X_past, x_newdata, C, diag_w_past, iter_PL, iter_max_BCD, phasecorrectionchoice, tol=0.001):
    # initialization
    stop_cond = np.inf
    iteration = 0

    p, n = X_past.shape
    k = 1
    inv_C = np.linalg.inv(C)
    S = SCM(X) # Initialise estimate to SCM
    S = np.asarray(S, dtype=np.complex128)
    w_past = np.diag(diag_w_past) # diagonal matrix of vector past w_theta 
    new_w_theta =np.array(1) # initialize the new w_theta to 1
    Sigma = ToeplitzMatrix(0.5, p+k) # initialize the coherence matrix to a Toeplitz
    new_past_coherence = Sigma[p, 0:p] # extract the the vector of coherence between the past imagesand the new ones
    variance_newdata = Sigma[p, p] # extract the variance of the new image

    x_newdata_reshaped = x_newdata.reshape((1, x_newdata.shape[0])) # inv(X_past@X_past.conj().T)

    # computations based only on the known parameters
    temp11 = x_newdata_reshaped@X_past.conj().T@inv_C.conj().T@diag_w_past 
    temp12 = x_newdata_reshaped.conj()@X_past.T@inv_C.T@diag_w_past.conj() 
    temp13 = diag_w_past.conj().T@inv_C@X_past@X_past.conj().T@inv_C.conj().T@diag_w_past 
    temp14 = diag_w_past.T@inv_C.conj()@X_past.conj()@X_past.T@inv_C.T@diag_w_past.conj() 
    temp15 = np.linalg.inv(temp13 + temp14)

    while (stop_cond>tol) and (iteration<iter_max_BCD):
        if iteration == iter_max_BCD:
            warnings.warn('Recursive algorithm did not converge')

        # bloc 1 : computation of the coherence between the new and the past images
        new_past_coherence = np.sum(new_w_theta.conj()*temp11 + new_w_theta*temp12, axis = 0) @ temp15

        # bloc 2 : computation of the new w_theta
        temp21 = X_past.conj().T@inv_C.conj().T@diag_w_past@new_past_coherence.T
        temp22 = new_past_coherence@diag_w_past.conj().T@inv_C@X_past@X_past.conj().T@inv_C.conj().T@diag_w_past@new_past_coherence.T
        new_w_theta = np.sum(x_newdata_reshaped * temp21)* (1/temp22)
        new_w_theta_norm = np.exp(1j * np.angle(new_w_theta)) # projection of new_w_theta on the complex circle (radius = 1)

        # bloc 3 : computation of the variance of the new image
        temp31 = new_past_coherence@diag_w_past.T@inv_C.conj()@X_past.conj()
        temp32 = x_newdata_reshaped.conj() - new_w_theta_norm.conj() * temp31
        temp33 = new_past_coherence@diag_w_past.conj().T@inv_C@X_past
        temp34 = x_newdata_reshaped - new_w_theta_norm * temp33
        temp35 = new_past_coherence@diag_w_past.conj().T@inv_C@diag_w_past@new_past_coherence.T
        variance_newdata_new = (1/n * np.sum(temp32 * temp34) + temp35).real
        
        # stop condition
        stop_cond = np.linalg.norm(variance_newdata_new - variance_newdata) / np.linalg.norm(variance_newdata)

        iteration = iteration + 1
        variance_newdata = variance_newdata_new
        new_w_theta = new_w_theta_norm

    
    line_vector = new_w_theta*new_past_coherence@diag_w_past.conj().T
    C_tilde = add_one_obs(C, line_vector, variance_newdata)
    C_tilde = np.asarray(C_tilde, dtype=np.complex128)
    w_all = np.append(w_past, new_w_theta)
    diag_w = np.diag(w_all)

    # corrections
    if phasecorrectionchoice == 3:
        new_phase = phasecorrection3(C_tilde)
        res = new_phase[-1]
        return C_tilde, res
    elif phasecorrectionchoice == 4:
        Sigma = (((diag_w.conj().T).dot(S)).dot(diag_w)).real
        new_phase = phasecorrection4(C_tilde, Sigma)
        res = new_phase[-1]
        return C_tilde, res
