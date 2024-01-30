/**
 * @return {Generator<number>}
 */


var fibGenerator = function* () {
  let index = 0;
  const value = [0, 1, 1, 2, 3];

  while (true) {
    if (index < 4) yield value[index++];
    if (!value[index]) {
      value[index] = value[index - 1] + value[index - 2];
    }
    yield value[index];
    index++;
  }
};



// var fibGenerator = function*() {
//   let answer = [];
//   for (i=0; i < callCount; i++) {
//     answer.push(i)
//   }

//   return answer;
    
// };

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

