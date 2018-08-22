import urllib
import json
import requests

def get_dict(searchWord,appId):

    data_id_dict={}

    #e-StatのURL
    url = "https://api.e-stat.go.jp/rest/2.1/app/json/getStatsList?"
    #設定するキー
    keys = {
        'appId' : appId,
        'lang' : 'J',
        'searchWord' : searchWord
    }
    #keysからパラメータの文字列を生成
    paramStr = urllib.parse.urlencode(keys)
    r = requests.get(url + paramStr).text

    #json形式として読み込む
    res = json.loads(r)
    for i in res["GET_STATS_LIST"]["DATALIST_INF"]["TABLE_INF"]:
        #print(i)
        jlist=[]
        cate=""
        for j in i["TITLE_SPEC"].values():
            jlist.append(j)
        if len(jlist)!=0:
            cate="/".join(map(str,jlist))
        else:
            cate=""
        data_id_dict[cate.replace("　","")]=i["@id"]

    return data_id_dict
    
