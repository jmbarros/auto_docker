#!/bin/bash
#install_client.sh

#install 
mkdir /root/tmp/

#download packets
curl -o /root/tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py 
curl -o /root/tmp/post_boot.py https://raw.githubusercontent.com/jmbarros/auto_docker/master/client/post_boot.py
curl -o /root/tmp/post_boot.service https://raw.githubusercontent.com/jmbarros/auto_docker/master/client/post_boot.service

#yum install 

/usr/bin/yum install -y python
/usr/bin/python /root/tmp/get-pip.py
/usr/bin/pip install python-etcd

/usr/bin/chmod +x /root/tmp/*
cp /root/tmp/post_boot.service /etc/systemd/system/post_boot.service
/usr/bin/systemctl enable post_boot.service
#/usr/sbin/poweroff
