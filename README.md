# Adaptive Multi-Modal Anomaly Detection

A cloud-native ML framework for detecting subtle anomalies in distributed systems by fusing metrics, logs, and traces.

This project demonstrates a modular, self-evolving, and explainable anomaly detection pipeline tailored for modern observability challenges in heterogeneous cloud workloads.

---

## Project Objectives

Traditional monitoring systems often fail in complex environments where signals are disjointed. This project aims to:

- Fuse heterogeneous telemetry (metrics, logs, traces) into a unified representation
- Detect both known and novel anomalies using hybrid machine learning models
- Continuously adapt through statistical drift detection and retraining
- Explain anomaly decisions using model-agnostic interpretability (SHAP)
- Integrate into cloud-native ecosystems with scalable architecture

---

## System Architecture

Below is a high-level diagram of the pipeline architecture:

![Architecture Overview](architecture/overview.png)


## Key Components
**1. Data Simulation**
- Synthetic telemetry generator (`generate_data.py`)
- Injects controlled anomalies (e.g., CPU spikes, log bursts, latency surges)

**2. Feature Engineering**
- Rolling statistics, lag features, correlation windows
- Frequency domain analysis using FFT
- Z-score normalization and derived anomaly-sensitive indicators
- Implemented in `feature-engineering.ipynb`

**3. Anomaly Detection**
- Unsupervised modeling with Isolation Forest
- Evaluation against synthetic ground truth
- Visual anomaly scoring
- See `modeling.ipynb`

**4. Explainability**
- SHAP-based explanation of anomaly decisions
- Local and global feature attributions
- Interactive visualizations for root cause inspection
- Implemented in `explainability.ipynb`

--

