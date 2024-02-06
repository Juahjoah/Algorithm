/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  try {
    const value1 = await promise1;
    const value2 = await promise2;
      
    return value1 + value2
  } 
  catch(error) {
    throw error;
  }
    
    
    
  
//   let newMyPromies = new Promise ((resolve, result) => {
//     setTimeout(() => resolve("완료"), 1000);
    
//     return promise1 + promise2
      
//   });
  
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */