import paramiko
import os

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
    #local directory
    successful = False
    localPath = "interface/assets/modules/" + str(module)

    # Fetch absolute remote directory path
    _, remoteRootDir, ssherr = ssh.exec_command('pwd')
    remoteRootDir = remoteRootDir.read().decode().strip()

    # Get the list of all relevent module content in this module
    sshin, sshout, ssherr = ssh.exec_command('find ./' + course + ' | grep ".*[Mm]od.*' + str(module) + '"')

    # Open sftp channel
    sftp = ssh.open_sftp()
    print("Open sftp connection for module: " + str(module))
    # Download all the files from the list of module content
    for line in sshout.read().decode().splitlines():
        successful = True

        # The filename for the file being downloaded
        filename = line[line.rfind('/')+1:]
        
        # Check for the presence of the interface module asset strucutre
        if not os.path.isdir("interface/assets/modules"):
            print("Could not find interface module output directory. Cloning the repository was skipped or failed.")
            return
        
        # Check if the module directory already exists, if not make it
        if not os.path.isdir(localPath):
            os.mkdir(localPath)

        # Attempt to get the file through sftp
        try:
            sftp.get(remoteRootDir + '/' + line[2:], localPath + '/' + filename)
        except Exception:
            print("Failed to get file from " + remoteRootDir + '/' + line[2:], "File Not found")

    sftp.close()

    return successful

def closeSSHChannels():
    ssh.close()
