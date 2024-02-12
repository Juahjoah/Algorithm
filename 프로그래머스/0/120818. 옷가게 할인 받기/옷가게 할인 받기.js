function solution(price) {
  // var answer = 0;
  
  if (price >= 500000) {
    return parseInt(0.8 * price);
  } else if (price >= 300000) {
    return parseInt(0.9 * price);
  } else if (price >= 100000) {
    return parseInt(0.95 * price);
  } 
    return price;
    
}