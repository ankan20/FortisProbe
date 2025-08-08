from datetime import datetime
import os

class ReportGenerator:
    def __init__(self, findings, output_path, overwrite=False):
        self.findings = findings
        self.output_path = output_path
        self.overwrite = overwrite

    def save(self):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mode = "w" if self.overwrite else "a"  # overwrite or append
        with open(self.output_path, mode, encoding="utf-8") as f:
            f.write(f"=== FortisProbe Scan Report ({timestamp}) ===\n")
            if not self.findings:
                f.write("✅ No vulnerabilities found.\n")
            else:
                for vuln, severity in self.findings:
                    f.write(f"❌ {vuln} - Severity: {severity}\n")
            f.write("\n")

        print(f"[INFO] Report saved to {self.output_path}")
