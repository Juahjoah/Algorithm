const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

// rl.on('line', function (line) {
//     input = line.split(' ');
// }).on('close', function () {
//     console.log(Number(input[0]));
// });


rl.on('line', function (line) {
    const n = parseInt(line.split(' ')[0], 10); // 입력 값을 정수로 변환
    const triangle = solution(n); // 삼각형 생성
    console.log(triangle); // 생성된 삼각형 출력
}).on('close', function () {
    process.exit();
});




function solution(n) {
  let answer = '';
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
      answer += '*';
    }
    answer += '\n';  
  }
  return answer;    
}