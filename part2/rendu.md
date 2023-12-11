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

### Notre décodage SDES  
Pour ce qui est des fonctions de décodage SDES, nous en avons trois.
Ces trois fonctions reprennent notamment les principes évoqués précédemment afin de rendre le décryptage de plus en plus efficace, en terme de réussite comme en temps.
Nos trois fonctions sont alors:  
- cassage_brtual: Renvoie un set des résultats possible. Lent mais réussite assurée.
- cassage_astucieux: Renvoie un set des couples de clés possible. Rapide mais environ 50% de chance de réussite.
- cassage_astucieux2: Renvoie aussi un set des couples de clés possibles. Environ 50% plus lent que cassage_astucieux, mais 100% de réussite.
Nos deux cassage_astucieux tente de reprendre le principe du "Meet in the Middle".  
![Screenshot des sorties lors de l'éxécution des tests](./img/SDES.png)  

Il est aussi important de noter la taille des sets renvoyés par nos fonctions. Malgrès le fait que celui peut paraitre conséquent, on dénombre en moyenne 256 couples de clés possible pour un encryptement par double SDES de taille de clé 8 (Soit 256 possibilités par clé). Sur les 65536 couples de clé1, clé2. On retourne alors 1/256<sup>ème</sup> des possibilités totale.  
![Screenshot de la sortie terminal quand à la taille des sets résultats](./img/nb_couples.png)  
Si jamais on souhaite trouver quelle clé est utilisé pour décoder un texte, on peut alors écrire une fonction qui test l'ensemble des 256 couples trouvé par cassage_astucieux pour ensuite appliqués les clés sur le texte et vérifier petit à petit que les mots formés appartiennent au dictionnaire français (anglais, etc).