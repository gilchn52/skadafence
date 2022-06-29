#!/usr/bin/env python
import argparse
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' %message)
        self.print_help()
        sys.exit(2)
parser = MyParser()
parser = argparse.ArgumentParser(description='my process.')
parser.add_argument("-wp", "--webpage", action="store_true", help="webpage test")
parser.add_argument('-dt', "--datevalid", action="store_true", help="date validaity test")
parser.add_argument("-dc", "--datecorret", action="store_true", help="date corret checkup")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
    

args = vars(parser.parse_args())


if (str(args.value="webpage"):
       
    



