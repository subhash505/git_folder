import configparser
def main():
    parser = configparser.ConfigParser()
    parser.read('sampleconfig.ini')
    for sect in parser.sections():
        print('Section:', sect)
        for k,v in parser.items(sect):
            print(' {} = {}'.format(k,v))
        print()

if __name__ == "__main__" :
    main()