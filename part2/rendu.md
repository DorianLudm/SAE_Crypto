# SAE 3.04, Cryptographie partie 2.
## Par LUDMANN Dorian et HAUDEBOURG Baptiste  

### Partie 1  
## En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout? En vous appuyant sur votre cours, justifiez votre réponse.  
Si le RSA est utilisé correctement, Eve peut espérer en venir à bout à l'aide de la méthode brute force.  
Peu importe sa compléxité, il est possible de le décrypter. Cependant, plus sa compléxité est élevée, plus le temps de décryptage par brute force est important.  


## En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai nécessaire à une méthode “force brute” pour retrouver la clé.  
Selon l'implémentation du [SDES en python](https://jhafranco.com/2012/02/10/simplified-des-implementation-in-python/), "il suffit, en moyenne, de seulement 512 essais afin de le décrypter", par le fait qu'il y ai seulement 2<sup>8</sup> possibilités unique sachant que la clé est codée sur 10 bits.  
L'algorithme SDES est donc très peu sécurisé par le fait que la force brute permet de "déchiffrer la clé en l'espace de quelques dixièmes de secondes".  


## Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal? Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé.  
Le double SDES est certes plus sécurisé qu'un chiffrage par SDES mais dans quelles mesures?  
- Contre un brut force, l'anciennement 2<sup>8</sup> possibilités se transforme désormais en 2<sup>8<sup>2</sup></sup> = 2<sup>64</sup> possibilités. Il faut donc en moyenne 9,2*10<sup>18</sup> essais en moyenne.
- Pourtant, sur un cassage astucieux, doubler le SDES est peu efficace, car contre sa variante brutale, où 2<sup>n</sup> est le nombre de possibilités d'encondage (avec n le nombre de cryptage par SDES), sur un cassage astucieux, le nombre d'itérations nécéssaire afin de décrypter le code est de 2n. Les 1024 possibilités deviennent 1024*2 = 2048, qui reste alors à moins d'une seconde d'éxécution pour décoder. En moyenne, il faudras alors 1024 essais pour décoder le message.
- D'un point de vue mathématiques, le double chiffrement par SDES créé un chevauchement lors du décodage, qui peut permettre de complexifier le déchiffrage.

Décodage astucieux par "Meet in the middle":
L'attaquant utilise un programme de déchiffrement qui se propagent des deux extrémités jusqu'au milieu du système, dans certains cas en devinant une partie de la clé. Si les événements ne correspondent pas au milieu, l'hypothèse de la clé est erronée et peut être jetée.
Ce principe provient de la théorie des graphes lorsqu'on essaye de relier deux sommets entre eux. Au lieu de faire un parcours simple depuis la racine, on fais un double parcours des deux cotés afin de transformer l'algorithme d'une compléxité de O(n<sup>n</sup>) à une compléxité de O(2n)

### Notre décodage astucieux