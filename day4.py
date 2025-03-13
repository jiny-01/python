#딕셔너리

profile = {
    "name" : "김지니",
    "age" : 25,
    "hobby" : ["운동", "유튜브보기"]
}
#
# print(profile)

# print(profile["hobby"][1]) #딕셔너리 내 리스트 안의 요소 접근
# profile["age"] = 26 #요소 수정, 키가 존재하면 수정
# print(profile)
# profile["job"] = "학생" #요소 추가, 키가 존재하지 않는 것은 추가
# print(profile)

# del profile["job"] #요소 삭제
# print(profile)

#키만 출력
# key_list = list(profile.keys())  #딕셔너리 내 키만 리스트 형태로 출력 list(): 리스트로 형 변환
# key_list.append("job") #원래의 딕셔너리에 job 키가 생긴 것은 아님
# print(key_list)
#값만 출력
# profile.values()
# print(profile.values())
# val_list = list(profile.values()) #값만 추출해서 리스트 형태로 출력한 것
# print(val_list)
#키-값 형태로 다 뽑아내기
# profile.items()
# print(profile.items())
# item_list = list(profile.items())
# item_list.append(("job", "학생"))
# print(item_list)
#
# #딕셔너리 정렬
# python_grade = {
#     "지니" : "B",
#     "길동" : "C",
#     "준식" : "A",
#     "상혁" : "D"
# }
# print(sorted(python_grade.items(),reverse=True)) #키 기준 내림차순
#
# print(sorted(python_grade.items(), key=lambda x: x[1])) #값 기준
# # #lambda x: x[1]:요소 1개를 x 로 보고 (0,1) 로 생각해서 [1], 즉 A,B,C 기준
# print(sorted(python_grade.items(), key=lambda x: x[1], reverse=True)) #값 기준 내림차순
#
# #이름 입력 받고 점수도 입력 받고 딕셔너리에 저장
# student = {}
#{"name" : "자기이름", "score":88}

# #print(student)
# #"input(""score": )}
#
# #방법1
# student = {
#     "name": input("이름 : "),
#     "score": int(input("점수 : "))
# }
# print(student)

#방법2
# student["name"] = input("이름 : ") #input은 무조건 입력한 것을 문자열로 인식함
# student["score"] = int(input("점수 : ")) #형변환 필요 ->int 사용
# print(student)

#세트
# fruits = {"사과", "딸기", "귤"}
# print(fruits)
# apple_str = set("apple") #-> 중복 알파벳 제외 출력
# print(apple_str)
#
# num = {1, 2, 4, 4, 5}
# num.add(8) #add -> 세트 내 요소 하나씩 추가
# num.update([10, 11, 12]) #여러 개 요소 한번에 추가 -> update

# num.remove(1) #세트 내 요소 삭제 (없는 걸 지우려고 하면 오류냄)
# print(num)
# #num.discard(1) #요소 삭제 (없는 값을 지워도 오류 안냄)
# #존재하지 않는 값을 지울 때, remove는 오류, discard 는 정상작동
# print(num)

# num.clear() #요소 전체 제거
# print(num)
#
#
# #empty_set = {} #빈 딕셔너리를 의미함
# #empty_set = set() #빈 세트를 선언
#
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# #합집합
# print(a.union(b))
# print(a|b)
# #교집합
# print(a.intersection(b))
# print(a & b)
# #차집합
# print(a.difference(b))
# print(a - b)
#
# color = {"b", "l", "u", "e"}
# print(color.pop()) #세트는 순서가 없어서 pop을 해도 마지막 것이 아닌 랜덤으로 지워짐
# print(color)

#모임날짜 찾기
# a = [21, 22, 23, 25, 26]
# b = [22, 24, 27]
# common = set(a) & set(b) #교집합을 사용하기 위해 list->set 변환
# print(common)
# print(set(a) & set(b))

#집합 문제 풀어보기
python_class = ["수현", "현호", "지니", "가인"]
java_class = ["현호", "지니", "홍수", "찬호"]

com = set(python_class) & set(java_class)
#결과물: 공통으로 출석한 학생:(a&b)
print(com)
#파이썬만 출석한 학생(a-(a&b))
print(set(python_class)-com)
#자바만 출석한 학생(b-(a&b))
print(set(java_class)-com)




