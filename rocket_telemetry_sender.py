import random
import time
from datetime import datetime, timezone
from elasticsearch import Elasticsearch

# CHANGE THIS to your Windows machine IP
ES_HOST = "http://100.24.140.127:9200"

es = Elasticsearch(ES_HOST)

INDEX_NAME = "rocket-telemetry"

def generate_event():
    anomaly = random.random() < 0.04  # 4% anomalies

    temp = random.gauss(780, 25)
    pressure = random.gauss(5.0, 0.3)
    cpu = random.gauss(35, 10)
    net = random.gauss(500, 150)

    if anomaly:
        temp += random.uniform(150, 300)
        cpu += random.uniform(40, 60)
        status = "anomalous"
    else:
        status = "nominal"

    event = {
        "@timestamp": datetime.now(timezone.utc).isoformat(),
        "host": {"name": "rocket-control-windows"},
        "scenario": "launch",
        "event_type": "telemetry",
        "temp_c": round(temp, 2),
        "pressure_bar": round(pressure, 2),
        "cpu_pct": round(cpu, 2),
        "net_kbps": round(net, 2),
        "status": status
    }

    return event

def send_event(event):
    es.index(index=INDEX_NAME, document=event)

if __name__ == "__main__":
    print("Sending rocket telemetry...")
    for i in range(5200):
        e = generate_event()
        send_event(e)
        time.sleep(0.05)

    print("Done.")
