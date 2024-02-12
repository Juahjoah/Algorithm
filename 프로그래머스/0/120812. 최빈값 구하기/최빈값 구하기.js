function solution(array) {
  let answerMap = new Map();
  
  array.forEach(i => {
    answerMap.set(i, (answerMap.get(i) || 0) + 1);
  })
  let maxNum = 0;
  let answer = null;  
  
  answerMap.forEach((count, i) => {
    if (count > maxNum) {
      maxNum = count;
      answer = i;
    } else if (count === maxNum) {
      answer = -1;
    }
  });
  
  if (answer === null ) {
    return array[0];
  }  
  return answer;
}
