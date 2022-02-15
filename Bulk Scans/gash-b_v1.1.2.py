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

with open('checkURL.txt') as f:
        lines  = f.readlines()

f = open('results.txt', 'a')


line = []
urlCount = 0
for line in lines:
        content = line.strip() 
        print("[+] TARGET URLL: " + content)
        f.write('\n') 
        f.write('[+] TARGET URL: ' + content + '\n')
        resp = req.get(content)
        #print(resp)
        pStatus = str(resp.status_code)
        f.write('Page Status: ' + pStatus + '\n')
        print('Page Status: ' + pStatus + '\n')
        print('\nPage Headers: ')
        f.write('\nPage Headers: \n')
        f.write('------------------------- \n')
        print('---------------------------')
        eType = str(resp.encoding)
        print('Encoding Type: ' + eType)
        f.write('Encoding Type: ' + eType + '\n')
        hInfo = resp.headers
                
        for key, value in hInfo.items():
            print(key + ' => ' + value)
            f.write(key + ' => ' + value + '\n')
        urlCount += 1    
        
        print("\n Analysis of Security Headers: ")
        f.write('\n  Analysis of Security Headers: \n')
        print("----------------------------------------")
        f.write("-------------------------------------\n")

        mFields = ['X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security', 'Content-Security-Policy', 'Access-Control-Allow-Origin']
        oFields = ['X-Content-Type-Options']
        rServer = ['Server']
        config = {'Strict-Transport-Security' : 'max-age:31536000; includeSubdomains; preload'}
        sFields = ['Server']
        
        checkFields = dict(hInfo)
        for x in mFields:
            if x in checkFields:
                print("[+] Mandatory Security FOUND: " + x)
                f.write('[+] Mandatory Security FOUND: ' + x + '\n')
            else:
                print("[-] Mandatory Security NOT FOUND: " + x)
                f.write('[-] Mandatory Security NOT FOUND: ' + x +'\n')

        for y in oFields:
            if y in checkFields:
                print("[+] Options Security FOUND: " + y)
                f.write('[+] Options Security FOUND: ' + y + '\n')
            else:
                print("[-] Options Security NOT FOUND: " + y)
                f.write('[-] Mandatory Security NOT FOUND: ' + y + '\n')

        for z in config:
            if z not in checkFields:
                print('[-] Misconfiguration of HSTS')
                f.write('[-] Misconfiguration of HSTS \n' )
            else:
                print('[+] Correct HSTS configuration')
                f.write('[+] Correct HSTS configuration \n')

        for s in sFields:
            if s not in checkFields:
                print("[-] Server Header NOT FOUND: " + s)
            else:
                print("[-] Server Header FOUND:" + s)


        print("\n       !PROCESSING COMPLETED!  ")
        print('*****************************************\n')
        f.write("\n     !PROCESSING COMPLETED!  ")
        f.write('\n***************************************\n')


f.write("Total URL scanned " + str(urlCount))
f.close()
print("Total URL scanned " + str(urlCount))

#####################################
# r = open('results.txt', 'a')
# r.write(pStatus + '\n')
#
# r.write(str(dict(hInfo) + '\n'))
#
# r.write(eType + '\n')
# r.close()
####################################
