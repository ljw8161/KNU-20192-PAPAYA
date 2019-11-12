import json
with open('C:/Users/GL62/openpose/Results/testt.json') as json_data:
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
print(info_list[1][10])
