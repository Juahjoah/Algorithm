function solution(s){
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack[stack.length - 1] === '(' && s[i] === ')') {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }

  // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
  // console.log('Hello Javascript')

  return !stack.length
}