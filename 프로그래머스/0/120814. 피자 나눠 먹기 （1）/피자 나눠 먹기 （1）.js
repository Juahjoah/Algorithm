function solution(n) {
  let answer = 0;
  if (n > 7) {
    let pizzaNum = 0;
    pizzaNum = Math.ceil(n / 7);
    answer = pizzaNum;
  } else {
    answer = 1;
  }
    
  return answer;
}