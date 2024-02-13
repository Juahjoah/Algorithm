function solution(money) {
  let answerArr = [0, 0]; 
  if (money >= 5500) {
    let n = Math.floor(money/5500);  
    answerArr[0] = n;
    answerArr[1] = money - 5500*n;
    
    return answerArr;
      
  } else {
    return [0, money];
  }
    
};