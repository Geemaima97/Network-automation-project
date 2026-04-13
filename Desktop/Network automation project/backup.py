from netmiko import ConnectHandler
from configuration import password, secret, userName
import datetime

def backup_device(device):
    connect = ConnectHandler(
        device_type=device['device_type'],
        host=device['ip'],
        username=userName,
        password=password,  
        secret=secret
    )
    connect.enable()
    backup= connect.send_command('show running-config')
    return backup

def save_backup(hostname, backup):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"backups/{hostname}_{timestamp}.cfg"
    with open(filename, 'w') as file:
        file.write(backup)
    print(f"Backup saved for {hostname} at {filename}")