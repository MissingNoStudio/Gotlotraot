#!/usr/bin/env python
#coding=utf-8
#
# ./download-resources.py
#
# Downloads Resources from svn:
# svn://missingnostudio.com/Gotlotraot
#

import subprocess
import getpass

import os.path

import sys
from sys import stdout

def _check_python_version():
    major_ver = sys.version_info[0]
    if major_ver > 2:
        print ("The python version is %d.%d. But python 2.x is required. (Version 2.7 is well tested)\n"
               "Download it here: https://www.python.org/" % (major_ver, sys.version_info[1]))
        return False

    return True


def main():
    workpath = os.path.dirname(os.path.realpath(__file__))

    if not _check_python_version():
        exit()

    print("=======================================================")
    print("==> Prepare to download Resources!")

    resources_path = os.path.join(workpath, 'Resources')

    print("==> Check if Resources folder exist...")
    if not os.path.isdir(resources_path):
        print("==> Create Resources folder...")
        os.mkdir(resources_path)

    svn_path = os.path.join(resources_path, '.svn')

    print("==> Check if Resources is a valid Svn repository...")
    if os.path.isdir(svn_path):
        ret = raw_input("==> Resources folder is already setup, do you want to update him? [yes/no]: ")
        ret = ret.strip()

        while (True):
            if ret == 'yes' or ret == 'y':
                p = subprocess.Popen("svn update %s" % (resources_path), stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                print "==>", output
                raw_input("Press Enter to continue")
                exit()
            elif ret == 'no' or ret == 'n':
                print("==> Do nothing...\n")
                raw_input("Press Enter to continue")
                exit()
            else:
                ret = raw_input("==> [yes/no]: ")
                ret = ret.strip()

    print("==> Checkout Svn repository : svn://missingnostudio.com/Gotlotraot")
    username = raw_input("==> Username: ")
    password = getpass.getpass("==> Password: ")

    p = subprocess.Popen("svn checkout svn://missingnostudio.com/Gotlotraot %s --username %s --password %s" % (resources_path, username, password), stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    print "==>", output

    raw_input("Press Enter to continue")
    exit()

# -------------- main --------------
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
