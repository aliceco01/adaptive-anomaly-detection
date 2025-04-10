# Adaptive Multi-Modal Anomaly Detection (AMMAD)

A production-grade anomaly detection framework built for heterogeneous cloud environments. This project fuses logs, metrics, and traces using hybrid ML models with self-evolving feedback loops for drift adaptation.



##  System Overview

This repository includes:
- A full whitepaper-style explanation of the architecture
- Hands-on PoC implementation using Isolation Forest + Autoencoders
- Diagrams for ingestion, feature fusion, and model serving
- Future-forward extensions with Transformers and causal overlays

> ⚠️ This system is designed to scale with AWS-native infrastructure (Kafka, Lambda, S3, SageMaker) and integrates into CI/CD with explainable ML outputs.

##  Repo Contents

```
adaptive-anomaly-detection/
├── README.md
├── architecture/          # Diagrams: AMMAD architecture, SHAP, PCA, ingestion
├── src/                   # Full implementation code
├── notebooks/             # Optional EDA and visual analysis
├── data/                  # Synthetic telemetry or sample input
└── LICENSE
```

##  Architecture Diagram

![image](https://github.com/user-attachments/assets/82de59ac-52f8-48e4-bbd7-bbd76e748f67)

Data Ingestion: Kafka / Kinesis connects to Prometheus (metrics), ELK (logs), and X-Ray / Jaeger (traces).

Feature Fusion: Aligns telemetry in time, embeds structured logs, normalizes signal strengths.

Model Core: Combines supervised (e.g., SVM, Random Forest) and unsupervised (e.g., Autoencoder, Isolation Forest) learners.

Anomaly Scoring: Produces scores via ensemble voting or hybrid strategies.

Adaptation Loop: Detects drift and retrains models as needed.

## Getting Started

To run the proof-of-concept demo:

```bash
cd src/
python anomaly_detection.py
```

Outputs anomaly detections over time and saves visualization to `anomaly_detection_results.png`.

##  Future Work

- Transformer fusion layers
- Cost-aware probabilistic alerting
- Causal graph overlays for RCA

---

By [Alice Cohen](https://github.com/aliceco01) | AWS DevOps Delivery Consultant
