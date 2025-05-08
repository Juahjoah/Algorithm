const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    n = Number(input[0]);
    
    if (n % 2 === 0) {
        input.push('is even')
    } else {
        input.push('is odd')
    }
    
    console.log(input[0], input[1])
});