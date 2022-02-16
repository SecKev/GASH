#!/usr/bin/env python3

#################################################################
#
# Create: 9/29/21
# Purpose: Scan all security headers
#           Identify misconfigured or missing headers
#
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
        mCount = 0
        for x in mFields:
            if x in checkFields:
                print("[+] Mandatory Security FOUND: " + x)
                f.write('[+] Mandatory Security FOUND: ' + x + '\n')
            else:
                print("[-] Mandatory Security NOT FOUND: " + x)
                f.write('[-] Mandatory Security NOT FOUND: ' + x +'\n')
                mCount += 1

        for y in oFields:
            if y in checkFields:
                print("[+] Options Security FOUND: " + y)
                f.write('[+] Options Security FOUND: ' + y + '\n')
            else:
                print("[-] Options Security NOT FOUND: " + y)
                f.write('[-] Mandatory Security NOT FOUND: ' + y + '\n')
        hstsCount = 0
        for z in config:
            if z not in checkFields:
                print('[-] Misconfiguration of HSTS')
                f.write('[-] Misconfiguration of HSTS \n' )
                hstsCount += 1
            else:
                print('[+] Correct HSTS configuration')
                f.write('[+] Correct HSTS configuration \n')
        serverCount = 0
        for s in sFields:
            if s not in checkFields:
                print("[-] Server Header NOT FOUND: ")
            else:
                print("[-] Server Header FOUND:" + s)
                serverCount += 1


        print("\n       !PROCESSING COMPLETED!  ")
        print('*****************************************\n')
        f.write("\n     !PROCESSING COMPLETED!  ")
        f.write('\n***************************************\n')


f.write("Total URL scanned " + str(urlCount))
f.close()
print("Total URL scanned " + str(urlCount))
print("HSTS misconfiguration: " + str(hstsCount))
print("Misconfigured Server Header: " + str(serverCount))


#####################################
# r = open('results.txt', 'a')
# r.write(pStatus + '\n')
#
# r.write(str(dict(hInfo) + '\n'))
#
# r.write(eType + '\n')
# r.close()
####################################
