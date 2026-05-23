# ⚛️ KEFF Data | PWR-SMR-2026-01 Dataset (Community Edition)

**Bridging academia and industry with high-fidelity synthetic simulation data for next-generation nuclear AI models.**

PWR-SMR-2026-01 is a community research dataset from KEFF Data for non-commercial nuclear AI research, anomaly-detection benchmarking, and offline surrogate-model development. The release provides high-fidelity synthetic Monte Carlo simulation data for a 17x17 PWR SMR lattice under a controlled set of static reactor-physics states.

## Dataset Access

The full **80+ GB raw HDF5 dataset** is hosted on Hugging Face:

**Download:** [https://huggingface.co/datasets/keffdata/pwr-smr-2026-01-community](https://huggingface.co/datasets/keffdata/pwr-smr-2026-01-community)

Researchers can download the dataset directly from Hugging Face or use the helper script provided in this repository:

```bash
pip install huggingface_hub
python scripts/download_hf.py --output-dir data/pwr-smr-2026-01-community
```

The repository intentionally remains lightweight. Large dataset artifacts are excluded from version control and should be downloaded from the official Hugging Face dataset page.

## Specifications Table

| Specification | Value |
| --- | --- |
| Simulation Engine | OpenMC |
| Cross-Section Library | ENDF/B-VIII.0 |
| Cases | 1,518 unique static states |
| Histories | 12,500,000 per case |
| Target Architecture | 17x17 PWR SMR Lattice |

## Verification & Validation

The dataset was verified for static Monte Carlo reactor-physics research and offline AI/ML benchmarking. Source convergence quality is reflected by a **Shannon entropy drift of 0.0419%**.

The nominal statistical uncertainty is conservatively corrected to **±56 pcm** due to lag-1 autocorrelation, providing a practical uncertainty floor for anomaly-detection experiments and architecture selection.

## Anomaly Regimes

Model selection should account for the separability index $Z = |\Delta\rho| / \sigma_{corrected}$, where the corrected uncertainty floor is **±56 pcm**.

**Regime A: Macro-Anomalies** include high-separability events with **Z > 3.0**. These cases are suitable for single-frame CNNs and MLPs because the signal is strong enough to separate from Monte Carlo statistical uncertainty in individual snapshots.

**Regime B: Micro-Perturbations** include low-separability events with **Z < 3.0**. These cases are better suited for LSTMs, Transformers, and other temporal or sequence-aware architectures because the physical signal approaches the statistical noise floor.

## Licensing

PWR-SMR-2026-01 Community Edition is released under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

Academic researchers, students, educators, and non-commercial research groups may use the dataset under the terms of CC BY-NC 4.0. Commercial use is not permitted under the Community Edition license.

Commercial entities must obtain a proprietary license from KEFF Data before using the dataset, derived models, benchmarks, methodology, or outputs for commercial R&D, product development, internal evaluation, model training, consulting, deployment, or any revenue-generating activity. For licensing inquiries, contact **contact@keffdata.com**.

## Citation & DOI

Official DOI: [10.57967/hf/8914](https://doi.org/10.57967/hf/8914)

Please cite this dataset in academic work using the following BibTeX entry:

```bibtex
@dataset{aslan2026keff,
author       = {Caglayan Aslan},
title        = {PWR-SMR-2026-01: High-Fidelity Monte Carlo Dataset for Nuclear Anomaly Detection},
publisher    = {Hugging Face},
year         = {2026},
month        = {March},
doi          = {10.57967/hf/8914},
url          = {https://doi.org/10.57967/hf/8914},
note         = {KEFF Data - Document ID: RED-PAPER-PH1-SMR}}
```
