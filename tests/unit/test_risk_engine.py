import pytest
from remote_work_ai_helper.models import OrgProfile, RemoteMode
from remote_work_ai_helper.risk_engine import RiskEngine

@pytest.fixture
def basic_profile():
    return OrgProfile(
        org_name="Test Org",
        industry="IT",
        employees_count=100,
        has_pdn=True,
        has_critical_infrastructure=False,
        remote_mode=RemoteMode(
            mode="fully_remote",
            remote_percentage=100,
            allow_byod=True
        )
    )

def test_risk_engine_byod_pdn(basic_profile):
    engine = RiskEngine()
    risks = engine.assess_risks(basic_profile)
    
    # Should have a risk related to BYOD and PDN
    byod_risks = [r for r in risks if "BYOD" in r.risk_description]
    assert len(byod_risks) > 0
    assert any(r.priority == "high" for r in byod_risks)

def test_risk_engine_critical_infra():
    profile = OrgProfile(
        org_name="Critical Org",
        industry="Energy",
        employees_count=1000,
        has_pdn=False,
        has_critical_infrastructure=True,
        remote_mode=RemoteMode(
            mode="hybrid",
            remote_percentage=20,
            allow_byod=False
        )
    )
    
    engine = RiskEngine()
    risks = engine.assess_risks(profile)
    
    kii_risks = [r for r in risks if "КИИ" in r.risk_description or "Critical" in r.risk_description]
    assert len(kii_risks) > 0
    assert any(r.priority == "critical" for r in kii_risks)
