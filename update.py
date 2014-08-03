#!/usr/bin/env python
# -*- coding: UTF-8 -*-

        

import mechanize
from bs4 import BeautifulSoup  
from misc import misc
from misc import bcolors

class update:
    def __init__(self):
        #print ""
        vnum = 1
        
    def update_dorks(self, db, lastDorkIdInDb):    
        # Update parameters
        urlGhdb = "http://www.exploit-db.com/ghdb/"
        nbOfFailure = 0
        i = lastDorkIdInDb[0]
        isUpdated = 0
        
        db_cur = db.cursor()
        misc_instance = misc()
        title_dork = ""
        link_dork = ""
        nbhits_dork = ""
        dateSubmission_dork = ""
        description_dork = ""
        
        link_dork = "" # Initialisation de link_dork
        
        # Initialization of browser
        browsing = mechanize.Browser()
        browsing.set_handle_robots(False)   # ignore robots
        browsing.set_handle_refresh(False)  # can sometimes hang without this
        browsing.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.0; rv:30.0) Gecko/20100101 Firefox/30.0')]
        
        while nbOfFailure < 5:  # For update
        
            i = i + 1 
            print "    Element N° %s" % i
            urlDork = "%s%s/" % (urlGhdb, i)
            
            # Check internet conectivity
            is_connected = misc.check_Internet_connectivity(misc_instance)
            if is_connected:
                print "    Opening: %s" % urlDork            
                error_Http = 0
                try:
                    response_browsing = browsing.open(urlDork)
                except Exception as e:
                    if e.code == 503:
                        print bcolors.WARNING+"[-] Service unavailable. Could be a Captcha. Pass to next dork!"+bcolors.ENDC
                        error_Http = 1
                        
                if error_Http == 0:
                    response_browsing.encoding = "UTF-8"            
                    if response_browsing.code == 200:
                        try:        
                            title_dork = browsing.title()
                        except:
                            print "["+bcolors.FAIL+"x"+bcolors.ENDC+"] Title parsing error!"
                        else:
                            
                            if "Page not found" in str(title_dork):
                                nbOfFailure = nbOfFailure + 1
                            else:    
                                if title_dork != None and title_dork != "":                         
                                    print "Title : %s" % title_dork
                                for link in browsing.links():
                                    
                                    links_dork = link.url
                                    
                                    if links_dork[0:29] == "http://www.google.com/search?":
                                        id_dork = i
                                        dork = link.text
                                        link_dork = link.url
                                        
                                        print "Dork Id = %s " % i
                                        
                                        if link.text != "":
                                            print "Dork text = %s " % link.text #Dork
                                        
                                        if link.url != "":
                                            print "Dork link = %s " % link.url
                                
                                # Using BSoup to search the page
                                soup = BeautifulSoup(browsing.response().read())
                                all_paragraphs = soup.find_all('p')
                                for paragraph in all_paragraphs:
                                    str_paragraph = str(paragraph)
                                    
                                    # Get number of hits
                                    if str_paragraph[0:8] == "<p>Hits:":
                                        nbhits_dork = str_paragraph[9:len(str_paragraph)-4]
                                        if nbhits_dork != "0":
                                            print "Dork Hits = %s" % nbhits_dork
                                    
                                    # Get date of submission
                                    if str_paragraph[0:12] == "<p>Submited:":
                                        dateSubmission_dork = str_paragraph[13:len(str_paragraph)-4]
                                        if dateSubmission_dork != "":
                                            print "Dork date submission  = %s" % dateSubmission_dork
                                        
                                    # GET DESCRIPTION
                                    
                                    if str_paragraph[0:16] == "<p class=\"text\">":
                                        description_dork = str_paragraph[16:len(str_paragraph)-4]
                                        if description_dork != "":
                                            print "Dork description  = %s" % description_dork
                                        
                                            
                                # bDD INSERT
                                if link_dork == "" or nbhits_dork == 0: #TODO: And Id dont exist
                                    #print "No insertion"
                                    nbOfFailure = nbOfFailure + 1
                                else:
                                    data = db_cur.execute("SELECT * FROM dorks WHERE dork_id = %s", id_dork) # Changed from id_dork to i for updates
                                    if data == 0 :
                                        db_cur.execute ("INSERT INTO dorks (dork_id, title, link, hits, date, description) values (%s, %s, %s, %s, %s, %s)",(id_dork, title_dork, link_dork, nbhits_dork, dateSubmission_dork, description_dork));
                                        # Changed id_dork to i
                                        # Adding .strip() for spaces
                                        db.commit()
                                        isUpdated = 1
                                    else:
                                        print "Existing dork. No insertion"
                                
                                #Reinitialisation des parametres
                                title_dork = ""
                                link_dork = ""
                                nbhits_dork = ""
                                dateSubmission_dork = ""
                                description_dork = ""
                                
                                
                                #print "-------------------"
                            
                    else:
                            print "Dork introuvable ..."
        return isUpdated
        
                    
