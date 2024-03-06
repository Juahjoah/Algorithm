/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const answerArr = [];
    for (let i = 0; i < arr.length; i++) {
      if(fn(arr[i], i)) answerArr.push(arr[i])    
    }
    return answerArr;
};