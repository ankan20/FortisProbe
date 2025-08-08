from datetime import datetime

def print_status(message, level="info"):
    levels = {
        "info": "[INFO]",
        "warning": "[WARNING]",
        "error": "[ERROR]"
    }
    print(f"{levels.get(level, '[INFO]')} {message}")

def save_results_to_file(target, findings):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("output/scan_results.txt", "a", encoding="utf-8") as f:
        f.write(f"--- Scan Report ({timestamp}) ---\n")
        f.write(f"Target: {target}\n")
        for vuln, severity in findings:
            f.write(f"{vuln} - Severity: {severity}\n")
        f.write("\n")
