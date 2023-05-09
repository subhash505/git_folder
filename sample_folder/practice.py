import configparser
def main():
    parser = configparser.ConfigParser()
    parser.read('test.ini')
    for sect in parser.sections():
        print('Section:', sect)
        for k,v in parser.items(sect):
            print(' {} = {}'.format(k,v))
        print()
    # import configparser
    parser = configparser.ConfigParser()
    parser.add_section('Manager')
    parser.set('Manager', 'Name', 'Ashok Kulkarni')
    parser.set('Manager', 'email', 'ashok@gmail.com')
    parser.set('Manager', 'password', 'secret')
    fp=open('test.ini','w')
    parser.write(fp)
    fp.close()

if __name__ == "__main__" :
    main()