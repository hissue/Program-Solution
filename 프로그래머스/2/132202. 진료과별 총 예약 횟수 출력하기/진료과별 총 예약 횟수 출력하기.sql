-- 코드를 입력하세요
SELECT MCDP_CD AS A, COUNT(PT_NO) AS B FROM (SELECT TO_CHAR(APNT_YMD, 'MM'), PT_NO, MCDP_CD FROM APPOINTMENT WHERE TO_CHAR(APNT_YMD, 'MM')*1 = 5) GROUP BY MCDP_CD ORDER BY B, A