# Python Port Scanner

## 📌 Project Overview
A basic Python-based **Port Scanner** that allows you to:
- Scan **custom or full port ranges**
- Choose between **TCP** or **UDP** scanning
- Display **open ports with service names**
- Save scan results into a formatted **report file**
  

## 🛠️ Features
- Custom IP input
- Choose TCP or UDP protocol
- Port range or full port scan (0–65535)
- Open port detection with associated service name
- Saves scan details (IP, protocol, time, open ports) into `scan_report.txt`


## 🚀 How It Works
1. User inputs target IP address.
2. Chooses between custom port range or full port scan.
3. Chooses scan type (TCP or UDP).
4. Scan begins with a progress bar.
5. Open ports and corresponding service names are printed.
6. Optionally, user can generate a report saved as `scan_report.txt`.

## 📁 Report Format Example
```
===== Port Scan Report =====
Target IP    : 192.168.233.130
Scan Type    : TCP
Port Range   : 0-80
Scan Time    : 2025-04-30 12:31:19.452003
Open Ports   :
- Port 21 (ftp)
- Port 22 (ssh)
- Port 23 (telnet)
- Port 25 (smtp)
- Port 53 (domain)
- Port 80 (http)
```

## 💻 Requirements
- Python 3.x
- Works on Windows, Linux, MacOS

## 📦 Run Instructions
```bash
python Port_Scanner.py
```

## 📎 Notes
- Scanning all 65535 ports may take time — use custom ranges for quicker tests.
- UDP scans may return fewer results due to their stateless nature.

## 🔗 GitHub Repository
> Upload this project and update the URL here:
**[GitHub Repo Link](https://github.com/Auraoflegend/Basic-Port-Scanner.git)**

---
**Author**: Aditya  
**Date**: April 30, 2025

