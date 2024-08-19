import requests
res = requests.get("http://google.com")
res.raise_for_status()
# res = requests.get("http://nadocoding.tistory.com")
# print("responed code : ", res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("It's good")

# else:
#     print("it has some problem. [error code : ", res.status_code, "]")
# print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)