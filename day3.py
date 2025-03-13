#list 예시
fruits = ["apple", "lemon", "banana"] #문자열 인덱스: 0,1,2
numbers = [1, 5, 3, 9, 1, 2] #숫자 리스트
bools = [True, False, True, True] #불리언 리스트
mixed_list = ["안녕하세요", 12, True] # 자료형 혼합 가능
print(fruits)
print(fruits[2]) # 리스트 안에 인덱스 0,1,2 중 2인 바나나만 출력
print(fruits[2][1]) # 2인 바나나에서 a 만 출력하기
print(fruits[-2]) # list 내의 뒤에서부터
fruits[0] = "cherry" # 리스트 내 요소 수정-> 변경
print(fruits)

# numbers.append("hi") #.append : 리스트 요소 추가 (마지막 자리에 추가)
# print(numbers)
# numbers.insert(1,3) #.insert(들어갈 자리, 들어갈 내용) : 특정 자리에 요소 추가(인덱스 넣어서 중간에 추가가능)
# print(numbers)
# #print(numbers.pop()) #.pop : 리스트의 마지막 요소가 리턴됨

# #print(numbers.remove("hi")) #.remove: 리스트의 특정 요소 제거
# print(numbers)
# del numbers[5] #del 리스트명 [없앨 인덱스 번호]

# print(len(mixed_list)) #리스트의 길이 -> 3 출력: 요소가 3개
#bools.sort() #리스트 내 요소 작은 것부터, 오름차순 정렬
#bools.sort(reverse=False) #sort(): 작은 순, 옵션으로 reverse=True 하면 큰 순
#print(bools) #정렬을 하고 출력
#bools.sort(reverse=False)
# numbers.reverse()
# print(numbers) #reverse : 정렬없이 그냥 순서를 역순으로 출력함
# fruits = "-".join(fruits)  #.join : 지정한 ""안의 것으로 리스트 내 요소를 결합한 것
# print(fruits)

#쇼핑목록, 입력받아서 하나씩 3가지를 출력
# cart = []
# cart1 = input("1 : ") # 추가할 상품 입력 3번 반복
# cart2 = input("2 : ")
# cart3 = input("3 : ")
# cart = [cart1, cart2, cart3]
# print(cart)

# # 정답
# cart = []
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
# print(cart)
#
#
# #튜플
colors = ("red", "green", "black")
numbers = [1, 5, 3, 9, 1, 2] #숫자 리스트
bools = [True, False, True, True] #불리언 리스트
# numbers = (1, 5, 3, 9)
# bools = (True, False, True)
# mixed_tuple = ("red", 1, True)
# a = ("first", ) #요소가 하나일 떄는 마지막 쉼표찍기!!

# print(colors[1])
# #colors[1] = "yellow" -> 튜플은 요소 변경 불가능 (추가, 삭제, 수정 불가능)
# print(numbers[0:3]) #튜플 슬라이싱 가능
# print(numbers.count(1))
#Q. 튜플은 append 처럼 추가는 안되는지
print(numbers.count(1))
print(numbers.index(1))

a, b, c = colors #튜플 요소를 a,b,c 로 정의하고 내용을 벗겨내서 출력
print(c)






