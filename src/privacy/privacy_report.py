import os
from datetime import datetime

REPORTS_DIR = "privacy_reports"

def save_privacy_report(query, answer, context, risk_score, pii_data=None):
    """Saves a detailed privacy report to a timestamped file."""

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{REPORTS_DIR}/report_{timestamp}.txt"

    report_content = f"""
================ PRIVACY REPORT ================

Timestamp      : {timestamp}

User Query     :
{query}

Privacy Score  : {risk_score:.2f}

PII Detected   : {pii_data if pii_data else "None"}



Generated Answer:
------------------------------------------------
{answer}

=================================================
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)

    return filename


def format_context(context):
    """Formats all retrieved chunks for readability."""
    out = ""
    for i, c in enumerate(context):
        out += f"[Chunk {i+1}]\n{c}\n\n"
    return out
