Avant juin 2016 :
	Réflexions et brouillons
	Premiers jets d'un outil générique permettant d'utiliser la technique
	de la génération évolutive, l'EvolutiveGenerator.
------------------------------------------------------------------------------

6-22 juin 2016 :
	Réalisation d'une présentation pour passage devant M Réal et Mme Chevalier
	(cf tipe.odp)
	Recherche de documentation sur le sujet, trouvé :
		NeuroEvolution of Augmenting Topologies by MIT
------------------------------------------------------------------------------

1-23 Juillet 2016 :
	...
	Objectif 1.0 :
		Adapter le jeu :
			- modification du jeu.
			- création d'un bridge permettant de faire le lien entre le
			logiciel de génération évolutive et le jeu.
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
		Coder le processus de génération.
	
	Objectif 2.0 :
		Coder l'EvolutiveGenerator.
	
	Objectif 2.1 :
		Représenter l'IA.
	
	Objectif 2.2 :
		Coder les algorithmes de création, mutations et combinaisons.
------------------------------------------------------------------------------

16 Août 2016 : Spécifications 2.1 et 2.2
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
				On crée 3 à 6 neurones de manière équiprobable.
			mutate():
				20% de chance de créer un nouveau neurone
				10% de chance de détruire un neurone
				pour chaque neurone: 20% de chance de muter
			combine():
				On prend 50% des neurones de chaque parent (arrondi par excès).
		Neurone :
			create():
				On crée un évènement.
				On crée une action.
			mutate():
				On mute un de ces éléments:
					- l'évènement
					- l'action
		Évènement :
			create():
				On tire un évènement et une coor au pif.
			mutate():
				On change soit le nom soit les coordonnées de manière
				équiprobable.
				Changement des coordonnées :
					On tire un entier entre [-100;+100] qu'on ajoute à x.
					Idem avec y.
		Action :
			create():
				On tire une action et une durée dans [2;30].
			mutate():
				On change soit la classe soit la durée de manière équiprobable.
				Changement de la durée :
					On tire un entier entre [2;30] (frames).
		
	Je décide finalement de séparer les modèles :
		- représentation en tant que données via 4 entités
		- manipulation en tant que GeneticElement via 4 factory
		- lecture des données et interaction avec l'event dispatcher dans la
		classe Neuron
------------------------------------------------------------------------------

17 Août 2016 :
	Objectifs 2.0, 2.1 et 2.2 atteints
	
	Objectif 2.3 :
		Coder le Graduator, utilisant le bridge pour évaluer les IA.
