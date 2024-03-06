/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
  // Promise 에 대한 문제
  // return millis
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(millis);      
      }, millis);  
  });
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

