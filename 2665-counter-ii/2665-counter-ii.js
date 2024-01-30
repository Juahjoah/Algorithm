/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let answer = init;
  
  return {
    increment: function() {
      return answer += 1;
    },
    decrement: function() {
      return answer -= 1;
    },    
    reset: function() {   
      return answer = init;
    }
  }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */