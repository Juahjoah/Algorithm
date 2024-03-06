/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
  var inputArr = arr;
  inputArr.sort(function(a,b) {
    return fn(a) - fn(b);
  });
  return inputArr;
  
    
    
    
    
};