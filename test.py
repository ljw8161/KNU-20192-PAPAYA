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
# print(info_list)
# 두번째 사람의 10번 관절 위치 및 정확도 뽑아내기 
print('눈  - ')
print(info_list[0][17])
print()
print('14번과 11번 중에 정확도 높은것?')
print( '14번'
	if info_list[0][14][2]>=info_list[0][11][2] else '11번')

print()
print('머리와 발의 y좌표 차이 ')
print(info_list[0][17][1] - info_list[0][14][1])