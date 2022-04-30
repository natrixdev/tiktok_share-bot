
import requests 
import threading
from pystyle import Colorate, Colors, Write, Add, Center
from utils import *


banner1 = '''

███▄▄▄▄      ▄████████     ███        ▄████████  ▄█  ▀████    ▐████▀ 
███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ ███    ███▌   ████▀  
███   ███   ███    ███    ▀███▀▀██   ███    ███ ███▌    ███  ▐███    
███   ███   ███    ███     ███   ▀  ▄███▄▄▄▄██▀ ███▌    ▀███▄███▀    
███   ███ ▀███████████     ███     ▀▀███▀▀▀▀▀   ███▌    ████▀██▄     
███   ███   ███    ███     ███     ▀███████████ ███    ▐███  ▀███    
███   ███   ███    ███     ███       ███    ███ ███   ▄███     ███▄  
 ▀█   █▀    ███    █▀     ▄████▀     ███    ███ █▀   ████       ███▄ 
                                     ███    ███                      

'''

text = "Bienvnue sur le TikTok tool\nPar natrix"

print(Colorate.Horizontal(Colors.yellow_to_red, Add.Add(banner1, text, 4)))

from pystyle import Box
print(Box.Lines("Menu - natrix TikTok tool "))





VideoURI     = str(Write.Input("Video Link > ", Colors.yellow_to_red, interval=0.0001))
amount       = int(Write.Input("Amount (0=inf) > ", Colors.yellow_to_red, interval=0.0001))
sendType     = int(Write.Input("[1] - Lancer le bot > ", Colors.yellow_to_red, interval=0.0001)); 
view_bot = sendType=0
share_bot = sendType=1


banner2 = '''
█                     
'''
share_amount = 0
text1 = '| Sending shares | Target:' + VideoURI + ' | New Share Sent | '



while share_bot == 1:
    share_amount = share_amount+1
    print(Colorate.Horizontal(Colors.yellow_to_red, Add.Add(banner2, text1, 4)))
    print(share_amount)
else: 
    print('| Error |')


request = 'request(url),loop'
loop = 'url&share&+1&'

    