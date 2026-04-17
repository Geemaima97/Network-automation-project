def audit_device(config):
    results = {}
    results["ssh"] = "ssh server vrf default" in config
    results["aaa"] = "aaa authentication login default" in config
    results["login_banner"] = "banner motd" in config
    results ["ntp"] = "ntp server" in config
    results ["password_encryption"] = "secret 10" in config
    results["snmp"] = "snmp-server community" in config
    return results

with open('backups/DEVNET-IOSXR_20260410192123.cfg', 'r') as file:
    config = file.read()
audit_results = audit_device(config)
print(audit_results)