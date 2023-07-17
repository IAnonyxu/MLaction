# _*_ coding=utf-8 _*_

#下载密码行业相关国家标准文件GB/T

import requests
import re
import json

url = "http://www.gmbz.org.cn/main/normsearch.json"

form_date = {
    "draw": "1",
    "columns[0][data]": "NORM_ISO_ID",
    "columns[0][name]": "NORM_ISO_ID",
    "columns[0][searchable]": "true",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "NORM_NAME_C",
    "columns[1][name]": "NORM_NAME_C",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "NORM_ZT_NAME",
    "columns[2][name]": "NORM_ZT",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "NORM_FLAG_NAME",
    "columns[3][name]": "NORM_FLAG_NAME",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "NORM_NAME_E",
    "columns[4][name]": "NORM_NAME_E",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "NORM_CO_NAME",
    "columns[5][name]": "NORM_CO_NAME",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "NORM_CA_NAME",
    "columns[6][name]": "NORM_CA_NAME",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "NORM_PUB_DATE",
    "columns[7][name]": "NORM_PUB_DATE",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "NORM_IMP_DATE",
    "columns[8][name]": "NORM_IMP_DATE",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "UP_GB_FLAG",
    "columns[9][name]": "UP_GB_FLAG",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "10",
    "columns[10][name]": "",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "order[0][column]": "0",
    "order[0][dir]": "asc",
    "start": "0",
    "length": "100",
    "search[value]": "",
    "search[regex]": "false",
    "norm_iso_id": "",
    "norm_flag": "",
    "norm_name_c": "",
    "norm_name_e": "",
    "norm_co_name": "",
    "norm_zt": "",
    "norm_pub_date_begin": "",
    "norm_pub_date_end": "",
    "norm_imp_date_begin": "",
    "norm_imp_date_end": ""}

response = requests.post(url, data=form_date)
# import json

content = json.loads(response.text)
# print(content['data'][0:])

for i in range(0, 94):
    # print(content['data'][i]['NORM_APP_ADDR'],content['data'][i]['NORM_ISO_ID']+" "+content['data'][i]['NORM_NAME_C'])
    # 获取文件名
    num = re.sub('/', '', content['data'][i]['NORM_ISO_ID'])
    file_name = num + " " + content['data'][i]['NORM_NAME_C'] + ".pdf"
    print(file_name)
    # 下载文件
    path = content['data'][i]['NORM_APP_ADDR']
    url = "http://www.gmbz.org.cn/file/" + path
    r = requests.get(url)
    with open(file_name, "wb") as code:
        code.write(r.content)
