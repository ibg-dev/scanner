import os
import time
import re
import sys
import smtplib, ssl

import IBG_Logger

target_network = sys.argv[1]
ip_address_list_old = []
ip_address_list_new = []
ip_address_template = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'

while True:

    command_output = os.popen("nmap -sP "+target_network).read()

    ip_address_list_new = re.findall(ip_address_template,command_output)

    recently_added_hosts = list(set(ip_address_list_new) - set(ip_address_list_old))

    recently_added_hosts.sort()

    recently_removed_hosts = list(set(ip_address_list_old) - set(ip_address_list_new))

    if (len(recently_added_hosts) != 0):
        email_context = "Hosts recently added ["+str(len(recently_added_hosts))+"]: "+str(recently_added_hosts)
        IBG_Logger.logger.critical(email_context)

    if(len(recently_removed_hosts) != 0):
        email_context = "Hosts recently removed ["+str(len(recently_removed_hosts))+"]: "+str(recently_removed_hosts)
        IBG_Logger.logger.critical(email_context)

    ip_address_list_old = ip_address_list_new

    time.sleep(30)
