function solution(numbers, num1, num2) {
  var answer = [];
  for (i = num1; i <= num2; i++) {
    answer.push(numbers[i])
  }
  return answer;
}