#!/usr/bin/env python 
# -*- coding: UTF-8 -*-



import MySQLdb
from misc import bcolors


class db_manager:
    def __init__(self):
        #print ""
        vnum = 1

    def connexion(self, connexionParameters):
        #print ""
        print "["+bcolors.OKBLUE+"*"+bcolors.ENDC+"] Connexion to local database."
        
        try:
            db = MySQLdb.connect(host=connexionParameters[0], user=connexionParameters[1], passwd=connexionParameters[2], db=connexionParameters[3])

        except Exception as im:
            #exception = str(im)
    
            if im[0:1] == (2002,):        
                print "["+bcolors.FAIL+"-"+bcolors.ENDC+"] Exception : Connexion to database error"
                print "["+bcolors.FAIL+"-"+bcolors.ENDC+"] Please, MySQL server must be running!"
                print "["+bcolors.FAIL+"*"+bcolors.ENDC+"] Exit!"                
            
            else:
                print "["+bcolors.FAIL+"-"+bcolors.ENDC+"] Please, verify your configuration file (config.py) section : #Database configuration"
            
            exit()
    
        else:
            print "["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Connected to database"    
            return (db)
        
    def deconnexion(self, db):
        db.close()
        print "\r\n \r\n["+bcolors.OKGREEN+"-"+bcolors.ENDC+"] Disconnected from database"
        
    def searchDorksWithKeywords(self, db_cur, keywords):
        # Search database for dorks with keywords
        if len(keywords) == 0:
            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
            result = 0
        if len(keywords) == 1:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%'")
        elif len(keywords) == 2:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%'")
        elif len(keywords) == 3:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%'")
        else:
            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%'")
        
        return result
    
    def searchDorksWithKeywordsByCategory(self, db_cur, keywords, categoryId):
        # Search database for dorks with keywords by category
        if categoryId == "1": #Sqli
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%SQL Injection%'")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%SQL Injection%'")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and description like '%SQL Injection%'")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and description like '%SQL Injection%'")
            
        if categoryId == "2": #LFI
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%LFI%' or description like '%Local file inclusion%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%LFI%' or description like '%Local file inclusion%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%LFI%' or description like '%Local file inclusion%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%LFI%' or description like '%local file inclusion%')")
        
        if categoryId == "3": #RFI
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%RFI%' or description like '%remote file inclusion%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%RFI%' or description like '%remote file inclusion%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%RFI%' or description like '%remote file inclusion%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%RFI%' or description like '%remote file inclusion%')")
        
        if categoryId == "4": #XSS
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%XSS%' or description like '%Cross-Site Scripting%' or description like '%Cross Site Scripting%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%XSS%' or description like '%Cross-Site Scripting%' or description like '%Cross Site Scripting%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%XSS%' or description like '%Cross-Site Scripting%' or description like '%Cross Site Scripting%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%XSS%' or description like '%Cross-Site Scripting%' or description like '%Cross Site Scripting%')")
        
        if categoryId == "5": #CSRF
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%CSRF%' or description like '%Cross-Site Request Forgery%' or description like '%Cross Site Request Forgery%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%CSRF%' or description like '%Cross-Site Request Forgery%' or description like '%Cross Site Request Forgery%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%CSRF%' or description like '%Cross-Site Request Forgery%' or description like '%Cross Site Request Forgery%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%CSRF%' or description like '%Cross-Site Request Forgery%' or description like '%Cross Site Request Forgery%')")
                
        if categoryId == "6": #PASSWD
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%passwd%' or description like '%password%' or description like '%pass%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%passwd%' or description like '%password%' or description like '%pass%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%passwd%' or description like '%password%' or description like '%pass%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%passwd%' or description like '%password%' or description like '%pass%')")
        
        if categoryId == "7": #ADV&VULNWWW.
            if len(keywords) == 0:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 keyword."
                result = 0
            if len(keywords) == 1:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and (description like '%CVE%' or description like '%http://www.exploit-db.com/exploits%')")
            elif len(keywords) == 2:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and (description like '%CVE%' or description like '%http://www.exploit-db.com/exploits%')")
            elif len(keywords) == 3:
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%CVE%' or description like '%http://www.exploit-db.com/exploits%')")
            else:
                print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 keywords are accepted!"
                result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE description like '%"+keywords[0].strip()+"%' and description like '%"+keywords[1].strip()+"%' and description like '%"+keywords[2].strip()+"%' and (description like '%CVE%' or description like '%http://www.exploit-db.com/exploits%')")
        return result
    
    def searchDorksByIds(self, db_cur, Ids):
        # Search database for dorks with keywords
        if len(Ids) == 0:
            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] You must enter at least 1 Id."
            result = 0
        if len(Ids) == 1:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE dork_id like '%"+Ids[0].strip()+"%'")
        elif len(Ids) == 2:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE dork_id like '%"+Ids[0].strip()+"%' or dork_id like '%"+Ids[1].strip()+"%'")
        elif len(Ids) == 3:
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE dork_id like '%"+Ids[0].strip()+"%' or dork_id like '%"+Ids[1].strip()+"%' or dork_id like '%"+Ids[2].strip()+"%'")
        else:
            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Only first 3 Ids are accepted!"
            result = db_cur.execute("SELECT dork_id, title, link, hits, date, description FROM dorks WHERE dork_id like '%"+Ids[0].strip()+"%' or dork_id like '%"+Ids[1].strip()+"%' or dork_id like '%"+Ids[2].strip()+"%'")
        
        return result
    
    def selectMaxDorkId(self, db_cur):
        db_cur.execute("SELECT MAX(dork_id) FROM dorks")
        max_id_dork = db_cur.fetchall()[0]
        return max_id_dork
