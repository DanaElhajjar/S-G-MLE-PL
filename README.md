# S-G-MLE-PL

This repository is dedicated to the implementation of Sequential Gaussian Phase Linking based on Maximum Likelihood Estimation (S-G-MLE-PL). This approach aims to estimate the phase of a new SAR image based on a block of past images.

The repository provides reproduction of the results presented in the paper:
> Dana EL HAJJAR, Yajing YAN, Guillaume GINOLHAC, and Mohammed Nabil EL KORSO, "SEQUENTIAL PHASE LINKING : PROGRESSIVE INTEGRATION OF SAR IMAGES FOR OPERATIONAL PHASE ESTIMATION", IGARSS 2024

If you use any of the code or data provided here, please cite the above paper.

## Code organisation

├── environment.yml<br>
├── exp<br>
│   ├── mse_simulation.py<br>
│   └── simulation.py<br>
├── real_data<br>
│   ├── realdata_interrferogram.py<br>
│   └── real_data.py<br>
├── README.md<br>
└── src<br>
    ├── estimation.py<br>
    ├── generation.py<br>
    ├── __init__.py<br>
    ├── optimization.py<br>
    └── utility.py<br>


The main code for the methods is provided in src/ directory. The file optimization.py provides the function for the S-G-MLE-PL algorithm. The folder exp/ provides the simulations and the folder rd/ contains the processing on the real data. The data/ directory is used to store the dataset used. 


## Environment

A conda environment is provided in the file `environment.yml` To create and use it run:

```console
conda env create -f environment.yml
conda activate s-g-mle-pl
```

## Dataset

For real-world example, you need to download the dataset and decompress it into `data` folder:

```console
wget https://zenodo.org/records/11283419/files/Sentinel1_timeseries_mexico_interfero.zip?download=1
unzip data.zip data/
```

### Reproducing the results of the paper

| Command                             | Figure | Parameters                       |
|-------------------------------------|--------|----------------------------------|
| `python mse_simulation [OPTIONS]`   |   2    | n, l, rho, number of trials      |
| `python computation_time [OPTIONS]` |   3    | n, p_list, rho, number of trials |
| `python real data [OPTIONS]`        |   4    | n, l                             |

### Authors

* Dana El Hajjar, mail: dana.el-hajjar@univ-smb.fr, dana.el-hajjar@centralesupelec.fr
* Yajing Yan, mail: yajing.yan@univ-smb.fr
* Guillaume Ginolhac, mail: guillaume.ginolhac@univ-smb.fr
* Mohammed Nabil El Korso, mail: mohammed.nabil.el-korso@centralesupelec.fr


Copyright @Université Savoie Mont Blanc, 2024
