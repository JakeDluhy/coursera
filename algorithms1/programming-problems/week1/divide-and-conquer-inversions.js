fs = require('fs');

fs.readFile('./divide-and-conquer-array.txt', 'utf8', function(err, data) {
  if(err) {
    console.log(err);
  } else {
    var dataArray = data.split('\n');
    for(var i=0; i< dataArray.length; i++) {
      dataArray[i] = parseInt(dataArray[i]);
    }
    var result = sortAndCount(dataArray);
    console.log(result);
  }
});

// dataArray = [1,3,5,2,4,6];



// sortAndCount returns an object with keys array and count corresponding to the sorted array and the inversion count
function sortAndCount(array) {
  var length = array.length;
  if(length === 1) {
    return {"array": array, "count": 0};
  }
  var firstHalf = array.slice(0, length/2);
  var secondHalf = array.slice(length/2, length);

  var firstResults = sortAndCount(firstHalf);
  var secondResults = sortAndCount(secondHalf);

  var firstSorted = firstResults.array;
  var secondSorted = secondResults.array;

  var mergedResults = mergeArrays(firstSorted, secondSorted);
  mergedResults.count += firstResults.count + secondResults.count;
  return mergedResults;
}

// Returns the two arrays merged as object with key array, along with the count of the split inversions
function mergeArrays(fArray, sArray) {
  var comboLength = fArray.length + sArray.length;
  var comboArray = [];
  var i=0, j=0, inversions = 0;
  for(var k=0; k<comboLength; k++) {
    if(i >= fArray.length) {
      comboArray = comboArray.concat(sArray.slice(j, sArray.length));
      break;
    }
    if(j >= sArray.length) {
      comboArray = comboArray.concat(fArray.slice(i, fArray.length));
      break;
    }

    if(fArray[i] <= sArray[j]) {
      comboArray[k] = fArray[i];
      i++;
    } else {
      comboArray[k] = sArray[j];
      j++;
      inversions += (fArray.length - i);
    }
  }
  return {"array": comboArray, "count": inversions};
}