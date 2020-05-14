from tinyc_scanner import scanner
from tinyc_parser import parser

def main():

    scan = scanner()

    if scan:
        parser()


if __name__ == "__main__":
    main()
