/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
  this.arr = nums;
    
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
  // 합 계산하기
  this.value = this.arr.reduce((arr, cur)=> arr+cur, 0)
  return this.value
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
  // 문자열로 반환하기
  return `[${this.arr.join(",")}]`
    
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */