/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
  if (functions.length === 0) {
    return function(x) {
      return x
    }
  } else {
    return function(x) {
      let answer = x;
      for (let i = functions.length - 1; i >= 0; i--) {
        answer = functions[i](answer)
      }
      return answer;     
    }
  }
};




/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
