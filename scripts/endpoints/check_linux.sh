#!/bin/bash

# check_linux.sh - Basic security assessment for Linux endpoints
# Output: JSON

# Helper to check for command existence
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 1. OS Info
OS_NAME=$(grep -E '^(PRETTY_NAME|NAME)=' /etc/os-release | head -1 | cut -d= -f2 | tr -d '"')
HOSTNAME=$(hostname)

# 2. Disk Encryption (LUKS)
# This is a heuristic check. Real check is complex.
ENCRYPTION_STATUS="unknown"
if command_exists lsblk; then
    if lsblk -o TYPE,FSTYPE | grep -q "crypt"; then
        ENCRYPTION_STATUS="active"
    else
        ENCRYPTION_STATUS="inactive"
    fi
fi

# 3. Firewall
FIREWALL_STATUS="unknown"
if command_exists ufw; then
    if sudo -n ufw status 2>/dev/null | grep -q "Status: active"; then
        FIREWALL_STATUS="active"
    else
        FIREWALL_STATUS="inactive (or no perm)"
    fi
elif command_exists iptables; then
    # Check if there are rules
    RULE_COUNT=$(sudo -n iptables -L -n 2>/dev/null | wc -l)
    if [ "$RULE_COUNT" -gt 8 ]; then # Default empty table has some lines
        FIREWALL_STATUS="active"
    else
        FIREWALL_STATUS="inactive (or no perm)"
    fi
fi

# 4. Updates
UPDATES_STATUS="unknown"
LAST_UPDATE="unknown"
# Debian/Ubuntu
if [ -f /var/lib/apt/periodic/update-success-stamp ]; then
    LAST_UPDATE=$(date -r /var/lib/apt/periodic/update-success-stamp -Iseconds)
    UPDATES_STATUS="checked"
fi

# Output JSON
cat <<EOF
{
  "os": "$OS_NAME",
  "hostname": "$HOSTNAME",
  "timestamp": "$(date -Iseconds)",
  "checks": {
    "disk_encryption": "$ENCRYPTION_STATUS",
    "firewall": "$FIREWALL_STATUS",
    "updates": {
        "status": "$UPDATES_STATUS",
        "last_check": "$LAST_UPDATE"
    }
  }
}
EOF
