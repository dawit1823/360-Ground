def shortestRoute(buildings[{"A",10},{"B",15},{"C",20}], startingBuilding: buildings[0]) ->{ 
        # Find the shortest path from the starting building to each of the other buildings. 
    var shortestPath = null; 
        for (building in buildings) {
             if (building.location == startingBuilding) {
                 shortestPath = building; 
                 }
                  } 
                 return shortestPath; 
                 }