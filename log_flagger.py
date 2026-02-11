import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Log file path (fallback for CI if syslog not available)
log_file = "/var/log/syslog"

# Regex pattern for ISO 8601 logs
log_pattern = r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2})\s+([\w\-.]+)\s+([^\s]+):\s+(.*)"

# Severity keywords
severity_keywords = ["ERROR", "WARNING", "FAILED"]


def parse_logs(log_file):
    logs = []

    # If log file doesn't exist (like in GitHub runner), return empty DataFrame
    if not os.path.exists(log_file):
        print("⚠️ Log file not found. Skipping parsing.")
        return pd.DataFrame(columns=["timestamp", "host", "process", "message", "severity"])

    with open(log_file, "r") as f:
        for line in f:
            match = re.match(log_pattern, line)
            if match:
                timestamp, host, process, message = match.groups()
                severity = None
                for keyword in severity_keywords:
                    if keyword in message:
                        severity = keyword
                        break
                if severity:
                    logs.append([timestamp, host, process, message, severity])

    return pd.DataFrame(log
