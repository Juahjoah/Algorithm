/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let delayTimeOut;
  return function (...args) {
    clearTimeout(delayTimeOut);
    delayTimeOut = setTimeout(() => {
      fn(...args);
    }, t);
  };
};


/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */