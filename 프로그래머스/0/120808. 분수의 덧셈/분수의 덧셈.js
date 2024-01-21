function solution(numer1, denom1, numer2, denom2) {
    let topNum = numer1*denom2 + numer2*denom1;
    let botNum = denom1*denom2;
    let gcfNum = 1;
    
    for (let i = 1; i <= topNum; i++ ) {
      if ( topNum%i === 0 && botNum%i === 0 ) {
        gcfNum = i;
      }
    }
    return [topNum/gcfNum, botNum/gcfNum]
}