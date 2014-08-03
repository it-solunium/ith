ith
===

Open source Python tool to pentest websites using Mysql offline google dorks database (Offensive security Db).

Description :

[Ith] Is a python open source tool, under GPL v2 license, developped to do pentest for websites using MySql offline offensive security google dorks database.

Also, [Ith] is used to search this database for dorks by category or using keywords and export results for other works.

For example, if we like to pentest a given website for a specific dork or a list of common dorks, let's say that we wont to test a website running joomla (with some tiers modules) for SQLi, we will choose option (2) (Search database for dorks by category with keywords), with category (1) (SQL Injection) and keywords : (joomla; com_newsletter).

After getting the result, we launch the pentest.

[Ith] is easy for use and i hope that you find it helpful.

Pre-requisites:

* Python 2.7

* MySql

Installation:

 1- #~ git clone https://github.com/it-solunium/ith.git.
 
 2- Setup the database connexion in : config.py (Host, user, password & db).
 
 3- #~ python create_db.py (To create & import the google dorks database).
 
 4- #~ python ith.py (Enjoy!).

