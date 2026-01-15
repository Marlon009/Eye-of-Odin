#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Eye of Odin - Advanced OSINT Tool

import os
import time
import requests
import phonenumbers
import whois
import json
import re
import socket
import socks
import PyPDF2
from PIL import Image
from io import BytesIO
from docx import Document
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import quote, urlparse
from phonenumbers import carrier, geocoder, timezone
from odin.languages import lang
import argparse
#from animation import animar_cajado  # Importação da animação
idioma = "es"
usar_tor = False
# === Configuração Tor ===
proxy_tor = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
usar_tor = False

# === Cores compatíveis ===
class Cores:
    VERMELHO = '\033[1;31m'
    VERDE = '\033[1;32m'
    AMARELO = '\033[1;33m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CIANO = '\033[1;36m'
    BRANCO = '\033[1;37m'
    RESET = '\033[0m'


VERSION = "1.0.0"

def parse_args():
    parser = argparse.ArgumentParser(
        prog="odin",
        description="Eye of Odin - Advanced OSINT Tool"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"Odin {VERSION}"
    )
    return parser.parse_args()

# === Limpar tela ===
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# === Banner Eye of Odin ===
def mostrar_banner():
    print(f"""{Cores.VERDE}
                                                                             .......             
                                                                          ..............         
                                                                       .......*.....%%....       
                                                                      ...+...**::::::@.....      
                                                                     ....#.::%#::::::@......     
                                                                     ....%::##:.  :#:@*:....     
                                                                     .....***::*  *#:#@:....     
                                                                     .....:#*::*::+*::%*....     
                                           @@@@@@@                   .....:@@:#%*:%%:=@.....     
                                        @@@@@@@@@@@@@                 .....@@..####:#@@....      
                                       @@@@@@@@@@@@@@@                 ....@@..##@..@@@...       
                                     +@@@@@@@@@@@@@@@@%                 ....@@@##..@@@..         
                         %@@@        @@@@@@@@@@@@@@@@@@#                   ...%*#.*#%#           
                       -@@@@@@@@@-  @@@@@@@@@@@@@@@@@@@%                      @#*%##.            
                     @@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@                     #@@@@              
                    :--:-%@@@       @@@@=@@@@=@@@@@@@@%##                     %*%@@              
                  @++-%@:-@@@      @@@%@@###-%@@@@@##@@%#%                    @@*@@              
                 :--::@@@*:@@@     @@@--%=-=%@*@@+++#@@@@#                   @*#@#               
                @@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@                   @@@@               
               --:@++@@@=@@@@     @@@-#@@=--@@*@@@@@@@-@#**                   @*%@               
              --@:@@:@@@@@@@     @@@-@@*@@%@@-@@@@@@@@%@@***                  #@@%@              
             ==@:+#=@@+@@@@     @@@*@@*=-@@=@@@=+@=@%#%-@#**#                  #@#%              
            -:@@%@@@@+@@@@     @@@@@@@@#=+*@@-%@@@@@@%-+@@***+                 @#@@              
           @#@@#:@#=+=@@@      @@@@@@==-@*@@-@@@@@@@%@+@@@@#%%                 @@@@              
         =@@@@@@@@@@@@@@      = @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@              
        @ @#@@@@@@@@    @@ @@@@@@@@@@@@-@=--+@@@@@@@@%-@@**#@#%%%              @@@@              
         @@@@@@@    @+:@#@@@@@@@@%@@@-@@@@=-=+@=@@@@%@@%%@@%*@**#@%            @%@@              
        @@-@@@@:   @***@@%@@@@@@@@@**@@@*#@%%@@@@@@@@@@@%%*#@**@*##%#*      @@=--%@@@@@          
      @@ @@@@@@ #%##*%#**%@@@@@@@@@@-----@@@-+=@@@@@@@@@%#**@**@#*#%@%##+   :-@@=%@@@@@          
        @@@@@  =@%*#**@@@@@@@@@@@@@@:+@#%=:@@@@@@@@@@@@@@%@##%##%#@#%@@@@   @@-+%@@@@@%@         
       @@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#    @@@@@@@@@          
             @@@@@@@@@#***@@@@@@@%#@@-*%=@*@@*%%%@@@@@@@@@@@#***####*####@*: @=-=@@@@@@          
            *****@@@@@@@@@@@@@@@=@@@@@@@@@@@**#@@@@@@@@@%##@@@@###%%#**#%##*  @:#@@@@@@          
           %@@@@@#---@@=@@-@@@@@@-@@@@@@@-@@@@@@@@@@@@@@%@#*%@**#%@@@@@@@@*#@ @@@@@@@@           
           @@@@@@@@@@@@#@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**###*%##%%@ @@@@@@@@          
           @@=@@@-@-==@=@@+@@@@@@@-@@@@@@@@=@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@%%@@=@@#@@@:%%         
           @@@##%+--*---@@%-@@@@@@+-@@@@@@@@-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@%@@@@@@#-@          
          @@@@@@@@@@@@@@@@@%@@@@@@@-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-@=---*--=+@@@@%@@          
{Cores.VERMELHO}  
            ███████╗██╗   ██╗███████╗      ██████╗ ███████╗    ██████╗ ██████╗ ██╗███╗   ██╗
            ██╔════╝╚██╗ ██╔╝██╔════╝     ██╔═══██╗██╔════╝   ██╔═══██╗██╔══██╗██║████╗  ██║
            █████╗   ╚████╔╝ █████╗       ██║   ██║█████╗     ██║   ██║██║  ██║██║██╔██╗ ██║
            ██╔══╝    ╚██╔╝  ██╔══╝       ██║   ██║██╔══╝     ██║   ██║██║  ██║██║██║╚██╗██║
            ███████╗   ██║   ███████╗      ██████╔╝██╝        ╚██████╔╝██████╔╝██║██║ ╚████║
            ╚══════╝   ╚═╝   ╚══════╝      ╚═════╝ ╚═╝         ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                                                                OSINT TOOL
        {Cores.RESET}
{Cores.BRANCO}
                                         github:Marlon009
        {Cores.RESET}""")
# === Conversor Decimal para DMS ===
def decimal_para_dms(lat, lon):
    def converter(valor, pos, neg):
        graus = int(abs(valor))
        minutos_dec = (abs(valor) - graus) * 60
        minutos = int(minutos_dec)
        segundos = (minutos_dec - minutos) * 60
        direcao = pos if valor >= 0 else neg
        return f"{graus}°{minutos}'{round(segundos, 1)}\"{direcao}"

    lat_dms = converter(lat, 'N', 'S')
    lon_dms = converter(lon, 'E', 'W')
    return lat_dms, lon_dms

# === Rastrear IP ===
def rastrear_ip():
    ip = input(f"{Cores.BRANCO}{lang[idioma]['input_ip']}{Cores.VERDE}")
    try:
        sessao = requests.Session()
        if usar_tor:
            sessao.proxies = proxy_tor
            
        res = sessao.get(f"https://ipwho.is/{ip}", timeout=10).json()

        lat = res.get('latitude')
        lon = res.get('longitude')

        if lat is None or lon is None:
            raise ValueError(lang[idioma]['coordinates_error'])

        lat_dms, lon_dms = decimal_para_dms(lat, lon)

        # Codificar para URL
        lat_dms_encoded = quote(lat_dms)
        lon_dms_encoded = quote(lon_dms)

        link_dms = f"https://www.google.com/maps/place/{lat_dms_encoded}+{lon_dms_encoded}/"
        link_decimal = f"https://www.google.com/maps/@{lat},{lon},8z"

        print(f"\n{Cores.BRANCO}{lang[idioma]['info_ip']}{Cores.VERDE}{ip}:")
        print(f"{Cores.BRANCO}{lang[idioma]['country']}{Cores.VERDE}{res.get('country')}")
        print(f"{Cores.BRANCO}{lang[idioma]['city']}{Cores.VERDE}{res.get('city')}")
        print(f"{Cores.BRANCO}{lang[idioma]['isp']}{Cores.VERDE}{res.get('connection', {}).get('isp', 'N/A')}")
        print(f"{Cores.BRANCO}{lang[idioma]['map_decimal']}{Cores.VERDE}{link_decimal}")
        print(f"{Cores.BRANCO}{lang[idioma]['map_dms']}{Cores.VERDE}{link_dms}")

    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}{Cores.RESET}")

# === Rastrear Telefone ===
def rastrear_telefone():
    numero = input(f"{Cores.BRANCO}{lang[idioma]['input_phone']}{Cores.VERDE}")
    try:
        num = phonenumbers.parse(numero)
        print(f"\n{Cores.BRANCO}{lang[idioma]['info_phone']}")
        print(f"{Cores.BRANCO}{lang[idioma]['carrier']}{Cores.VERDE}{carrier.name_for_number(num, idioma)}")
        print(f"{Cores.BRANCO}{lang[idioma]['region']}{Cores.VERDE}{geocoder.description_for_number(num, idioma)}")
        print(f"{Cores.BRANCO}{lang[idioma]['timezone']}{Cores.VERDE}{', '.join(timezone.time_zones_for_number(num))}")
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}")

# === Busca de Usuário ===
def buscar_usuario():
    username = input(f"{Cores.BRANCO}{lang[idioma]['input_username']}{Cores.VERDE}")
    
    redes = {
    "GitHub": {
        "url": f"https://github.com/{username}",
        "check": lambda r: r.status_code == 200 and f'"{username}"' in r.text
    },
    "Instagram": {
        "url": f"https://instagram.com/{username}",
        "check": lambda r: r.status_code == 200 and "Página não encontrada" not in r.text
    },
    "Twitter (X)": {
        "url": f"https://twitter.com/{username}",
        "check": lambda r: r.status_code == 200 and "Esta conta não existe" not in r.text
    },
    "Facebook": {
        "url": f"https://facebook.com/{username}"
    },
    "TikTok": {"url": f"https://www.tiktok.com/@{username}"},
    "Reddit": {"url": f"https://www.reddit.com/user/{username}"},
    "YouTube": {"url": f"https://www.youtube.com/@{username}"},
    "Twitch": {"url": f"https://www.twitch.tv/{username}"},
    "Pinterest": {"url": f"https://www.pinterest.com/{username}"},
    "Snapchat": {"url": f"https://www.snapchat.com/add/{username}"},
    "LinkedIn": {"url": f"https://www.linkedin.com/in/{username}"},
    "Medium": {"url": f"https://medium.com/@{username}"},
    "Telegram": {"url": f"https://t.me/{username}"},
    "SoundCloud": {"url": f"https://soundcloud.com/{username}"},
    "DeviantArt": {"url": f"https://www.deviantart.com/{username}"},
    "GitLab": {"url": f"https://gitlab.com/{username}"},
    "Vimeo": {"url": f"https://vimeo.com/{username}"},
    "Flickr": {"url": f"https://www.flickr.com/people/{username}"},
    "Behance": {"url": f"https://www.behance.net/{username}"},
    "Dribbble": {"url": f"https://dribbble.com/{username}"},
    "Blogger": {"url": f"https://{username}.blogspot.com"},
    "Replit": {"url": f"https://replit.com/@{username}"},
    "Kaggle": {"url": f"https://www.kaggle.com/{username}"},
    "About.me": {"url": f"https://about.me/{username}"},
    "Steam": {"url": f"https://steamcommunity.com/id/{username}"},
    "Roblox": {"url": f"https://www.roblox.com/user.aspx?username={username}"},
    "Last.fm": {"url": f"https://www.last.fm/user/{username}"},
    "500px": {"url": f"https://500px.com/{username}"},
    "ProductHunt": {"url": f"https://www.producthunt.com/@{username}"},
    "Dev.to": {"url": f"https://dev.to/{username}"},
    "HackTheBox": {"url": f"https://app.hackthebox.com/profile/{username}"},
    "CodePen": {"url": f"https://codepen.io/{username}"},
    "Keybase": {"url": f"https://keybase.io/{username}"},
    "BuyMeACoffee": {"url": f"https://www.buymeacoffee.com/{username}"},
    "Patreon": {"url": f"https://www.patreon.com/{username}"},
    "Tripadvisor": {"url": f"https://www.tripadvisor.com/Profile/{username}"},
    "Disqus": {"url": f"https://disqus.com/by/{username}/"},
    "Imgur": {"url": f"https://imgur.com/user/{username}"},
    "Wattpad": {"url": f"https://www.wattpad.com/user/{username}"},
    "Venmo": {"url": f"https://venmo.com/{username}"},
    "Cash App": {"url": f"https://cash.app/${username}"},
    "Strava": {"url": f"https://www.strava.com/athletes/{username}"},
    "Goodreads": {"url": f"https://www.goodreads.com/{username}"},
    "Letterboxd": {"url": f"https://letterboxd.com/{username}"},
    "Anilist": {"url": f"https://anilist.co/user/{username}"},
    "MyAnimeList": {"url": f"https://myanimelist.net/profile/{username}"},
    "Bandcamp": {"url": f"https://{username}.bandcamp.com"},
    "IFTTT": {"url": f"https://ifttt.com/p/{username}"},
    "OKCupid": {"url": f"https://www.okcupid.com/profile/{username}"},
    "Taringa": {"url": f"https://www.taringa.net/{username}"},
    "Ello": {"url": f"https://ello.co/{username}"},
    "OpenSea": {"url": f"https://opensea.io/{username}"},
    "NameMC": {"url": f"https://namemc.com/profile/{username}"},
    "Pluralsight": {"url": f"https://app.pluralsight.com/profile/{username}"},
    "TryHackMe": {"url": f"https://tryhackme.com/p/{username}"},
    "Furaffinity": {"url": f"https://www.furaffinity.net/user/{username}"},
    "Pornhub": {"url": f"https://www.pornhub.com/users/{username}"},
    "XVideos": {"url": f"https://www.xvideos.com/profiles/{username}"},
    "XHamster": {"url": f"https://xhamster.com/users/{username}"},
    "Chess.com": {"url": f"https://www.chess.com/member/{username}"},
    "Lichess": {"url": f"https://lichess.org/@/{username}"},
    "Gravatar": {"url": f"https://en.gravatar.com/{username}"},
    "Instructables": {"url": f"https://www.instructables.com/member/{username}"},
    "Codeforces": {"url": f"https://codeforces.com/profile/{username}"},
    "TopCoder": {"url": f"https://www.topcoder.com/members/{username}"},
    "Stack Overflow": {"url": f"https://stackoverflow.com/users/story/{username}"},
    "SuperUser": {"url": f"https://superuser.com/users/{username}"},
    "AskUbuntu": {"url": f"https://askubuntu.com/users/{username}"},
    "Unix.SE": {"url": f"https://unix.stackexchange.com/users/{username}"},
    "BitcoinTalk": {"url": f"https://bitcointalk.org/index.php?action=profile;u={username}"},
    "Scratch": {"url": f"https://scratch.mit.edu/users/{username}"},
    "Houzz": {"url": f"https://www.houzz.com/user/{username}"},
    "Mix": {"url": f"https://mix.com/{username}"},
    "WeHeartIt": {"url": f"https://weheartit.com/{username}"},
    "DailyMotion": {"url": f"https://www.dailymotion.com/{username}"},
    "AngelList": {"url": f"https://angel.co/u/{username}"},
    "Shutterstock": {"url": f"https://www.shutterstock.com/g/{username}"},
    "Tripit": {"url": f"https://www.tripit.com/people/{username}"},
    "Canva": {"url": f"https://www.canva.com/{username}/"},
    "Bitbucket": {"url": f"https://bitbucket.org/{username}/"},
    "Hackaday.io": {"url": f"https://hackaday.io/{username}"},
    "Badoo": {"url": f"https://badoo.com/profile/{username}"},
    "Zoho": {"url": f"https://zoho.com/{username}"},
    "Zoosk": {"url": f"https://www.zoosk.com/profile/{username}"},
    "Imgflip": {"url": f"https://imgflip.com/user/{username}"},
    "Giphy": {"url": f"https://giphy.com/{username}"},
    "MeWe": {"url": f"https://mewe.com/i/{username}"},
    "Rumble": {"url": f"https://rumble.com/{username}"},
    "Brighteon": {"url": f"https://www.brighteon.com/channels/{username}"},
    "PeerTube": {"url": f"https://peertube.social/accounts/{username}"},
    "Gab": {"url": f"https://gab.com/{username}"},
    "Mastodon.social": {"url": f"https://mastodon.social/@{username}"},
    "Pixiv": {"url": f"https://www.pixiv.net/en/users/{username}"},
    "Myspace": {"url": f"https://myspace.com/{username}"},
    "Vero": {"url": f"https://getvero.com/{username}"},
    "Triller": {"url": f"https://triller.co/@{username}"},
    "Ravelry": {"url": f"https://www.ravelry.com/people/{username}"},
    "VSCO": {"url": f"https://vsco.co/{username}"},
    "Zillow": {"url": f"https://www.zillow.com/profile/{username}/"},
    "Unsplash": {"url": f"https://unsplash.com/@{username}"},
    "Ellucian": {"url": f"https://{username}.elluciancloud.com"}
}
    sessao = requests.Session()
    sessao.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    
    if usar_tor:
        sessao.proxies = proxy_tor

    print(f"\n{Cores.BRANCO}{lang[idioma]['results_for']}{Cores.VERDE}{username}:")
    
    for nome, data in redes.items():
        url = data['url']
        try:
            res = sessao.get(url, timeout=15)
            
            # Verificação personalizada
            if 'check' in data:
                encontrado = data['check'](res)
            else:
                encontrado = res.status_code == 200
                
            if encontrado:
                estado = f"{Cores.VERDE}{lang[idioma]['found']}"
            else:
                estado = f"{Cores.VERMELHO}{lang[idioma]['not_found']}"
                
            print(f"{Cores.BRANCO}- {nome}: {estado} {Cores.BRANCO}→ {Cores.CIANO}{url}")
            
        except Exception as e:
            estado = f"{Cores.VERMELHO}{lang[idioma]['connection_error']}"
            print(f"{Cores.BRANCO}- {nome}: {estado} {Cores.BRANCO}→ {Cores.CIANO}{url}")

# === Informações de Domínio ===
def informacao_dominio():
    dominio = input(f"{Cores.BRANCO}{lang[idioma]['input_domain']}{Cores.VERDE}")
    try:
        dados = whois.whois(dominio)

        # Normalizar dados
        registrador = dados.registrar or lang[idioma]['not_available']
        
        data_criacao = dados.creation_date
        if isinstance(data_criacao, list):
            data_criacao = data_criacao[0]
        data_criacao = data_criacao.strftime('%Y-%m-%d') if data_criacao else lang[idioma]['not_available']
        
        data_expiracao = dados.expiration_date
        if isinstance(data_expiracao, list):
            data_expiracao = data_expiracao[0]
        data_expiracao = data_expiracao.strftime('%Y-%m-%d') if data_expiracao else lang[idioma]['not_available']

        print(f"\n{Cores.BRANCO}{lang[idioma]['whois_info']}{Cores.VERDE}{dominio}:")
        print(f"{Cores.BRANCO}{lang[idioma]['registrar']}{Cores.VERDE}{registrador}")
        print(f"{Cores.BRANCO}{lang[idioma]['creation_date']}{Cores.VERDE}{data_criacao}")
        print(f"{Cores.BRANCO}{lang[idioma]['expiration_date']}{Cores.VERDE}{data_expiracao}")
        
        # Verificar histórico DNS
        try:
            print(f"\n{Cores.BRANCO}{lang[idioma]['dns_history']}")
            sessao = requests.Session()
            if usar_tor:
                sessao.proxies = proxy_tor
                
            res = sessao.get(f"https://securitytrails.com/domain/{dominio}/dns", timeout=10)
            if res.status_code == 200:
                print(f"{Cores.VERDE}{lang[idioma]['data_available']}")
            else:
                print(f"{Cores.AMARELO}{lang[idioma]['no_history']}")
        except:
            print(f"{Cores.VERMELHO}{lang[idioma]['connection_error']}")

    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_whois']}{e}")

# === Verificar vazamentos de email ===
def verificar_vazamentos_email():
    email = input(f"{Cores.BRANCO}{lang[idioma]['input_email']}{Cores.VERDE}")
    try:
        print(f"\n{Cores.BRANCO}{lang[idioma]['checking_leaks']}")
        
        sessao = requests.Session()
        sessao.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        
        if usar_tor:
            sessao.proxies = proxy_tor

        # Verificar em várias fontes
        encontrado = False
        
        # Verificador local por padrões
        vazamentos = []
        
        # Verificar em pastebin
        try:
            res = sessao.get("https://pastebin.com/", timeout=15)
            if res.status_code == 200:
                if email in res.text:
                    vazamentos.append("Pastebin")
                    encontrado = True
        except:
            pass
        
        # Verificar em haveibeenpwned via scraping
        try:
            res = sessao.get(f"https://haveibeenpwned.com/unifiedsearch/{email}", timeout=15)
            if res.status_code == 200:
                if email in res.text:
                    vazamentos.append("Have I Been Pwned")
                    encontrado = True
        except:
            pass
        
        # Verificar em leakedsource (site alternativo)
        try:
            res = sessao.get(f"https://leakedsource.ru/main/search?q={email}", timeout=15)
            if res.status_code == 200:
                if "Found in" in res.text:
                    vazamentos.append("LeakedSource")
                    encontrado = True
        except:
            pass
            
        if encontrado:
            print(f"{Cores.VERMELHO}{lang[idioma]['leaks_found']}")
            for vazamento in vazamentos:
                print(f"{Cores.BRANCO}- {Cores.VERMELHO}{vazamento}")
        else:
            print(f"{Cores.VERDE}{lang[idioma]['no_leaks_found']}")
            
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}")

# === Análise de Imagem ===
def analisar_imagem():
    url = input(f"{Cores.BRANCO}{lang[idioma]['input_image_url']}{Cores.VERDE}")
    try:
        print(f"\n{Cores.BRANCO}{lang[idioma]['image_analysis']}")
        
        sessao = requests.Session()
        if usar_tor:
            sessao.proxies = proxy_tor
            
        # Baixar imagem
        response = sessao.get(url, timeout=15)
        img = Image.open(BytesIO(response.content))
        
        # Informações básicas
        print(f"{Cores.BRANCO}{lang[idioma]['image_size']}{Cores.VERDE}{img.size}")
        print(f"{Cores.BRANCO}{lang[idioma]['image_format']}{Cores.VERDE}{img.format}")
        
        # Verificar metadados EXIF
        try:
            exif_data = img._getexif()
            if exif_data:
                print(f"\n{Cores.BRANCO}{lang[idioma]['exif_data']}")
                for tag, value in exif_data.items():
                    tag_name = Image.TAGS.get(tag, tag)
                    print(f"  - {tag_name}: {value}")
            else:
                print(f"{Cores.AMARELO}{lang[idioma]['no_exif']}")
        except:
            print(f"{Cores.VERMELHO}{lang[idioma]['exif_error']}")
            
        # Pesquisa reversa no Google
        print(f"\n{Cores.BRANCO}{lang[idioma]['reverse_search']}")
        print(f"{Cores.CIANO}  https://lens.google.com/uploadbyurl?url={quote(url)}")
        
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}")

# === Analisador de Metadados de Documentos ===
def analisar_documentos():
    url = input(f"{Cores.BRANCO}{lang[idioma]['input_doc_url']}{Cores.VERDE}")
    try:
        sessao = requests.Session()
        if usar_tor:
            sessao.proxies = proxy_tor
            
        # Baixar documento
        response = sessao.get(url, timeout=20)
        extensao_arquivo = url.split('.')[-1].lower()
        
        if extensao_arquivo == 'pdf':
            # Analisar PDF
            with BytesIO(response.content) as pdf_file:
                leitor = PyPDF2.PdfReader(pdf_file)
                info = leitor.metadata
                
                print(f"\n{Cores.BRANCO}{lang[idioma]['pdf_metadata']}")
                print(f"{Cores.BRANCO}{lang[idioma]['title']}{Cores.VERDE}{info.get('/Title', 'N/A')}")
                print(f"{Cores.BRANCO}{lang[idioma]['author']}{Cores.VERDE}{info.get('/Author', 'N/A')}")
                print(f"{Cores.BRANCO}{lang[idioma]['creator']}{Cores.VERDE}{info.get('/Creator', 'N/A')}")
                print(f"{Cores.BRANCO}{lang[idioma]['producer']}{Cores.VERDE}{info.get('/Producer', 'N/A')}")
                print(f"{Cores.BRANCO}{lang[idioma]['creation_date']}{Cores.VERDE}{info.get('/CreationDate', 'N/A')}")
                print(f"{Cores.BRANCO}{lang[idioma]['mod_date']}{Cores.VERDE}{info.get('/ModDate', 'N/A')}")
                
        elif extensao_arquivo in ['docx', 'doc']:
            # Analisar DOCX
            with BytesIO(response.content) as docx_file:
                doc = Document(docx_file)
                propriedades = doc.core_properties
                
                print(f"\n{Cores.BRANCO}{lang[idioma]['docx_metadata']}")
                print(f"{Cores.BRANCO}{lang[idioma]['title']}{Cores.VERDE}{propriedades.title}")
                print(f"{Cores.BRANCO}{lang[idioma]['author']}{Cores.VERDE}{propriedades.author}")
                print(f"{Cores.BRANCO}{lang[idioma]['created']}{Cores.VERDE}{propriedades.created}")
                print(f"{Cores.BRANCO}{lang[idioma]['modified']}{Cores.VERDE}{propriedades.modified}")
                print(f"{Cores.BRANCO}{lang[idioma]['last_modified_by']}{Cores.VERDE}{propriedades.last_modified_by}")
                
        else:
            print(f"{Cores.VERMELHO}{lang[idioma]['unsupported_doc']}")
            
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}")

# === Rastrear Criptomoedas ===
def rastrear_criptomoedas():
    endereco = input(f"{Cores.BRANCO}{lang[idioma]['input_crypto']}{Cores.VERDE}")
    print(f"\n{Cores.BRANCO}{lang[idioma]['crypto_info']}")
    
    sessao = requests.Session()
    if usar_tor:
        sessao.proxies = proxy_tor
    
    # Bitcoin
    try:
        res = sessao.get(f"https://blockchain.info/rawaddr/{endereco}", timeout=15)
        if res.status_code == 200:
            dados = res.json()
            print(f"{Cores.BRANCO}Bitcoin (BTC):")
            print(f"{Cores.BRANCO}- {lang[idioma]['balance']}: {Cores.VERDE}{dados['final_balance'] / 100000000:.8f} BTC")
            print(f"{Cores.BRANCO}- {lang[idioma]['total_received']}: {Cores.VERDE}{dados['total_received'] / 100000000:.8f} BTC")
            print(f"{Cores.BRANCO}- {lang[idioma]['total_sent']}: {Cores.VERDE}{dados['total_sent'] / 100000000:.8f} BTC")
            print(f"{Cores.BRANCO}- {lang[idioma]['transactions']}: {Cores.VERDE}{dados['n_tx']}")
        else:
            print(f"{Cores.VERMELHO}Bitcoin: {lang[idioma]['no_data']}")
    except:
        print(f"{Cores.VERMELHO}Bitcoin: {lang[idioma]['connection_error']}")
    
    # Ethereum
    try:
        res = sessao.get(f"https://api.etherscan.io/api?module=account&action=balance&address={endereco}&tag=latest", timeout=15)
        if res.status_code == 200:
            dados = res.json()
            if dados['status'] == '1':
                saldo = int(dados['result']) / 10**18
                print(f"\n{Cores.BRANCO}Ethereum (ETH):")
                print(f"{Cores.BRANCO}- {lang[idioma]['balance']}: {Cores.VERDE}{saldo:.8f} ETH")
            else:
                print(f"\n{Cores.VERMELHO}Ethereum: {lang[idioma]['no_data']}")
        else:
            print(f"\n{Cores.VERMELHO}Ethereum: {lang[idioma]['connection_error']}")
    except:
        print(f"\n{Cores.VERMELHO}Ethereum: {lang[idioma]['connection_error']}")

# === Buscar Documentos Vazados ===
def buscar_documentos_vazados():
    termo = input(f"{Cores.BRANCO}{lang[idioma]['input_doc_query']}{Cores.VERDE}")
    print(f"\n{Cores.BRANCO}{lang[idioma]['searching_docs']}")
    
    sessao = requests.Session()
    if usar_tor:
        sessao.proxies = proxy_tor
    
    # Repositórios públicos
    repositorios = {
        "Google Dorks": f"https://www.google.com/search?q=filetype:pdf+{quote(termo)}",
        "Archive.org": f"https://archive.org/search.php?query={quote(termo)}",
        "GitHub": f"https://github.com/search?q={quote(termo)}&type=code",
        "Pastebin": f"https://pastebin.com/search?q={quote(termo)}"
    }
    
    for nome, url in repositorios.items():
        print(f"{Cores.BRANCO}- {nome}: {Cores.CIANO}{url}")

# === Pesquisa em Lote ===
def pesquisa_em_lote():
    print(f"{Cores.BRANCO}{lang[idioma]['batch_instructions']}")
    print(f"{Cores.BRANCO}1. {lang[idioma]['batch_option1']}")
    print(f"{Cores.BRANCO}2. {lang[idioma]['batch_option2']}")
    print(f"{Cores.BRANCO}3. {lang[idioma]['batch_option3']}")
    
    escolha = input(f"{Cores.BRANCO}{lang[idioma]['option']}{Cores.VERDE}")
    
    sessao = requests.Session()
    if usar_tor:
        sessao.proxies = proxy_tor
        
    if escolha == '1':
        # Pesquisa de múltiplos usuários
        usuarios = input(f"{Cores.BRANCO}{lang[idioma]['input_usernames']}{Cores.VERDE}").split(',')
        for usuario in usuarios:
            usuario = usuario.strip()
            if usuario:
                print(f"\n{Cores.CIANO}=== {usuario} ===")
                buscar_usuario_simulado(usuario, sessao)
                
    elif escolha == '2':
        # Verificar múltiplos emails
        emails = input(f"{Cores.BRANCO}{lang[idioma]['input_emails']}{Cores.VERDE}").split(',')
        for email in emails:
            email = email.strip()
            if email:
                print(f"\n{Cores.CIANO}=== {email} ===")
                verificar_vazamentos_email_simulado(email, sessao)
                
    elif escolha == '3':
        # Rastrear múltiplos IPs
        ips = input(f"{Cores.BRANCO}{lang[idioma]['input_ips']}{Cores.VERDE}").split(',')
        for ip in ips:
            ip = ip.strip()
            if ip:
                print(f"\n{Cores.CIANO}=== {ip} ===")
                rastrear_ip_simulado(ip, sessao)

# === Funções auxiliares para pesquisa em lote ===
def buscar_usuario_simulado(username, sessao):
    # Implementação simplificada para demonstração
    print(f"{Cores.BRANCO}GitHub: {Cores.CIANO}https://github.com/{username}")
    print(f"{Cores.BRANCO}Twitter: {Cores.CIANO}https://twitter.com/{username}")

def verificar_vazamentos_email_simulado(email, sessao):
    # Implementação simplificada para demonstração
    print(f"{Cores.BRANCO}Have I Been Pwned: {Cores.CIANO}https://haveibeenpwned.com/unifiedsearch/{email}")

def rastrear_ip_simulado(ip, sessao):
    # Implementação simplificada para demonstração
    try:
        res = sessao.get(f"https://ipwho.is/{ip}", timeout=5).json()
        print(f"{Cores.BRANCO}{lang[idioma]['country']}{Cores.VERDE}{res.get('country', 'N/A')}")
        print(f"{Cores.BRANCO}{lang[idioma]['city']}{Cores.VERDE}{res.get('city', 'N/A')}")
    except:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}")

# === Análise de Redes ===
def analise_de_redes():
    dominio = input(f"{Cores.BRANCO}{lang[idioma]['input_domain_net']}{Cores.VERDE}")
    print(f"\n{Cores.BRANCO}{lang[idioma]['network_analysis']}")
    
    sessao = requests.Session()
    if usar_tor:
        sessao.proxies = proxy_tor
        
    try:
        # Obter IPs associados
        ips = socket.getaddrinfo(dominio, 80)
        print(f"{Cores.BRANCO}{lang[idioma]['associated_ips']}:")
        for ip in set(i[4][0] for i in ips):
            print(f"{Cores.CIANO}- {ip}")
            
        # Obter subdomínios com Censys
        print(f"\n{Cores.BRANCO}{lang[idioma]['possible_subdomains']}:")
        try:
            res = sessao.get(f"https://search.censys.io/search?resource=hosts&q={quote(dominio)}", timeout=15)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                subdominios = set()
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and dominio in href and '//' not in href:
                        subdominios.add(href.split('.')[0])
                
                for sub in list(subdominios)[:10]:
                    print(f"{Cores.CIANO}- {sub}.{dominio}")
            else:
                print(f"{Cores.AMARELO}{lang[idioma]['no_subdomains']}")
        except:
            print(f"{Cores.VERMELHO}{lang[idioma]['connection_error']}")
            
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['error_general']}{e}")

# === Alternar Tor ===
def alternar_tor():
    global usar_tor
    usar_tor = not usar_tor
    status = f"{Cores.VERDE}{lang[idioma]['enabled']}" if usar_tor else f"{Cores.VERMELHO}{lang[idioma]['disabled']}"
    print(f"\n{Cores.BRANCO}Tor: {status}{Cores.RESET}")

# === Gerar Relatório ===
def gerar_relatorio():
    nome_arquivo = input(f"{Cores.BRANCO}{lang[idioma]['report_name']}{Cores.VERDE}")
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"Relatório Eye of Odin - Gerado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            f.write("[RESUMO DE OPERAÇÕES]\n")
            # Adicione aqui os resultados das operações
            f.write("\n- IP rastreado: 192.168.1.1\n")
            f.write("- Usuário encontrado: johndoe\n")
            f.write("- Documentos relacionados: 3 encontrados\n")
            
        print(f"{Cores.VERDE}{lang[idioma]['report_saved']}{nome_arquivo}")
    except Exception as e:
        print(f"{Cores.VERMELHO}{lang[idioma]['report_error']}{e}")

# === Menu de Idiomas ===
def escolher_idioma():
    global idioma
    limpar_tela()
    mostrar_banner()
    print(f"{Cores.BRANCO}Selecione o idioma:")
    print(f"{Cores.CIANO}1. Español\n2. English\n3. Português")
    opc = input(f"{Cores.VERDE}>>> ")
    if opc == "2":
        idioma = "en"
    elif opc == "3":
        idioma = "pt"
    else:
        idioma = "es"

# === Menu Principal ===
def main():
    global usar_tor
    
    while True:
        limpar_tela()
        mostrar_banner()
        status_tor = f"{Cores.VERDE}[TOR]" if usar_tor else f"{Cores.VERMELHO}[WITHOUT-TOR]"
        print(f"{Cores.BRANCO}{status_tor} {lang[idioma]['menu']}")
        print(f"{Cores.CIANO}[1] {Cores.BRANCO}{lang[idioma]['ip_track']}")
        print(f"{Cores.CIANO}[2] {Cores.BRANCO}{lang[idioma]['phone_track']}")
        print(f"{Cores.CIANO}[3] {Cores.BRANCO}{lang[idioma]['user_search']}")
        print(f"{Cores.CIANO}[4] {Cores.BRANCO}{lang[idioma]['domain_info']}")
        print(f"{Cores.CIANO}[5] {Cores.BRANCO}{lang[idioma]['email_check']}")
        print(f"{Cores.CIANO}[6] {Cores.BRANCO}{lang[idioma]['image_analysis']}")
        print(f"{Cores.CIANO}[7] {Cores.BRANCO}{lang[idioma]['doc_analysis']}")
        print(f"{Cores.CIANO}[8] {Cores.BRANCO}{lang[idioma]['crypto_track']}")
        print(f"{Cores.CIANO}[9] {Cores.BRANCO}{lang[idioma]['leaked_docs']}")
        print(f"{Cores.CIANO}[10] {Cores.BRANCO}{lang[idioma]['batch_search']}")
        print(f"{Cores.CIANO}[11] {Cores.BRANCO}{lang[idioma]['network_analysis']}")
        print(f"{Cores.CIANO}[12] {Cores.BRANCO}{lang[idioma]['tor_toggle']}")
        print(f"{Cores.CIANO}[13] {Cores.BRANCO}{lang[idioma]['generate_report']}")
        print(f"{Cores.CIANO}[0] {Cores.BRANCO}{lang[idioma]['exit']}")

        opcao = input(f"\n{Cores.VERDE}{lang[idioma]['option']}{Cores.BRANCO}")
        """""
        # Mostrar animação quando uma opção válida é selecionada
        if opcao in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            #animar_cajado()
            limpar_tela()
            mostrar_banner()
            """
        if opcao == '1':
            rastrear_ip()
        elif opcao == '2':
            rastrear_telefone()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            informacao_dominio()
        elif opcao == '5':
            verificar_vazamentos_email()
        elif opcao == '6':
            analisar_imagem()
        elif opcao == '7':
            analisar_documentos()
        elif opcao == '8':
            rastrear_criptomoedas()
        elif opcao == '9':
            buscar_documentos_vazados()
        elif opcao == '10':
            pesquisa_em_lote()
        elif opcao == '11':
            analise_de_redes()
        elif opcao == '12':
            alternar_tor()
        elif opcao == '13':
            gerar_relatorio()
        elif opcao == '0':
            print(f"{Cores.VERMELHO}{lang[idioma]['exit']}...{Cores.RESET}")
            break
        else:
            print(f"{Cores.VERMELHO}{lang[idioma]['invalid_option']}")

        input(f"\n{Cores.AMARELO}{lang[idioma]['press_enter']}{Cores.RESET}")

#== Executar ==

def run():
    parse_args()
    escolher_idioma()
    main()
 
if __name__ == "__main__":
    parse_args()
    escolher_idioma()
    main()