import yaml
import json
from pathlib import Path
from .models import OrgProfile



def load_profile(file_path: str) -> OrgProfile:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Profile file not found: {file_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        if path.suffix in (".yaml", ".yml"):
            data = yaml.safe_load(f)
        elif path.suffix == ".json":
            data = json.load(f)
        else:
            raise ValueError("Unsupported file format. Use .yaml or .json")
            
    return OrgProfile(**data)
