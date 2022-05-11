import os
import json
path = 'D:/math_hiwi/GenericDecMats_web/data'

files = os.listdir(path)

file_list = []
for f in files:
	file_list.append(f)


# print(file_list)

def merge_JsonFiles(filename,path):
    result = []
    for f1 in filename:
    	# print(f1)
        with open(path+'/'+f1) as infile:
            result.append(json.load(infile))

    with open('data.json','w+') as output_file:
    	for data in result:
        	json.dump(data, output_file)
        	output_file.write("\n")

    # print(result[1])
merge_JsonFiles(file_list,path)

f = open(path + '/' + file_list[20])

d = json.load(f)

print(d['type'])