import json
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Generate endpoint report")
    parser.add_argument("--input", help="Input JSON file from check script", required=True)
    parser.add_argument("--output", help="Output report file", required=True)
    args = parser.parse_args()
    
    try:
        with open(args.input, "r") as f:
            data = json.load(f)
            
        report = [
            f"# Endpoint Security Report for {data.get('hostname', 'Unknown')}",
            f"**OS:** {data.get('os', 'Unknown')}",
            f"**Date:** {data.get('timestamp', 'Unknown')}",
            "",
            "## Checks",
            "| Check | Status |",
            "|---|---|"
        ]
        
        checks = data.get("checks", {})
        for key, value in checks.items():
            status_icon = "✅" if value in ["active", "checked"] else "⚠️"
            if value == "inactive":
                status_icon = "❌"
            report.append(f"| {key} | {status_icon} {value} |")
            
        with open(args.output, "w") as f:
            f.write("\n".join(report))
            
        print(f"Report generated: {args.output}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
