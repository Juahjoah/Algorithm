/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  return Promise.all ([promise1, promise2]).then(values => {
    const sum = values[0] + values[1];
      
    return sum;
  });
    
    
    
//   try {
//     const value1 = await promise1;
//     const value2 = await promise2;
      
//     return value1 + value2
//   } 
//   catch(error) {
//     throw error;
//   }
    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */