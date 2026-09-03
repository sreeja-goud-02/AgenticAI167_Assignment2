import re
from datetime import datetime


# -----------------------------
# Security Log Analysis Agent
# -----------------------------

class SecurityLogAgent:

    def __init__(self):
        self.threat_rules = {
            "Brute Force Attack": {
                "patterns": ["failed login", "multiple failed", "brute force"],
                "severity": "HIGH",
                "mitigation": "Block the source IP, enable account lockout, and enforce MFA."
            },

            "Port Scanning": {
                "patterns": ["port scan", "nmap", "multiple ports"],
                "severity": "MEDIUM",
                "mitigation": "Block the source IP and restrict unnecessary open ports."
            },

            "Malware Detection": {
                "patterns": ["malware", "trojan", "virus", "ransomware"],
                "severity": "CRITICAL",
                "mitigation": "Isolate the affected system, remove the malware, and perform a security scan."
            },

            "Unauthorized Access": {
                "patterns": ["unauthorized access", "access denied", "privilege escalation"],
                "severity": "HIGH",
                "mitigation": "Review user permissions, disable suspicious accounts, and investigate access logs."
            },

            "Suspicious Network Activity": {
                "patterns": ["suspicious connection", "unusual traffic", "unknown connection"],
                "severity": "MEDIUM",
                "mitigation": "Investigate network traffic and block suspicious connections."
            }
        }

    def analyze_log(self, log):
        log_lower = log.lower()

        for threat, details in self.threat_rules.items():

            for pattern in details["patterns"]:

                if pattern in log_lower:
                    return {
                        "log": log,
                        "threat": threat,
                        "severity": details["severity"],
                        "mitigation": details["mitigation"]
                    }

        return {
            "log": log,
            "threat": "No Threat Detected",
            "severity": "LOW",
            "mitigation": "Continue monitoring the system."
        }

    def analyze_logs(self, logs):

        results = []

        for log in logs:
            result = self.analyze_log(log)
            results.append(result)

        return results


# -----------------------------
# Main Agent
# -----------------------------

def main():

    print("=" * 70)
    print("        AGENTIC AI - SECURITY LOG ANALYSIS AGENT")
    print("=" * 70)

    print("\nAnalyzing security logs...\n")

    logs = [
        "2026-09-03 10:15:23 Failed login attempt from IP 192.168.1.20",
        "2026-09-03 10:16:05 Multiple failed login attempts detected - possible brute force",
        "2026-09-03 10:20:44 Nmap port scan detected from IP 10.0.0.15",
        "2026-09-03 10:25:12 Malware detected on workstation WS-101",
        "2026-09-03 10:30:55 Unauthorized access attempt to admin account",
        "2026-09-03 10:35:20 Normal user login successful"
    ]

    agent = SecurityLogAgent()

    results = agent.analyze_logs(logs)

    print("-" * 70)
    print("SECURITY ANALYSIS RESULTS")
    print("-" * 70)

    for i, result in enumerate(results, 1):

        print(f"\n[{i}] Security Alert")
        print(f"Log       : {result['log']}")
        print(f"Threat    : {result['threat']}")
        print(f"Severity  : {result['severity']}")
        print(f"Mitigation: {result['mitigation']}")
        print("-" * 70)

    print("\nAnalysis completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
