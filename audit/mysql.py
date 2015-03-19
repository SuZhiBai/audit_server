#!/usr/bin/env python
#author
#by 20150315
import MySQLdb
def group_info(group_table,add_host=None,del_host=None):
    conn = MySQLdb.connect(host='192.168.10.46',user='root',passwd='123456',db='host_db')
    #DATBASENAME:host_db
    cur=conn.cursor()
    if add_host == None and del_host == None:
        cur.execute('select * from %s'%group_table)
    #TABLE:group_table as "web group","db group"
    #(host_ID,host_name,username,password,host_desc)
        group_list = cur.fetchall()
        cur.close()
        conn.close()
        return group_list
    elif del_host == None:
        cur.execute('insert into group_table values(add_host)')
        cur.close()
        conn.commit()
        conn.close()
        return True
    elif add_host == None:
        cur.execute('drop from group_table where host_ID == del_host')
        cur.close()
        conn.commit()
        conn.close()
        return True
    else:
        return 'please check your input'
def host_info(host_id=None,add_host=None,del_host=None):
    conn = MySQLdb.connect(host='192.168.10.46',user='root',passwd='123456',db='host_db')
    cur=conn.cursor()
    if host_id == None and add_host == None and del_host == None:
        cur.execute('select host_ID,host_name from host_table')
        #TABLE:host_table
        #(host_ID,host_name,password,host_desc)
        host_list = cur.fetchall()
        for i in host_list:
            print i[0],i[1]
        cur.close()
        conn.close()
    elif add_host == None and del_host == None:
        cur.execute('select host_name,username,password from host_table where host_ID=%s'%host_id)
        host_list = cur.fetchall()
        cur.close()
        conn.close()
        return host_list
    elif del_host == None:
        cur.execute('insert into host_table values(add_host)')
        cur.close()
        conn.commit()
        conn.close()
        return True
    elif add_host == None:
        cur.execute('drop from host_table where host_ID == del_host')
        cur.close()
        conn.commit()
        conn.close()
        return True
    else:
        return 'please check your input'
#group_list = group_info('group1')
#    for i in group_list:
#    print i[0],i[1],i[4]
#print host_info(host_id=1)
