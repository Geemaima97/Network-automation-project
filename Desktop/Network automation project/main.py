from configuration import read_csv
from backup import backup_device, save_backup
from audit import audit_device
from report import generate_report
from emailer import send_email
from configuration import EMAIL_RECEIVER

def main():
    devices = read_csv('devices.csv')
    for device in devices:
        backup = backup_device(device)
        save_backup(device['hostname'], backup)
        audit_results = audit_device(backup)
        report = generate_report(audit_results, device)
        emailer = send_email(f"Audit Report for {device['hostname']}", report, EMAIL_RECEIVER)
       


if __name__ == "__main__":
    main()
