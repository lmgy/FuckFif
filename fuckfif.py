# -*- coding: UTF-8 -*-

import json
import random


def change(input_data, length, key, mix, max):
    for i in range(length):
        input_data[i][key] = random.randint(mix, max)


def change_detail(input_data, length):
    for i in range(length):
        str_tmp = input_data[i]["ansDetail"]
        str_pre = str_tmp[:str_tmp.find("#")]
        # print(str_pre)
        str_sur = str_tmp[str_tmp.find("#") + 1:]
        str_score = ""
        for score in str_sur.split(","):
            try:
                if int(float(score)) < 85:
                    int_score = float(score) + random.randint(85 - int(float(score)), 95 - int(float(score)))
                    str_score += str(int_score) + ","
                else:
                    str_score += score + ","
            except ValueError:
                    pass
        if not str_score.endswith(","):
            str_score += ","
        input_data[i]["ansDetail"] = str_pre + "#" + str_score


data = input("请输入post提交的jsonobject：\n")
data_json = json.loads(data.strip())
length = len(data_json)
change(data_json, length, "score", 86, 94)  # 自己设置分数区间
change(data_json, length, "accuracy", 95, 98)
change(data_json, length, "fluency", 96, 100)
change(data_json, length, "complete", 96, 100)
change_detail(data_json, length)
print(json.dumps(data_json))






