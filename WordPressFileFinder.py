import requests
import bcolors


URL= '<website Here>'

ResponseCode = requests.get(URL).status_code
print('\n''*********************license*****************')
LicenseFile = URL + 'license.txt'
print('LICENSE FILE',LicenseFile , requests.get(LicenseFile).status_code)
if(('license'in LicenseFile) and (requests.get(LicenseFile).status_code == 200)):
    print('License file does not exists')
else:
    print(bcolors + 'License file not exists')

print('\n''*********************xmlrpc*****************')
XmlrpcFile = URL + 'xmlrpc.php'
print('XMLRPC FILE',XmlrpcFile , requests.get(XmlrpcFile).status_code)
if('xmlrpc'in XmlrpcFile):
   if(requests.get(XmlrpcFile).status_code == 200):
      print('XMLRPC file exists and you can access')
   elif(requests.get(XmlrpcFile).status_code == 405):
      print('XMLRPC file exists but only accepts POST requests')
   elif (requests.get(XmlrpcFile).status_code == 404):
    print('XMLRPC file not exists')
   elif(requests.get(XmlrpcFile).status_code == 403):
       print('XMLRPC file exists but you do not have authorization')

print('\n''*********************Wp-activate*****************')
WpActivateFile = URL + 'wp-activate.php'
print('WP-ACTIVATE',WpActivateFile , requests.get(WpActivateFile).status_code)
if('wp-activate'in WpActivateFile):
    if(requests.get(WpActivateFile).status_code == 404):
     print('Wp-activate file does not exists')
    elif(requests.get(WpActivateFile).status_code == 200):
        print('Wp-activate file exists but redirect to the login page')
    elif(requests.get(WpActivateFile).status_code == 500):
        print('Wp-activate file exists')

print('\n''*********************wp-config*****************')
WpConfigFile= URL + 'wp-config.php'
print('WP-CONFIG',WpConfigFile , requests.get(WpConfigFile).status_code)
if('wp-config'in WpConfigFile):
    if (requests.get(WpConfigFile).status_code == 404):
        print('WP-CONFIG file does not exists')
    elif (requests.get(WpConfigFile).status_code == 200):
        print('WP-CONFIG file exists')

print('\n''*********************wp-content*****************')
WpcontentFile = URL + 'wp-content/uploads'
print('wpcontent',WpcontentFile , requests.get(WpcontentFile).status_code)
if('uploads'in WpcontentFile):
    if (requests.get(WpcontentFile).status_code == 404):
        print('Uploads file does not exists')
    elif (requests.get(WpcontentFile).status_code == 200):
        print('Uploads file exists')
    if (requests.get(WpcontentFile).status_code == 403):
        print('Uploads file exist but user do not have authorization')
