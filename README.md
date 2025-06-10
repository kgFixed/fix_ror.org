## But de ce répertoire

L'objectif est de traiter les données de l'api ROR, pour les extraire sous forme de json, et ensuite faire un traitement à l'aide de sema.subyt pour passer de json à rdf.

### Adresse de l'api ror.org

```
    https://api.ror.org/organizations // all the organizations
    https://api.ror.org/organizations?query=vliz // for vliz
```

### Limite de l'API

Il n'est pas possible via l'API ror.org de récupérer toutes les données des entreprises, il faut passer par ce site, propre à ror, pour y accéder:

```
https://zenodo.org/records/15475023
```

En effet, en allant sur la documentation de ror, il est bien expliqué qu'il y a des limites à l'utilisation de l'api.

![Limit of data](/assets/limit.png "Limit of data")

De plus, comme depuis l'API je n'ai pas accès à toutes les données, et que dans les documents téléchargeable par ror.org, il n'y a pas de format jsonld, je ne suis pas en capacité de comparé les formats json et jsonld, ou encore jsonld et rdf.

### Prochaine étape

Les limites de l'API ne sont pas forcément un problème dans le sens où il n'est pas nécessaire de reprendre toutes les données de l'API à chaque fois, mais seulement les updates. Il faut faire la vérification des updates (journaliers, semaines...). 

Pour faire simple, une fois avoir toutes les données, plus qu'à récupérer les updates de la base uniquement.