/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
  let cancelled = false;
  const result = [];

  setTimeout(() => {
    if (!cancelled) {
      const start = performance.now();
      const returnValue = fn(...args);
      const timeTaken = Math.floor(performance.now() - start);
      result.push({ "time": timeTaken, "returned": returnValue });
      console.log(result); // 실행 결과 로그 출력
    }
  }, t);

  return function cancel() {
    cancelled = true; // 함수 실행 취소
  };
    
};

/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */