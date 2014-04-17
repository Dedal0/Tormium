#!/usr/bin/python

#Written By Dedalo (@SeguridadBlanca)

import commands

end = "\033[0m"
red = "\033[1;91m"
green = "\033[92m"

#verify if tor running
output = commands.getoutput('ps -A')

#DefinePort
port = 9050


#Execute
def executetor():
	print green + '''
 _______                   _                 
|__   __|                 (_)                
   | | ___  _ __ _ __ ___  _ _   _ _ __ ___  
   | |/ _ \| '__| '_ ` _ \| | | | | '_ ` _ \ 
   | | (_) | |  | | | | | | | |_| | | | | | |
   |_|\___/|_|  |_| |_| |_|_|\__,_|_| |_| |_|
    Welcome To Tormium                                         
''' + end

	ruta = "tor/.config/chromium/Tormium"
	exetor = "chromium-browser --user-data-dir=\"" + ruta + "\" --proxy-server=\"socks5://127.0.0.1:" + str(port) + "\" --no-referrers --user-agent=\"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0\" --disable-translate --disable-geolocation --dns-prefetch-disable --no-pings --disable-javascript check.torproject.org"
	commands.getoutput(exetor)
	commands.getoutput("rm -rf tor/")


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
