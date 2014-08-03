ith
===

Open source Python tool to pentest websites using Mysql offline google dorks database (Offensive security Db).

Description :

["Ith"] Is a python open source tool, under GPL v2 license, developped to do pentest for websites using MySql offline offensive security google dorks database.

Also, [Ith] is used to search this database for dorks by category or using keywords and export results for other works.

For example, if we like to pentest a given website for a specific dork or a list of common dorks, let's say that we wont to test a website running joomla (with some tiers modules) for SQLi, we will choose option (2) (Search database for dorks by category with keywords), with category (1) (SQL Injection) and keywords : (joomla; com_newsletter).

After getting the result, we launch the pentest.

["Ith"] is easy for use and i hope that you find it helpful.

Home screen:

Initialisation :
[*] Reading Bdd configuration section
[*] Connexion to local database.
[-] Connected to database

        ### ##### ### ##### ## ### ##### ##### ####################
        #                   [ITH] IN THE HELL                     #
        #                                                         #
        #           - Pentesting websites with dorks              #
        #   - Searching Google dorks from an offline database     #
        #                                                         #
        ### ##### ### ##### ## ### ##### ##### ####################
        Version: 1.0 
        Date : 31/07/2014 
        Author :  FATHI Med Ali (It-Solunium) 
        Source of dorks : [http://www.exploit-db.com/google-dorks/] 


  Please, select an option : 

    (1) Search database for dorks with keywords. 
    (2) Search database for dorks by category with keywords. 
    (3) Search database for dorks by Id(db-exploit). 
    (4) ITH configuration. 
    (u) Update database. 
    (h) Help. 
    (q) Quit. 

 -> 

Pre-requisites:

[*] Python 2.7
[*] MySql

Installation:

1- Clone the git solution from :  https://github.com/it-solunium/ith.git
2- Setup the database connexion from : config.py (Host, user, password & db)
3- Execute : Python create_db.py (To create & import the google dorks database)
4- Enjoy! (Python ith.py)

