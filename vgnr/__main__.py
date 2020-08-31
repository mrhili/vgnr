
import argparse
from funcmodule import fire


#staring script
parser = argparse.ArgumentParser(
description='''
Its a simple script to decode and encode in vegener cypher way.
check this link : https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
'''
)


#-d or -e for the mode
#-q or -v for the behaviour (quiet, verbose)

parser.add_argument('key', metavar='', type=str, help='The necessary key to decrypt or encrypt')
input = parser.add_mutually_exclusive_group(required=True)
input.add_argument('-d','--decrypt', metavar='', type=str, help='The string to decrypt')
input.add_argument('-e','--encrypt', metavar='', type=str, help='The string to encrypt')

# quiet or verbose

behaviour = parser.add_mutually_exclusive_group()
behaviour.add_argument('-q','--quiet', action='store_true', help='Quiet and simple output')
behaviour.add_argument('-v','--verbose', action='store_true', help='Verbose output')

#parsing args
args = parser.parse_args()

#firing script
def main():
    fire( args )

#required in python
if __name__ == '__main__':
    main(  )
