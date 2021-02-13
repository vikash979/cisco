#!/bin/sh

# location of index.php to overwrite with temporary message   
index_php_loc='sitepath/index.php';       
mailid="info@linuxtweaks.in"



check=`cat /proc/loadavg | sed 's/./ /' | awk '{print $1}'`



max_load='25'



high_load_log='/var/log/apache_high_load_restart.log';



apache_init='/etc/init.d/apache2';

site_maintenance_msg="Site Maintenance in progress - We will be back online in a minute";

if [ $check -gt "$max_load" ]; then>



cp -rpf $index_php_loc $index_php_loc.bak_ap

echo "$site_maintenance_msg" > $index_php_loc

sleep 15;

if [ $check -gt "$max_load" ]; then

$apache_init stop

sleep 5;

$apache_init restart

echo "$(date) : Apache Restart due to excessive load | $check |" >> $high_load_log;

cp -rpf $index_php_loc.bak_ap $index_php_loc
echo "service restart on high load please check the server"|mail -s "Apache Restart on high load" $mailid

fi

fi
