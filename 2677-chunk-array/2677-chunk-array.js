/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */

var chunk = function (arr, size) {
  if (!arr.length) return [];
  if (size >= arr.length) return [arr];
  const answer = [];

  let tempArr = [];
  arr.forEach((item, idx) => {
    tempArr.push(item);
    if ((idx + 1) % size === 0) {
      answer.push([...tempArr]);
      tempArr = [];
    }
  });

  if (tempArr.length) answer.push(tempArr);

  return answer;
};


    
// var chunk = function(arr, size) {
//   let answer = [];
//   let index = 0;
  
//     while (index < arr.length) {
//       answer.push(arr.slice(index, size + index))
//       index += size
//     }
//   return answer  
// };








