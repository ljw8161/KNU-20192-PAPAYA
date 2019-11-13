import json
with open('C:/Users/GL62/openpose/Results/falldown3.json') as json_data:
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

#15,16,17,18 중에 머릿값 하나 (정확도 제일 높은 것 )

init_value = info_list[0][15][2]

for i in range (4):
	if info_list[0][15+i][2]>=init_value:
		init_value = info_list[0][15+i][2]
		eye_pos = 15+i

# print('최종 눈 좌표:')
# print(eye_pos)

if info_list[0][14][2]>=info_list[0][11][2]:
	foot_pos = 14
else:
	foot_pos = 11

print()
print('쓰러졌을 때 머리와 발의 y좌표 차이 ')
falling_y_differ = info_list[0][eye_pos][1]-info_list[0][foot_pos][1]

print(falling_y_differ)

###################쓰러지기 전 ##############################

with open('C:/Users/GL62/openpose/Results/notfalldown3.json') as json_data2:
	data2 = json.load(json_data2)

info_list2 = list()

for  i in range(len(data2["people"])) :
	person_data2 = data2["people"][i]
	joint_data2 = person_data2["pose_keypoints_2d"]

	person_info2 = list()

	for j in range(len(joint_data2)):
		if j%3==0 :
			if j>=3 : 
				person_info2.append(pose_info2)
			pose_info2 = list()
		pose_info2.append(joint_data2[j])
	info_list2.append(person_info2)	

############데이터 파싱 완료#######################
# print(info_list)

#############좌표 구하기 시작######################

#15,16,17,18 중에 머릿값 하나 (정확도 제일 높은 것 )

init_value2 = info_list2[0][15][2]

for i in range (4):
	if info_list2[0][15+i][2]>=init_value2:
		init_value2 = info_list2[0][15+i][2]
		eye_pos2 = 15+i

# print('최종 눈 좌표:')
# print(eye_pos)

if info_list2[0][14][2]>=info_list2[0][11][2]:
	foot_pos2 = 14
else:
	foot_pos2 = 11

print()
print('서있을 때 머리와 발의 y좌표 차이 ')
standing_y_differ = info_list2[0][eye_pos2][1] - info_list2[0][foot_pos2][1]
print(standing_y_differ)

answer= standing_y_differ/falling_y_differ
print()
print('서있을 때/쓰러졌을 때 = ',answer)

