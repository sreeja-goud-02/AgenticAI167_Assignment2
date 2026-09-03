# Question 3 – Security Log Analysis Agent

## Objective

Create an agent that analyzes security logs and alerts, identifies potential security threats, classifies their severity, and suggests appropriate mitigation steps.

## Description

This project implements a simple Security Log Analysis Agent using Python.

The agent examines security logs and detects potential threats based on predefined security patterns. It identifies the type of threat, assigns a severity level, and recommends mitigation steps.

## Features

- Analyzes security logs automatically
- Detects potential security threats
- Classifies threats based on severity
- Suggests mitigation steps
- Handles multiple security logs
- Identifies normal activity where no threat is detected

## Threats Detected

The agent can identify:

1. Brute Force Attack
2. Port Scanning
3. Malware Detection
4. Unauthorized Access
5. Suspicious Network Activity
6. No Threat Detected

## Severity Levels

| Severity | Description |
|----------|-------------|
| CRITICAL | Very serious threat requiring immediate action |
| HIGH | Serious security threat |
| MEDIUM | Potential security risk requiring investigation |
| LOW | No significant threat detected |

## Technologies Used

- Python 3
- Regular expressions
- Rule-based security analysis
- Object-Oriented Programming

## Project Structure

```text
Question3_Security_Log_Analysis/
│
├── app.py
└── README.md
