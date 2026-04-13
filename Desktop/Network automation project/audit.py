def audit_device(config):
    results = {}
    results["ssh"] = "ip ssh version 2" in config
    results["aaa"] = "aaa new-model" in config
    results["login_banner"] = "banner login" in config
    results ["ntp"] = "ntp server" in config
    results ["password_encryption"] = "service password-encryption" in config
    results["snmp"] = "snmp-server community" in config
    return results

with open('backups/DEVNET-IOSXR_20260410192123.cfg', 'r') as file:
    config = file.read()
audit_results = audit_device(config)
print(audit_results)