Avant juin 2016 :
	réflexions, premiers jets, début du Generator
------------------------------------------------------------------------------

6-7 juin 2016 :
	Réalisation d'une présentation pour passage devant M Réal et Mme Chevalier (cf tipe.odp)
------------------------------------------------------------------------------

Juillet 2016 :
	...
	Objectif 1.0 :
		Adapter le jeu
------------------------------------------------------------------------------

23 Juillet 2016 :
	Objectif 1.0 atteint

	Problème 1 :
		Le programme plante souvent à l'extinction.

	Problème 2 :
		Pour pouvoir accélérer le jeu, il a fallut convertir les délais en nombres de frames,
		et ce en multipliant les temps par le framerate.
		Ne devrait-on pas calculer un nombre de frames absolu ?
		Il me semble que c'est ce qu'il faudrait faire, mais les résultats attendus semble déjà atteint
		avec la solution actuelle. Pourquoi ?
------------------------------------------------------------------------------

11 Août 2016 :
	Il semblerait que le problème 1 soit dû au son.
	Objectif 1.1 :
		Enlever le son. Peut résoudre le problème 1.
	
	Objectif 1.2 :
		Fixer get_fps constant à 60 fps. Devrait résoudre le problème 2.
		
	Objectif 2 :
		Coder le processus de génération
	
	Objectif 2.1 :
		Représenter l'IA
------------------------------------------------------------------------------
