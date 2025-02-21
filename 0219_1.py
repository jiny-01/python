email = input("email : ") #allie7019@naver.com 에서 id 만 출력하기
#id 는 allie7019, 슬라이싱을 해야함, @인덱스를 구하는 함수를 이용, -> 알고리즘

print(email.index("@"))
email_id = (email[0:email.index("@")])
print(f"id는 {email_id}")
 #앞에서부터 찾는데 해당문자의 인덱스 번호를 찾아줌

