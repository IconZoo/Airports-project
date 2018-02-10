# Airports-project
Pagerank on the worlds airtravel networks


This project simply uses data of the airnetworks to initialize an (for now) undirected graph.
The standard pagerank (networkx's implementation) is then applied to the graph to estimate the relative importance of the different airports.


For fun the basemap toolkit is then used to plot the positions of the airports onto a world map.

The data is found in the "airports.txt" and "routes.txt" files respectively.
