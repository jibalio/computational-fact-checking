import Truth
from Truth import Path

from scrapers.request import get_path
from scrapers.logger import log
import argparse


if __name__ == '__main__':

    # Read the parameters
    log("PathEvaluator.py started.")
    parser = argparse.ArgumentParser(description='All in one package (pathfinding + truthvalue)')
    parser.add_argument('x', help='Source Node')
    parser.add_argument('y', help='End Node')
    parser.add_argument('token', help="Access token to be used when querying wikipaths.")
    
    args = vars(parser.parse_args())


    Truth.TOKEN = args['token']
    b = Path(args['x'], args['y'])
    print(b.get_truthvalue())