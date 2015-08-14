// The Naive implementation of Dijkstra's shortest Path Algorithm

var fs = require('fs');


fs.readFile('./data.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var nodes = [];
    var Xarray = [];
    var dataArray = data.split('\n');
    for(var i=0; i< dataArray.length; i++) {
      var relations = dataArray[i].trim().split(/[ ]+/);
      relations.splice(0, 1);
      nodes[i] = {
        edges: [],
        lengths: [],
        shortestPath: null,
        includedInX: false,
        nodeIndex: i+1
      };
      for(var j=0; j<relations.length; j++) {
        var edge = relations[j].split(',');

        nodes[i].edges.push(parseInt(edge[0])-1);
        nodes[i].lengths.push(parseInt(edge[1]));
      }
    }
    nodes[0].shortestPath = 0;
    nodes[0].includedInX = true;
    Xarray.push(nodes[0]); // Add the first element to X
    // nodes is an array with two arrays: one of all the edges, and one of the associated lengths of those edges
    // it also has the shortest path, which starts with null and will be filled in, and a boolean as to whether it is included in X
    // edges is an array filled with tuples => [start, end, length]
    
    // Algorithm: Loop through nodes in X, look at all the connections, pick the shortest, move that node to X, and remove it from nodes.
    // Then remove the edge from the node that is in X

    desiredIndices = [7,37,59,82,99,115,133,165,188,197];
    var shortestPathValues = DijkstrasShortest(nodes, Xarray);
    for(var i=0; i<shortestPathValues.length; i++) {
      if(desiredIndices.indexOf(shortestPathValues[i].nodeIndex) !== -1) {
        console.log('Index: '+shortestPathValues[i].nodeIndex+' ShortestPath: '+shortestPathValues[i].shortestPath);
      }
    }
  }
});

// Returns the array of nodes in X, each one flagged with the shortest path to the node.
DijkstrasShortest = function(nodes, Xarray) {
  var nodeCounter = nodes.length-1;
  while(nodeCounter > 0) {
    var shortest = {
      length: Math.pow(10, 10),
      xNode: null,
      vNode: null,
      xEdge: null
    }
    for(var i=0; i<Xarray.length; i++) {
      var xNode = Xarray[i];
      for(var j=0; j<xNode.edges.length; j++) {
        var vLength = xNode.shortestPath + xNode.lengths[j];
        // console.log(nodes[xNode.edges[j]].includedInX);
        if(nodes[xNode.edges[j]].includedInX === false && vLength < shortest.length) {
          shortest.length = vLength;
          shortest.xNode = i;
          shortest.vNode = xNode.edges[j]
          shortest.xEdge = j;
        }
      }
    }
    if(shortest.xNode === null) {
      console.log('Failure, no shortest found');
      break;
    } else {
      nodes[shortest.vNode].shortestPath = shortest.length; // Set the shortestPath of the node
      nodes[shortest.vNode].includedInX = true;
      Xarray.push(nodes[shortest.vNode]); // Remove the node from nodes and add it to the Xarray
      Xarray[shortest.xNode].edges.splice(shortest.xEdge, 1);
      Xarray[shortest.xNode].lengths.splice(shortest.xEdge, 1);
      nodeCounter--;
    }
  }
  return Xarray;
}