<#
.SYNOPSIS
    Checks basic security settings on Windows.
.OUTPUTS
    JSON string
#>

$ErrorActionPreference = "SilentlyContinue"

$os = Get-CimInstance Win32_OperatingSystem
$hostname = $env:COMPUTERNAME

# BitLocker
$bitlocker = Get-BitLockerVolume -MountPoint "C:"
$encryptionStatus = if ($bitlocker.ProtectionStatus -eq "On") { "active" } else { "inactive" }

# Firewall
$firewall = Get-NetFirewallProfile -Profile Domain,Public,Private
$firewallStatus = if (($firewall | Where-Object {$_.Enabled -eq $true}).Count -gt 0) { "active" } else { "inactive" }

# Defender
$defender = Get-MpComputerStatus
$avStatus = if ($defender.AntivirusEnabled -eq $true) { "active" } else { "inactive" }

$result = @{
    os = $os.Caption
    hostname = $hostname
    timestamp = (Get-Date).ToString("o")
    checks = @{
        disk_encryption = $encryptionStatus
        firewall = $firewallStatus
        antivirus = $avStatus
    }
}

$result | ConvertTo-Json -Depth 3
