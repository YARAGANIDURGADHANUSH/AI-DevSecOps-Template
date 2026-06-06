from prometheus_client import Counter


# ==========================================
# API METRICS
# ==========================================

REQUESTS_TOTAL = Counter(
    "requests_total",
    "Total API Requests"
)

SUCCESSFUL_REQUESTS_TOTAL = Counter(
    "successful_requests_total",
    "Successful AI Analyses"
)


# ==========================================
# AI SECURITY METRICS
# ==========================================

PROMPT_INJECTION_TOTAL = Counter(
    "prompt_injection_total",
    "Prompt Injection Attacks Detected"
)

JAILBREAK_TOTAL = Counter(
    "jailbreak_total",
    "Jailbreak Attacks Detected"
)

PII_TOTAL = Counter(
    "pii_total",
    "PII Detections"
)

RAG_POISONING_TOTAL = Counter(
    "rag_poisoning_total",
    "RAG Poisoning Attempts Detected"
)

SECRET_LEAKAGE_TOTAL = Counter(
    "secret_leakage_total",
    "Secret Leakage Detections"
)

HALLUCINATION_TOTAL = Counter(
    "hallucination_total",
    "Hallucination Events Detected"
)


# ==========================================
# OBSERVABILITY METRICS
# ==========================================

ANALYSIS_FAILURES_TOTAL = Counter(
    "analysis_failures_total",
    "Total Analysis Failures"
)

LLM_CALL_FAILURES_TOTAL = Counter(
    "llm_call_failures_total",
    "Total LLM API Failures"
)