import sys
import requests


def main():
    params = {
        "access_key": "Your API Access Key",
        "number": "9455048950",  # ダミーの電話番号
        "country_code": "PH",
        "format": 1,
    }
    try:
        r = requests.get("http://apilayer.net/api/validate", params=params)
        print(r.text)
        if r.json()["valid"] == True:
            print("存在します")
        else:
            print("存在しません")
    except:
        print(f"エラー: {sys.exc_info()}")


if __name__ == "__main__":
    main()

# 実行結果
# {
#   "valid":true,
#   "number":"639455048950",
#   "local_format":"09455048950",
#   "international_format":"+639455048950",
#   "country_prefix":"+63",
#   "country_code":"PH",
#   "country_name":"Philippines (Republic of the)",
#   "location":"",
#   "carrier":"",
#   "line_type":"mobile"
# }