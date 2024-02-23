function solution(n, k) {
    // var answer = 0;
    // return answer;
  // var drinkCount = 0
  // if (n >= 10) {
    // let drinkService = n % 10
    // let drinkService = parseInt(n / 10)
    // drinkCount = k - drinkService
  // }
  // return 12000*n + 2000*drinkCount
  var drinkService = parseInt(n / 10); 
  var drinkCount = k - drinkService; 
  if (drinkCount < 0) {
    drinkCount = 0; 
  }
  return 12000 * n + 2000 * drinkCount;   
    
    
    
}