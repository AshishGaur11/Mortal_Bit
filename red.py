
# we starting from [345:534] UI and os, sys, node, file system, cmd running form code, matrix, node !!



# we starting from [345:534] UI and os, sys, node, file system, cmd running form code, matrix, node !!
import subprocess
from bs4 import BeautifulSoup
import requests
from requests.models import Response
import scapy
import csv
import speech_recognition 
import pyttsx3

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
    
    def delete(self,index):
        pre = None 
        node = self.head
        i = 0
        
        while node != None and i < index :
            pre = node
            node = node.next
            i = i + 1
            
        if pre == None:
            self.head = node.next
        else:
            pre.next = node.next
            
    def show(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next 
    

if __name__=="__main__":
    
    qlist = linkedlist()


    def push():
    
       w = (input("Enter values\n"))
       qlist.add(w)
       main()
    
    def pop():
    
        q = int(input("Enter values remove by positions----\n"))
        qlist.delete(q)
        main()    
        
    def display():
    
        print("your entries are down here----\n")
        qlist.show()
        main()
    
    def MAC_changer():
        subprocess.call("ifconfig wlan0 down", shall=True)
        subprocess.call("ifconfig wlan0 hw ether 00:r4:0r:9t:b4:fg", shall=True)
        subprocess.call("ifconfig wlan0 up", shall=True)
        main()

    def scan(ip):
        scapy.arping(ip)
        main()

    def scan(ip):
        print("will allow you send packets and get the mac on same net(wi-if or ethernet)\n")
        arp_request = scapy.ARP(pdst=ip)
        print(arp_request.summary())
        main()


    def scan(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        print(broadcast.summary())
        arp_request_broadcast = broadcast/arp_request
        print(arp_request_broadcast.summary())
        arp_request_broadcast.show()
        answered, unanswered = scapy.srp(arp_request_broadcast)
        main()


    def subdomain(B1):
        url = B1
        try:
            get_response = requests.get("https://" + url)
            print(get_response)
        except requests.exceptions.ConnectionError:
            pass
        main()

    def subfiles(wer):
        
        target_url = wer
        with open("q.txt","r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = target_url + "/" + word
                Response = request(test_url)
                if Response:
                    print("[+] Discovered URL -->", test_url)
        main()


    def request(url):
        try:
            return requests.get("https://" + url)
        except request.exceptions.ConnectionError:
            pass
    
    def webscreper(url):

        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        csv_file = open('cms_scrape.csv', 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['headline', 'summary', 'video_link'])
        for article in soup.find_all('article'):
            headline = article.h2.a.text
            print(headline)
            summary = article.find('div', class_='entry-content').p.text
            print(summary)
            try:
                vid_src = article.find('iframe', class_='youtube-player')['src']
                vid_id = vid_src.split('/')[4]
                vid_id = vid_id.split('?')[0]
                yt_link = f'https://youtube.com/watch?v={vid_id}'
            except Exception as e:
                yt_link = None
            print(yt_link)
            print()
            csv_writer.writerow([headline, summary, yt_link])
        csv_file.close()
        main()


    def voice():
        engine = pyttsx3.init()
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("we are ready please tell me")
            audio = recognizer.listen(source)
            words = recognizer.recognize_google(audio)
            print("\nWelcome to MortalBit an AI based voice operated tool for Information gathering--\n")
            print("Author & Writer Ashish Gaur")
            print("\nPress the value to perform those functions in down there--\n")
            print("0 for Keep on Voice")
            print("1 for last insert.")
            print("2 for last remove.")
            print("3 for last display.")
            print("3.1 for changing MAC.")
            print("3.2 for changing IPv6 & IPv4.")
            print("3.3 for using VPN into VPN.")
            print("4 for full scan Decode javaScript.")
            print("5 for full scan Decode HTML.")
            print("6 for full scan Decode CSS.")
            print("7 for full scan Decode python.")
            print("8 for full scan Decode ruby.")
            print("9 To find links in whole website.")
            print("10 To paste text for whole scan as string.")
            print("11 for Json files, xml")
            print("12 for clone the device")
            print("13 To connect with wire shark")
            print("14 Direct to camera")
            print("15 Direct to audio")
            print("16 Direct to screen")
            print("17 To get Subdomain")
            print("18 To get Subfiles")
            print("19 To get webscraper")


            print("press q & Enter--\n")


            if "sub domain" in words:
                engine.say("Please provide the IP")
                print("Please provide the IP")
                audio = recognizer.listen(source)
                q = recognizer.recognize_google(audio)
                print(q)
                audio = recognizer.listen(source)
                m = recognizer.recognize_google(audio)
                if "Go on" in m:
                    subdomain(q)
                    engine.runAndWait()
                    voice()
            elif "Point Break" or "Break it" or "break" or "stop it" in words:
                engine.say("Ok bye")
                engine.runAndWait()
                break
            else:
                voice()

        main()





    
    def main():
    
        print("\nWelcome to MortalBit an AI based voice operated tool for Information gathering--\n")
        print("Author & Writer Ashish Gaur")
        print("\nPress the value to perform those functions in down there--\n")
        print("0 for Keep on Voice")
        print("1 for last insert.")
        print("2 for last remove.")
        print("3 for last display.")
        print("3.1 for changing MAC.")
        print("3.2 for changing IPv6 & IPv4.")
        print("3.3 for using VPN into VPN.")
        print("4 for full scan Decode javaScript.")
        print("5 for full scan Decode HTML.")
        print("6 for full scan Decode CSS.")
        print("7 for full scan Decode python.")
        print("8 for full scan Decode ruby.")
        print("9 To find links in whole website.")
        print("10 To paste text for whole scan as string.")
        print("11 for Json files, xml")
        print("12 for clone the device")
        print("13 To connect with wire shark")
        print("14 Direct to camera")
        print("15 Direct to audio")
        print("16 Direct to screen")
        print("17 To get Subdomain")
        print("18 To get Subfiles")
        print("19 To get webscraper")


        print("press q & Enter--\n")
        
        
        n = input()
        while True  :
            if n == '0':
                voice()
            elif n == '1':
                push()
            elif n == '2':
                pop()
            elif n == '3':
                display()

            elif n == '4':
                A1 = int(input("Enter resource value(ower own IP)"))
                scan(A1) 

            elif n == '17':
                A1 = input("Enter website (or IP)")
                subdomain(A1)     

            elif n == '18':
                A1 = input("Enter website (or IP)")
                subfiles(A1)

            elif n == '19':
                A1 = input("Enter website (or IP)")
                webscreper(A1)                  

            elif n == 'q':
                print("Hope your expireance was good!!")
                break
            else :
                print("sorry does'nt work")
                main()
                
        
    main()






















