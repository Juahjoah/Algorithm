/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
  let answer = {};

  this.forEach((i) =>{
    const key = fn(i);
    if (answer[key]) {
      answer[key].push(i);
    } else {
      answer[key] = [i];
    }
  });
  return answer;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */