# SIEM + ML Anomaly Detection

This project implements an end-to-end telemetry monitoring and anomaly detection system using Elasticsearch, Kibana, and Isolation Forest.

## Architecture

Telemetry Generator → Elasticsearch → Data Cleaning → Isolation Forest → Enriched Index → Dashboards & Alerts

## Features

- Simulated rocket telemetry generator
- Real-time ingestion into Elasticsearch
- Data cleaning and validation pipeline
- Isolation Forest anomaly detection
- ML-enriched telemetry index
- Kibana dashboards and alerts

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/siem-ml-anomaly-detection.git
cd siem-ml-anomaly-detection
