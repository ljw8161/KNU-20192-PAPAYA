#붓꽃의 품종을 머신러닝을 이용하여 꽃잎과 꽃받침의 크기를 기반으로 분류
from sklearn import svm, metrics
import random, re
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from matplotlib import pyplot as plt
import mglearn
from matplotlib import font_manager, rc
#한글 처리를 위해 폰트 설정
font_name = font_manager.FontProperties(\
    fname="C:/Windows/Fonts/malgun.ttf").get_name()
    rc('font',family=font_name)
iris = datasets.load_iris()
#2,3열만 선택(3, 4번째 필드)
X = iris.data[:,[2,3]]
y = iris.target

import random
#BMI를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "normal"
    return "fat"
# 출력 파일 준비하기
fp = open("D:/data/bmi/bmi.csv","w",encoding="utf-8")
fp.write("height, weight, label\r\n")
# 무작위고 데이터 생성하기
cnt = {"thin":0,"normal":0,"fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35,80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0}, {1}, {2}\r\n".format(h, w, label))
fp.close()
print("데이터가 생성되었습니다.", cnt)

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
# 데이터 로딩
tbl = pd.read_csv("D:/data/bmi/bmi.csv")
# 칼럼(열)을 자르고 정규화
label = tbl["label"]
w = tbl["weight"]/100 # 최대 100kg 이라 가정
h = tbl["height"]/200 # chleo 200cm 라고 가정
# 정규화시킨 데이터(0 ~ 1 사이의 값)
wh = pd.concat([w,h], axis = 1)
# 학습용 데이터셋과 검증용 데이터셋으로 분리
data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)
# 데이터 학습
clf = svm.SVC()
clf.fit(data_train, label_train)
# 데이터 예측
predict = clf.predict(data_test)
# 결과 출력
print("학습용 데이터셋 정확도 : {:.3f}".format(clf.score(data_train, label_train)))
print("검증용 데이터셋 정확도 : {:.3f}".format(clf.score(data_test, label_test)))
cl_report = metrics.classification_report(label_test, predict)
print("리포트:\n", cl_report)
# 2만개의 데이터 테스트 98.7% 정밀도로 분류하는데 성공

# 감마, c값을 증가시켜 더 복잡한 모델 만들기
svc = SVC(C=1)
# svc = SVC(C=100)
# svc = SVC(C=1000)
svc.fit(X_train_scaled, y_train)
print("학습용 데이터셋 정확도 : {:.3f}".format(svc.score(X_train_scaled, y_train)))
print("검증용 데이터셋 정확도 : {:.3f}".format(svc.score(X_test_scaled, y_test)))