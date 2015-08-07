var fs = require('fs');
var arr;
var m = 0;
var useCase = 3;
var t1 = [7, 5, 1, 4, 8, 3, 10, 2, 6, 9];
var t2 = [8, 10, 1, 9, 7, 2, 6, 3, 5, 4];

fs.readFile('./quicksort-input.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var dataArray = data.split('\n');
    for(var i=0; i< dataArray.length; i++) {
      dataArray[i] = parseInt(dataArray[i]);
    }
    arr = dataArray;
    var index = partition(0, arr.length-1);
    m += arr.length - 1;
    quicksortAndCount(0, index, arr.length-1);
    // console.log(arr);
    console.log(m);
  }
});

// var partition = function(l, r) {
//   var p = arr[l];
//   var i = l + 1;
//   var oneSmaller = false;
//   for(var j=l+1; j <= r; j++) {
//     if(arr[j] < p) {
//       swap(i, j);
//       i++;
//       oneSmaller = true;
//     }
//   }
//   if(oneSmaller) {
//     swap(l, i-1);
//   }
//   return i-1;
//   function swap(a, b) {
//     var temp = arr[b];
//     arr[b] = arr[a];
//     arr[a] = temp; 
//   }
// }

var partition = function(l, r) {
  setPivotIndex(l, r);
  var p = arr[l];
  var i = l + 1;
  var oneSmaller = false;
  for(var j=l+1; j <= r; j++) {
    if(arr[j] < p) {
      swap(i, j);
      i++;
      oneSmaller = true;
    }
  }
  if(oneSmaller) {
    swap(l, i-1);
  }
  return i-1;
  function swap(a, b) {
    var temp = arr[b];
    arr[b] = arr[a];
    arr[a] = temp; 
  }
}

// var partition = function(l, r) {
//   setPivotIndex(l, r);
//   p = arr[l];
//   swap(l, pIndex);
//   var i = l + 1;
//   var oneSmaller = false;
//   for(var j=l+1; j <= r; j++) {
//     if(arr[j] < p) {
//       swap(i, j);
//       i++;
//       oneSmaller = true;
//     }
//   }
//   if(oneSmaller) {
//     swap(l, i-1);
//   }
//   return i-1;
//   function swap(a, b) {
//     var temp = arr[b];
//     arr[b] = arr[a];
//     arr[a] = temp; 
//   }
// }

var quicksortAndCount = function(l, index, r) {
  if(index-l-1 >= 1) {
    var i1 = partition(l, index-1);
    m += index-l-1;
    quicksortAndCount(l, i1, index-1);
  }
  if(r-index+1 > 1) {
    m += r-(index+1);
    var i2 = partition(index+1, r);
    quicksortAndCount(index+1, i2, r);
  }
  return;
}

var setPivotIndex = function(l, r) {
  if(useCase === 1) {
    return;
  } else if(useCase === 2) {
    swap(l, r);
  } else if(useCase === 3) {
    var medianIndex = l + Math.floor((r-l)/2);
    var tempArr = [l, medianIndex, r].sort(function(a, b) {
      return arr[b] - arr[a];
    });
    swap(tempArr[1], l);
  }
}

var swap = function(a, b) {
  var temp = arr[b];
  arr[b] = arr[a];
  arr[a] = temp; 
}