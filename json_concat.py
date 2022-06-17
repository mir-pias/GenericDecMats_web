import os
import json
path = 'D:/math_hiwi/GenericDecMats_web/data'

files = os.listdir(path)

file_list = []
for f in files:
	file_list.append(f)


# print(file_list)

def replace_zeta(obj):

    def decode_dict(a_dict):
        for key, value in a_dict.items():
            if type(value) is int or type(value) is bool:
                pass
            else:
                for i in value:
                    if type(i) == str:
                        a_dict[key] = i.replace('\\', '/')
                        # a_dict[key] = i.replace('\p', '\ p')

        return a_dict

    return json.loads(json.dumps(obj), object_hook=decode_dict)

def merge_JsonFiles(filename,path):
    result = []
    for f1 in filename:
    	# print(f1)
        with open(path+'/'+f1) as infile:
            result.append(json.load(infile))

    with open('GenericDecMats_web/data.json','w+') as output_file:
    	for data in result:
            data = replace_zeta(data)
            # print(data)
            json.dump(data, output_file)
            output_file.write("\n")


def main():
    merge_JsonFiles(file_list,path)

    # f = open('data.json')

    # d = json.load(f)

    # for i in d:
    #     print(i['type'])

if __name__== '__main__':
    main()