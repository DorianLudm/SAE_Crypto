from scapy.all import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#ouverure du fichier cap
packets = rdpcap('./part2/trace_sae.cap')
#clef de 64 bits récupéré à partir de l'image et dupliqué pour avoir 256 bits
key = b"1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100"
#conversion de la clef en bytes
key = int(key, 2).to_bytes(32, byteorder='big')

def remove_iv_and_unpad(payload):
    """Permet de retirer le vecteur d'initialisation et de retirer le padding du message

    Args:
        payload (String): le contenu du packet

    Returns:
        String: un tuble contenant le vecteur d'initialisation et le message sans le padding
    """
    iv = payload[:16]
    encrypted_message = payload[16:]
    return iv, encrypted_message
#on va parcourir tous les packets dans le fichier
for packet in packets:
    #si le packet est un packet UDP et qu'il est envoyé sur le port 9999 on va pouvoir l'analyser
    if packet.haslayer("UDP") and packet["UDP"].dport == 9999:
        #on récupère le contenu du packet et on le converti en bytes
        payload = bytes(packet["UDP"].payload)
        #on retire le vecteur d'initialisation et le padding du message
        iv, encrypted_message = remove_iv_and_unpad(payload)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        #on déchiffre le message
        decrypted_message = cipher.decrypt(encrypted_message)
        #on décode le message
        decoded_message = decrypted_message.decode("utf-8")
        print(decoded_message)


