from simple_salesforce import Salesforce
import pymssql
import pyodbc
import json

sf=Salesforce(username='', password='',security_token='')
done = False
def statuscheck():
    ##cid='05338520'
    cid_ask = input(str("Enter Case Number to get Status: " ))
    try:
        a=sf.query("SELECT Status, Owner.Name FROM case where CaseNumber = '{0}'".format(cid_ask))
        status = a['records'][0]['Status']
        owner = a['records'][0]['Owner']['Name']
        return("Case {0} is owned by {1} and is in status {2}".format(cid_ask, owner, status))
        global done
        done = True
    except:
        print("The case number you have entered is invalid.")
while (done == False):
    statuscheck()


#what the fudge
