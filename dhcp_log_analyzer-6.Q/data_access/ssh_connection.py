# data_access/ssh_connection.py
import paramiko

def connect_ssh(host, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout
