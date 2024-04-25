function solution(A,B){
  let answer = 0;
  
  // A와 B를 역순으로 따져서 서로 곱해주면 각각 최소 곱을 구할 수 있음.
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  // console.log(A, B)

  for (let i = 0; i < A.length; i++) {
    answer += A[i] * B[i];
  }
  return answer;
}
