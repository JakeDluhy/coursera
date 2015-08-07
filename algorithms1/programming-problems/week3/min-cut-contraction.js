var fs = require('fs');
var rand = require('random-seed').create();

fs.readFile('./min-cut-contraction.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var nodes = [];
    var edges = [];
    var n;
    var minCut = 200;

    var nodesArray = data.split('\n');
    n = nodesArray.length;
    for(var i=0; i< nodesArray.length; i++) {
      var relations = nodesArray[i].split(/[ ]+/);
      relations.splice(0, 1);
      nodes[i] = [];
      for(var j=0; j<relations.length; j++) {
        nodes[i].push(relations[j]-1);
        if(relations[j] > i) {
          edges.push([i, relations[j]-1]);
        }
      }
    }
    var seedString = '0';

    // for(var k=0; k<(n*n); k++) {
    //   rand.seed(seedString);
      var newMin = minCutContraction(nodes, edges);
      console.log(newMin);
    //   console.log(newMin);
    //   if(newMin < minCut) {
    //     minCut = newMin;
    //   }
    //   seedString = 'a' * Math.floor(k/250);
    // }

    // console.log(minCut);
  }
});


minCutContraction = function(nodes, edges) {
  var nodesLength = nodes.length
  while(nodesLength > 2) {
    var indexOf = Math.floor(Math.random()*edges.length);
    var edge = edges[indexOf];
    var node1Index = edge[0];
    var node2Index = edge[1];
    if(node1Index > node2Index) {
      node1Index = node2Index;
      node2Index = edge[0];
    }
    var node1 = nodes[node1Index];
    var node2 = nodes[node2Index];
    var node3 = [];
    for(var i=0; i<node1.length; i++) {
      if(node1[i] !== node1Index && node1[i] !== node2Index) {
        node3.push(node1[i]);
      }
    }
    for(var j=0; j<node2.length; j++) {
      if(node2[j] !== node1Index && node2[j] !== node2Index) {
        node3.push(node2[j]);
      }
    }
    nodes.splice(node1Index, 1, node3);
    nodes.splice(node2Index, 1);
    for(var i=0; i<nodes.length; i++) {
      var relations = nodes[i];
      for(var k=0; k<relations.length; k++) {
        if(relations[k] === node2Index) {
          relations[k] = node1Index;
        } else if(relations[k] > node2Index) {
          relations[k] --;
        }
      }
      nodes[i] = relations;
    }

    for(var j=0; j<edges.length; j++) {
      if((edges[j][0] === node1Index && edges[j][1] === node2Index) || (edges[j][1] === node1Index && edges[j][0] === node2Index)) {
        edges.splice(j, 1);
        j--;
        continue;
      } else if(edges[j][0] === node2Index) {
        edges[j][0] = node1Index;
      } else if(edges[j][1] === node2Index) {
        edges[j][1] = node1Index;
      }
      if(edges[j][0] > node2Index) {
        edges[j][0]--;
      }
      if(edges[j][1] > node2Index) {
        edges[j][1]--;
      }
      if(edges[j][0] === edges[j][1]) {
        edges.splice(j,1);
        j--;
      }
    }

    nodesLength--;
    
  }
  return edges.length;
}

deleteMergedNodes = function(relations, node1Index, node2Index) {
  var iO = relations.indexOf(node2Index);
  while(iO !== -1) {
    relations.splice(iO, 1, node1Index);
    iO = relations.indexOf(node2Index);
  }
  return relations;
}