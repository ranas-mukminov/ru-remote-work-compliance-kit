
from typer.testing import CliRunner
from cli.main import app

runner = CliRunner()



def test_generate_policy_help():
    result = runner.invoke(app, ["generate-policy", "--help"])
    assert result.exit_code == 0
    assert "generate-policy" in result.stdout



def test_generate_policy_missing_profile():
    result = runner.invoke(app, ["generate-policy"])
    assert result.exit_code != 0
