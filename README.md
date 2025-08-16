# SystemLogAnalyzer

## What the Project Does
SystemLogAnalyzer is a Python tool that helps system administrators analyze system logs automatically. It detects and flags issues like ERROR, WARNING, and FAILED messages, summarizes the results, and generates visual charts.

## Features
- Parses system logs (Linux syslog or structured CSV logs)
- Flags errors, warnings, and failed messages
- Provides a summary of issues and top processes causing them
- Generates charts: bar charts for severity and top processes, pie chart for severity distribution
- Optional display of charts
- Exports flagged logs to CSV for further analysis

## How to Run
1. Make sure Python 3 and required packages are installed (`pandas`, `matplotlib`, `argparse`)
2. Run the script:
```bash
python3 log_flagger.py
