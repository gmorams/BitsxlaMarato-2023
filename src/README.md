En aqesut directori hi ha vais scripts de python que ens han permès fer les gràfiques i tractar les dades.

Tots es basen en obrir el fitxer .csv on hi ha el dataset, fer clusters i observar els resultats.

`4clustersFamily.py`  fa 4 clusters amb el mètode Agglomerative clustering i mostra una representació geràrquica (Dendrograma) de tots els pacients. I s'observa que hi ha un cluster de 2 pacients infèrtils que son molt disjunts a la resta.

`clustering.py` fa clusters amb el mètode DBSCAN clustering i mostra quins pacients s'hi troben dins.

`correlation_matrix.py` al final del codi, s'ha d'especificar si es vol PHYLUM, FAMILY o GENUS i crea la matriu de correlacio que es pot indicar si es de només pacients de UAB o CON on esta el: crea_mat_corr(   ,al segon parametre).

`grafGran4KFamily.py` mostra dins de un cluster de 2 pacients infèrtils de family, la relació entre els microbiotes.

`k2UABgraf_family.py` mostra dins de family la relació entre els microbiotes més relacionats entre ells, centrant-se en un cluster de 2 pacients infertils.
