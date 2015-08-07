// Need to run using /bin/bash -c "ulimit -s 65500; exec /usr/local/bin/node --stack-size=65500 compute-scc.js" from the same directory
// This increases the stack size to allow for the necessary recursion

var fs = require('fs');
var nodesArray = [];
var secondPassArray = [];
var finishingCounter = 0;
var sccCounter = 0;
var sccArray = [0,0,0,0,0];

fs.readFile('./SCC.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var edgesArray = data.split('\n');
    for(var i=0; i< edgesArray.length; i++) {
      var fromTo = edgesArray[i].split(/[ ]+/);
      var from = parseInt(fromTo[0])-1;
      var to = parseInt(fromTo[1])-1;
      if(nodesArray[from] === undefined) { nodesArray[from] = {index: 0, outgoing: [], reversedOutgoing: [], passedReverse: false, finishingTime: 0, passedForward: false}; }
      if(nodesArray[to] === undefined) { nodesArray[to] = {index: 0, outgoing: [], reversedOutgoing: [], passedReverse: false, finishingTime: 0, passedForward: false}; }
      nodesArray[from].outgoing.push(to);
      nodesArray[from].index = from;
      nodesArray[to].reversedOutgoing.push(from);
      nodesArray[to].index = to;
    }
    console.log(nodesArray.length);
    DFSLoop(true);
    DFSLoop(false);
    console.log(sccArray);
  }
});

DFSLoop = function(reverse) {
  var passedKey = (reverse ? 'passedReverse' : 'passedForward');
  var useArray = (reverse ? nodesArray : secondPassArray);
  for(var i=(useArray.length-1); i>=0; i--) {
    if(useArray[i] !== undefined && useArray[i][passedKey] === false) {
      if(!reverse) {sccCounter = 0;}
      DFS(useArray[i].index, reverse);
      if(!reverse) { allocatePlacement(sccCounter); }
    }
  }
}

DFS = function(nodeIndex, reverse) {
  if(nodesArray[nodeIndex] !== undefined) {
    if(reverse) {
      var outgoingKey = 'reversedOutgoing';
      var passedKey = 'passedReverse';
    } else {
      var outgoingKey = 'outgoing';
      var passedKey = 'passedForward';
    }
    nodesArray[nodeIndex][passedKey] = true;
    var outgoingNodes = nodesArray[nodeIndex][outgoingKey];
    for(var i=0; i<outgoingNodes.length; i++) {
      if(nodesArray[outgoingNodes[i]] !== undefined && nodesArray[outgoingNodes[i]][passedKey] === false) {
        DFS(outgoingNodes[i], reverse);
      }
    }
    if(reverse) {
      nodesArray[nodeIndex].finishingTime = finishingCounter;
      secondPassArray[finishingCounter] = nodesArray[nodeIndex];
      finishingCounter++;
    } else {
      sccCounter++;
    }
  }
}

allocatePlacement = function(counter) {
  sccArray.push(counter);
  sccArray.sort(function(a,b) {
    return parseInt(b)-parseInt(a);
  });
  sccArray.pop();
}