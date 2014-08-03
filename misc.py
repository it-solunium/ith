#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
from config import bddConfiguration
import sys
import os
import chardet
import re

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
class misc:
    def __init__(self):
        vnum = 1

    def readConfFile(self, section):
        if (section == "BddConfig"):
            host = bddConfiguration.host
            user = bddConfiguration.user
            passwd = bddConfiguration.passwd
            db = bddConfiguration.db
            
            print "["+ bcolors.OKBLUE+"*"+bcolors.ENDC+"] Reading Bdd configuration section"
            
            
            # Reading configuration from simple file
            '''
            try:
                with open('config.file') as fileConfig:
                    configDetails = fileConfig.read().splitlines()
                    #print configDetails
                    for configDetail in configDetails:
                        #print configDetail[0:4]
                        if configDetail[0:4] == "host":
                            host = configDetail[7:]
                            host = host.strip()
                            #print host
                        
                        if configDetail[0:4] == "user":
                            user = configDetail[7:]
                            user = user.strip()
                            #print user
                        
                        if configDetail[0:6] == "passwd":
                            passwd = configDetail[8:]
                            passwd = passwd.strip()
                            #print passwd
                            
                        if configDetail[0:2] == "db":
                            db = configDetail[5:]
                            db = db.strip()
                            #print db
                        
                            
            except Exception as ex:
                print ex.message
            else:
            '''
            connexionParameters = [host, user, passwd, db]
            return connexionParameters
            
    def bannerEN(self):
        App_Header = "\r\n"
        App_Header += "        ### ##### ### ##### ## ### ##### ##### ####################\r\n"
        App_Header += "        #                   "
        App_Header += bcolors.OKGREEN+"["+bcolors.ENDC+bcolors.FAIL+"ITH"+bcolors.ENDC+bcolors.OKGREEN+"] IN THE HELL"+bcolors.ENDC
        App_Header += "                     #\r\n"
        App_Header += "        #                                                         #\r\n"            
        App_Header += "        #      "
        App_Header += bcolors.WARNING+"     - Pentesting websites with dorks"+bcolors.ENDC
        App_Header += "              #\r\n" 
        App_Header += "        #   "
        App_Header += bcolors.WARNING+"- Searching Google dorks from an offline database"+bcolors.ENDC
        App_Header += "     #\r\n"
        App_Header += "        #                                                         #\r\n"
        App_Header += "        ### ##### ### ##### ## ### ##### ##### ####################\r\n"
        App_Header += "        "
        App_Header += bcolors.OKBLUE+"Version:"+bcolors.ENDC
        App_Header += " 1.0 \r\n"
        App_Header += bcolors.OKBLUE+ "        Date :"+bcolors.ENDC
        App_Header += " 31/07/2014 \r\n"
        App_Header += bcolors.OKBLUE + "        Author :"  +bcolors.ENDC+"  FATHI Med Ali (It-Solunium) \r\n"
        App_Header += bcolors.OKBLUE + "        Source of dorks : "  +bcolors.ENDC+"[http://www.exploit-db.com/google-dorks/] \r\n"
        #App_Header += bcolors.OKBLUE + "        Database update date : "  +bcolors.ENDC+"\r\n"
        print App_Header
        
    def homeMenuEN(self):
        menu = "\r\n"
        menu += "  Please, select an option : \r\n"
        menu += "\r\n"
        menu += "    (1) Search database for dorks with keywords. \r\n"
        menu += "    (2) Search database for dorks by category with keywords. \r\n"
        #menu += "    (3) Search database for dorks by category, between two dates with keywords. \r\n"
        #menu += "    (3) Search database for 10 most popular dorks by category with keywords. \r\n"
        menu += "    (3) Search database for dorks by Id(db-exploit). \r\n"
        menu += "    (4) ITH configuration. \r\n"
        menu += "    (u) Update database. \r\n"
        menu += "    (h) Help. \r\n"
        menu += "    (q) Quit. \r\n"
        print menu
    
    def categoryEN(self):
        categoryMenu = "\r\n"
        categoryMenu += "  List of categories : \r\n"
        categoryMenu += "\r\n"
        categoryMenu += "    (1) SQL Injection [SQLi]. \r\n"
        categoryMenu += "    (2) Local File Inclusion [LFI]. \r\n"
        categoryMenu += "    (3) Remote File Inclusion [RFI]. \r\n"
        categoryMenu += "    (4) Cross-Site Scripting [XSS]. \r\n"
        categoryMenu += "    (5) Cross-Site Request Forgery [CSRF]. \r\n"
        categoryMenu += "    (6) File containing passwords [PASSWD]. \r\n"
        categoryMenu += "    (7) Advisories and Vulnerabilities (With exploit from exploit-db) [ADV&VULN]. \r\n"
        categoryMenu += "    (q) Back to main menu. \r\n"
        
        print categoryMenu
    
    def check_Internet_connectivity(self):
        try:
            urllib2.urlopen('http://www.who.is',timeout=5)
            return True
        except urllib2.URLError: pass
        return False
    
    def clearScreen(self):
        # Clear screen
        is_windows = sys.platform.startswith('win')
        is_linux = sys.platform.startswith('linux')
        
        if is_windows:
            os.system('cls')
        elif is_linux:
            os.system('clear') # For linux & 'cls' for windows
        else:
            print "Unknown plateform."
            
    def get_encoding(self, soup):
        '''
        This is a method to find the encoding of a document.
        It takes in a Beautiful soup object and retrieves the values of that documents meta tags
        it checks for a meta charset first. If that exists it returns it as the encoding.
        If charset doesnt exist it checks for content-type and then content to try and find it.
        '''
        encod = soup.meta.get('charset')
        if encod == None:
            encod = soup.meta.get('content-type')
            if encod == None:
                content = soup.meta.get('content')
                match = re.search('charset=(.*)', content)
                if match:
                    encod = match.group(1)
                else:
                    dic_of_possible_encodings = chardet.detect(unicode(soup))
                    encod = dic_of_possible_encodings['encoding'] 
        return encod
    
    def help(self):

        print "["+bcolors.FAIL+"Ith"+bcolors.ENDC+"] Is a python open source tool, under "+bcolors.OKGREEN+"GPL v2 license"+bcolors.ENDC+", developped to do pentest for websites using MySql offline offensive security google dorks database. \r\n"
        print "Also, ["+bcolors.FAIL+"Ith"+bcolors.ENDC+"] is used to search this database for dorks by category or using keywords and export results for other works.\r\n"
        print "For example, if i like to pentest a given website for a specific dork or a list of common dorks, let's say that i wont to test a website running joomla (with some tiers modules) for SQLi, i choose option (2) Search database for dorks by category with keywords, with category (1) SQL Injection and keywords : joomla; com_newsletter. \r\n"
        print "After getting the result, we launch the pentest.\r\n"
        print bcolors.WARNING+"It's easy for use and i hope that you find it helpful"+bcolors.ENDC
        
        
