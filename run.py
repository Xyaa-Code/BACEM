import os, sys, time, random
from requests.exceptions import ConnectionError

from rich import print as prints
from rich.panel import Panel
from rich.console import Console
console = Console()

class Crack:
   
    def __init__(self):
        self.menu()
    
    def clear(self):
        try:os.system("clear")
        except:os.system("cls")
    
    def menu(self):
        self.clear()
        prints(Panel(" script bacem ( [green1]MBF[white] ) sedang dalam proses perbaikan oleh admin keep waiting"))
        xcTeam = console.input(" [white]([green1]?[white]) apakah ingin menghubungi admin? (y/t) : ")
        if xcTeam in ["y","Y"]:
          self.contact()
        else:
            prints(" [white]([green1]+[white]) selamat tinggal...")
            time.sleep(3);exit()
    
    def contact(self):
        prints(" [white]([pink1]![white]) anda akan di arahkan ke WhatsApp admin")
        try:os.system("xdg-open https://wa.me/+16143244921?text=assalamualaikum+bang+update+kapan+selesai+ya+?")
        except KeyError:
           prints(" [white]([red1]![white]) opss.. terjadi kesalahan")
           time.sleep(3);exit()
        
if __name__ == '__main__':
  try:os.system("git pull")
  except:pass
  try:Crack()
  except requests.exceptions.ConnectionError:
     prints(" [white]([red1]![white]) koneksi internet anda bermasalah...")
     time.sleep(3);exit()
