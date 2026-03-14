# SIEM + ML Anomaly Detection (Rocket Telemetry)

This project implements an end-to-end SIEM-style telemetry monitoring and machine learning anomaly detection system using Elasticsearch, Kibana, and an Isolation Forest model.

It simulates rocket launch telemetry and detects abnormal behavior across system and network signals.

---

## Problem Statement

Modern SIEM platforms collect massive volumes of telemetry data from distributed systems. Identifying abnormal system behavior within this data is difficult using traditional rule-based monitoring.

This project demonstrates how machine learning can be integrated into a telemetry pipeline to automatically detect anomalous system activity.

---

## System Architecture

Telemetry Generator (Python)
→ Elasticsearch Raw Telemetry Index  
→ Data Cleaning & Feature Extraction  
→ Isolation Forest ML Model  
→ Elasticsearch ML-Enriched Index  
→ Kibana Dashboards & Visualization

---

## Key Features

- Simulated rocket telemetry generator
- Real-time telemetry ingestion into Elasticsearch
- Data cleaning and feature extraction pipeline
- Isolation Forest anomaly detection
- ML-enriched telemetry index
- Kibana dashboards for anomaly monitoring

---

## Telemetry Schema

| Field | Type | Description |
|------|------|-------------|
| @timestamp | datetime | Event timestamp |
| temp_c | float | Engine temperature |
| cpu_pct | float | System CPU utilization |
| net_kbps | float | Network throughput |
| pressure_bar | float | Chamber pressure |
| status | string | Simulated anomaly label |
| anomaly_type | string | Type of injected anomaly |
| ml_score | float | Isolation Forest anomaly score |
| ml_anomaly | boolean | ML anomaly classification |

---

## Setup

Clone repository

```bash
git clone https://github.com/<your-username>/siem-ml-anomaly-detection.git
cd siem-ml-anomaly-detection
Create virtual environment

python3 -m venv .venv
source .venv/bin/activate
Install dependencies

pip install -r requirements.txt
Running the System
Start telemetry generator

python rocket_telemetry_sender.py
Run anomaly detection

python train_isolation_forest.py
Viewing Results
Open Kibana and create data views:

rocket-telemetry*
rocket-telemetry-ml*
Filter anomalies:

ml_anomaly : true
Technologies Used
Python
Elasticsearch
Kibana
Scikit-Learn
Pandas

