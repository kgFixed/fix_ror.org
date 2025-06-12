# But de ce répertoire

L'objectif est de traiter les données de l'api ROR, pour les extraire sous forme de json, et ensuite faire un traitement à l'aide de sema.subyt pour passer de json à rdf.

## Adresse de l'api ror.org

```
    https://api.ror.org/organizations // all the organizations
    https://api.ror.org/organizations?query=vliz // for vliz
```

## Limite de l'API

Il n'est pas possible via l'API ror.org de récupérer toutes les données des entreprises, il faut passer par ce site, propre à ror, pour y accéder. C'est donc grâce à cela que nous allons peupler la première base de données avec toutes les informations des organisations:

```
    https://zenodo.org/records/15475023
```

En effet, en allant sur la documentation de ror, il est bien expliqué qu'il y a des limites à l'utilisation de l'api.

![Limit of data](/assets/limit.png "Limit of data")

De plus, comme depuis l'API je n'ai pas accès à toutes les données, et que dans les documents téléchargeable par ror.org, il n'y a pas de format jsonld, je ne suis pas en capacité de comparé les formats json et jsonld, ou encore jsonld et rdf.

## Prochaine étape

Les limites de l'API ne sont pas forcément un problème dans le sens où il n'est pas nécessaire de reprendre toutes les données de l'API à chaque fois, mais seulement les updates. Il faut faire la vérification des updates (journaliers, semaines...). 

Pour faire simple, une fois toutes les données récupérées, plus qu'à récupérer les updates de la base uniquement, de manière journalière, ou de la manière dont ils le font.

## Updates

Il y a plusieurs méthodes possibles pour acquérir les différents update de la base de données. 

1- Dans un premier temps, dès que des modifications sont ajoutées ou qu'il y a eu des ajouts dans la base, il y a une release sur github : 

```
    https://github.com/ror-community/ror-updates/releases
```

Il y a à la fois le résumé des changements, le nombre d'organisations ajoutées, le nombre d'organisations modifiées and la liste complète des organisations ajoutées et modifiées.

2- Dans un second temps, il est possible de récupérer de nouveau toute la base de données avec les modifications et les ajouts sur:

```
    https://zenodo.org/communities/ror-data/records?q=&l=list&p=1&s=10&sort=newest
```

En ce qui concerne le nombre d'update, il y en a **au moins un**, mais souvent il y en a **plutôt deux** par mois.

![Update of data](/assets/update.png "Update of data")

### Problème & Solution potentielles

D'après plusieurs tests et recherche, il semble peu probable de passer par l'API pour récuperer les nouveaux updates. En effet, il y a bien un paramètre 'last_modified', mais il ne serait pas possible de regarder pour chaque organisation ce paramètre, pour le même principe que la récupération des données, qui est limité à 10'000 organisations.

La solution la plus probable pour récupérer ces updates serait de passer par le github, qui fournit toutes les modifications ainsi que les ajouts des organisations.

Il serait aussi possible de passer par le dump totale de la base, et ensuite de faire une comparaison avec celle que nous avions, mais vu la quantité de données, cela semble compliqué.

## test

https://api.ror.org/v2/organizations?query.advanced=admin.last_modified.date:%5B2025-05-01%20TO%202025-05-16%5D&all_status // entre les dates des dernières releases (01 mai 2O25 - 16 mai 2025).

=> 763 diff selon l'api alors que normalement (github), il y a 172 added et 241 added != 763 au final.

## Utilisation de subyt

Avant toute chose, pour pouvoir accèder à la librairie sema.subyt, il faut suivre ces étapes:

```
python -m venv venv // création d'un environnement python
source venv/Scripts/activate // active le nouvel environnement
touch requirements.txt // création d'un fichier texte
git+https://github.com/vliz-be-opsci/py-sema.git // a mettre dans le fichier précédement créé
pip install -r requirements.txt // installation de la librairie subyt
```

Ensuite pour vérifier la bonne installation:

```
from sema.subyt import (
    Generator,
    GeneratorSettings,
    Sink,
    Source,
    SinkFactory,
    SourceFactory,
    JinjaBasedGenerator,
)
```
Cela ne devrait pas s'afficher en rouge si les installations ont bien fonctionnées.