from netmiko import ConnectHandler
from configuration import password, secret, userName
import datetime
from logger import logger

def backup_device(device):
    logger.info(f"Connecting to {device['hostname']}")
    connect = ConnectHandler(
        device_type=device['device_type'],
        host=device['ip'],
        username=userName,
        password=password,  
        secret=secret
    )

    connect.enable()
    backup= connect.send_command('show running-config')
    logger.info(f"Backup retrieved for {device['hostname']}")
    return backup


def save_backup(hostname, backup):
   
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"backups/{hostname}_{timestamp}.cfg"
    with open(filename, 'w') as file:
        file.write(backup)
    logger.info(f"Backup saved for {hostname} at {filename}")

def get_logs(device):
    connect = ConnectHandler(
        device_type=device ['device_type'],
        host=device["ip"],
        username=userName,
        password=password,
        secret=secret
  )
    connect.enable()
    logs = connect.send_command('show logging')
    return logs
      