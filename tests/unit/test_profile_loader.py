import pytest
import yaml
from remote_work_ai_helper.profile_loader import load_profile
from remote_work_ai_helper.models import OrgProfile



def test_load_profile_valid(tmp_path):
    profile_data = {
        "org_name": "Test Org",
        "industry": "IT",
        "employees_count": 50,
        "has_pdn": True,
        "has_critical_infrastructure": False,
        "remote_mode": {
            "mode": "hybrid",
            "remote_percentage": 60,
            "allow_byod": True
        }
    }
    
    p = tmp_path / "profile.yaml"
    with open(p, "w") as f:
        yaml.dump(profile_data, f)
        
    profile = load_profile(str(p))
    
    assert isinstance(profile, OrgProfile)
    assert profile.org_name == "Test Org"
    assert profile.remote_mode.mode == "hybrid"
    assert profile.remote_mode.allow_byod is True



def test_load_profile_invalid(tmp_path):
    # Missing required field
    profile_data = {
        "industry": "IT"
    }
    
    p = tmp_path / "invalid_profile.yaml"
    with open(p, "w") as f:
        yaml.dump(profile_data, f)
        
    with pytest.raises(ValueError):
        load_profile(str(p))



def test_load_profile_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_profile("non_existent.yaml")
