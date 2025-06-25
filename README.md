# Purpose of this repository

The aim is to process the data from the ROR api, to extract it in json form, and then process it using sema.subyt to go from json to rdf.

## api ror.org address

```
    https://api.ror.org/organizations // all the organizations
    https://api.ror.org/organizations?query=vliz // for vliz
```

## Limite of API

It is not possible to retrieve all company data via the ror.org API; you have to go through this site, which is specific to ror, to access it. So that's how we're going to populate the first database with all the organisations' information:

```
    https://zenodo.org/records/15475023
```

If you go to the ror documentation, it's clearly explained that there are limits to the use of the api.

![Limit of data](/assets/limit.png "Limit of data")

What's more, as I don't have access to all the data from the API, and there is no jsonld format in the documents that can be downloaded from ror.org, I'm not able to compare json and jsonld formats, or even jsonld and rdf.

## Next step

The limits of the API are not necessarily a problem in the sense that it is not necessary to take all the data from the API each time, but only the updates. You need to check the updates (daily, weekly, etc.).

To put it simply, once all the data has been retrieved, all you have to do is retrieve the database updates only, on a daily basis, or in the way they do it.

## Updates

There are several possible methods for acquiring the various database updates. 

1- In the first instance, as soon as changes are added or additions are made to the database, there is a release on github :

```
    https://github.com/ror-community/ror-updates/releases
```

There is a summary of the changes, the number of organisations added, the number of organisations modified and the complete list of organisations added and modified.

2- Secondly, it is possible to retrieve the entire database with all the changes and additions:

```
    https://zenodo.org/communities/ror-data/records?q=&l=list&p=1&s=10&sort=newest
```

As far as the number of updates is concerned, there is **at least one**, but often there are **more like two** per month.

![Update of data](/assets/update.png "Update of data")

### Potential problems & solutions

According to several tests and research, it seems unlikely that the API will be used to retrieve new updates. In fact, there is a “last_modified” parameter, but it would not be possible to look at this parameter for each organisation, for the same reason as data retrieval, which is limited to 10,000 organisations.

The most likely solution for retrieving these updates would be to go through the github, which provides all the changes and additions made by the organisations.

It would also be possible to dump the entire database, and then compare it with the one we had, but given the amount of data, that seems complicated.

## Test API

https://api.ror.org/v2/organizations?query.advanced=admin.last_modified.date:%5B2025-05-01%20TO%202025-05-16%5D&all_status // entre les dates des dernières releases (01 mai 2O25 - 16 mai 2025).

=> 763 diff according to the api whereas normally (github), there are 172 added and 241 added != 763 in the end.

## Use of subyt

First of all, to access the sema.subyt library, you need to follow these steps:

```
python -m venv venv // creating a python environment
source venv/Scripts/activate // activate the new environment
touch requirements.txt // create a text file
git+https://github.com/vliz-be-opsci/py-sema.git // to be placed in the file previously created
pip install -r requirements.txt // installing the subyt library
```

Then to check the correct installation:

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
This should not be displayed in red if the installations were working properly.

Instead, another approach has been discussed and used. Here is the code:

```
from sema.subyt import Subyt

Subyt(
    template_name="template.ttl",
    template_folder=str(Path(template_path).parent),
    sink=str(Path(output_path).resolve()),
    extra_sources={"qres": str(Path(json_path).resolve())},
).process()
```

It's the use of the subyt class that saves us many of the steps directly carried out by the class itself.
