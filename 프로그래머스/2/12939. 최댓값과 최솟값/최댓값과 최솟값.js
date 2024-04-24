
function solution(s) {
  // 문자열 공백 기준으로 분리, 숫자형으로 변환
  const inputNum = s.split(' ').map(Number); // 숫자형으로 변환해주지 않으면 문자형 변화로 확인함. = 원했던 결과와 다른 값이 나올 수 있음.
  let maxNum = inputNum[0]; // 최대값
  let minNum = inputNum[0]; // 최소값
    
  for (let i = 1; i < inputNum.length; i++) {
    if (maxNum < inputNum[i]){
      maxNum = inputNum[i];
    } 
    if (minNum > inputNum[i]) {
      minNum = inputNum[i];
    }
  }
  return `${minNum} ${maxNum}` 
    
  // 최대값 찾기
  // const maxNum = Math.max(inputNum);
  // 최소값 찾기
  // const minNum = Math.min(inputNum);
    
  // return `"${maxNum} ${minNum}"`

}