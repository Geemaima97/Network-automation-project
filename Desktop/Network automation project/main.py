from configuration import read_csv
from backup import backup_device, save_backup
from audit import audit_device
from report import generate_report

def main():
    devices = read_csv('devices.csv')
    for device in devices:
        backup = backup_device(device)
        save_backup(device['hostname'], backup)
        audit_results = audit_device(backup)
        report = generate_report(audit_results, device)
       


if __name__ == "__main__":
    main()
