#!/usr/bin/env python
# -*- coding: utf8 -*-

"""

                      __                    __    
        .---.-.--.--.|  |_.----.---.-.----.|  |--.
        |  _  |  |  ||   _|   _|  _  |  __||    < 
        |___._|\___/ |____|__| |___._|____||__|__|

		avtrack keeps track of status for avatars on imvu.
		
		Version: 0.1
		
		Written by Peter Bartels - https://www.kangafoo.de
        
        Requirements:
        
        python -m pip install requests
		
"""

import sys
import argparse
import os
import requests
import time
import datetime
import json

stat = "1"


def clear():
    """
    
    clear() -> no return
    
    just clear screen for linux and windows
    
    """
    os.system("cls" if os.name == "nt" else "clear")	


def infoheader():
    """
    
    infoheader() -> no return
    
    prints header logo and avatar target name and CID
    
    """
    clear()
    print("              __                    __     ")
    print(".---.-.--.--.|  |_.----.---.-.----.|  |--. ")
    print("|  _  |  |  ||   _|   _|  _  |  __||    <  ")
    print("|___._|\___/ |____|__| |___._|____||__|__| \n")
    print("-"*50)
    print("->>  Target: %s%s" %(options.cid,options.user))
    print("-"*50)


def printhelp():
    """
    
    printhelp() -> no return
    
    prints header logo and displays help parameters
    
    """
    clear()
    print("              __                    __     ")
    print(".---.-.--.--.|  |_.----.---.-.----.|  |--. ")
    print("|  _  |  |  ||   _|   _|  _  |  __||    <  ")
    print("|___._|\___/ |____|__| |___._|____||__|__| \n")
    parser.print_help()
    
def getusercid(username):
    """
    
    getusercid(string) -> string
    
    tries to retrieve the CID of an avatar for a name to cid lookup
    
    """
    getuser = 'http://www.imvu.com/catalog/web_av_pic.php?av=%s' % (username)
    r = requests.get(getuser)
    link = r.url
    cid = link[link.index('avatars/')+len('avatars/'):link.index('_')]
    return cid
	
def checkavatar(cid):
    """
    
    checkavatar(string) -> no return
    
    checks the online status of an avatar using inofficial imvu api and prints status
    
    """
    room = 'http://client-dynamic.imvu.com/api/avatarcard.php?cid=%s&viewer_cid=%s' % (cid,cid)
    response = requests.get(room)
    rcontent = response.content
    # imvu servers block temporarily ip addresses when too many requests are made, so we pause then
    if rcontent.find(b'You have made too many requests recently') != -1:
        print('\n\r\n\r')
        print(' --- too many requests, lets have a break and get a coffee for a bit. waiting 3 minutes ---\n\r')
        time.sleep(180) #3 minutes
    else:
        global stat
        cstatus = "0"
        now = datetime.datetime.now()
        dat = now.strftime("%Y-%m-%d %H:%M")
        dict = json.loads(response.content)
        # check whether the status changed and display then
        if 'availability' in dict:
            cstatus = dict['availability']
            if cstatus != stat:
                print (dat+" Status: "+cstatus)
                stat = cstatus
            else:
                if verb:
                    print (dat+" Status: "+cstatus)
                    stat = cstatus
		
if __name__=="__main__":
    parser = argparse.ArgumentParser("%prog [options] arg1 arg2")
    parser.add_argument("-c", "--cid", dest="cid",default="",help="specify the cid of a user")
    parser.add_argument("-u", "--user", dest="user",default="",help="specify the username of a user")
    parser.add_argument("-d", "--delay", dest="delay",default=60,help="define a delay between repetition in seconds")
    parser.add_argument("-v", "--verbose",dest="verbose_switch",default=False, action="store_true",help="shows all attempts")
    options = parser.parse_args()
    if len(sys.argv) < 2:
        printhelp()
        quit()
    else:
        cid = options.cid
        verb = options.verbose_switch
        user = options.user
        dele = options.delay
        infoheader()
        if options.cid:
            while 1 > 0:
                checkavatar(cid)
                time.sleep(float(dele))
        elif options.user:
            usercid = getusercid(user)
            if usercid != 'default':
                while 1 > 0:
                    checkavatar(usercid)
                    time.sleep(float(dele))
            else:
                print('User not found, try using the cid instead?')