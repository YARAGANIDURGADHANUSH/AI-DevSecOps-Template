import csv

print("AI Security Monitoring")

with open("ai_security/pipeline_metrics.csv") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    if int(row["vulnerabilities"]) > 10:
        print(f"Anomaly detected: {row}")

print("Monitoring completed")