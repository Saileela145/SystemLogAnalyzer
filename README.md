# 📝 SystemLogAnalyzer  

A Python-based tool to analyze Linux system logs, flag anomalies (ERROR, WARNING, FAILED), and generate useful reports with charts.  

## 🚀 Features  
- Parse `/var/log/syslog` for anomalies  
- Identify severity levels (Error, Warning, Failed)  
- Save flagged logs to CSV for further analysis  
- Generate visual reports:  
  - 📊 Bar chart of severity counts  
  - 🥧 Pie chart of severity distribution  
  - 📈 Top processes causing issues  

---

## 📂 Project Structure  
SystemLogAnalyzer/

│── README.md # Project documentation

│── log_flagger.py # Main Python script

│── flagged_logs.csv # Flagged log entries (output)

│── severity_counts.png # Bar chart of severity

│── severity_pie.png # Pie chart of severity

│── top_processes.png # Top processes chart

---

## ⚙️ Installation & Usage  

1. **Clone the Repository**  
```bash
git clone https://github.com/Saileela145/SystemLogAnalyzer.git
cd SystemLogAnalyzer
```
2. **Run the Script**
```
python3 log_flagger.py
```
3. **Check Outputs**
``` 
flagged_logs.csv → contains flagged anomalies

severity_counts.png → bar chart of severity levels

severity_pie.png → pie chart of severity distribution

top_processes.png → top processes causing issues
```
#### 📊 Sample Output

**Example Flagged Logs (CSV)**
timestamp           | host     | process   | severity | message
2025-08-12 10:15:22 | myhost   | kernel    | ERROR    | Disk failure detected
2025-08-12 10:18:45 | myhost   | systemd   | WARNING  | Service restart attempted

📊 Example Charts
Bar Chart — Severity Counts

Pie Chart — Severity Distribution

Top Processes Chart
📑 Sample Flagged Logs Output

When the script runs, it generates a CSV file (flagged_logs.csv) with the anomalies.
Here’s a sample preview of the CSV data:
| timestamp           | host       | process | pid  | message                                  | severity |
| ------------------- | ---------- | ------- | ---- | ---------------------------------------- | -------- |
| 2025-08-16 10:05:01 | myhostname | sshd    | 1234 | Failed password for invalid user admin   | FAILED   |
| 2025-08-16 11:12:45 | myhostname | kernel  | 5678 | WARNING: CPU temperature above threshold | WARNING  |
| 2025-08-16 11:50:30 | myhostname | systemd | 9102 | ERROR: Failed to start NetworkManager    | ERROR    |

**🛠️ Tech Stack**

Language: Python 3

Libraries: pandas, matplotlib

**🤝 Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

**📜 License**

This project is licensed under the MIT License.

## ⚙️ How It Works

1. Reads Linux system logs from `/var/log/syslog`
2. Scans log entries for known severity keywords:
   - ERROR
   - WARNING
   - FAILED
3. Flags suspicious or critical log entries
4. Saves flagged logs into a CSV file for review
5. Generates visual reports:
   - Severity distribution
   - Top processes causing issues

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Saileela145/SystemLogAnalyzer.git
   cd SystemLogAnalyzer
   ```
2.Run the script
```
python3 log_flagger.py
```

Add this section near the bottom:

```markdown
## 🧠 Real-World Use Case

System administrators can use this tool to:
- Quickly identify critical system issues
- Monitor recurring warnings and failures
- Analyze system health during outages
- Support incident investigation and root cause analysis

This tool can be integrated into:
- Cron jobs
- Monitoring pipelines
- DevOps alerting workflows
   


