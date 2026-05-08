function solution(n, w, num) {
    let answer = 0;
    
    const boxList = [];
    let flagBoxList = [];
    let flag = true;
    
    for (let i = 1; i <= n; i++) {
        flagBoxList.push(i);
        
        if (flagBoxList.length === w) {
            if (!flag) {
                flagBoxList.reverse();
            }
            
            boxList.push(flagBoxList);
            flag = !flag
            flagBoxList = [];
        }
    }
    
    // 마지막 줄이 w개 미만으로 남은 경우
    if (flagBoxList.length > 0) {
        const listLength = flagBoxList.length;
        
        if (flag) {
            while (flagBoxList.length < w) {
                flagBoxList.push(0);
            }
            boxList.push(flagBoxList);
        } else {
            flagBoxList.reverse();
            const finalRow = Array(w - listLength).fill(0).concat(flagBoxList);
            boxList.push(finalRow);
        }
    }

    // num의 위치 찾기
    let targetRow = 0;
    let targetCol = 0;
    
    for (let r = 0; r < boxList.length; r++) {
        const col = boxList[r].indexOf(num);
        
        if (col !== -1) {
            targetRow = r;
            targetCol = col;
            break;
        }
    }
    
    // 같은 열에 있는 상자 개수 세기
    for (let r = targetRow; r < boxList.length; r++ ) {
        if (boxList[r][targetCol] !== 0) {
            answer++;
        }
    }
    
    return answer;
}