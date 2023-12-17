En aqesut directori hi ha varis scripts de python que ens han permès fer les gràfiques i tractar les dades.

Tots es basen en obrir el fitxer .csv on hi ha el dataset, fer clusters i observar els resultats.

`4clustersFamily.py`  fa 4 clusters amb el mètode Agglomerative clustering i mostra una representació geràrquica (Dendrograma) de tots els pacients. I s'observa que hi ha un cluster de 2 pacients infèrtils que són molt disjunts a la resta.

`clustering.py` fa clusters amb el mètode DBSCAN clustering i mostra quins pacients s'hi troben dins.

`correlation_matrix.py` al final del codi, s'ha d'especificar si es vol PHYLUM, FAMILY o GENUS i crea la matriu de correlació que es pot indicar si es de només pacients de UAB o CON on està el: crea_mat_corr(   ,al segon parametre).

`grafGran4KFamily.py` mostra dins de un cluster de 2 pacients infèrtils de family, la relació entre els microbiotes.

`k2UABgraf_family.py` mostra dins de family la relació entre les microbiotes més relacionats entre ells, centrant-se en un cluster de 2 pacients infèrtils.
En aqesut directori hi ha varis scripts de python que ens han permès fer les gràfiques i tractar les dades.

Tots es basen en obrir el fitxer .csv on hi ha el dataset, fer clusters i observar els resultats.

`4clustersFamily.py`  fa 4 clusters amb el mètode Agglomerative clustering i mostra una representació geràrquica (Dendrograma) de tots els pacients. I s'observa que hi ha un cluster de 2 pacients infèrtils que són molt disjunts a la resta.

`clustering.py` fa clusters amb el mètode DBSCAN clustering i mostra quins pacients s'hi troben dins.

`correlation_matrix.py` al final del codi, s'ha d'especificar si es vol PHYLUM, FAMILY o GENUS i crea la matriu de correlació que es pot indicar si es de només pacients de UAB o CON on està el: crea_mat_corr(   ,al segon parametre).

`grafGran4KFamily.py` mostra dins de un cluster de 2 pacients infèrtils de family, la relació entre els microbiotes.

`k2UABgraf_family.py` mostra dins de family la relació entre les microbiotes més relacionats entre ells, centrant-se en un cluster de 2 pacients infèrtils.

`kmeans_clustering.py` construeix un model de 4 clusters amb mètode KMeans i dona la seva representació en 2 dimensions. Els resultats no son plausibles donada la naturalesa de la tècnica KMeans, i la distribució de les dades en el csv donat.

