import typer
import json
import platform
import subprocess
import sys
from pathlib import Path
from typing import Optional

app = typer.Typer()

def run_assessment_script(os_type: str) -> dict:
    # This is a placeholder. In real implementation, it would call the shell/ps1 scripts.
    # For now, we return a mock result or try to run the script if it exists.
    
    script_path = Path(__file__).parents[2] / "scripts" / "endpoints"
    
    if os_type == "Linux":
        script = script_path / "check_linux.sh"
        if script.exists():
             # In a real scenario we would execute it. 
             # For safety in this environment, we might just return a stub if not actually running on a target.
             pass
    
    return {
        "os": os_type,
        "status": "ok",
        "checks": {
            "disk_encryption": "unknown",
            "firewall": "unknown"
        }
    }

@app.callback(invoke_without_command=True)
def main(
    format: str = typer.Option("json", help="Output format (json/text)"),
    output: Optional[str] = typer.Option(None, help="Output file path")
):
    """
    Assess the security posture of the current endpoint.
    """
    os_type = platform.system()
    result = run_assessment_script(os_type)
    
    output_content = json.dumps(result, indent=2) if format == "json" else str(result)
    
    if output:
        with open(output, "w") as f:
            f.write(output_content)
        typer.echo(f"Report saved to {output}")
    else:
        typer.echo(output_content)
