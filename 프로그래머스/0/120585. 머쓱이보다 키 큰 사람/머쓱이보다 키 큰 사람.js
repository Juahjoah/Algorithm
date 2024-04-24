function solution(array, height) {
  let answer = 0;
  for (i=0; i <= array.length; i++) {
    if (array[i] > height) {
      answer += 1
    }
  }
  return answer;
}