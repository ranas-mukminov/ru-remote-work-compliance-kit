from typing import List
from .models import OrgProfile, RiskItem



class RiskEngine:
    def assess_risks(self, profile: OrgProfile) -> List[RiskItem]:
        risks = []
        
        # 1. BYOD Risks
        if profile.remote_mode.allow_byod:
            if profile.has_pdn:
                risks.append(RiskItem(
                    risk_description="Обработка ПДн на личных устройствах (BYOD) без должного контроля",
                    probability="high",
                    impact="high",
                    recommendation="Внедрить VDI или жесткие политики BYOD (контейнеризация, MDM). Запретить локальное хранение ПДн.",
                    priority="high"
                ))
            else:
                risks.append(RiskItem(
                    risk_description="Использование личных устройств для работы",
                    probability="medium",
                    impact="medium",
                    recommendation="Обязать использовать антивирус, шифрование диска и сложные пароли.",
                    priority="medium"
                ))
        
        # 2. Critical Infrastructure
        if profile.has_critical_infrastructure:
            risks.append(RiskItem(
                risk_description="Удалённый доступ к объектам КИИ",
                probability="medium",
                impact="high",
                recommendation="Использовать сертифицированные средства защиты (VPN, 2FA), выделенные АРМ, согласовать с регулятором.",
                priority="critical"
            ))
            
        # 3. General Remote Access
        if profile.remote_mode.mode in ["fully_remote", "hybrid"]:
            risks.append(RiskItem(
                risk_description="Перехват трафика при работе из публичных сетей",
                probability="medium",
                impact="medium",
                recommendation="Обязательное использование VPN (WireGuard/OpenVPN) для всех рабочих подключений.",
                priority="high"
            ))
             
        return risks
