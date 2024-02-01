function solution(n, arr1, arr2) {
    return arr1.map((v, i) => {
        const binaryString = (v | arr2[i]).toString(2);
        let paddedBinaryString = binaryString.padStart(n, '0');
        let answer = '';

        for (let i of paddedBinaryString) {
            answer += i === '1' ? '#' : ' ';
        }

        return answer;
    });
}