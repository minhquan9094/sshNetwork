import paramiko
import time

ip_address = "192.168.100.30"
username = "quandm"
password = "123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("enable\n")
remote_connection.send("123\n")

while True:
    output = remote_connection.recv(65535)
    cli= raw_input(output +"")
    remote_connection.send(cli+"\n")
    time.sleep(1)

def ssh_connect(ip,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    remote_connection = ssh_client.invoke_shell()
    print "Successful connection", ip_address
    return remote_connection

def save_config(ssh,filenameSave,command,pass_enable):
    ssh.send("enable\n")
    ssh.send("123\n")
    ssh.send("terminal leng 0\n")
    ssh.send(command + "\n")
    output=ssh.recv(65535)
    print output
    ssh_client.close
    

