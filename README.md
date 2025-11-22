# 🔒 ru-remote-work-compliance-kit

[![CI](https://github.com/ranas-mukminov/ru-remote-work-compliance-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/ranas-mukminov/ru-remote-work-compliance-kit/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

🇬🇧 English | 🇷🇺 [Русская версия](README.ru.md)

**Comprehensive toolkit for secure remote work compliance in Russia (152-FZ, CII, best practices)**

## Overview

`ru-remote-work-compliance-kit` is an open-source repository providing templates, scripts, and automation tools to help Russian organizations establish secure remote work environments that align with regulatory requirements and security best practices.

This toolkit addresses the challenge faced by small and medium businesses, IT integrators, and DevSecOps teams who need to implement secure remote work infrastructure but lack dedicated security staff or ready-to-use solutions. It provides practical, deployable components for VPN setup, endpoint security assessment, policy documentation, and risk management.

The project is designed for organizations handling personal data (PD) under 152-FZ, operating critical information infrastructure (CII) under 187-FZ, or simply following modern security best practices for distributed teams.

## Key Features

- **VPN configuration templates** — WireGuard and OpenVPN configs for split-tunnel and forced-tunnel scenarios, ready for production adaptation
- **Endpoint security assessment scripts** — Cross-platform automation (Linux, Windows, macOS) to check disk encryption, firewall status, updates, and antivirus
- **Policy templates** — Production-ready Markdown/ODT documents covering remote work policies, BYOD, personal data handling, VPN usage rules, incident reporting, and endpoint hardening checklists
- **AI-powered policy generator** — Command-line tool to generate custom compliance policies based on your organization's profile and risk assessment
- **Risk assessment engine** — Automated evaluation of security risks specific to your remote work setup, with prioritized recommendations
- **CLI workflow** — Simple command-line interface for endpoint assessment, policy generation, and risk reporting
- **Compliance-focused** — Built with Russian regulatory requirements (152-FZ, 187-FZ, Labor Code) in mind, while remaining flexible for general security needs
- **GitHub Actions CI/CD** — Automated testing, linting, type checking, and security scanning (bandit, pip-audit) out of the box

## Architecture / Components

The toolkit consists of four main layers:

```
┌─────────────────────────────────────────────────────────┐
│  CLI: ru-remote-kit (Typer-based command interface)     │
└──────────────────┬──────────────────────────────────────┘
                   │
       ┌───────────┴───────────┬──────────────────┐
       ▼                       ▼                  ▼
┌──────────────┐    ┌────────────────────┐  ┌───────────────┐
│  Endpoint    │    │   AI Helper        │  │  VPN Configs  │
│  Assessment  │    │   (Policy Gen +    │  │  & Policy     │
│  Scripts     │    │    Risk Engine)    │  │  Templates    │
└──────────────┘    └────────────────────┘  └───────────────┘
```

**Components:**

1. **CLI (`/cli`)** — Typer-based command-line application providing three main commands:
   - `assess-endpoint` — Run endpoint security checks
   - `generate-policy` — Create custom remote work policies
   - `generate-risk-list` — Output risk assessment tables

2. **Endpoint Assessment (`/scripts/endpoints`)** — Bash/PowerShell scripts that audit workstations for:
   - Disk encryption (LUKS on Linux, BitLocker on Windows, FileVault on macOS)
   - Firewall configuration (ufw, iptables, Windows Firewall)
   - System update status
   - Antivirus presence (where applicable)

3. **AI Helper (`/ai/src`)** — Python modules for intelligent policy generation:
   - `profile_loader` — Parses organization YAML/JSON profiles
   - `risk_engine` — Evaluates risks based on industry, data classification, remote work model
   - `policy_generator` — Renders policies using Jinja2 templates

4. **Configuration & Templates (`/vpn-configs`, `/policies`)** — Ready-to-use examples:
   - WireGuard and OpenVPN server/client configs
   - Markdown policy templates (remote work, BYOD, PD handling, VPN usage, incident response, hardening checklists)

## Requirements

### System Requirements

- **Operating System:**
  - Linux: Ubuntu 20.04+, Debian 11+, RHEL 8+, Rocky Linux 8+, or compatible distributions
  - Windows: 10/11 or Server 2019+ (for endpoint scripts only)
  - macOS: 11+ (for endpoint scripts only)

- **Resources:**
  - Minimal: 1 CPU core, 512 MB RAM, 500 MB disk space
  - Recommended: 2 CPU cores, 2 GB RAM for AI policy generation

### Software Dependencies

- **Python:** 3.10 or higher
- **Package manager:** pip (included with Python)
- **VPN software:** WireGuard and/or OpenVPN (only if deploying VPN infrastructure)
- **Shell:** Bash 4.0+ (Linux/macOS), PowerShell 5.1+ (Windows)

### Access Requirements

- **Permissions:** Standard user privileges for CLI tools; `sudo` or administrator rights for endpoint assessment scripts
- **Network:** Internet access for Python package installation; no external network dependencies for core functionality
- **Optional:** GitHub account for contributing, CI/CD integration

## Quick Start (TL;DR)

```bash
# 1. Clone the repository
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit

# 2. Install Python dependencies
pip install -e .

# 3. Assess your workstation security
ru-remote-kit assess-endpoint --format json --output my-endpoint-report.json

# 4. Generate a remote work policy for your organization
ru-remote-kit generate-policy \
  --profile examples/org-profiles/smb-it-outsourcing.yaml \
  --out my-remote-work-policy.md

# 5. Review risk assessment
ru-remote-kit generate-risk-list \
  --profile examples/org-profiles/smb-it-outsourcing.yaml
```

Default output locations: current directory unless specified with `--output` or `--out`.

## Detailed Installation

### Install on Ubuntu / Debian

```bash
# Update package index
sudo apt update

# Install Python 3.10+ if not present
sudo apt install -y python3 python3-pip git

# Clone repository
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit

# Install in editable mode (recommended for development)
pip install -e .

# OR install as a package
pip install .

# Verify installation
ru-remote-kit --help
```

### Install on RHEL / Rocky Linux / Alma Linux

```bash
# Install Python 3.10+ and Git
sudo dnf install -y python3 python3-pip git

# Clone repository
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit

# Install package
pip install -e .

# Verify
ru-remote-kit --help
```

### Install on macOS

```bash
# Install Homebrew if not present (https://brew.sh)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10+
brew install python@3.10 git

# Clone and install
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit
pip3 install -e .
ru-remote-kit --help
```

### Install on Windows

```powershell
# Install Python 3.10+ from https://www.python.org/downloads/
# During installation, check "Add Python to PATH"

# Install Git from https://git-scm.com/download/win

# Clone repository (in PowerShell or CMD)
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit

# Install package
pip install -e .

# Verify
ru-remote-kit --help
```

### Development Installation

For contributors and those who want to run tests:

```bash
# Clone repository
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit

# Install with development dependencies
pip install -e .
pip install pytest pytest-mock flake8 mypy bandit pip-audit types-PyYAML types-requests

# Install shellcheck (for shell script linting)
# Ubuntu/Debian:
sudo apt install -y shellcheck

# macOS:
brew install shellcheck

# Run tests
pytest

# Run all quality checks
chmod +x scripts-dev/*.sh
./scripts-dev/dev_run_all_tests.sh
```

## Configuration

### Organization Profile

Create a YAML file describing your organization to enable AI-powered policy generation and risk assessment. Example:

```yaml
# example-org-profile.yaml
organization:
  name: "Example IT Services LLC"
  industry: "IT Services & Consulting"
  size: 50  # number of employees
  
remote_work:
  model: "hybrid"  # remote-first | hybrid | occasional
  allow_byod: true
  personal_data_processing: true
  data_classification:
    - "public"
    - "internal"
    - "confidential"
    - "personal_data"

compliance_requirements:
  - "152-FZ"  # Personal Data Law
  - "187-FZ"  # Critical Information Infrastructure

vpn:
  required: true
  type: "split-tunnel"  # split-tunnel | forced-tunnel

endpoints:
  os_allowed:
    - "Linux"
    - "Windows"
    - "macOS"
  encryption_required: true
  antivirus_required: true
```

Save this as `my-org-profile.yaml` and use with:

```bash
ru-remote-kit generate-policy --profile my-org-profile.yaml --out policy.md
```

### VPN Configuration

#### WireGuard Split-Tunnel Example

Edit `vpn-configs/wireguard/wg-split-tunnel.conf.example`:

```ini
[Interface]
PrivateKey = <SERVER_PRIVATE_KEY>
Address = 10.8.0.1/24
ListenPort = 51820
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
# Client 1
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.8.0.2/32
```

Generate keys:
```bash
umask 077
wg genkey | tee server-privatekey | wg pubkey > server-publickey
wg genkey | tee client-privatekey | wg pubkey > client-publickey
```

Deploy on server:
```bash
sudo cp wg-split-tunnel.conf /etc/wireguard/wg0.conf
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0
```

#### OpenVPN Example

See `vpn-configs/openvpn/server.conf.example` for detailed OpenVPN server configuration. Key settings:

```conf
port 1194
proto udp
dev tun
ca /etc/openvpn/ca.crt
cert /etc/openvpn/server.crt
key /etc/openvpn/server.key
dh /etc/openvpn/dh2048.pem
server 10.8.0.0 255.255.255.0
push "route 192.168.1.0 255.255.255.0"
keepalive 10 120
cipher AES-256-GCM
auth SHA256
user nobody
group nobody
```

Generate certificates using Easy-RSA (see `vpn-configs/openvpn/README.ru.md` for step-by-step instructions).

### Policy Templates

Pre-built policy templates are available in `policies/templates/`:

- `remote-work-policy.ru.md` — General remote work policy
- `byod-policy.ru.md` — Bring Your Own Device guidelines
- `pdl-home-handling-policy.ru.md` — Personal data handling at home
- `vpn-usage-rules.ru.md` — VPN usage requirements
- `incident-reporting-procedure.ru.md` — Security incident reporting workflow
- `endpoint-hardening-checklist.ru.md` — Workstation security checklist

Copy and customize these templates for your organization, or use the AI generator for automated customization based on your profile.

## Usage & Common Tasks

### Assess Endpoint Security

Run security checks on the current workstation:

```bash
# JSON output (machine-readable)
ru-remote-kit assess-endpoint --format json --output endpoint-report.json

# Human-readable output to console
ru-remote-kit assess-endpoint --format text

# Check and save to specific path
ru-remote-kit assess-endpoint --format json --output /var/log/compliance/$(hostname)-$(date +%Y%m%d).json
```

The assessment checks:
- Disk encryption status
- Firewall configuration
- System update status
- OS version and hostname
- Timestamp of assessment

### Generate Custom Policies

Create a remote work policy tailored to your organization:

```bash
# Using example profile
ru-remote-kit generate-policy \
  --profile examples/org-profiles/smb-it-outsourcing.yaml \
  --out custom-policy.md

# Using your own profile
ru-remote-kit generate-policy \
  --profile /path/to/your-org-profile.yaml \
  --out /docs/policies/remote-work-2024.md
```

The generated policy includes sections on:
- Scope and definitions
- Allowed work locations
- Device requirements
- VPN and network security
- Personal data handling
- Incident reporting
- Responsibilities

### Review Risk Assessment

Generate a prioritized list of security risks:

```bash
ru-remote-kit generate-risk-list --profile examples/org-profiles/smb-it-outsourcing.yaml
```

Output example:
```
| Риск | Приоритет | Рекомендация |
|---|---|---|
| Unencrypted devices handling PD | HIGH | Require full-disk encryption on all endpoints |
| No VPN for remote workers | HIGH | Deploy WireGuard with forced-tunnel for PD access |
| BYOD without MDM | MEDIUM | Implement conditional access or provide corporate devices |
```

### Deploy VPN Infrastructure

**WireGuard deployment:**

```bash
# On server (Ubuntu/Debian)
sudo apt install -y wireguard

# Generate server keys
cd vpn-configs/wireguard
umask 077
wg genkey | tee server.key | wg pubkey > server.pub

# Configure (edit wg-split-tunnel.conf.example with your keys)
sudo cp wg0.conf /etc/wireguard/
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0

# Check status
sudo wg show
```

**OpenVPN deployment:**

```bash
# Install OpenVPN and Easy-RSA
sudo apt install -y openvpn easy-rsa

# Set up PKI (see vpn-configs/openvpn/README.ru.md for full guide)
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
./easyrsa init-pki
./easyrsa build-ca
./easyrsa gen-dh
./easyrsa build-server-full server nopass

# Deploy config
sudo cp vpn-configs/openvpn/server.conf.example /etc/openvpn/server.conf
# (adjust paths in server.conf)
sudo systemctl enable openvpn@server
sudo systemctl start openvpn@server
```

### Run Endpoint Assessment Scripts Directly

Without installing the Python package, you can run standalone scripts:

**Linux:**
```bash
chmod +x scripts/endpoints/check_linux.sh
./scripts/endpoints/check_linux.sh > report.json
```

**Windows (PowerShell as Administrator):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\endpoints\check_windows.ps1 | Out-File -Encoding utf8 report.json
```

**macOS:**
```bash
chmod +x scripts/endpoints/check_macos.sh
./scripts/endpoints/check_macos.sh > report.json
```

## Update / Upgrade

### Update the Toolkit

```bash
# Navigate to repository directory
cd /path/to/ru-remote-work-compliance-kit

# Pull latest changes
git pull origin main

# Reinstall package to update CLI and dependencies
pip install -e . --upgrade

# Verify version (check commit hash)
git log -1 --oneline
```

### Upgrade Python Dependencies

```bash
# Update all dependencies to latest compatible versions
pip install -e . --upgrade --upgrade-strategy eager

# OR update specific dependencies
pip install --upgrade pyyaml pydantic typer jinja2
```

### Update Policy Templates

Policy templates are versioned with the repository. After `git pull`, review changes:

```bash
# Check what changed in templates
git diff HEAD~1 policies/templates/

# Copy updated templates to your customized policies location if needed
cp policies/templates/remote-work-policy.ru.md /your/docs/policies/
```

**Breaking changes:** Major updates will be noted in commit messages and CHANGELOG.md (if present). Always review diff before deploying updated VPN configs or policies in production.

## Logs, Monitoring, Troubleshooting

### Logs

**Endpoint assessment logs:**
- Scripts output JSON to stdout; redirect to file for logging:
  ```bash
  ./scripts/endpoints/check_linux.sh >> /var/log/compliance-checks/$(date +%Y%m%d).log 2>>/var/log/compliance-checks/errors.log
  ```

**VPN logs:**
- WireGuard: `sudo journalctl -u wg-quick@wg0 -f`
- OpenVPN: `sudo journalctl -u openvpn@server -f` or check `/var/log/openvpn/`

**Python CLI errors:**
- CLI errors are printed to stderr
- For verbose output, add debug logging (modify CLI source or set environment variables if supported)

### Common Issues

**Issue:** `ru-remote-kit: command not found`

**Solution:**
```bash
# Ensure Python bin directory is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Or reinstall with --user flag
pip install --user -e .

# Add to shell profile for persistence
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

**Issue:** Endpoint assessment script returns `permission denied`

**Solution:**
```bash
# Make scripts executable
chmod +x scripts/endpoints/*.sh
chmod +x scripts/endpoints/*.ps1

# Run with sudo for system-level checks
sudo ./scripts/endpoints/check_linux.sh
```

---

**Issue:** `ModuleNotFoundError: No module named 'remote_work_ai_helper'`

**Solution:**
```bash
# Ensure ai/src modules are in Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd):$(pwd)/ai/src"

# OR reinstall package
pip uninstall ru-remote-work-compliance-kit
pip install -e .
```

---

**Issue:** VPN connection fails with `Permission denied (publickey)`

**Solution:**
- WireGuard: Verify keys are correctly placed in config, check firewall allows UDP 51820
  ```bash
  sudo ufw allow 51820/udp
  sudo systemctl restart wg-quick@wg0
  ```
- OpenVPN: Check certificate paths, ensure client has correct `.ovpn` file with embedded certs

---

**Issue:** Policy generation fails with `KeyError` or `YAML parsing error`

**Solution:**
```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('your-profile.yaml'))"

# Check required fields in profile (see Configuration section)
# Ensure organization.name, remote_work.model, compliance_requirements are present
```

---

**Issue:** No data in endpoint report (empty checks)

**Solution:**
- **Linux:** Script may need `sudo` for `lsblk`, `ufw`, `iptables`
- **Windows:** Run PowerShell as Administrator
- **macOS:** Grant Terminal full disk access in System Preferences > Security & Privacy
- Check that required commands exist (e.g., `lsblk`, `ufw`, `iptables`, `Get-BitLockerVolume`)

## Security Notes

> [!CAUTION]
> **This toolkit does NOT provide automatic compliance.** It offers tools and templates; actual compliance requires legal review, organizational policy enforcement, and ongoing monitoring.

### Security Best Practices

1. **Change default credentials and keys:**
   - Always generate unique VPN keys and certificates for each deployment
   - Never commit private keys or passwords to version control
   - Use `.gitignore` to exclude sensitive files (`.key`, `.pem`, `.ovpn` with embedded certs)

2. **Restrict access to VPN and management interfaces:**
   - Do not expose VPN management ports (WireGuard 51820, OpenVPN 1194) directly to the Internet without firewall rules
   - Use fail2ban or similar tools to prevent brute-force attacks
   - Consider placing VPN behind reverse proxy or firewall with geo-blocking for Russian compliance

3. **Limit web UI and API exposure:**
   - If deploying any web dashboards or APIs (future features), use HTTPS only
   - Implement authentication (BasicAuth, OAuth, client certificates)
   - Use VPN or IP whitelisting to restrict access

4. **Encrypt sensitive data:**
   - Store organization profiles containing PD classification or internal network details encrypted at rest
   - Use ansible-vault, SOPS, or similar for secret management in CI/CD

5. **Regular updates:**
   - Keep Python dependencies updated to patch vulnerabilities
   - Subscribe to security advisories for WireGuard, OpenVPN, and Python packages
   - Run `pip-audit` regularly: `pip install pip-audit && pip-audit`

6. **Audit and logging:**
   - Enable VPN access logging for compliance (required by 152-FZ for PD processing)
   - Centralize endpoint assessment reports for periodic review
   - Implement log rotation and retention policies (consult legal for data retention requirements under Russian law)

7. **Principle of least privilege:**
   - Run VPN processes as non-root users where possible (OpenVPN supports `user nobody`)
   - Limit sudo access for endpoint assessment scripts to specific commands

8. **Legal compliance:**
   - Consult with legal counsel before deploying policies or processing personal data
   - Ensure VPN logging and data retention align with 152-FZ and labor law
   - Review [LEGAL.md](LEGAL.md) for disclaimers and prohibited uses

## Project Structure

```
ru-remote-work-compliance-kit/
├── ai/                          # AI-powered policy generator
│   └── src/remote_work_ai_helper/
│       ├── profile_loader.py    # YAML/JSON profile parsing
│       ├── risk_engine.py       # Risk assessment logic
│       └── policy_generator.py  # Jinja2-based policy rendering
├── cli/                         # Command-line interface
│   ├── main.py                  # Typer app entry point
│   └── commands/                # CLI command modules
│       └── assess_endpoint.py   # Endpoint assessment CLI
├── examples/                    # Sample organization profiles
│   └── org-profiles/
│       ├── smb-it-outsourcing.yaml
│       └── fintech-remote-first.yaml
├── policies/                    # Policy templates
│   └── templates/
│       ├── remote-work-policy.ru.md
│       ├── byod-policy.ru.md
│       ├── pdl-home-handling-policy.ru.md
│       ├── vpn-usage-rules.ru.md
│       ├── incident-reporting-procedure.ru.md
│       └── endpoint-hardening-checklist.ru.md
├── scripts/                     # Standalone assessment scripts
│   ├── endpoints/
│   │   ├── check_linux.sh
│   │   ├── check_windows.ps1
│   │   └── check_macos.sh
│   └── reporting/               # (Future: aggregation scripts)
├── scripts-dev/                 # Development and CI scripts
│   └── dev_run_all_tests.sh    # Run all tests and linters
├── tests/                       # Pytest test suite
├── vpn-configs/                 # VPN configuration examples
│   ├── wireguard/
│   │   ├── wg-split-tunnel.conf.example
│   │   └── wg-forced-tunnel.conf.example
│   └── openvpn/
│       ├── server.conf.example
│       ├── client.conf.example
│       └── README.ru.md
├── .github/workflows/           # GitHub Actions CI/CD
│   ├── ci.yml                   # Main CI pipeline
│   └── security.yml             # Security scanning (bandit, pip-audit)
├── CONTRIBUTING.md              # Contribution guidelines
├── LEGAL.md                     # Legal disclaimers
├── LICENSE                      # Apache 2.0 License
├── pyproject.toml               # Python package configuration
├── README.md                    # This file
└── README.ru.md                 # Russian version
```

## Contributing

We welcome contributions from the community! Here's how to contribute:

### Reporting Issues

- Use [GitHub Issues](https://github.com/ranas-mukminov/ru-remote-work-compliance-kit/issues)
- Provide clear description, steps to reproduce, and environment details (OS, Python version)
- For security vulnerabilities, see [SECURITY.md](SECURITY.md) (if present) or contact the author privately

### Proposing Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Make changes following code style:
   - Python: PEP 8, type hints, docstrings
   - Shell scripts: ShellCheck compliant, POSIX where possible
   - YAML: 2-space indentation
4. Write or update tests for your changes
5. Run quality checks: `./scripts-dev/dev_run_all_tests.sh`
6. Commit with clear messages: `git commit -m "Add: support for Fedora in check_linux.sh"`
7. Push and open a Pull Request

### Development Setup

```bash
git clone https://github.com/ranas-mukminov/ru-remote-work-compliance-kit.git
cd ru-remote-work-compliance-kit
pip install -e .
pip install pytest pytest-mock flake8 mypy bandit types-PyYAML types-requests
chmod +x scripts-dev/*.sh
./scripts-dev/dev_run_all_tests.sh
```

All PRs must pass CI checks (tests, linting, type checking, security scans).

## License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute this software for commercial and non-commercial purposes, provided you include the original license and copyright notice.

See [LICENSE](LICENSE) for full details.

## Author and Commercial Support

**Author:** [Ranas Mukminov](https://github.com/ranas-mukminov)

This project is developed and maintained by an experienced DevOps/DevSecOps engineer specializing in secure infrastructure for Russian organizations.

### Commercial Services

For production deployments, custom policy development, security audits, and ongoing support, commercial services are available through [run-as-daemon.ru](https://run-as-daemon.ru).

**We provide:**
- **Compliance consulting** — Gap analysis, 152-FZ alignment, CII readiness assessment
- **VPN infrastructure setup** — WireGuard/OpenVPN deployment, high-availability configurations, monitoring integration
- **Endpoint security automation** — Integration with SIEM, MDM, and compliance dashboards
- **Custom policy development** — Tailored policies for your industry, legal review coordination, employee training materials
- **Incident response planning** — Runbooks, tabletop exercises, integration with SOC processes
- **DevSecOps process integration** — CI/CD security gates, infrastructure-as-code audits, secret management

Contact: Visit [run-as-daemon.ru](https://run-as-daemon.ru) or reach out via [GitHub profile](https://github.com/ranas-mukminov).

---

**Disclaimer:** This project does not constitute legal advice. Compliance with Russian Federation laws requires legal analysis specific to your organization. Consult with your legal and security compliance teams before deploying in production. See [LEGAL.md](LEGAL.md) for full disclaimer.
