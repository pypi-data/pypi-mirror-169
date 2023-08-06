import os, sys, argparse, json
try:
    input = raw_input
except:
    pass
print('usage:')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
executable = sys.executable
if ' ' in executable: executable='"%s"'%executable
#for method in ('find', 'valid'):
#    print(' '*4+' '.join([sys.executable, '-m', 'moofei.'+method, '-h']))

def set_config(cmd=None):
    parser = argparse.ArgumentParser(description="""Set Moofei-Config""")
    if cmd:
       parser.add_argument('cmd',  help="Command line mode; generally can be ignored") 
    parser.add_argument('-set-user','--set-user', help='set auth user')
    parser.add_argument('-set-pwd','--set-pwd', help='set auth password')
    parser.add_argument('--pprint', action='store_true', help='print  moofei-config')
    parser.add_argument('--clear-all', action='store_true', help='delete moofei-config')
    
    args = parser.parse_args()
    if '-h' in sys.argv :
        print(args)
    else:
        cfgpath = os.path.join(BASE_DIR, '.conf')
        if os.path.isfile(cfgpath):
            config = json.load(open(cfgpath))
        else:
            config = {}
        if args.pprint:
            print(json.dumps(config, sort_keys=True, indent=4, separators=(', ', ': ')))
            exit(0)
        elif args.clear_all:
            os.remove(cfgpath)
            print('Remove succeed:', cfgpath)
            exit(0)
        if args.set_user and args.set_pwd:
            config.setdefault('users', {})[args.set_user] = args.set_pwd
            print('Save User:', args.set_user)
        with open(cfgpath, 'w') as fp:
            fp.write(json.dumps(config))
            
if len(sys.argv)==1:
    print(' 0. Reset password of Admin in Moofei-Config')
    print(' 1. Full-Text-Search Webbrowser')
    print(' 2. SiteMap-Download Webbrowser')
    print(' *. More')
    ex = [
            '31. Dos2unix Format Filename', 
            '32. Show Image Info',
            '33. Watermark Word on Images',             
         ]
    #for e in ex: print(e)
    cmd = ""
    N = str(input('Please Input Number: ')).strip()
    if N=='*':
        for e in ex: print(e)
        N = str(input('Please Input Number: ')).strip()
    if N=='0':
        pwd = str(input('Please Input Password: ') or "").strip()
        if pwd:
            cmd = executable+' -m moofei config -set-user admin -set-pwd "%s"'%pwd                            
    elif N=='1':
        cmd = executable+' -m moofei.find 0.0.0.0:5000 --webbrowser'
    elif N=='2':
        os.environ.setdefault('MOOFEI_SITE_INDEX', 'sitemap.html')
        cmd = executable+' -m moofei.find 0.0.0.0:5000 --webbrowser'    
    elif N=='31':
        cmd = executable+' -m moofei.ext.dos2unix'
    elif N=='32':
        image = str(input('Please Input ImageFile: ') or "").strip()
        if image:
            cmd = executable+' -m moofei._image -exif "%s"'%image
    elif N=='33':
        word = str(input('Please Input watermark word: ') or "").strip()
        path = str(input('Please Input ImageFile Path: ') or "./").strip()
        print('rgba：(default #FFFFFF26)')
        rgba = str(input('Please Input Image rgba: ') or "").strip()
        if word:
            from _image import test_watermark_word
            test_watermark_word(word, path, rgba=rgba,rebackIm=True)    
    if cmd: os.system(cmd)
            
elif len(sys.argv)==2:
    if sys.argv[1] in (":help", '-h', '--help', 'help'):
        print('python -m :(find|config|cat|V)')
    elif sys.argv[1] in (":V",':v','-V'):
        from .__version__ import __version__
        print(__version__)
           
elif len(sys.argv)>2:
    if sys.argv[1] in (":find",'find'):
        from ._find import main
    elif sys.argv[1] in (":config", ':conf', ':cfg', 'config'):
        main = set_config
    elif sys.argv[1] in (":cat", 'cat'):
        from ._cat import main
    
    main(sys.argv[1])
    
exit(0)
