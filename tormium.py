#!/usr/bin/python

#Written By Dedalo (@SeguridadBlanca)

import sys
import commands

end = "\033[0m"
red = "\033[1;91m"

#verify if tor running
output = commands.getoutput('ps -A')

#DefinePort
port = 9050


#Execute
def executetor():
	ruta = "tor/.config/chromium/Tormium"
	exetor = "chromium-browser --user-data-dir=\"" + ruta + "\" --proxy-server=\"socks5://127.0.0.1:" + str(port) + "\" --incognito check.torproject.org"
	commands.getoutput(exetor)


#Goodbye
def goodbye():
	verify = commands.getoutput('service --status-all')
	if "tor" in verify:
		print red + "Please run Tor Service: sudo service tor start" + end
	else:
		print red + "seems you don't have tor project, Download it from https://www.torproject.org" + end


if ' tor' in output:
    executetor()
else:
	goodbye()
