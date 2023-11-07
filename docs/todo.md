# Todo
- [ ] inspi https://larmarange.github.io/analyse-R/analyse-de-survie.html
- [ ] diapo pas mal https://jonathanlenoir.files.wordpress.com/2013/12/analyse-de-survie-cox.pdf
- [ ] modele de ML
- [ ] jeu de données https://www.kaggle.com/datasets/kemical/kickstarter-projects?select=ks-projects-201801.csv & https://www.kaggle.com/datasets/sripaadsrinivasan/kickstarter-campaigns-dataset
- [ ] faire un tableau à 3 colonnes : paramètre / formules / explication interpréation


# Todo cours
- [ ] modèles à tester
  - [ ] Kaplan-Meier
  - [ ] Cox
  - [ ] Weibull?
- [ ] tracer les fonctions ![image](https://github.com/Ab2nour/analyse-survie/assets/61651582/bae53279-5cb7-4cdd-99b9-2001532da63a)
  - [ ] densité
  - [ ] répartition
  - [ ] risque
  - [ ] survie
- [ ] estimation $\displaystyle \hat{s}(t) = \dfrac{1}{n} \sum_{i = 1}^{n} \mathbb{1}_{\{ t_i > t \}}$

# séance du 24/10
I) estimation de S
a) Sans censure <-- vous la connaissez déjà...
b) en présence de censure : estimateur de Kaplan-Meier, S_KM
b-1) Donner l'expression de S_KM
b-2) Donner les proprités de l'estimateur :

Biais 
* Est il biaisé?  Si oui donner la valeur du biais?   asymptotiquement sans biais?
* Comment expliqueriez vous la notion dans le cas de votre use case à Mr et Mme Toutlemonde?

Variance 
* Donner La variance de l’estimateur (la formule)

Normalité asymptotique (TCL)

* Donner le résultat de convergence en loi
* Comment expliqueriez vous cela à Mr et Mme Toutlemonde ?

En déduire un intervalle de confiance (asymptotique).
* Comment expliqueriez vous cela à Mr et Mme Toutlemonde ?

Graphique :  (si vos données s’y prêtent)
Si vos données sont censurées
* Faire la représentation  de S_KM(t) + intervalle de confiance à 5% (avec censure)
2.  Superposer sur le même graphique S_KM(t) et   \hat(S)(t) sans censure (cette question est là pour apprécier l’impact de la prise en compte ou non de la  censure )
Sinon 
* Faire la représentation  de S(t) + intervalle de confiance à 5%  (sans censure)

* Interpréter quelques dates (si ce n'est déjà fait)…

II) Estimation de H(t) et h(t) :  
1. Sans censure.
2. En présence de censure : 2 estimateurs de H sont proposées 
* Donner l'estimateur de Breslow, H_Breslow ? Donner ses propriétés : biais, variance, TCL?
* Donner l'estimateur de Nelson Aalen, H_NA? Donner ses propriétés : biais, variance, TCL?

* Comparer les variances théoriques de H_Breslow et H_NA

Graphique pour H et h.
* Faire l’équivalent de ce que vous avez pour les graphiques pour S avec  H_breslow, H_NA.
* Commenter
* Interpréter quelques dates (si ce n'est déjà fait)…
