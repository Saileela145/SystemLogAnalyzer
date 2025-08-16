import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Log file path
log_file = "/var/log/syslog"

# Regex pattern for ISO 8601 logs
log_pattern = r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2})\s+([\w\-.]+)\s+([^\s]+):\s+(.*)"

# Severity keywords
severity_keywords = ["ERROR", "WARNING", "FAILED"]

def parse_logs(log_file):
    logs = []
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
    return pd.DataFrame(logs, columns=["timestamp", "host", "process", "message", "severity"])

def filter_logs(df, process=None, severity=None):
    if process:
        df = df[df["process"].str.contains(process, case=False, regex=False)]
    if severity:
        df = df[df["severity"].str.upper() == severity.upper()]
    return df

def visualize_data(df):
    if df.empty:
        print("⚠️ No issues found, nothing to visualize.")
        return
    
    # Ask user before showing charts
    show_chart = input("Do you want to display the charts now? (yes/no): ").strip().lower()
    
    # 1. Bar chart - Severity counts
    severity_counts = df["severity"].value_counts()
    plt.figure(figsize=(6,4))
    severity_counts.plot(kind="bar", color=["orange","red","purple"])
    plt.title("Log Issues by Severity")
    plt.xlabel("Severity")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("severity_counts.png")
    if show_chart == "yes":
        plt.show()
    plt.close()

    # 2. Bar chart - Top processes
    top_processes = df["process"].value_counts().head(5)
    plt.figure(figsize=(6,4))
    top_processes.plot(kind="bar", color="blue")
    plt.title("Top 5 Processes with Issues")
    plt.xlabel("Process")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("top_processes.png")
    if show_chart == "yes":
        plt.show()
    plt.close()

    # 3. Pie chart - Severity distribution
    plt.figure(figsize=(5,5))
    severity_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["orange","red","purple"])
    plt.title("Severity Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("severity_pie.png")
    if show_chart == "yes":
        plt.show()
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer with CLI filtering")
    parser.add_argument("--process", help="Filter logs by process name")
    parser.add_argument("--severity", help="Filter logs by severity (ERROR, WARNING, FAILED)")
    parser.add_argument("--top", type=int, default=5, help="Number of top processes to display")
    args = parser.parse_args()

    df = parse_logs(log_file)
    df = filter_logs(df, args.process, args.severity)
    df.to_csv("flagged_logs.csv", index=False)
    print("✅ Log analysis complete. Results saved to flagged_logs.csv")

    if not df.empty:
        # Terminal summary
        print("\n📊 Summary of Issues:")
        for sev, count in df["severity"].value_counts().items():
            print(f"{sev}: {count}")

        print(f"\n🔥 Top {args.top} Processes with Issues:")
        for proc, count in df["process"].value_counts().head(args.top).items():
            print(f"{proc}: {count}")

        visualize_data(df)
        print("\n📈 Charts saved: severity_counts.png, top_processes.png, severity_pie.png")
    else:
        print("⚠️ No issues found for the given filters.")

if __name__ == "__main__":
    main()
