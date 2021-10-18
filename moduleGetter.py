import paramiko
import os
from stat import S_ISDIR as isdir


host = "51.222.87.170"

def fetchModule():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=host, username='ftpuser', password='emseODU')
    except Exception:
        print("Cannot valid SSH connection to fetch module information")
    
    sshin, sshout, ssherr = ssh.exec_command('ls -a | grep test.txt')

    for line in sshout.read().splitlines():
        print(line)

    return
