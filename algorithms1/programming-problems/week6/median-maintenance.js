// run npm install heap to get the heap node module

var fs = require('fs');
var Heap = require('heap');
var maxHeap = new Heap(function(a,b) {
  return b - a;
});
var minHeap = new Heap();


fs.readFile('./median-maintenance-data.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var dataArray = data.split('\n');
    var median = parseInt(dataArray[0]);
    var medianSum = median;
    maxHeap.push(median);
    for(var i=1; i< dataArray.length; i++) {
      var x = parseInt(dataArray[i]);
      if(maxHeap.size() > minHeap.size()) {
        if(x < median) {
          maxHeap.push(x);
          var poper = maxHeap.pop();
          minHeap.push(poper);
          median = maxHeap.peek();
        } else {
          minHeap.push(x);
          // median stays the same
        }
      } else if(minHeap.size() > maxHeap.size()) {
        if(x > median) {
          minHeap.push(x);
          var poper = minHeap.pop();
          maxHeap.push(poper);
        } else {
          maxHeap.push(x);
        }
        median = maxHeap.peek();
      } else {
        if(x <= median) {
          maxHeap.push(x);
          // median stays the same
        } else {
          minHeap.push(x);
          median = minHeap.peek();
        }
      }
      medianSum += median;
    }
    console.log('Median sum mod 10000 = ');
    var result = medianSum%10000;
    console.log(result);
  }
});