function solution(n) {
  let answerArr = [];
    
  for (i = 0; i <= n; i++) {
    if (i % 2 === 1) {
      answerArr.push(i)
    }
  }

  return answerArr;
}