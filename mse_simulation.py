import numpy as np
from src.estimation import phasecorrection3

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser("MSE simulation of the phase difference")
    parser.add_argument("--l", type=int, help="Number of time stamps in the time series", default=20)
    parser.add_argument("--rho", type=float, default=0.7, help="Correlation coefficient for Toeplitz coherence matrix")
    parser.add_argument("--n_list", type=str, default=", ".join([str(x) for x in range(10, 400, 20)]),
                        help="List of the size of patch to use")
    parser.add_argument("--n_trials", type=int, default=1000, help="Number of Monte-Carlo Trials")
    args = parser.parse_args()

    # Parse n values for str
    args.n_list = [int(x) for x in args.n_list.split(",")]

    print("MSE over size of patch simulation with parameters:")
    for key, val in vars(args).items():
        print(f"  * {key}: {val}")

    

    