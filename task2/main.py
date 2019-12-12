from flickr.flickr import Flickr

from dotenv import load_dotenv

import sys
from os import environ

def main():
    if (len(sys.argv) == 3):
        keyword = sys.argv[1]
        try:
            noImg = int(sys.argv[2])
            if (noImg < 1):
                raise ValueError('Number must be greater than zero')
        except ValueError:
            raise Exception('Second argument must contain number greater than zero')
    else:
        raise Exception('Invalid number of parameters')

    load_dotenv()
    client = Flickr()

if __name__ == '__main__':
    main()