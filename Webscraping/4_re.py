import re #정규식
#abcd, book, desk
# ca?e
#care, cafe, case, cave
#caae, cabe, cace, cade, ...


p = re.compile("ca.e") # p : pattern
# . (ca.e) : 하나의 문자를 의미 > care, cafe, cave | caffe
# ^ (^de)  : 문자열의 시작 > desk, destination (O) |fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)
def print_match(m):
    if m:
        print("m.group() : ",m.group()) #일치하는 문자열 반환
        print("m.string : ",m.string) #입력받은 문자열
        print("m.start : ",m.start()) #일치하는 문자열의 시작 index
        print("m.end : ",m.end()) #일치하는 문자열의 끝 index\
        print("m.span() : ", m.span()) #일치하는 문자열의 시작
    else:
        print("매칭되지 않았습니다.")

m = p.match("careless") #match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
# print(m.group()) #매치되지 않으면 에러가 발생

#정규식2
m = p.search("good care") # search : 주어진 문자열 중에 일피하는게 있는지 확인
print_match(m) 