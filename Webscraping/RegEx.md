# 정규식

## 1. re.compile("원하는 형태(정규식)")
## 2. m = p.match("바교할 문자열") : 주어진 문자열의 처음부터 일치하는게 있는지 확인
## 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
## 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 변환

# 원하는 형태 : 정규식
## . (ca.e) : 하나의 문자를 의미 > care, cafe, cave | caffe
## ^ (^de)  : 문자열의 시작 > desk, destination (O) |fade (X)
## $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

## 정규식 공부 => w3schools.com/Python/Python regEx
## python re(regular expresion)