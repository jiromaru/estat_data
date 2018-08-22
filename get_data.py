import urllib
import json
import requests

def get_data(appId,statsDataId,file_path):
    #取得したアプリケーションIDを設定

    #e-StatのURL
    url = "https://api.e-stat.go.jp/rest/2.1/app/getSimpleStatsData?"

    #設定するキー
    keys = {
            "appId"            : appId,
            "lang"             : "J" ,
            "statsDataId"      : statsDataId 
    }

    #keysからパラメータの文字列を生成
    paramStr = urllib.parse.urlencode(keys)

    #CSVデータの取得
    r = requests.get(url + paramStr).text

    with open(file_path + statsDataId + ".csv","w",encoding='utf-8') as f:
        flg=0
        for line in r.split("\n"):
            
            if flg==1:
                f.writelines(line + "\n")
                
            if "VALUE" in line:
                flg=1

