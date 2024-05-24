# S-G-MLE-PL

This repository is dedicated to the implementation of Sequential Gaussian Phase Linking based on Maximum Likelihood Estimation (S-G-MLE-PL). This approach aims to estimate the phase of a new SAR image based on a block of past images.

The repository provides reproduction of the results presented in the paper:
> Dana EL HAJJAR, Yajing YAN, Guillaume GINOLHAC, an Mohammed Nabil EL KORSO, "SEQUENTIAL PHASE LINKING : PROGRESSIVE INTEGRATION OF SAR IMAGES FOR OPERATIONAL PHASE ESTIMATION", IGARSS 2024

## Code organisation

## Environment

A conda environment is provided in the file `environment.yml` To create and use it run:

```console
conda env create -f environment.yml
conda activate s-g-mle-pl
```

### Reproducing the results of the paper

| Command                           | Figure | Parameters                  |
|-----------------------------------|--------|-----------------------------|
| `python mse_simulation [OPTIONS]` | 2      | n, l, rho, number of trials |
|                                   |        |                             |
|                                   |        |                             |

### Authors

* Dana El Hajjar, mail:
* Yajing Yan
...

Copyright @Université Savoie Mont Blanc, 2024
