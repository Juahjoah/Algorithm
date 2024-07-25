function solution(n, k, cmd) {
    let answer = Array(n).fill('O');
    let removedStack = [];
    let curr = k;
    let prev = Array.from({length: n}, (_, i) => i - 1);
    let next = Array.from({length: n}, (_, i) => i + 1);
    next[n - 1] = -1; // 마지막 행 이후의 값은 존재하지 않음

    cmd.forEach(command => {
        if (command.startsWith("C")) {
            // 현재 행 삭제
            removedStack.push([curr, prev[curr], next[curr]]);
            answer[curr] = 'X';

            // 연결 끊기
            if (prev[curr] !== -1) {
                next[prev[curr]] = next[curr];
            }
            if (next[curr] !== -1) {
                prev[next[curr]] = prev[curr];
            }

            // 현재 행 업데이트
            if (next[curr] !== -1) {
                curr = next[curr];
            } else {
                curr = prev[curr];
            }

        } else if (command.startsWith("Z")) {
            // 가장 최근에 삭제된 행 복구
            const [r, p, n] = removedStack.pop();
            answer[r] = 'O';

            if (p !== -1) {
                next[p] = r;
            }
            if (n !== -1) {
                prev[n] = r;
            }

        } else {
            const [direction, X] = command.split(" ");
            const steps = parseInt(X);
            if (direction === "U") {
                for (let i = 0; i < steps; i++) {
                    curr = prev[curr];
                }
            } else if (direction === "D") {
                for (let i = 0; i < steps; i++) {
                    curr = next[curr];
                }
            }
        }
    });

    return answer.join('');
};
