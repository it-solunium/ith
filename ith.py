#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from misc import misc, bcolors
from bdd import db_manager
from pentest import pentest
from config import bddConfiguration
from update import update
import os
import sys

import signal


def exitHandler(signum, frame):
    print "\r\n \r\n["+bcolors.OKBLUE+">"+bcolors.ENDC+"] Thank you for using ITH. See you soon!"
    exit()

signal.signal(signal.SIGINT, exitHandler)

# Get connexion parameters from config.py section bdd
misc_instance = misc()
# Clear screen
misc.clearScreen(misc_instance)
print "Initialisation :"

connexionParameters = []
connexionParameters = misc.readConfFile(misc_instance, "BddConfig")




# Connexion to database
db_manager_instance = db_manager()
db = db_manager.connexion(db_manager_instance, connexionParameters)
db_cur = db.cursor()

# Pentest instantiation
pentest_instance = pentest()
update_instance = update()
misc.bannerEN(misc_instance)
misc.homeMenuEN(misc_instance)

# Read input choice from user
user_choice = ""
keywords = ""
bad_caracter = 0

# Result filds
title = ""
link = ""
cmd_pentest = ""

while 1 == 1:
    user_choice = raw_input(" -> ")
    if user_choice == "1":
        # Search database for dorks with keywords
        keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks with keywords"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
        list_keywords = []
        list_keywords = keywords.split(";")
        for key in list_keywords:
            if "'" in key or "-" in key or "#" in key or "%" in key:
                bad_caracter = 1
                print "[-] Bad caracter in keywords!"
        if bad_caracter != 1:
            # Search database
            result = db_manager.searchDorksWithKeywords(db_manager_instance, db_cur, list_keywords)
            data_found = db_cur.fetchall()            
            
            for data_result in data_found:
                dork_id = str(data_result[0])
                title = str(data_result[1])
                link = str(data_result[2])
                hits = str(data_result[3])
                date = str(data_result[4]) 
                description = str(data_result[5])
                print "----- ----- -----"
                print bcolors.OKBLUE+"Dork ID :"+bcolors.ENDC+" %s" % dork_id
                print bcolors.OKBLUE+"Title :"+bcolors.ENDC+" %s" % title
                print bcolors.OKBLUE+"link :"+bcolors.ENDC+" %s" % link
                print bcolors.OKBLUE+"Hits :"+bcolors.ENDC+" %s" % hits
                print bcolors.OKBLUE+"Date of submission:"+bcolors.ENDC+" %s" % date
                print bcolors.OKBLUE+"Description :"+bcolors.ENDC+" %s" % description
                print "\r\n"
            print "[*] Number of result(s) = %s \r\n" %result
            
            while 1==1:
                if result > 0:
                    cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks with keywords"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                    if cmd_pentest == "Y":
                        # Check internet conectivity
                        is_connected = misc.check_Internet_connectivity(misc_instance)
                        if is_connected:
                            # Launch pentest with current results
                            webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks with keywords/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                            print "["+bcolors.OKBLUE+"*"+bcolors.ENDC+"] Launching pentest !"
                            pentest.pentestWebSite(pentest_instance, webSiteUrl, data_found)
                            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                            misc.homeMenuEN(misc_instance)
                            break
                        else:
                            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Check your Internet connectivity."
                            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                            misc.homeMenuEN(misc_instance)
                            break
                        
                    elif cmd_pentest == "N":
                        # back to main menu
                        
                        print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                        misc.homeMenuEN(misc_instance)
                        break
                else: # nb of result = 0
                    print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                    misc.homeMenuEN(misc_instance)
                    break
            
    elif user_choice == "2":
        # Search database for dorks by category with keywords
        misc.categoryEN(misc_instance)
        category = 0
        while 1==1:
            category = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords"+bcolors.ENDC+") Please, choose a category : ")
            if category == "q":
                print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                misc.homeMenuEN(misc_instance)
                break
            elif category == "1":                
                break
            elif category == "2":
                break
            elif category == "3":
                break
            elif category == "4":
                break
            elif category == "5":
                break
            elif category == "6":
                break
            elif category == "7":
                break
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You have to choose a category in [1,2,3,4,5,6,7]."
        
        
        if category != "q":
            if category == "1":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/SQLi"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "2":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/LFI"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "3":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/RFI"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "4":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/XSS"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "5":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/CSRF"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "6":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/PASSWD"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            if category == "7":        
                keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/ADV&VULN"+bcolors.ENDC+") Please, enter keywords separated by (;) : ")
            
            list_keywords = []
            list_keywords = keywords.split(";")
            for key in list_keywords:
                if "'" in key or "-" in key or "#" in key or "%" in key:
                    bad_caracter = 1
                    print "[-] Bad caracter in keywords!"
            if bad_caracter != 1:
                # Search database
                result = db_manager.searchDorksWithKeywordsByCategory(db_manager_instance, db_cur, list_keywords, category)
                data_found = db_cur.fetchall()            
                
                for data_result in data_found:
                    dork_id = str(data_result[0])
                    title = str(data_result[1])
                    link = str(data_result[2])
                    hits = str(data_result[3])
                    date = str(data_result[4]) 
                    description = str(data_result[5])
                    print "----- ----- -----"
                    print bcolors.OKBLUE+"Dork ID :"+bcolors.ENDC+" %s" % dork_id
                    print bcolors.OKBLUE+"Title :"+bcolors.ENDC+" %s" % title
                    print bcolors.OKBLUE+"link :"+bcolors.ENDC+" %s" % link
                    print bcolors.OKBLUE+"Hits :"+bcolors.ENDC+" %s" % hits
                    print bcolors.OKBLUE+"Date of submission:"+bcolors.ENDC+" %s" % date
                    print bcolors.OKBLUE+"Description :"+bcolors.ENDC+" %s" % description
                    print "\r\n"
                print "[*] Number of result(s) = %s \r\n" %result
                
                while 1==1:
                    if result > 0:
                        if category == "1":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/SQLi"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "2":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/LFI"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "3":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/RFI"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "4":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/XSS"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "5":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/CSRF"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "6":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/PASSWD"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if category == "7":
                            cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/ADV&VULND"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                        if cmd_pentest == "Y":
                            # Check internet conectivity
                            is_connected = misc.check_Internet_connectivity(misc_instance)
                            if is_connected:
                                # Launch pentest with current results
                                if category == "1":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/SQLi/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "2":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/LFI/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "3":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/RFI/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "4":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/XSS/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "5":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/CSRF/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "6":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/PASSWD/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                if category == "7":
                                    webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by category with keywords/ADV&VULND/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                                print "["+bcolors.OKBLUE+"*"+bcolors.ENDC+"] Launching pentest !"
                                pentest.pentestWebSite(pentest_instance, webSiteUrl, data_found)
                                print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                                misc.homeMenuEN(misc_instance)
                                break
                            else:
                                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Check your Internet connectivity."
                                print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                                misc.homeMenuEN(misc_instance)
                                break
                            
                        elif cmd_pentest == "N":
                            # back to main menu
                            
                            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                            misc.homeMenuEN(misc_instance)
                            break
                    else: # Nb of result = 0
                        print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                        misc.homeMenuEN(misc_instance)
                        break
                    
    elif user_choice == "3":
    # Search database for dorks by Id (Exploit-db)
        keywords = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by Id (exploit-db)"+bcolors.ENDC+") Please, enter an Id (Ex:3948; 3920) : ")
        list_keywords = []
        list_keywords = keywords.split(";")
        for key in list_keywords:
            if "'" in key or "-" in key or "#" in key or "%" in key:
                bad_caracter = 1
                print "[-] Bad caracter in keywords!"
        if bad_caracter != 1:
            # Search database
            result = db_manager.searchDorksByIds(db_manager_instance, db_cur, list_keywords)
            data_found = db_cur.fetchall()            
            
            for data_result in data_found:
                dork_id = str(data_result[0])
                title = str(data_result[1])
                link = str(data_result[2])
                hits = str(data_result[3])
                date = str(data_result[4]) 
                description = str(data_result[5])
                print "----- ----- -----"
                print bcolors.OKBLUE+"Dork ID :"+bcolors.ENDC+" %s" % dork_id
                print bcolors.OKBLUE+"Title :"+bcolors.ENDC+" %s" % title
                print bcolors.OKBLUE+"link :"+bcolors.ENDC+" %s" % link
                print bcolors.OKBLUE+"Hits :"+bcolors.ENDC+" %s" % hits
                print bcolors.OKBLUE+"Date of submission:"+bcolors.ENDC+" %s" % date
                print bcolors.OKBLUE+"Description :"+bcolors.ENDC+" %s" % description
                print "\r\n"
            print "[*] Number of result(s) = %s \r\n" %result
            
            while 1==1:
                if result > 0:
                    cmd_pentest = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by Ids"+bcolors.ENDC+") Do you want to launch pentest with this results ? (Y/N) : ")
                    if cmd_pentest == "Y":
                        # Check internet conectivity
                        is_connected = misc.check_Internet_connectivity(misc_instance)
                        if is_connected:
                            # Launch pentest with current results
                            webSiteUrl = raw_input(" ->("+bcolors.FAIL+"Search database for dorks by Ids/pentest"+bcolors.ENDC+") Enter a website url to pentest : ")
                            print "["+bcolors.OKBLUE+"*"+bcolors.ENDC+"] Launching pentest !"
                            pentest.pentestWebSite(pentest_instance, webSiteUrl, data_found)
                            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                            misc.homeMenuEN(misc_instance)
                            break
                        else:
                            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Check your Internet connectivity."
                            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                            misc.homeMenuEN(misc_instance)
                            break
                        
                    elif cmd_pentest == "N":
                        # back to main menu
                        
                        print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                        misc.homeMenuEN(misc_instance)
                        break
                else: # nb of result = 0
                    print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
                    misc.homeMenuEN(misc_instance)
                    break

    elif user_choice == "4":
        # Clear screen
        misc.clearScreen(misc_instance)
        print bcolors.WARNING+"  Configuration : \r\n"+bcolors.ENDC
        
        print "      Database configuration : \r\n"
        print bcolors.OKBLUE+"          Hostname"+bcolors.ENDC+" = %s \r\n" % bddConfiguration.host
        print bcolors.OKBLUE+"          Username"+bcolors.ENDC+" = %s \r\n" % bddConfiguration.user
        print bcolors.OKBLUE+"          Password"+bcolors.ENDC+" = %s \r\n" % bddConfiguration.passwd
        print bcolors.OKBLUE+"          Database name"+bcolors.ENDC+" = %s \r\n" % bddConfiguration.db
        
        print "  If you want to change database configuration, please edit config.py."
        misc.homeMenuEN(misc_instance)
        
        
    elif user_choice == "u":
        isUpdated = 0
        maxDorkId = db_manager.selectMaxDorkId(db_manager_instance, db_cur)
        print "["+bcolors.OKBLUE+"*"+bcolors.ENDC+"] Updating database from http://www.exploit-db.com/ghdb/\r\n"
        print "Last ID in database = %s" %maxDorkId
        print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Updating ..."
        isUpdated = update.update_dorks(update_instance, db, maxDorkId)
        if isUpdated:
            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Updated."
        else:
            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] No update."
        misc.homeMenuEN(misc_instance)
        
    
    elif user_choice == "h":
        misc.clearScreen(misc_instance)
        misc.bannerEN(misc_instance)
        misc.help(misc_instance)
        print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Back to main menu"
        misc.homeMenuEN(misc_instance)
    
    elif user_choice == "q":
        print "\r\n \r\n["+bcolors.OKBLUE+">"+bcolors.ENDC+"] Thank you for using ITH. See you soon!"
        exit()
    else:
        print "["+bcolors.FAIL+"-"+bcolors.ENDC+"] Wrong choice, please choose a value in (1,2,3,4,u,h,q)"
        

    
        
            


print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Exit!"



# Deconnexion from database
db_manager.deconnexion(db_manager_instance, db)


