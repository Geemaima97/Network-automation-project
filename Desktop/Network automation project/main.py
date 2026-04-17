from configuration import read_csv
from backup import backup_device, save_backup, get_logs
from audit import audit_device
from report import generate_report
from emailer import send_email
from configuration import EMAIL_RECEIVER
from log_parser import parse_logs


def main():
    devices = read_csv('devices.csv')
    for device in devices:
        backup = backup_device(device)
        save_backup(device['hostname'], backup)
        logs = get_logs(device)

        audit_results = audit_device(backup)
        parsed_logs = parse_logs(logs)

        report = generate_report(audit_results, parsed_logs, device)
        send_email(f"Audit Report for {device['hostname']}", report, EMAIL_RECEIVER)
       


if __name__ == "__main__":
    main()
