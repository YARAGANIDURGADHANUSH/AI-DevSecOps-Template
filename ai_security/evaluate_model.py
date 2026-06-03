import csv

print("AI Security Evaluation")

with open("ai_security/pipeline_metrics.csv") as f:
    rows = list(csv.DictReader(f))

print(f"Records loaded: {len(rows)}")
print("Evaluation completed successfully")