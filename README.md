# README - Modélisation par homologie d’un domaine de la protéine p63 chez la souris

## Description du Projet

Ce projet consiste en la **modélisation par homologie** du domaine de liaison à l'ADN (**DNA binding domain**) de la protéine p63 chez la souris. Cette protéine, appartenant à la famille des antigènes tumoraux p53, joue un rôle essentiel dans divers processus biologiques tels que la transcription, la morphogenèse épithéliale et l'apoptose. La structure tridimensionnelle de la p63 chez la souris n'étant pas connue, ce projet vise à prédire un modèle fiable basé sur des structures expérimentales homologues connues, telles que celles de p63, p73 et p53 chez d'autres organismes.

L'objectif principal est de construire et d'évaluer un modèle tridimensionnel du domaine **DNA binding** de p63, qui pourra servir à des recherches futures sur les maladies associées à cette protéine, comme le syndrome ADULT ou le syndrome AEC.

---

## Pré-requis Techniques

- **Logiciels** :
  - MODELLER
  - EMBOSS Needle/Water
  - BLAST/PSI-BLAST
  - Clustal Omega
  - ProSA-Web, Verify 3D
- **Langages** : Python (scripts pour MODELLER), R (analyse des scores).

---

## Utilisation

1. **Préparer les données** :
   - Télécharger la séquence cible et les structures PDB des supports dans `src/`.

2. **Lancer les scripts** :
   - Utiliser les scripts Python pour générer les modèles.
   - Analyser les scores avec R pour sélectionner le meilleur modèle.

3. **Évaluer le modèle** :
   - Charger le modèle dans ProSA-Web et Verify 3D pour valider la qualité.

---

## Limitations et Perspectives

- Le modèle obtenu est fiable pour le domaine **DNA binding** (170-362), mais les régions externes restent mal définies.
- Des méthodes complémentaires comme la dynamique moléculaire pourraient être utilisées pour affiner la structure.

---

## Contribution

Projet réalisé dans le cadre des travaux pratiques de bio-informatique structurale. Pour plus d'informations, consultez le document détaillé dans le dossier `doc/`.