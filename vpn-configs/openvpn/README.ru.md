# OpenVPN Configurations

## Рекомендации по безопасности (Hardening)

1. **Шифрование:** Используйте `AES-256-GCM`. Избегайте устаревших `BF-CBC` и т.п.
2. **Аутентификация:** Используйте сертификаты + User/Pass (MFA).
3. **TLS-Auth:** Включите `tls-auth` или `tls-crypt` для защиты от DoS и сканирования портов.
4. **Сжатие:** Отключите сжатие (`comp-lzo no` или `allow-compression no`), чтобы избежать атак типа VORACLE/CRIME.

## MFA (Многофакторная аутентификация)
Для соответствия лучшим практикам и требованиям регуляторов, настройте MFA:
- Через плагин `openvpn-plugin-auth-pam.so` (Google Authenticator).
- Через интеграцию с LDAP/Radius.
