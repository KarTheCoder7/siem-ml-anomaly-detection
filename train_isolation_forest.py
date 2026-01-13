from elasticsearch import Elasticsearch
import pandas as pd
from sklearn.ensemble import IsolationForest

ES_HOST = "http://100.24.140.127:9200"
RAW_INDEX = "rocket-telemetry"
ML_INDEX = "rocket-telemetry-ml"

es = Elasticsearch(ES_HOST)
resp = es.search(index=RAW_INDEX, body={"size": 5000, "query": {"match_all": {}}})

df = pd.DataFrame([hit["_source"] for hit in resp["hits"]["hits"]])
X = df[["temp_c", "cpu_pct", "net_kbps", "pressure_bar"]]

model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(X)

df["ml_score"] = model.decision_function(X)
df["ml_anomaly"] = model.predict(X) == -1
df["model"] = "isolation_forest_v1"

for _, row in df.iterrows():
    es.index(index=ML_INDEX, document=row.to_dict())

print("Scored and indexed", len(df), "events")
