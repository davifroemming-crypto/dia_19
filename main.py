import sys


def main():
    if len(sys.argv) > 1:
        print('ola,', sys.argv[1] + '!')
    else:
        print('ola!')

if __name__ == '__main__':
    main()
