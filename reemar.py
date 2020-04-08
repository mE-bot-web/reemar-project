# Author ? gada bosque
# Cuma percobaan wkwk nanti di banyakin dah biar agak kerenan diki awokawok
import os, time
#------------------
m = '\x1b[1;31m'
p = '\x1b[1;37m'
#------------------
banner = f'''
{m}╦═╗{p}┌─┐┌─┐┌┬┐┌─┐┬─┐
{m}╠╦╝{p}├┤ ├┤ │││├─┤├┬┘
{m}╩╚═{p}└─┘└─┘┴ ┴┴ ┴┴└─
  {m}╔═╗{p}┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐
  {m}╠═╝{p}├┬┘│ │ │├┤ │   │
  {m}╩  {p}┴└─└─┘└┘└─┘└─┘ ┴ '''
def tts():
        gas = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
        if gas.lower() in ['gombalin saya reemar']:
                os.system('termux-tts-speak -r 1.2 Kamulah bulan bagi matahariku... Cahaya kemilau dirimu menerangi malamku yang sunyi')
                wow = str(input(f'{m}[{p}?{m}]{p}Apakah anda ingin mendengarkan lagi y/t : '))
                if wow.lower() in ['y']:
                        os.system('termux-tts-speak -r 1.2 Tahu nggak kenapa menara pisa miring?')
                        time.sleep(1)
                        os.system('termux-tts-speak -r 1.2 Soalnya ketarik sama senyuman kamu')
                else:
                        exit()
        elif gas.lower() in ['putarkan saya musik']:
                os.system('termux-tts-speak -r 1.2 Baiklah')
                wiw = str(input(f'{m}[{p}?{m}]{p}Masukkan nama folder ex : /Music/ _{m}>{p} '))
                os.system('mpv /sdcard'+wiw)
        else:
                exit()
def main():
        piw = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
        if piw.lower() in ['saya butuh hiburan']:
                print(f'\n\t{m}------------------------{p}')
                print('\t - putarkan saya musik')
                print('\t - gombalin saya reemar')
                print(f'\t{m}-------------------------{p}')
                tts()
        elif piw.lower() in ['siapa yang menciptakanmu reemar']:
                os.system('termux-tts-speak -r 1.2 Baiklah')
                os.system('termux-tts-speak -r 1.2 Orang yang menciptakan saya bernama. Muhamad Royyani. Dia Hanyalah Seorang anak yang masih berumur 16 tahun')
        elif piw.lower() in ['install bahan']:
                os.system('pkg install termux-api')
        else:
                print('Pilihan tidak ada !!')
def duar():
        os.system('clear')
        print(banner)
        while(True):
                pil = str(input(f'{m}[{p}?{m}]{p}Reemar _{m}>{p} '))
                if pil.lower() in ['reemar -help','-help']:
                        print('\n\t[ List command ]')
                        print('\tsaya butuh hiburan')
                        print('\tsiapa yang menciptakanmu reemar')
                        print('\tinstall bahan')
                        print('\t----Cooming soon----\n')
                        main()
                elif pil in ['',' ']:
                        print(f'{m}type : {p}-help {m}for show all command')
                else:
                        print(f'{p}[{m}!{p}] Salah {m}!!')



if __name__ == '__main__':
        duar()
