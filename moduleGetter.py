import paramiko
import os
from stat import S_ISDIR as isdir

host = "51.222.87.170"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=host, username='ftpuser', password='emseODU')
except Exception:
    print("Cannot valid SSH connection to fetch module information")


def fetchCourses():
    sshin, sshout, ssherr = ssh.exec_command('ls')
    return sshout.read().decode()

def fetchModule(course, module):
    sshin, sshout, ssherr = ssh.exec_command('ls -R -a ' + course + ' | grep ".*[Mm]od.*' + str(module) + '"')

    for line in sshout.read().decode().splitlines():
        print(line)

    return
