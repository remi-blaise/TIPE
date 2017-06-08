TIPE Mode d'emploi
==================

1) rechercher git-bash puis ENTRER
2) taper :
cd ~/Documents/TIPE/tipe6/bin
3) Pour lancer un nouveau processus, taper :
python app.py new 30

3 commandes sont disponibles :
python app.py new <pop_length>
python app.py new <pop_length> --generations=<generations>
python app.py resume <processus_id>
python app.py play <processus_id>
python app.py play <processus_id> --generation_id=<generation_id>
python app.py play <processus_id> --ia_id=<ia_id>
python app.py print <processus_id>

Pour afficher l'aide :
python app.py --help        Pour l'aide générale
python app.py new --help    Pour l'aide sur la commande new
python app.py resume --help    Pour l'aide sur la commande resume
python app.py play --help    Pour l'aide sur la commande play
python app.py print --help    Pour l'aide sur la commande print

En voici les effets :
'python app.py new 30' :                Lance un processus générant des populations de 30 individus jusqu'à ce qu'un individu finisse le niveau
'python app.py new 30 --generations=40' Lance un processus générant 40 populations de 30 individus
'python app.py resume 3'                Reprend le processus stoppé d'id 15
'python app.py play 4'                  Fait jouer la meilleure intelligence artificielle de la dernière génération évaluée du processus 4
'python app.py print 3'                 Imprime l'ensemble des résultats dans un tableur csv, disponible dans le dossier data du processus

Pour arrêter un processus, CRL+C.

Les commandes new et resume ont désormais une option --show qui permet d'afficher les évaluations. N'impacte pas le temps d'évaluation.
La commande 'print' a aussi une option --as_grading qui permet de se rapprocher au mieux des conditions d'évaluation,
sans pour autant pouvoir les atteindres avec exactitude.

Si le processus s'arrête par une erreur :
Copier tout le texte qui s'est affiché depuis la ligne en couleur jusqu'en bas avec CLIC DROIT puis copy, et me l'envoyer par mail.
