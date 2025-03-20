#모듈화
#표준 모듈: math, random, datetime, json, re(정규표현식)
#정규 표현식: 정해진 규칙대로 표현이 되어있는지 검증 ex) 이메일(아이디@도메인), 전화번호
#외부 모듈: flask, tensorflow, torch, matplotlib, seaborn, beautifulsoap4,
#pip freeze>requirements.txt: 필요한 모듈 리스트를 명단화하는 것
#pip install -r requirements.txt: 다시 가져올 떄 텍스트파일을 읽어오겠다

#API: 인터페이스, 소프트웨어 생성하거나 외부 시스템과 상호작용 -> 요청하면 데이터 전달하는 과정, 인터페이스
#requests: HTTP요청을 쉽게 보낼 수 있는 모듈
#beautifulsoup4: 웹페이지에서 원하는 데이터 추출



#외부모듈: 파이썬에서 제공하는 모듈이 아닌 개발자가 추가로 설치해서 사용하는 모듈
#pip(pakage installer for python)

#pip install 모듈명                #pip uninstall 모듈명
#pip list                         #pip freeze>requirements.txt 필요한 모듈을 txt파일로 보여줌
#pip install --upgrade 모듈명      #pip install -r requirements.txt  txt 파일을 읽어들임

#request : HTTP(요청을 쉽게 보낼 수 있는 모듈
#beautifulsoup4 : 웹 페이지에서 원하는 데이터를 추출할 때 사용
#pandas : csv, excel 등 다양한 데이터 파일을 쉽게 처리하고 분석
#numpy : 다차원 배열, 행렬 연산, 과학 계산 등 사용
#matplotlib & seaborn : 그래프 및 차트를 그려서 데이터를 시각적으로 표현
#openpyxl : excel 파일을 읽고, 쓰고, 저장하는 데 사용
#flask : 간단한 웹 사이트 또는 API 서버를 만들 때 사용
#tensorflow & torch : 딥러닝 및 머신러닝 모델을 만들 때 사용

# #request 모듈
# import requests
# response = requests.get("https://www.naver.com/") #get 요청을 보냄-웹 페이지에 대한 데이터 넘겨줌 (크롬 기준-> 웹페이지에서 f12 누르면 됨)
# print(response.status_code) #요청 시 에러  404: 존재하지 않음  200: 정상적 접근
# print(response.text)
#
# #pandas 모듈
import pandas as pd
#
# df = pd.read_csv("data.csv") #df: 데이터 파일
# print(df)
# print(df.describe())  #describe: 파일 데이터 요약분석

"""
count - 해당 열의 데이터 갯수
mean - 평균값
std - 표준편차 (데이터의 분산 정도)
min/max - 최솟값/최댓값
25% / 50% / 75% - 데이터의 25/50/75% 지점
"""

# print(df[["ID", "Age", "Salary"]])

# #matplotlib 모듈
import matplotlib.pyplot as plt
#
# df.groupby("Age")["Salary"].mean().plot(kind="bar") #정의한 것
# plt.show()

# #numpy 모듈
import numpy as np
#
# arr1 = np.array([1,2,3,4,5]) #1차원 배열
# print(arr1)  #->출력 [1 2 3 4 5] 리스트는 아님, 그냥 배열일 뿐
# arr2 = np.array([[1,2,3],[4,5,6]]) #2차원 배열
# print(arr2)  #2차원 배열
#
# #0으로 채운 다차원 배열
# zeros = np.zeros((3, 4))    #1번째 인자: 행 / 2번째 인자: 열 -> 3행 4열
# print(zeros)
#
# #1로 채운 다차원 배열
# ones = np.ones((3, 4))
#
# #특정한 값으로 채운 다차원 배열
# filled = np.full((3, 4), 5)
# print(filled)

#연속된 값으로 채운 1차원 배열
# arr = np.array(1, 10, 2)
# print(arr)

#랜덤 값으로 채운 배열
random_arr = np.random.randint(1, 100, (3, 4))
print(random_arr)

arr1 = np.array([1,3,5])
arr2 = np.array([2,5,8])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)


#seaborn 모듈
import seaborn as sns

df = pd.read_csv("tips.csv")
plt.figure(figsize=(8,5)) #그래프 크기
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="Set2")
plt.title("tips")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()










