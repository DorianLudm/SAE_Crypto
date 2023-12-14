import scapy.all as scapy
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

packets = scapy.rdpcap('trace_sae.cap')
print(packets)
for packet in packets:
    print(packet.src)
    print(packet.dst)
    print(packet.summary())
    
cle = 0b11100111011011010011000100111111100100101011100110010000010011


