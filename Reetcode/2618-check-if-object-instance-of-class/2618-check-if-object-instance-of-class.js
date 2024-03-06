/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
  if ((typeof obj === 'number' && classFunction === Number) ||
     (typeof obj === 'string' && classFunction === String) ||
     (typeof obj === 'boolean' && classFunction === Boolean)) {
    return true;
  }
  while(obj!=null) {
    if(obj.constructor === classFunction) {
      return true;
    }
    obj = Object.getPrototypeOf(obj);
    }
  return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
