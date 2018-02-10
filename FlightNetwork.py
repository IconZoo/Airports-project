# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:49:47 2015

@author: mark_kamper
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

#Fetching airport positions and fligth routes
network = open('airports.txt')
flightRoutes  = open('routes.txt')
#Fetching airport names and their location - (lat, lon)
airNames = []
lats = []
lons = []
for line in network:
    #Each line corrosponds to a seperate airport
    line = line.split(",")
    if line[4] == '""':
        pass
    
    # Dataset requires this
    else:
        airNames.append(line[4].replace('"',''))
        if len(line) == 12:
            lats.append(float(line[6]))
            lons.append(float(line[7]))
        elif len(line) == 13:
            lats.append(float(line[7]))
            lons.append(float(line[8]))
            
#Getting each route
routes = []
for line in flightRoutes:
    line = line.split(',')
    # The data of interest is stored as the third and fourth element of line
    routes.append((line[2], line[4]))
    del line
#Deleting element of initialization
del routes[0]

#Initially we add the edges to the network
flightMap = nx.DiGraph()
flightMap.add_edges_from(routes)


#Then we check which airports we have position data and removing the rest:
place_holder = list(flightMap.nodes())
for node in place_holder:
    pass    
    if node not in airNames:
        flightMap.remove_node(node) 
        
pageRank = nx.pagerank(flightMap, alpha = 1)
pageMax = max(pageRank, key = pageRank.get)

#Next we initialize the basemap:
plt.figure(figsize = (12,6))
WorldMap = Basemap(projection = 'robin', lon_0 = 0, resolution = 'c')
WorldMap.drawcountries()
WorldMap.drawstates()
WorldMap.fillcontinents(color = 'green')
# WorldMap.filloceans(color = "blue")

# Then we store the position data as lon/lat
mx , my  =  WorldMap(lons,lats)


# Creating dictonary of positions

pos={}
label = {}
colors = {}
for i in range(len(airNames)):
    pos[airNames[i]] = (mx[i], my[i]) 
    label[airNames[i]] = ""
    colors[airNames[i]] = 'blue'
#Making sure plt is a figure to enable size regulation

nx.draw_networkx(flightMap,node_size = 1 ,pos = pos, node_color = 'red', edge_size = 0.01, edge_color = 'blue')
plt.title('Airport network')
plt.show()
