from mk_display import mk_display
from get_data import get_data

#取得したcsvファイルを保存するpath
file_path=""

if __name__ == '__main__':

    id_list,appId=mk_display()
    
    for id in id_list:
        get_data(appId,id,file_path)