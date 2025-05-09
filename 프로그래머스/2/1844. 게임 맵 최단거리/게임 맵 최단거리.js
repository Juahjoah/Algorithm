function bfs(maps, visited, n, m) {
    const dx = [0, -1, 0, 1];
    const dy = [1, 0, -1, 0];
    
    let queue = [[0, 0, 1]];
    
    while (queue.length) {

        const [x, y, cnt] = queue.shift()
            
        if ( x === n - 1 && y === m - 1) {
            return cnt; 
        }

        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && maps[nx][ny] === 1) {
                queue.push([nx, ny, cnt + 1]);
                visited[nx][ny] = true;
            } 
        }  
        
    }
    return -1
}

function solution(maps) {
    var answer = 0;
    
    const n = maps.length;
    const m = maps[0].length;
    
    let visited = Array.from({ length: n }, () => Array(m).fill(false));
    visited[0][0] = true
    
    answer = bfs(maps, visited, n, m)
        
    return answer;
}