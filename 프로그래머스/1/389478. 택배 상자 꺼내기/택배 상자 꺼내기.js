function solution(n, w, num) {
    let answer = 0;
    
    let row = Math.floor((num - 1) / w);
    let col;
    
    if (row % 2 === 0) {
        col = (num - 1) % w
    } else {
        col = w - 1 - ((num - 1) % w)
    }
    
    // 본인의 열보다 위에 있는 상자의 갯수를 세기
    for (let r = row + 1; r < Math.ceil(n / w); r++) {
        let boxIdx;
        if (r % 2 === 0) {
            boxIdx = r * w + (col + 1);
        } else {
            boxIdx = (r + 1) * w - col;
        }
        
        if (boxIdx <= n) {
            answer += 1;
        }
    }
    
    // 본인 값 더해서 출력
    return answer + 1;
}