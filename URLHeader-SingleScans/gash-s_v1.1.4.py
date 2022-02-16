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
#        'username': 'bofa.admin.gep.com',
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

    xframeField = ['X-Frame-Options']
    xssField =['X-XSS-Protection']
    cspField = ['Content-Security-Policy']
    accessField = ['Access-Control-Allow-Origin']
    oFields = ['X-Content-Type-Options']
    config = {'Strict-Transport-Security' : 'max-age:31536000; includeSubdomains; preload'}
    sFields = ['Server']

    checkFields = dict(hInfo)
    for x in xframeField:
        if x in checkFields:
            print("[+] Mandatory Security FOUND: " + x)
        else:
            print("[-] Mandatory Security NOT FOUND: " + x)

    for w in xssField:
        if w in checkFields:
            print("[+} Mandatory Security FOUND: " + w)
        else:
            print("[-] Mandatory Security NOT FOUND: " + w)

    for v in cspField:
        if v in checkFields:
            print("[+] Mandatory Security FOUND: " + v)
        else:
            print("[-] Mandatory Security NOT FOUND: " + v)

    for t in accessField:
        if t in checkFields:
            print("[+] Mandatory Security FOUND: " + t)
        else:
            print("[-] Mandatory Security NOT FOUND: " + t)
            
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
        if s not in checkFields:
            print("[+] Server Header NOT FOUND: " + s)
        else:
            print("[-] Server Header FOUND: " + s)

print("\nPROCESSING COMPLETED \n")

headInfo()
