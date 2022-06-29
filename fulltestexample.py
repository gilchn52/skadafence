import argparse
 
parser = argparse.ArgumentParser(description="a test program", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-dt", "--datevalid", action="store_true", help="date validaity test")
parser.add_argument("-wp", "--webpage", action="store_true", help="webpage test")
parser.add_argument("-dc", "--datecorret", help="date corret checkup")




args = parser.parse_args()
config = vars(args)
print(config)
