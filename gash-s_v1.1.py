#!/usr/bin/env python3

#################################################################
# Create: 9/29/21
# Purpose: Scan for Javascript vulnerabilities
#
# Functions:
#  1. Crawl website
#  2. Search for Form, Messages, and Comments section of website
#  3. Test for XSS, xxe, CORS, CLI, RFI
#   * find all the input filed: search, comment box, username / password field
#   * contact forms, message forms, ALL FORM and INPUT field.
#   * Web crawler: general, focused, deep
##################################################################

import requests as req


print("[+] Target URL to scan: ") 
tURL = str(input())
resp = req.get(tURL)

####################################################################
#Function for authentication
#def authIO():
#    payload ={
#        'username': '--',
#        'pass': '--'
#        }
#
#    with req.Session() as session:
#        post = session.post('https://nexxeqc.gep.com', 'data=payload')
#        r = session.get('https://nexxeqc.gep.com/BOFA/')
#        print(r.text)
######################################################################

def headInfo():
    global hInfo

    pStatus = str(resp.status_code)
    hInfo = resp.headers
    eType = str(resp.encoding)
    print("Target URL: " + tURL)
    print("Page Status: " + pStatus)
    print("Encoding Type: " + eType)
    for key, value in hInfo.items():
        print(key + " => " + value)
       

    print("\n   Search Security Headers")
    print("----------------------------")

    mFields = ['X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security', 'Content-Security-Policy', 'Access-Control-Allow-Origin']
    oFields = ['X-Content-Type-Options']
    config = {'Strict-Transport-Security' : 'max-age:31536000; includeSubdomains; preload'}
    sFields = ['Server']

    checkFields = dict(hInfo)
    for x in mFields:
        if x in checkFields:
            print("[+] Mandatory Security FOUND: " + x)
        else:
            print("[-] Mandatory Security NOT FOUND: " + x)

    for y in oFields:
        if y in checkFields:
            print("[+] Options Security FOUND: " + y)
        else:
            print("[-] Options Security NOT FOUND: " + y)

    for z in config: 
        if z not in checkFields:
            print('[-] Misconfiguration of HSTS')
        else:
            print('[+] Correct HSTS configuration')
    
    for s in sFields:
        if s in sFields:
            print("[+] Server Header FOUND: " + s)
        else:
            print("[-] Server Header NOT FOUND!" + s)

print("\nPROCESSING COMPLETED \n")

headInfo()
