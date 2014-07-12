#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lev
#
# Created:     15/01/2014
# Copyright:   (c) lev 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import sys
from sys import argv, exit
import ntpath
import os

dir_sep = "\\"

def findfile(dirname, filename):
# list dir
    fs = os.listdir(dirname)

#    print "fs: ", str(fs), "\n"
#    print "\nFiles: "

    for fn in fs:
#       print "\t" , fn
        if (fn == filename):
             print "Found: %s%s%s\n"% (dirname, dir_sep, filename)

#        print "File ", filename, " not found"


def my_walk(dirname):
    print "\n\n ***** my_walk ***** \n\n"
    for root, dirs, files in os.walk(dirname, topdown=False):
        for name in files:
            print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


def remove_underscore(dirname):
    print "remove_underscore"
    fs = os.listdir(dirname)
    for f in fs:
        print "file: ", f
        if (f[0] == '_'):
            fold = os.path.join(dirname,f);
            fnew = os.path.join(dirname, f[1].upper() + f[2:])
            os.rename(fold, fnew)
        else:
            if (f[0].islower()):
                fnew = os.path.join(dirname, f[0].upper() + f[1:])
                os.rename(fold, fnew)

def print_catalog(dirname):
    fs = os.listdir(dirname)
    for f in fs:
        full_path = os.path.join(dirname, f)
        if os.path.isdir(full_path):
            print "\n\n\t\tDir: ", f, "\n"
            ff = os.listdir(full_path)
            for b in ff:
                print b



def main():
#    print "Hello"

    argc = len(argv)
    if (argc < 3):
        print "Usage: ", ntpath.basename(argv[0]), " <dir> <file_name>"
        exit(255)

    print 'Number of arguments:', argc, 'arguments.'
    print 'Argument List:', str(argv)

    dirname, filename = argv[1], argv[2]
    print "dir: ", dirname, " filename: ", filename

    findfile(dirname, filename)

    print "\n\n\n *****************"

#   my_walk(dirname)s

#    remove_underscore(dirname)

    print_catalog(dirname)

if __name__ == '__main__':
    main()

