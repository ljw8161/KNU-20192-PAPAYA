import math
import json
with open('C:/Users/GL62/openpose/Results/kick3_14_keypoints.json') as json_data:
	data = json.load(json_data)

info_list = list()
for i in range(len(data["people"])):
	person_data = data["people"][i]
	joint_data = person_data["pose_keypoints_2d"]

	person_info = list()

	for j in range(len(joint_data)):
		if j%3 == 0 :
			if j>=3 :
				person_info.append(pose_info)
			pose_info = list()
		pose_info.append(joint_data[j])
	info_list.append(person_info)
############데이터 파싱 완료#######################
# print(info_list)

#############좌표 구하기 시작######################

# 사람 0의 왼쪽 발목 정확도, x좌표값, y좌표값
person0_left_ankle_x = info_list[0][11][0]
person0_left_ankle_y = info_list[0][11][1]
person0_left_ankle_accuracy = info_list[0][11][2]

# 사람 0의 왼쪽 발뒤꿈치 정확도, x좌표값, y좌표값
person0_left_ankleheel_x = info_list[0][22][0]
person0_left_ankleheel_y = info_list[0][22][1]
person0_left_ankleheel_accuracy = info_list[0][22][2]

#발뒤꿈치와 발목 중에 정확도 높은 것의 x,y 좌표가 사람1의 왼쪽 발 좌표가 됨.
if person0_left_ankle_accuracy >= person0_left_ankleheel_accuracy :
	person0_left_feet_x = person0_left_ankle_x
	person0_left_feet_y = person0_left_ankle_y
else:
	person0_left_feet_x = person0_left_ankleheel_x
	person0_left_feet_y = person0_left_ankleheel_y

print('사람0의 왼쪽 발 좌표')
print(person0_left_feet_x)

# 사람 0의 오른쪽 발목 정확도, x좌표값, y좌표값
person0_right_ankle_x = info_list[0][14][0]
person0_right_ankle_y = info_list[0][14][1]
person0_right_ankle_accuracy = info_list[0][14][2]

# 사람 0의 오른쪽 발뒤꿈치 정확도, x좌표값, y좌표값
person0_right_ankleheel_x = info_list[0][21][0]
person0_right_ankleheel_y = info_list[0][21][1]
person0_right_ankleheel_accuracy = info_list[0][21][2]

#발뒤꿈치와 발목 중에 정확도 높은 것의 x,y 좌표가 사람1의 왼쪽 발 좌표가 됨.
if person0_right_ankle_accuracy >= person0_right_ankleheel_accuracy :
	person0_right_feet_x = person0_right_ankle_x
	person0_right_feet_y = person0_right_ankle_y
else:
	person0_right_feet_x = person0_right_ankleheel_x
	person0_right_feet_y = person0_right_ankleheel_y

print('사람0의 오른쪽 발 좌표')
print(person0_right_feet_x)

#사람 0의 왼쪽발~오른쪽 발 거리
person0_foot_distance=((person0_left_feet_x-person0_right_feet_x)**2 + (person0_left_feet_y-person0_right_feet_y)**2)**0.5

print('사람0의 왼쪽 발~ 오른쪽 발 거리')
print(person0_foot_distance)
print('*************************************************')
############################객체2#######################################

# 사람 0의 왼쪽 발목 정확도, x좌표값, y좌표값
person1_left_ankle_x = info_list[1][11][0]
person1_left_ankle_y = info_list[1][11][1]
person1_left_ankle_accuracy = info_list[1][11][2]

# 사람 0의 왼쪽 발뒤꿈치 정확도, x좌표값, y좌표값
person1_left_ankleheel_x = info_list[1][22][0]
person1_left_ankleheel_y = info_list[1][22][1]
person1_left_ankleheel_accuracy = info_list[1][22][2]

#발뒤꿈치와 발목 중에 정확도 높은 것의 x,y 좌표가 사람1의 왼쪽 발 좌표가 됨.
if person1_left_ankle_accuracy >= person1_left_ankleheel_accuracy :
	person1_left_feet_x = person1_left_ankle_x
	person1_left_feet_y = person1_left_ankle_y
else:
	person1_left_feet_x = person1_left_ankleheel_x
	person1_left_feet_y = person1_left_ankleheel_y

print('사람1의 왼쪽 발 좌표')
print(person1_left_feet_x)

# 사람 0의 오른쪽 발목 정확도, x좌표값, y좌표값
person1_right_ankle_x = info_list[1][14][0]
person1_right_ankle_y = info_list[1][14][1]
person1_right_ankle_accuracy = info_list[1][14][2]

# 사람 0의 오른쪽 발뒤꿈치 정확도, x좌표값, y좌표값
person1_right_ankleheel_x = info_list[1][21][0]
person1_right_ankleheel_y = info_list[1][21][1]
person1_right_ankleheel_accuracy = info_list[1][21][2]

#발뒤꿈치와 발목 중에 정확도 높은 것의 x,y 좌표가 사람1의 왼쪽 발 좌표가 됨.
if person1_right_ankle_accuracy >= person1_right_ankleheel_accuracy :
	person1_right_feet_x = person1_right_ankle_x
	person1_right_feet_y = person1_right_ankle_y
else:
	person1_right_feet_x = person1_right_ankleheel_x
	person1_right_feet_y = person1_right_ankleheel_y

print('사람1의 오른쪽 발 좌표')
print(person1_right_feet_x)

#사람 1의 왼쪽발~오른쪽 발 거리
person1_foot_distance=((person1_left_feet_x-person1_right_feet_x)**2 + (person1_left_feet_y-person1_right_feet_y)**2)**0.5

print('사람1의 왼쪽 발~ 오른쪽 발 거리')
print(person1_foot_distance)
