#!/usr/bin/env python
#author
#20150315
import paramiko
import sys,os
def SSH(host_ip,username,password,cmd):
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(host_ip,22,username,password,timeout=15)
    stdin,stdout,stderr = s.exec_command(cmd)
    cmd_result = stdout.read(),stderr.read()
    #cmd_result = stdout.readlines()
    for line in cmd_result:
		print line,
    s.close()
    return cmd_result
def SFTP(host_ip,USERNAME,PASSWORD,source,target,action):
	t =paramiko.Transport((host_ip,22))
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())	
	t.connect(usename=USERNAME,password=PASSWORD)
	sftp = paramiko.SFTPClient.from_transport(t)
	if action == 'get':
		sftp.get(source,target)
		s.close()
		return 'file is download successful'		
	if action == 'put':
		stfp.put(source,target)
		s.close()
		return 'file is dump successful'
if __name__ == 'main':
    SSH('192.168.10.14','root','111111','ifconfig')










