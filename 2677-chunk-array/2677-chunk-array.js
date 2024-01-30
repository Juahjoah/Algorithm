/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
    
var chunk = function(arr, size) {
  let answer = [];
  let index = 0;
  
    while (index < arr.length) {
      answer.push(arr.slice(index, size + index))
      index += size
    }
  return answer  
};








