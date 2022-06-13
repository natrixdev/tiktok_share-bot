import requests; import threading; from pystyle import Colorate, Colors, Write, Add, Center; import os 
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
text = "Welcome on TikTok master\nBy natrix"
print(Colorate.Horizontal(Colors.yellow_to_red, Add.Add(banner1, text, 4)))
from pystyle import Box
print(Box.Lines("Please insert the asked informations"))
VideoURI     = str(Write.Input("Video ID > ", Colors.yellow_to_red, interval=0.0001))
amount       = int(Write.Input("Amount (0=inf) > ", Colors.yellow_to_red, interval=0.0001))
sendType     = int(Write.Input("[1] - Launch > ", Colors.yellow_to_red, interval=0.0001)); 
view_bot = sendType=0
share_bot = sendType=1
share_amount = 0
daemon = True
while share_bot == 1:
    share_amount = share_amount+1
    print(Colorate.Horizontal(Colors.yellow_to_red, "[+] Sending shares on " + str(VideoURI) + ", amount of shares : [" + str(share_amount) + "]"))
    os.system("title Sent [" + str(share_amount) + "] shares")
else: 
    print('| Error |')
request = 'request(url),loop'
loop = 'url&share&+1&'
