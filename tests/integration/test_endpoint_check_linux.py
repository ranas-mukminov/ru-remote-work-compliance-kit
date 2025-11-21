import pytest
import subprocess
import json
import os
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[2] / "scripts" / "endpoints" / "check_linux.sh"

@pytest.mark.skipif(not os.path.exists(SCRIPT_PATH), reason="Script not found")
def test_check_linux_script_output_structure():
    # Ensure the script is executable
    os.chmod(SCRIPT_PATH, 0o755)
    
    # Run the script
    result = subprocess.run([str(SCRIPT_PATH)], capture_output=True, text=True)
    
    # Check exit code
    assert result.returncode == 0, f"Script failed: {result.stderr}"
    
    # Parse JSON
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        pytest.fail(f"Output is not valid JSON: {result.stdout}")
        
    # Check structure
    assert "os" in data
    assert "hostname" in data
    assert "checks" in data
    assert "disk_encryption" in data["checks"]
    assert "firewall" in data["checks"]
    assert "updates" in data["checks"]
