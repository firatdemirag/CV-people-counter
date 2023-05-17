import argparse


def main():
    parser = argparse.ArgumentParser(description='CV People Counter', add_help=False)
    parser.add_argument('--help', '-h', action='help', help='show this help message and exit')
    args = parser.parse_args()


if __name__ == '__main__':
    main()