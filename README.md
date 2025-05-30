# Homework 9 – Securing Systems Against Log4Shell Exploits

## Overview
This project demonstrates the exploitation and mitigation of the Log4Shell vulnerability (CVE-2021-44228) using a Dockerized Java web application with vulnerable Log4j 2.14.1. The setup includes a simulated malicious LDAP server to demonstrate the JNDI injection attack path. After exploitation, the system is hardened by upgrading Log4j, validating input, and applying MITRE D3FEND and ATT&CK recommendations.

## Folder Structure