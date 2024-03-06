/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  let answer = [];
  
  function flattenDeeplyNestedArray(currentArr, currentDepth) {
    currentArr.forEach (i => {
      if (Array.isArray(i) && currentDepth > 0) {
        flattenDeeplyNestedArray(i, currentDepth - 1);
      } else {
        answer.push(i);
      }
    });
  }
    
  flattenDeeplyNestedArray(arr, n)

  return answer;
    
};

