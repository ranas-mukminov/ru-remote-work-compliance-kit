from typing import List
import os
from .models import OrgProfile, RiskItem

class PolicyGenerator:
    def __init__(self, template_dir: str = "policies/templates"):
        self.template_dir = template_dir

    def generate(self, profile: OrgProfile, risks: List[RiskItem]) -> str:
        # In a real scenario, we would use Jinja2 and load templates from files.
        # For this MVP/stub, we will construct the markdown programmatically or use a simple string template.
        
        policy_content = [
            f"# Политика удалённой работы для {profile.org_name}",
            "",
            "## 1. Общие положения",
            f"Настоящая политика регулирует порядок выполнения трудовых обязанностей сотрудниками {profile.org_name} в дистанционном режиме.",
            f"Режим работы: {profile.remote_mode.mode} ({profile.remote_mode.remote_percentage}% сотрудников).",
            "",
            "## 2. Требования к безопасности",
        ]
        
        if profile.remote_mode.allow_byod:
            policy_content.append("- Разрешено использование личных устройств (BYOD) при соблюдении требований безопасности (см. раздел Риски).")
        else:
            policy_content.append("- Использование личных устройств для доступа к корпоративным ресурсам ЗАПРЕЩЕНО.")
            
        if profile.has_pdn:
            policy_content.append("- **ВНИМАНИЕ:** Организация обрабатывает ПДн. Запрещено сохранять файлы с ПДн на локальные диски домашних компьютеров.")

        policy_content.append("")
        policy_content.append("## 3. Таблица рисков и мер")
        policy_content.append("| Риск | Вероятность | Влияние | Рекомендация | Приоритет |")
        policy_content.append("|---|---|---|---|---|")
        
        for risk in risks:
            policy_content.append(f"| {risk.risk_description} | {risk.probability} | {risk.impact} | {risk.recommendation} | {risk.priority} |")
            
        policy_content.append("")
        policy_content.append("> [!IMPORTANT]")
        policy_content.append("> Данный документ является проектом (draft). Необходимо согласование с юридическим отделом.")

        return "\n".join(policy_content)
