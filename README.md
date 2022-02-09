# GASH
GEP Application Security Header Automation Tool 

Targeted Scanner Framework

  Current Production:
  * Security Header Findings
  * Basic mis-configuration
  * Sensitive Data Exposure
  
  Current Development:
  * Create directory for results
  * Results file name will include date of scan
  * Total URL scanner (* for future metrics)
  * Security Header scanner will retrieve and listed misconfigured header
  * Web Crawler [general, focused, deep-dive]
  * Directory Search
  
  Future Modules for Framework:
  * Automate Search Criteria for Web Forms Messages, and Comments sections
  * Test for XSS, CORS, CLI, RFI, XXE
  * DNS Scan / SubDomain Scan
  * Custom Sub Scan
  * Related Domain Information
  * Wayback Urls
  * CVE Scanner
  * IP/Port Scan
  * Sensitive files disclosure
  * Common vulnerability detection
  * Services Detector
  * Exposed Secrets
 
REQUIREMENTS: 
* Installation of newest stable Python 3 version<br>
     https://www.python.org/downloads/windows/

Use the following command to install Libraries: 
* python -m pip <Library name><br>
     |-> For example: python -m pip requests
  
REQUIRED PYTHON LIBRARIES: 
* Requests
* BeautifulSoup4
