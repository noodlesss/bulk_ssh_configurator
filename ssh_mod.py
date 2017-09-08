import paramiko


class SSH_Connect(object):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.con = paramiko.SSHClient()
        self.con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.con.connect(host, username = self.username, password = self.password)
    
    def send_command(self,line):
        stdin, stdout, stderr = self.con.exec_command(line+'\n')
        return stdin, stdout, stderr