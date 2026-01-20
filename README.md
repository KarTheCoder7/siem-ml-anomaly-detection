# SIEM + ML Anomaly Detection (Rocket Telemetry)

This project implements an end-to-end SIEM-style telemetry monitoring and machine learning anomaly detection system using Elasticsearch, Kibana, and an Isolation Forest model.  
It simulates rocket launch telemetry and detects abnormal behavior across cyber and physical signals.

---

## Problem Statement

Modern SIEM and observability platforms generate massive volumes of telemetry, making it difficult to identify meaningful anomalies in real time.  
This project demonstrates how machine learning can be applied on top of telemetry data to automatically detect abnormal system behavior.

---

## Architecture Overview

Telemetry Generator  
→ Elasticsearch (Raw Telemetry Index)  
→ Data Cleaning & Feature Extraction  
→ Isolation Forest Anomaly Detection  
→ Elasticsearch (ML-Enriched Index)  
→ Kibana Dashboards & Alerts

---

## Key Features

- Simulated rocket telemetry generator (Python)
- Real-time ingestion into Elasticsearch
- Data cleaning and validation pipeline
- Isolation Forest–based anomaly detection
- ML-enriched telemetry indexed back into Elasticsearch
- Kibana dashboards for monitoring and investigation

---

## Telemetry Schema

| Field | Type | Description |
|-----|-----|-------------|
| @timestamp | datetime | Event timestamp |
| temp_c | float | Engine temperature |
| cpu_pct | float | System CPU utilization |
| net_kbps | float | Network throughput |
| pressure_bar | float | Chamber pressure |
| status | string | Simulated anomaly label |
| anomaly_type | string | Type of injected anomaly |
| ml_score | float | Isolation Forest anomaly score |
| ml_anomaly | boolean | ML-detected anomaly flag |

---

## Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/siem-ml-anomaly-detection.git
cd siem-ml-anomaly-detection
2. Create and activate virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Generate telemetry
bash
Copy code
python rocket_telemetry_sender.py
4. Train and run anomaly detection
bash
Copy code
python train_isolation_forest.py
5. View results
Open Kibana

Use data views:

rocket-telemetry*

rocket-telemetry-ml*

Filter anomalies using:

kql
Copy code
ml_anomaly : true
