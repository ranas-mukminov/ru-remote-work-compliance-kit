import typer
import sys
import json
import yaml
from pathlib import Path
from typing import Optional
from remote_work_ai_helper.profile_loader import load_profile
from remote_work_ai_helper.risk_engine import RiskEngine
from remote_work_ai_helper.policy_generator import PolicyGenerator
from cli.commands import assess_endpoint

app = typer.Typer()

app.add_typer(assess_endpoint.app, name="assess-endpoint")

@app.command()
def generate_policy(
    profile: str = typer.Option(..., help="Path to organization profile (YAML/JSON)"),
    out: str = typer.Option(..., help="Output markdown file path")
):
    """
    Generate a remote work policy based on the organization profile.
    """
    try:
        org_profile = load_profile(profile)
        engine = RiskEngine()
        risks = engine.assess_risks(org_profile)
        
        generator = PolicyGenerator()
        policy_md = generator.generate(org_profile, risks)
        
        with open(out, "w", encoding="utf-8") as f:
            f.write(policy_md)
            
        typer.echo(f"Policy generated successfully: {out}")
        
    except Exception as e:
        typer.echo(f"Error generating policy: {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def generate_risk_list(
    profile: str = typer.Option(..., help="Path to organization profile (YAML/JSON)")
):
    """
    Generate a list of risks based on the organization profile.
    """
    try:
        org_profile = load_profile(profile)
        engine = RiskEngine()
        risks = engine.assess_risks(org_profile)
        
        typer.echo("| Риск | Приоритет | Рекомендация |")
        typer.echo("|---|---|---|")
        for risk in risks:
            typer.echo(f"| {risk.risk_description} | {risk.priority} | {risk.recommendation} |")
            
    except Exception as e:
        typer.echo(f"Error generating risk list: {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
