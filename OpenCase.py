#Travis Kasinger
from simple_salesforce import Salesforce
import pymssql
import pyodbc
import json

done = False
def statuscheck():
    global done
    uname = input(str("Enter Username: "))
    pword = input(str("Enter password: "))
    key = input(str("Enter API key: "))
    sf=Salesforce(username=uname, password=pword, security_token=key)
    cid_ask = input(str("Enter Case Number to get Status: " ))
    try:
        a=sf.query("SELECT Status, Owner.Name FROM case where CaseNumber = '{0}'".format(cid_ask))
        status = a['records'][0]['Status']
        owner = a['records'][0]['Owner']['Name']
        print("Case {0} is owned by {1} and is in status {2}".format(cid_ask, owner, status))
        done = True
    except:
        print("The case number you have entered is invalid.")

while (done == False):
    statuscheck()

