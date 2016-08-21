Setup static ip in /etc/dhcpcd.conf

    interface eth0
    static ip_address=192.168.1.20/24
    static routers=192.168.1.1
    static domain_name_servers=192.168.1.1


Disable ssh by password (TODO)

Instal afraid-cron script into /etc/cron.hourly with: (https://freedns.afraid.org/dynamic/)

    PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin

    wget --no-check-certificate -O - https://freedns.afraid.org/dynamic/update.php?VVVNY1JLMzFVMVVBQU5PTEhCVUFBQUF6OjExODM4NzY3 >> /tmp/freedns_pedro-badajoz_mooo_com.log 2>&1 &




