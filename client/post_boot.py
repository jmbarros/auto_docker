#!/usr/bin/python

import etcd
import sys
import socket
import os

#change IP or hostname for your ETCD
etcd_server = '192.168.150.25'

#######################################################################
#defs
def set_hostname( hostname ):
   "function_docstring"
   str(hostname)
   set_hostname = "hostnamectl set-hostname "+hostname
   os.system(set_hostname)
   return;

def post_boot( status ):
   "disable service"
   set_status = "systemctl " + status + " post_boot.service"
   os.system(set_status)
   return;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = (s.getsockname()[0])
print ip
s.close()

##########################################################################

client = etcd.Client(host=etcd_server, port=2379)

project = client.read('/adm/conf/project')
server = client.read('/adm/conf/server')
num_server = client.read('/adm/conf/numserver')
setting = client.read('/adm/conf/setting')

project = project.value
server = server.value
num_server = num_server.value
setting = setting.value

setting_int = int(setting)
setting_str = str(setting)

###########################################################################

if setting_int == 1: 
   	hostname = server + setting_str
   	set_hostname(hostname)
   	setting_p = setting_int + 1
   	client.write('/adm/conf/setting', setting_p)
   	client.write('/projects/' + project + '/hosts/', None, dir=True) 
   	client.write('/projects/' + project + '/hosts/' + hostname, ip )
   	post_boot('disable')
   	print 'if 1   >>>>>  ' + hostname
   	sys.exit(1)

elif setting_int == int(num_server): 
	hostname = server + setting_str
	set_hostname(hostname)
	client.write('/adm/conf/setting', 0 )
	client.write('/projects/' + project + '/hosts/' + hostname, ip) 
	print ('chegou ao limite')
	post_boot('disable')
	print 'elif 1    >>>> ' + hostname
	sys.exit(1)

elif setting_int == 0:
	print ('elif2 >>>>>>. chegou ao limite')
	post_boot('disable')
	sys.exit(1)

else:
	hostname = server + setting_str
	setting_p = setting_int + 1
	set_hostname(hostname) 
	client.write('/adm/conf/setting', setting_p)
	client.write('/projects/' + project + '/hosts/' + hostname, ip)
	print 'else   >>>>' + hostname
	post_boot('disable')
 
	



#