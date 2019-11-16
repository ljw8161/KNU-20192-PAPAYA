import math
import json
with open('C:/Users/GL62/openpose/Results/rock1_1_000000000000_keypoints.json') as json_data:
	data = json.load(json_data)

info_list = list()

for  i in range(len(data["people"])) :
	person_data = data["people"][i]
	joint_data = person_data["pose_keypoints_2d"]

	person_info = list()

	for j in range(len(joint_data)):
		if j%3==0 :
			if j>=3 : 
				person_info.append(pose_info)
			pose_info = list()
		pose_info.append(joint_data[j])
	info_list.append(person_info)	

############데이터 파싱 완료#######################
# print(info_list)

#############좌표 구하기 시작######################

print('사람 0의 왼쪽 어깨 x,y : ')

person0_left_shoulder_x = info_list[0][2][0]
person0_left_shoulder_y = info_list[0][2][1]
print(person0_left_shoulder_x,person0_left_shoulder_y)

print('사람 0의 왼쪽 손 x,y : ')
person0_left_hand_x = info_list[0][4][0]
person0_left_hand_y = info_list[0][4][1]
print(person0_left_hand_x,person0_left_hand_y)

print('사람 0의 왼쪽 어깨 ~ 왼쪽 손 사이의 거리')
person0_left_shoulder_hand_distance=((person0_left_shoulder_x-person0_left_hand_x)**2 + (person0_left_shoulder_y-person0_left_hand_y)**2)**0.5

print(person0_left_shoulder_hand_distance)

print('사람 0의 오른쪽 어깨 x,y : ')
person0_right_shoulder_x = info_list[0][5][0]
person0_right_shoulder_y = info_list[0][5][1]
print(person0_right_shoulder_x,person0_right_shoulder_y)

print('사람 0의 오른쪽 손 x,y : ')
person0_right_hand_x = info_list[0][7][0]
person0_right_hand_y = info_list[0][7][1]
print(person0_right_hand_x,person0_right_hand_y)

print('사람 0의 오른쪽 어깨 ~ 오른쪽 손 사이의 거리')
person0_right_shoulder_hand_distance=((person0_right_shoulder_x-person0_right_hand_x)**2 + (person0_right_shoulder_y-person0_right_hand_y)**2)**0.5

print(person0_right_shoulder_hand_distance)

print('사람 0의 왼쪽 어깨~손, 오른쪽 어깨~ 손 거리 : ')
print(person0_left_shoulder_hand_distance,person0_right_shoulder_hand_distance)
print('둘 평균: ')
print((person0_right_shoulder_hand_distance+person0_left_shoulder_hand_distance)/2)

print('########################두번째 객체 ############################################')
print('사람 1의 왼쪽 어깨 x,y : ')

person1_left_shoulder_x = info_list[1][2][0]
person1_left_shoulder_y = info_list[1][2][1]
print(person1_left_shoulder_x,person1_left_shoulder_y)

print('사람 1의 왼쪽 손 x,y : ')
person1_left_hand_x = info_list[1][4][0]
person1_left_hand_y = info_list[1][4][1]
print(person1_left_hand_x,person1_left_hand_y)

print('사람 1의 왼쪽 어깨 ~ 왼쪽 손 사이의 거리')
person1_left_shoulder_hand_distance=((person1_left_shoulder_x-person1_left_hand_x)**2 + (person1_left_shoulder_y-person1_left_hand_y)**2)**0.5

print(person1_left_shoulder_hand_distance)

print('사람 1의 오른쪽 어깨 x,y : ')
person1_right_shoulder_x = info_list[1][5][0]
person1_right_shoulder_y = info_list[1][5][1]
print(person1_right_shoulder_x,person1_right_shoulder_y)

print('사람 1의 오른쪽 손 x,y : ')
person1_right_hand_x = info_list[1][7][0]
person1_right_hand_y = info_list[1][7][1]
print(person1_right_hand_x,person1_right_hand_y)

print('사람 1의 오른쪽 어깨 ~ 오른쪽 손 사이의 거리')
person1_right_shoulder_hand_distance=((person1_right_shoulder_x-person1_right_hand_x)**2 + (person1_right_shoulder_y-person1_right_hand_y)**2)**0.5

print(person1_right_shoulder_hand_distance)

print('사람 1의 왼쪽 어깨~손, 오른쪽 어깨~ 손 거리 : ')
print(person1_left_shoulder_hand_distance,person1_right_shoulder_hand_distance)
print('둘 평균: ')
print((person1_right_shoulder_hand_distance+person1_left_shoulder_hand_distance)/2)
