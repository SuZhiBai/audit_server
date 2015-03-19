#!/usr/bin/env python
#by 20150316
import paramiko
import mysql
import action
import threading
import pexpect
while 1:
    print ''' welcome login audit system:
            1   group operate
            2   one operate'''
    std = int(raw_input('input your option:'))
    if std == 1:
        print '------1 group list:--------'
        group_list = mysql.group_info('group1')
        
        for host in group_list:
            print host[0],host[1],host[4]
        print '-------2 group list:--------'
        std_group_num = raw_input('choose your group:')
        print '''choose your oparate:
            1   command
            2   get
            3   put'''
        std_action = int(raw_input('choose your action:'))
        std_com = raw_input('input command:')        
        if 'group' + str(std_group_num) == 'group1':
            if std_action == 1:
                for host in group_list:
                    p = threading.Thread(target=action.SSH,args=(host[1],host[2],host[3],std_com))
                    p.start()
                break
            elif std_action == 2:
                for host in group_list:
                    p = threading.Thread(target=action.SFTP,args=(host[1],host[2],host[3],std_com.split()[0],std_com.split()[1],'get'))  
                    p.start()
                break
    if std == 2:
        print '---------host list:--------------'
        print mysql.host_info()
        std_host_num = int(raw_input('choose your host for oparate:'))
        host = mysql.host_info(std_host_num)
        print host
        cmd = 'python demo.py %s' % host[0][0]
        server = pexpect.spawn(cmd)
        server.expect(':')
        server.sendline(host[0][1])
        server.expect('[p]')
        server.sendline('p')
        server.expect(':')
        server.sendline(host[0][2])
        server.interact()

            
        
