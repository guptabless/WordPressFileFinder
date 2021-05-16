import requests
import bcolors
import sys, argparse
import os

def banner():
    print("""
            ░██╗░░░░░░░██╗██████╗░░░░░░░███████╗██╗██╗░░░░░███████╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
            ░██║░░██╗░░██║██╔══██╗░░░░░░██╔════╝██║██║░░░░░██╔════╝░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
            ░╚██╗████╗██╔╝██████╔╝█████╗█████╗░░██║██║░░░░░█████╗░░█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
            ░░████╔═████║░██╔═══╝░╚════╝██╔══╝░░██║██║░░░░░██╔══╝░░╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
            ░░╚██╔╝░╚██╔╝░██║░░░░░░░░░░░██║░░░░░██║███████╗███████╗░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
            ░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝                                                         
                                                                                                        Code By: NG
              """
          )
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 'u'):
        try:
            input_url = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-u", required=True)

            print(bcolors.BITALIC + "Testing for Word Press Files")
            if (os.path.exists(input_url) == True):
                print('\n''*********************license*****************')
                file = open(input_url, "r")
                lines = file.readlines()

                for te in lines:
                    striped_Input_url = te.strip()
                    print(bcolors.BOLD, '########################Website Name:#########################' , bcolors.OK,striped_Input_url)
                    ResponseCode = requests.get(striped_Input_url).status_code
                    LicenseFile = striped_Input_url + 'license.txt'
                    print('LICENSE FILE',LicenseFile , requests.get(LicenseFile).status_code)
                    try:
                        if(('license'in LicenseFile) and (requests.get(LicenseFile).status_code == 200)):
                            print('License file does not exists')
                        else:
                            print(bcolors + 'License file not exists')
                    except:
                        print('License file not exists')

                    print('\n''*********************xmlrpc*****************')
                    XmlrpcFile = striped_Input_url + 'xmlrpc.php'
                    print('XMLRPC FILE', XmlrpcFile, requests.get(XmlrpcFile).status_code)
                    try:
                        if ('xmlrpc' in XmlrpcFile):
                            if (requests.get(XmlrpcFile).status_code == 200):
                                print('XMLRPC file exists and you can access')
                            elif (requests.get(XmlrpcFile).status_code == 405):
                                print('XMLRPC file exists but only accepts POST requests')
                            elif (requests.get(XmlrpcFile).status_code == 404):
                                print('XMLRPC file not exists')
                            elif (requests.get(XmlrpcFile).status_code == 403):
                                print('XMLRPC file exists but you do not have authorization')
                    except:
                        print('xmlrpc.php file not exists')

                    print('\n''*********************Wp-activate*****************')
                    WpActivateFile = striped_Input_url + 'wp-activate.php'
                    print('WP-ACTIVATE', WpActivateFile, requests.get(WpActivateFile).status_code)
                    try:
                        if ('wp-activate' in WpActivateFile):
                            if (requests.get(WpActivateFile).status_code == 404):
                                print('Wp-activate file does not exists')
                            elif (requests.get(WpActivateFile).status_code == 200):
                                print('Wp-activate file exists but redirect to the login page')
                            elif (requests.get(WpActivateFile).status_code == 500):
                                print('Wp-activate file exists')
                    except:
                        print('Wp - activate file not exists')

                    print('\n''*********************wp-config*****************')
                    WpConfigFile = striped_Input_url + 'wp-config.php'
                    print('WP-CONFIG', WpConfigFile, requests.get(WpConfigFile).status_code)
                    try:
                        if ('wp-config' in WpConfigFile):
                            if (requests.get(WpConfigFile).status_code == 404):
                                print('WP-CONFIG file does not exists')
                            elif (requests.get(WpConfigFile).status_code == 200):
                                print('WP-CONFIG file exists')
                    except:
                        print('wp-config file not exists')

                    print('\n''*********************wp-content*****************')
                    WpcontentFile = striped_Input_url + 'wp-content/uploads'
                    print('wpcontent', WpcontentFile, requests.get(WpcontentFile).status_code)
                    try:
                        if ('uploads' in WpcontentFile):
                            if (requests.get(WpcontentFile).status_code == 404):
                                print('Uploads file does not exists')
                            elif (requests.get(WpcontentFile).status_code == 200):
                                print('Uploads file exists')
                            if (requests.get(WpcontentFile).status_code == 403):
                                print('Uploads file exist but user do not have authorization')
                    except:
                        print('wp - content')

            elif (os.path.exists(input_url) != True):
                ResponseCode = requests.get(input_url).status_code
                print('\n''*********************license*****************')
                LicenseFile = input_url + 'license.txt'
                print('LICENSE FILE', LicenseFile, requests.get(LicenseFile).status_code)
                try:
                    if (('license' in LicenseFile) and (requests.get(LicenseFile).status_code == 200)):
                        print('License file does not exists')
                    else:
                        print(bcolors + 'License file not exists')
                except:
                    print('License file not exists')

                print('\n''*********************xmlrpc*****************')
                XmlrpcFile = input_url + 'xmlrpc.php'
                print('XMLRPC FILE', XmlrpcFile, requests.get(XmlrpcFile).status_code)
                try:
                    if ('xmlrpc' in XmlrpcFile):
                        if (requests.get(XmlrpcFile).status_code == 200):
                            print('XMLRPC file exists and you can access')
                        elif (requests.get(XmlrpcFile).status_code == 405):
                            print('XMLRPC file exists but only accepts POST requests')
                        elif (requests.get(XmlrpcFile).status_code == 404):
                            print('XMLRPC file not exists')
                        elif (requests.get(XmlrpcFile).status_code == 403):
                            print('XMLRPC file exists but you do not have authorization')
                except:
                    print('xmlrpc file does not exists')

                print('\n''*********************Wp-activate*****************')
                WpActivateFile = input_url + 'wp-activate.php'
                print('WP-ACTIVATE', WpActivateFile, requests.get(WpActivateFile).status_code)
                try:
                    if ('wp-activate' in WpActivateFile):
                        if (requests.get(WpActivateFile).status_code == 404):
                            print('Wp-activate file does not exists')
                        elif (requests.get(WpActivateFile).status_code == 200):
                            print('Wp-activate file exists but redirect to the login page')
                        elif (requests.get(WpActivateFile).status_code == 500):
                            print('Wp-activate file exists')
                except:
                    print('Wp-activate file does n ot exists')

                print('\n''*********************wp-config*****************')
                WpConfigFile = input_url + 'wp-config.php'
                print('WP-CONFIG', WpConfigFile, requests.get(WpConfigFile).status_code)
                try:
                    if ('wp-config' in WpConfigFile):
                        if (requests.get(WpConfigFile).status_code == 404):
                            print('WP-CONFIG file does not exists')
                        elif (requests.get(WpConfigFile).status_code == 200):
                            print('WP-CONFIG file exists')
                except:
                    print('wp - config file does  not exists')

                print('\n''*********************wp-content*****************')
                WpcontentFile = input_url + 'wp-content/uploads'
                print('wpcontent', WpcontentFile, requests.get(WpcontentFile).status_code)
                try:
                    if ('uploads' in WpcontentFile):
                        if (requests.get(WpcontentFile).status_code == 404):
                            print('Uploads file does not exists')
                        elif (requests.get(WpcontentFile).status_code == 200):
                            print('Uploads file exists')
                        if (requests.get(WpcontentFile).status_code == 403):
                            print('Uploads file exist but user do not have authorization')
                except:
                    print('WpcontentFile file does not exists')
        except:
            print(bcolors.OKMSG + 'Please enter python wp-filefinder.py -u <valid URL with https:// or http://> ')
    elif (sys.argv[1] == '-h'):
        print(bcolors.BOLD + 'usage: wp-filefinder.py [-h] -u URL' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-u URL,   --url URL Which wordpress website you want to check')
    elif (sys.argv[1] != '-u'):
        print(bcolors.OKMSG + 'Please enter -u < valid URL with http:// or https:// >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u or -h, with a valid URL')
