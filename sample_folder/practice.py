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
    parser.set('Manager', 'Name', 'subhash sharma')
    parser.set('Manager', 'email', 'mr.subhash505@gmail.com')
    parser.set('Manager', 'password', 'secret')
    fp=open('test.ini','w')
    parser.write(fp)
    fp.close()
    # p= parser.get()
    # print(p)

    r = 0
    s = [59, 47, 7, 17, 45]
    l  = lambda s: sum(s)
    print(l(s))


if __name__ == "__main__" :
    main()