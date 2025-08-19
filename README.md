
---
# 🔎 Recon Automation for Web Pentesting

This project is a **Python-based Reconnaissance and Automation Toolkit** designed to assist in **web pentesting, network scanning, and information gathering**.

It was developed and tested on **Kali Linux (running on VMware Workstation 16 Player)**.

---

## ⚙️ Features

### 1. **Network and Port Scanner**

* Built using **Python + Nmap library**.
* Detects if a host is alive.
* Performs TCP Port Scanning with service detection.
* Example usage:

  ```bash
  python3 NetworkAndPortScanner.py -o <HOST_IP> -p 22,80,443
  ```

### 2. **Recon Automation Tool**

A multi-functional script providing various pentesting utilities:

* **IP Scanner** – Get local host and IP information.
* **Port Scanner** – Multi-threaded port scanner with customizable modes.
* **Barcode Generator** – Generate **EAN-13 barcodes** and save as PNG.
* **QR Code Generator** – Generate QR codes from links.
* **Password Generator** – Create random strong passwords.
* **Wordlist Generator** – Generate custom password lists for brute-force attacks.
* **Phone Number Information Gathering** – Get telecom provider and region details using `phonenumbers`.
* **Subdomain Checker** – Discover subdomains using a built-in wordlist.
* **DDOS Attack Tool (Educational Purpose Only)** – Simulates a Distributed Denial of Service attack. ⚠️ **Use responsibly in controlled environments only.**

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ReconAutomation.git
   cd ReconAutomation
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies include:**

   * `nmap`
   * `requests`
   * `tqdm`
   * `pyfiglet`
   * `pyqrcode`
   * `pillow`
   * `python-barcode`
   * `phonenumbers`
   * `tabulate`

---

## ▶️ Usage

Run the **Recon Tool**:

```bash
python3 ReconAutomationForWebPentesting.py
```

You will see a menu like:

```
 1. IP Scanner
 2. Port Scanner
 3. Barcode Generator
 4. QRCode Generator
 5. Password Generator
 6. Wordlist Generator
 7. Phone number information gathering
 8. Subdomain Checker
 9. DDos Attack Tool
```

Select the desired option and follow the instructions.

---

## 💻 Environment Setup

* **Host System:** VMware Workstation 16 Player
* **Guest OS:** Kali Linux (Latest Version)
* **Python Version:** 3.10+ recommended

---

## ⚠️ Disclaimer

This project is developed **strictly for educational and research purposes**.
The author is **not responsible for any misuse**. Only use these tools on systems you have explicit permission to test.

---

## 📌 Future Enhancements

* Add GUI interface for user-friendly experience.
* Integration with Shodan API for advanced reconnaissance.
* Export results to CSV/JSON for reporting.

---

