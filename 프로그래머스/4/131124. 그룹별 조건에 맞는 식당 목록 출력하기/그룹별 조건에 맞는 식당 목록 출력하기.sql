-- 코드를 입력하세요

SELECT MP.MEMBER_NAME, RE.REVIEW_TEXT, DATE_FORMAT(RE.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
  FROM REST_REVIEW AS RE
  JOIN (
      SELECT MEMBER_ID
      FROM REST_REVIEW
      GROUP BY MEMBER_ID
      ORDER BY COUNT(*) DESC
      LIMIT 1  
      ) AS TOP_REVIEW
    ON RE.MEMBER_ID = TOP_REVIEW.MEMBER_ID
    
LEFT JOIN MEMBER_PROFILE AS MP
  ON RE.MEMBER_ID = MP.MEMBER_ID
ORDER BY RE.REVIEW_DATE, RE.REVIEW_TEXT;

# SELECT MP.MEMBER_NAME, RE.REVIEW_TEXT, DATE_FORMAT(RE.REVIEW_DATE, "%y-%m-%d") AS REVIEW_DATE
#   FROM MEMBER_PROFILE AS MP JOIN REST_REVIEW AS RE
#     ON MP.MEMBER_ID = RE.MEMBER_ID
#   JOIN (
#      SELECT MEMBER_ID
#      FROM REST_REVIEW
#      GROUP BY MEMBER_ID
#      ORDER BY COUNT(*) DESC
#      LIMIT 1
#   ) AS TOP_RE
#   ON RE.MEMBER_ID = TOP_RE.MEMBER_ID
# ORDER BY RE.REVIEW_DATE, RE.REVIEW_TEXT;




# SELECT MP.MEMBER_NAME, RE.REVIEW_TEXT, DATE_FORMAT(RE.REVIEW_DATE, "%y-%m-%d") AS REVIEW_DATE
#   FROM MEMBER_PROFILE AS MP JOIN REST_REVIEW AS RE
#     ON MP.MEMBER_ID = RE.MEMBER_ID
#  WHERE RE.MEMBER_ID = (
#      SELECT MEMBER_ID
#      FROM REST_REVIEW
#      GROUP BY MEMBER_ID
#      ORDER BY COUNT(*) DESC
#      LIMIT 1
#  )
# ORDER BY RE.REVIEW_DATE, RE.REVIEW_TEXT;
