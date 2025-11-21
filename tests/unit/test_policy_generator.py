import pytest
from remote_work_ai_helper.models import OrgProfile, RemoteMode, RiskItem
from remote_work_ai_helper.policy_generator import PolicyGenerator

@pytest.fixture
def basic_profile():
    return OrgProfile(
        org_name="Test Org",
        industry="IT",
        employees_count=10,
        has_pdn=False,
        has_critical_infrastructure=False,
        remote_mode=RemoteMode(
            mode="fully_remote",
            remote_percentage=100,
            allow_byod=False
        )
    )

def test_generate_policy_structure(basic_profile):
    generator = PolicyGenerator(template_dir="policies/templates")
    # Mocking template loading if necessary, but for now assuming templates exist or using simple string replacement
    # For this test, we might need to mock the file system or ensure templates exist.
    # Let's assume the generator can work with default internal templates if files are missing, 
    # or we mock the _load_template method.
    
    policy_md = generator.generate(basic_profile, risks=[])
    
    assert "# Политика удалённой работы" in policy_md
    assert "Test Org" in policy_md
    assert "Общие положения" in policy_md

def test_generate_policy_with_risks(basic_profile):
    generator = PolicyGenerator(template_dir="policies/templates")
    risks = [
        RiskItem(
            risk_description="Test Risk",
            probability="low",
            impact="low",
            recommendation="Do nothing",
            priority="low"
        )
    ]
    
    policy_md = generator.generate(basic_profile, risks=risks)
    
    assert "Таблица рисков" in policy_md
    assert "Test Risk" in policy_md
