#!/bin/bash
server_ip=''

dip=$(dig +short myip.opendns.com @resolver1.opendns.com)
ip=$(cat < /root/a)   #Create a file named a and enter your current IP once 
if [ $dip = $ip ]
	then
	echo "if condition"

	

	else
	echo $dip > /scripts/a
	ssh root@$server_ip << EOF
sed -i "1002s/.*/A record $dip/" /etc/named.conf
exit
EOF
	service named restart
fi
echo $dip
echo $ip
