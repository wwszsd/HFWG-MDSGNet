# HFWG-MDSGNet

Code for spectral compressive imaging (SCI) reconstruction — a single-network baseline for reconstructing hyperspectral images (HSI) from snapshot compressed measurements.

## Introduction

Snapshot compressive imaging (SCI) captures an entire 3D hyperspectral datacube in a single coded exposure and recovers the original HSI from the compressed 2D measurement with a reconstruction algorithm. This repository provides the **training, testing, and visualization** code for **HFWG-MDSGNet**, a spectral-wise reconstruction network. The network maps a compressed measurement to a 28-band hyperspectral image covering approximately 450–650 nm, and can be trained on both simulated and real captured data.

This codebase is kept as a compact baseline: it contains a single network architecture and the necessary data-loading, training, testing, quality-assessment, and visualization scripts.

## Paper

**Physics-Informed High-Fidelity Weight Generation with Multi-Scale Detail–Structure Guidance for Hyperspectral Imaging**

Ruoyu Dong, Zhiguo Wang*, Wei Wang, and Rui Zheng
Key Laboratory of Physical Electronics and Devices, Ministry of Education, School of Electronic Science and Engineering, Xi'an Jiaotong University, Xi'an, China

*Corresponding author: wangzg@mail.xjtu.edu.cn

## Environment

- Python 3 (e.g., Anaconda)
- NVIDIA GPU + CUDA
- Install dependencies:

```shell
pip install -r requirements.txt
```

## Dataset

Prepare the following datasets and place them under `datasets/`:

```
datasets/
├── cave_1024_28/          # simulation training set (28-band)
│   ├── scene1.mat
│   └── ...
├── CAVE_512_28/           # real training set
│   ├── scene1.mat
│   └── ...
├── KAIST_CVPR2021/        # real training set
│   ├── 1.mat
│   └── ...
├── TSA_simu_data/         # simulation test set
│   ├── mask.mat
│   └── Truth/
│       ├── scene01.mat
│       └── ...
└── TSA_real_data/         # real test set
    ├── mask.mat
    └── Measurements/
        ├── scene1.mat
        └── ...
```

Following the common practice, `cave_1024_28` is used as the simulation training set, and both `CAVE_512_28` and `KAIST_CVPR2021` are used as the real training set.

## Training

### Simulation

```shell
cd simulation/train_code
python train.py --template hfwg_mdsgnet --outf ./exp/hfwg_mdsgnet/ --method hfwg_mdsgnet
```

The training log, checkpoints, and reconstructed HSI will be saved under `simulation/train_code/exp/`.

### Real

```shell
cd real/train_code
python train.py --template hfwg_mdsgnet --outf ./exp/hfwg_mdsgnet/ --method hfwg_mdsgnet
```

## Testing

### Simulation

Place the pre-trained model at `simulation/test_code/model_zoo/` and run:

```shell
cd simulation/test_code
python test.py --template hfwg_mdsgnet --outf ./exp/hfwg_mdsgnet/ --method hfwg_mdsgnet --pretrained_model_path ./model_zoo/hfwg_mdsgnet.pth
```

The reconstructed HSIs are output to `simulation/test_code/exp/`.

### Real

```shell
cd real/test_code
python test.py --data_path ../../datasets/TSA_real_data/Measurements/ --mask_path ../../datasets/TSA_real_data/mask.mat --pretrained_model_path ./model_zoo/hfwg_mdsgnet.pth --outf ./exp/real_test_result/
```

## Quality Assessment

Compute PSNR / SSIM of the reconstructed HSIs on the simulation dataset by placing the results into `simulation/test_code/Quality_Metrics/results` and running the MATLAB script:

```shell
Cal_quality_assessment.m
```

## Visualization

- **Simulation results**: put the reconstructed HSI into `visualization/simulation_results/results` (renamed as `hfwg_mdsgnet.mat`) and run `show_simulation.m` to generate the RGB image.
- **Real results**: put the reconstructed HSI into `visualization/real_results/results` (renamed as `hfwg_mdsgnet.mat`) and run `show_real.m` to generate the RGB image.
- **Spectral density lines**: use `show_line.m`.

## Citation

If this repository is helpful in your research, please consider citing:

```bibtex
@article{dong2026physics,
  title={Physics-Informed High-Fidelity Weight Generation with Multi-Scale Detail-Structure Guidance for Hyperspectral Imaging},
  author={Dong, Ruoyu and Wang, Zhiguo and Wang, Wei and Zheng, Rui},
  year={2026}
}
```