#!/bin/bash

# check_macos.sh - Basic security assessment for macOS
# Output: JSON

HOSTNAME=$(hostname)
OS_VER=$(sw_vers -productVersion)

# FileVault
FV_STATUS=$(fdesetup status)
ENCRYPTION="inactive"
if [[ "$FV_STATUS" == *"FileVault is On"* ]]; then
    ENCRYPTION="active"
fi

# Firewall
FW_STATUS=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate)
FIREWALL="inactive"
if [[ "$FW_STATUS" == *"enabled"* ]]; then
    FIREWALL="active"
fi

# Gatekeeper
GK_STATUS=$(spctl --status)
GATEKEEPER="inactive"
if [[ "$GK_STATUS" == *"assessments enabled"* ]]; then
    GATEKEEPER="active"
fi

cat <<EOF
{
  "os": "macOS $OS_VER",
  "hostname": "$HOSTNAME",
  "timestamp": "$(date -Iseconds)",
  "checks": {
    "disk_encryption": "$ENCRYPTION",
    "firewall": "$FIREWALL",
    "gatekeeper": "$GATEKEEPER"
  }
}
EOF
