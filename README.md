# vresutils Package

collects various small helpers, which make your programming life
easier (or arguably harder, as long you still have to figure out, how
to use them).

**Unfortunately we do not have the resources to provide any support
for this library. Feel inspired, file bug reports for broken bits or
better yet pull requests, but please do not ask for help, sorry!**

## Configuration

A simple configuration file `~/.vresutils.config` allows to configure
several data related paths:
```python
# data directory
data_dir = "<path to data discussed in the data section>"

# caching (functions decorated with @cachable persist their results in some directory)
cache_dir = "<path to writable empty directory>"

# entsoetransparency url (fill in the blanks from [13])
entsoeftp = 'ftp://<username>:<password>@<hostname>/export/export/'
```

The `reatlas` module expects a configuration file `~/.reatlas.config`:
```python
hostname = '<hostname with a running Aarhus Renewable Energy Atlas server>'
username = '<username>'
password = '<password>'
notify = False
```

## Required data

Expected to be found below the data sub-directory.

### landuse

    Natura2000/Natura2000_end2016.* :
        Natura 2000 GIS data - the European network of protected sites [11]
        As a shapefile.

    corine/g250_clc06_V18_5.* :
        Corine Land Cover (CLC) 2012, Version 18.5.1 [12]
        250m or 100m raster data.

### hydro

    Hydro_Inflow :
        Results from the RESTORE 2050 project (private communication, sorry!)

### shapes

    germany.npy :
        German outline as sequence of points, again, extracted from vg250.

    vg250 :
        Geometry of various German divisions, for example Landkreise and
        Länder The geometry of these Landkreise must be available as
        shapefiles at data/vg250 in the UTM32 projection, they are
        available from the Bundesamt für Kartographie and Geodäsie at [1].

    ne_10m_admin_countries :
        Worldwide country shapes from naturalearthdata.com [2]

    World_EEZ :
        World wide Exclusive Economic Zones from marineregions.org [10], i.e. VLIZ (2014)

    NUTS_2010_60M_SH :
        EU shapes from Eurostat [3]

    plz-gebiete :
        The german postcode areas obtained from [4], based on OSM

### grid

    links_de_power_150601.csv, vertices_de_power_150601.csv :
        For graph.read_scigrid the data csv files available at [5] must be
        present.

    entsoe_2009_final.gpickle :
        An networkx representation of the network published by Bialek
        at [6] with approximate geographical coordinates.

### dispatch

    Kraftwerksliste_CSV_deCP850ed.csv :
        A list of the German powerplants as published by BNetzA at [7].
        The encoding of the CSV on their page is originally compatible to
        CP850 and has to be reencoded to UTF-8 (using recode f.ex.).

    global_energy_observatory_power_plants.sqlite :
        An sqlite dump of the http://globalenergyobservatory.org/ page
        scraped using [8].

    nrg_113a.xls :
        Extracted Eurostat dataset of the Electrical backup capacity per
        European country in the years 2012/13 from [9].

## License

Copyright 2015-2017 Frankfurt Institute for Advanced Studies

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Footnotes

[1] http://www.geodatenzentrum.de/geodaten/gdz_rahmen.gdz_div?gdz_spr=deu&gdz_akt_zeile=5&gdz_anz_zeile=1&gdz_unt_zeile=14&gdz_user_id=0

[2] http://www.naturalearthdata.com/downloads/10m-cultural-vectors/
(Admin 0 - Countries)

[3] http://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units

[4] http://www.suche-postleitzahl.org/downloads

[5] http://www.scigrid.de/pages/downloads.html

[6] http://www.powerworld.com/bialek

[7] http://www.bundesnetzagentur.de/DE/Sachgebiete/ElektrizitaetundGas/Unternehmen_Institutionen/Versorgungssicherheit/Erzeugungskapazitaeten/Kraftwerksliste/kraftwerksliste-node.html

[8] https://morph.io/coroa/global_energy_observatory_power_plants

[9] http://ec.europa.eu/eurostat/product?code=nrg_113a&mode=view

[10] http://www.marineregions.org/downloads.php (World EEZ v8, Low res)

[11] https://www.eea.europa.eu/data-and-maps/data/natura-8#tab-gis-data

[12] http://land.copernicus.eu/pan-european/corine-land-cover/clc-2012/

[13] https://entsoe.zendesk.com/hc/en-us/articles/115000173266-Overview-of-data-download-options-on-Transparency-Platform
