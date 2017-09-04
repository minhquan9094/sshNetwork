import paramiko
import time

ip = "192.168.100.30"
username = "quandm"
password = "123"
def ssh_connect(ip,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    remote_connection = ssh_client.invoke_shell()
    #print "Successful connection", ip
    return remote_connection

def save_config(ssh,filenameSave,command,pass_enable):
    ssh.send("\r\n")
    ssh.send("enable\n")
    ssh.send("123\n")
    ssh.send("terminal leng 0\n")
    ssh.send(command+"\n")
    ssh.send("exit\n")
    time.sleep(1)
    output = ssh.recv(65535)
    print output   
    fileConfig = open(filenameSave,"w")
    fileConfig.write(output)
    fileConfig.close()
    
    
save_config(ssh_connect(ip,username,password),"text.txt","show running-config","123")
    

