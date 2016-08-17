Avant juin 2016 :
	réflexions, premiers jets, début du Generator
------------------------------------------------------------------------------

6-7 juin 2016 :
	Réalisation d'une présentation pour passage devant M Réal et Mme Chevalier
	(cf tipe.odp)
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
		Pour pouvoir accélérer le jeu, il a fallut convertir les délais en
		nombres de frames, et ce en multipliant les temps par le framerate.
		Ne devrait-on pas calculer un nombre de frames absolu ?
		Il me semble que c'est ce qu'il faudrait faire, mais les résultats
		attendus semble déjà atteint avec la solution actuelle. Pourquoi ?
------------------------------------------------------------------------------

11 Août 2016 :
	Il semblerait que le problème 1 soit dû au son.
	Objectif 1.1 :
		Enlever le son. Peut résoudre le problème 1.
	
	Objectif 1.2 :
		Fixer get_fps constant à 60 fps. Devrait résoudre le problème 2.
		[Édit] Fait.
		
	Objectif 2 :
		Coder le processus de génération
	
	Objectif 2.1 :
		Représenter l'IA
	
	Objectif 2.2 :
		Coder les algorithmes de création, mutations et combinaisons
------------------------------------------------------------------------------

16 Août 2016 :
	Réprésentation des données :
		IA :
			{ Neurones }
		Neurone :
			( Évènement, Action )
		Évènement :
			- nom
			- coordonnées (x, y)
		Action :
			- classe
			- durée
	Algorithmes :
		IA :
			create():
				On crée 5 neurones
			mutate():
				20% de chance de créer un nouveau neurone
				10% de chance de détruire un neurone
				pour chaque neurone: 20% de chance de muter
			combine():
				On prend 50% des neurones de chaque parent
		Neurone :
			create():
				On crée un évènement
				On crée une action
			mutate():
				On mute un de ces éléments:
					- l'évènement
					- l'action
		Évènement :
			create():
				On tire un évènement et une coor au pif
			mutate():
				On change soit le nom soit les coordonnées à 50%/50%.
				Changement des coordonnées :
					On tire un flottant entre [-100;+100] qu'on ajoute à x.
					Idem avec y.
		Action :
			create():
				On tire une action et une durée dans [2;30]
			mutate():
				On change soit la classe soit la durée à 50%/50%.
				Changement de la durée :
					On tire un flottant entre [2;30] (frames).
		
	Je décide finalement de séparer les modèles :
		- représentation en tant que données via 4 entités
		- manipulation en tant que GeneticElement via 4 factory
		- lecture des données et interaction avec l'event dispatcher dans la
		classe Neuron
------------------------------------------------------------------------------
