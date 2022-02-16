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
xframeCount = 0
xssCount = 0
cspCount = 0
hstsCount = 0
serverCount = 0
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

        xframeFields = ['X-Frame-Options']
        xssFields = ['X-XSS-Protection']
        cspFields = ['Content-Security-Policy']
        accessFields = ['Access-Control-Allow-Origin']
        oFields = ['X-Content-Type-Options']
        rServer = ['Server']
        config = {'Strict-Transport-Security' : 'max-age:31536000; includeSubdomains; preload'}
        sFields = ['Server']
        
        checkFields = dict(hInfo)
        for x in xframeFields:
            if x in checkFields:
                
                print("[+] Mandatory Header FOUND: " + x)
                f.write('[+] Mandatory Header FOUND: ' + x)
            else:
                print("[-] Mandatory Header NOT FOUND: " + x)
                f.write('[-] Mandatory Header NOT FOUND: ' + x)
                xframeCount += 1

        
        for w in xssFields:
            if w in checkFields:
                
                print("[+] Mandatory Header FOUND: " + w)
                f.write('[+]Manatory Header FOUND: ' + w)
            else:
                print("[-] Mandatory Header NOT FOUND: " + w)
                f.write('{-] Mandatory Header NOT FOUND: ' + w)
                xssCount += 1

        
        for v in cspFields:
            if v in checkFields:
                
                print("[+] Mandatory Header FOUND: " + v)
                f.write('[+] Mandatory Header FOUND: ' + v)
            else:
                print("[-] Mandatory Header NOT FOUND: " + v)
                f.write('[-] Mandatory Header NOT FOUND: ' + v)
                cspCount += 1
     
        for t in accessFields: 
            if t in checkFields:
                print("[+] Mandatory Header FOUND: " + t)
                f.write('[+] Mandatory Header FOUND: ' + t)
            else:
                print("[-] Mandatory Header NOT FOUND: " + t)
                f.write('[-] Mandatory Header NOT FOUND: ' + t)
                
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
                hstsCount += 1
            else:
                print('[+] Correct HSTS configuration')
                f.write('[+] Correct HSTS configuration \n')

        
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
print("Misconfigured XFrame Options: " + str(xframeCount))
print("XSS Protection: " + str(xssCount))
print("Misconfigured CSP: " + str(cspCount))
#print("Misconfigured Access-Control-Allow-Origin: " + str(accessCount))
print("HSTS misconfiguration: " + str(hstsCount))
print("Misconfigured Server Header: " + str(serverCount))


