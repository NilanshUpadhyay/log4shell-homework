# Homework 9 – Securing Systems Against Log4Shell Exploits

## Overview
This project demonstrates the exploitation and mitigation of the Log4Shell vulnerability (CVE-2021-44228) using a Dockerized Java web application with vulnerable Log4j 2.14.1. The setup includes a simulated malicious LDAP server to demonstrate the JNDI injection attack path. After exploitation, the system is hardened by upgrading Log4j, validating input, and applying MITRE D3FEND and ATT&CK recommendations.

## Report
- Mitigation Report: [mitigation_report.pdf](mitigation_report.pdf)
- Architecture Diagram: [homework.png](homework.png)

## Screenshots
- Application Startup: [screenshots/screenshot_app_startup.png](screenshots/screenshot_app_startup.png)
- Application Test: [screenshots/screenshot_app_test.png](screenshots/screenshot_app_test.png)
- LDAP Server Startup: [screenshots/screenshot_ldap_startup.png](screenshots/screenshot_ldap_startup.png)
- Exploit Payload: [screenshots/screenshot_exploit_payload.png](screenshots/screenshot_exploit_payload.png)
- LDAP Exploit Log: [screenshots/screenshot_ldap_exploit.png](screenshots/screenshot_ldap_exploit.png)
- Application Logs: [screenshots/screenshot_app_logs.png](screenshots/screenshot_app_logs.png)

## Screen Recording
Video: [Log4Shell Demo](<paste-your-google-drive-link-here>)

## Author
**Nilansh Upadhyay**  
SEAS 8405 – Cybersecurity Architectures  
May 30, 2025