-- 코드를 입력하세요
SELECT ICE.INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
  FROM FIRST_HALF AS FH JOIN ICECREAM_INFO AS ICE
    ON FH.FLAVOR = ICE.FLAVOR
GROUP BY ICE.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
    