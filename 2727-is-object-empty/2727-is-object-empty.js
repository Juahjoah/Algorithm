/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
  // 1
  // return Object.keys(obj).length === 0;  
  
  for (let i in obj) {
    return false;
  }  
  return true;  
    
  // if (!obj) {
  //   return true
  // }
  //   return false
};