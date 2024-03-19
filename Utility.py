
def ToeplitzMatrix(rho, p):
    """ A function that computes a Hermitian semi-positive matrix.
            Inputs:
                * rho = a scalar
                * p = size of matrix
            Outputs:
                * the matrix """

    return sp.linalg.toeplitz(np.power(rho, np.arange(0, p)))
    # sp.linalg.toeplitz : Construct a Toeplitz matrix.

def CRB_Covar_Gaussian_Real(𝚺,echelle):
    "CRB Covar Matrix - Gaussian Data"

    m=𝚺.shape[0]
    # N=echelle.shape
    𝚺_inv = inv(𝚺)

    # Construction basis
    𝛀 = basis_euc_sym_mat_real(m)
    M = 𝛀.shape[2] 

    # Construction de la FIM
    F=np.zeros((M,M))
    for i in range(M):
        for j in range(M):
            F[i,j]=np.matrix.trace(𝚺_inv@𝛀[:,:,i]@𝚺_inv@𝛀[:,:,j])

    # CRB_Gaussian=np.zeros(N)
    CRB_Gaussian=2*np.matrix.trace(inv(F))/echelle
    return(CRB_Gaussian)
