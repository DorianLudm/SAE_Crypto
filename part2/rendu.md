# SAE 3.04, Cryptographie partie 2.
## Par LUDMANN Dorian et HAUDEBOURG Baptiste  

### Partie 1  
## En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout? En vous appuyant sur votre cours, justifiez votre réponse.  
Si le RSA est utilisé correctement, Eve peut espérer en venir à bout à l'aide de la méthode brute force.  
Peu importe sa compléxité, il est possible de le décrypter. Cependant, plus sa compléxité est élevée, plus le temps de décryptage par brute force est important.  


## En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai nécessaire à une méthode “force brute” pour retrouver la clé.  
Selon l'implémentation du [SDES en python](https://jhafranco.com/2012/02/10/simplified-des-implementation-in-python/), "il suffit, en moyenne, de seulement 512 essais afin de le décrypter", par le fait qu'il y ai seulement 2<sup>10</sup> possibilités unique sachant que la clé est codée sur 10 bits.  
L'algorithme SDES est donc très peu sécurisé par le fait que la force brute permet de "déchiffrer la clé en l'espace de quelques dixièmes de secondes".  


## Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal? Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé.  

A vous de coder!
• Proposez une méthode cassage_brutal(message_chiffre, taille_cle1, taille_cle2) qui tente de
retrouver la clé utilisée pour chiffrer le message en testant toutes les possibilités de clé.
• Proposez enfin une fonction cassage_astucieux(message_chiffre, ?) qui prend en entrée le message chiffré
et potentiellement d’autres paramètres.