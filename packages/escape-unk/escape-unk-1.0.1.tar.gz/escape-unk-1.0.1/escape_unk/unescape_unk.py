from argparse import ArgumentParser
import logging
import regex
import sys

try:
    from .utils import setup_logging
except ImportError:
    from utils import setup_logging


escaped_re = regex.compile(r"\[\[[a-z\d]+\]\]")


def unescape(match):
    ''' Convert hex values to unicode string '''
    hexvalue = match.captures()[0].strip('[]')
    logging.debug(f"Unescaping: '{hexvalue}'")
    return bytes.fromhex(hexvalue).decode('utf-8')


def main():
    parser = ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Debug mode')
    args = parser.parse_args()
    setup_logging(args)

    for line in sys.stdin:
        # Find splits and matches inside the sentence
        escaped = list(escaped_re.finditer(line.strip()))
        splits = list(escaped_re.splititer(line.strip()))
        output = ''

        # Join splits with unescaped matches
        for i, split in enumerate(splits):
            if i != len(splits)-1:
                output += split + unescape(escaped[i])
            else:
                output += split

        print(output)


if __name__ == "__main__":
    main()
