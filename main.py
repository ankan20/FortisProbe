import argparse
from scanner.vulnerability_scanner import VulnerabilityScanner
from scanner.reports import ReportGenerator
from scanner.utils import print_status

def main():
    parser = argparse.ArgumentParser(description="FortisProbe - Lightweight OWASP Top 10 Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target URL to scan")
    parser.add_argument("-o", "--output", default="results/report.txt", help="Output file path")
    args = parser.parse_args()

    scanner = VulnerabilityScanner(args.target)
    findings = scanner.run_all_tests()

    # Show pass/fail in console
    if findings:
        print_status("Vulnerabilities detected:", "warning")
        for vuln, severity in findings:
            print(f"❌ {vuln} | Severity: {severity}")
    else:
        print_status("No vulnerabilities detected!", "info")
        print("✅ All tests passed.")

    # Save report 
    report = ReportGenerator(findings, args.output, overwrite=True)
    report.save()

if __name__ == "__main__":
    main()
