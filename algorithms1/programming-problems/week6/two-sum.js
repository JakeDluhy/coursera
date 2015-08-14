// For this application, and this dataset, the two sum algorithm given in class was painfully slow. I have implemented
// one found that takes the subarray of possible combinations and then makes the comparisons.

var fs = require('fs');
var dataArray;

fs.readFile('./two-sum-data.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var tHash = {};
    dataArray = data.split('\n');
    dataArray.sort(function(a,b) {
      return parseInt(a) - parseInt(b);
    });
    for(var i=0; i<dataArray.length; i++) {
      if(!(i%10000)) { console.log(i); }
      var x = parseInt(dataArray[i]);
      var start = bisectSearch(-10000-x, 0, dataArray.length-1, true);
      var end = bisectSearch(10000-x, 0, dataArray.length-1, false);
      var yCands = dataArray.slice(start, end+1);
      for(var j=0; j<yCands.length; j++) {
        var t = x + parseInt(yCands[j]);
        if(t >= -10000 && t <= 10000) {
          tHash[t] = true;
        }
        
      }
    }
    console.log('Number of unique additions: ');
    console.log(Object.keys(tHash).length);
  }
});

bisectSearch = function(val, start, end, lower) {
  val = parseInt(val);
  start = parseInt(start);
  end = parseInt(end);
  if(end-start === 1) {
    if(lower) {
      return start;
    } else {
      return end;
    }
  }
  var middle = Math.floor((end+start)/2);
  if(dataArray[middle] === val) {
    return middle
  } else if(val < dataArray[middle]) {
    return bisectSearch(val, start, middle);
  } else if(val > dataArray[middle]) {
    return bisectSearch(val, middle, end);
  } else {
    console.log('error');
  }
}