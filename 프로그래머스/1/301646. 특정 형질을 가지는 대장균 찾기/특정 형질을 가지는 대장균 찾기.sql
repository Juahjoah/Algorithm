-- 코드를 작성해주세요
-- 개체의 형질을 이진수로 변환해 갖고 있는 형질을 확인
SELECT COUNT(*) AS COUNT
  FROM ECOLI_DATA
 WHERE (
     SUBSTRING(CONV(GENOTYPE, 10, 2), -1, 1) = 1 OR
     SUBSTRING(CONV(GENOTYPE, 10, 2), -3, 1) = 1
 ) AND
       SUBSTRING(CONV(GENOTYPE, 10, 2), -2, 1) = 0;
