# 簡単プログラミング！その電話番号が実在するかチェックしてみよう

## はじめに

ある電話番号が実在しているのかチェックしたい時があるかもしれません。そんなときは、「numverify」というAPIサービスを利用してみましょう。

このサービスは世界232ヶ国の電話番号照会を提供しています。
電話番号照会APIを利用するためには、アカウントを作成する必要がありますが、簡単ですのでサクッと作ってしまいましょう。

https://numverify.com/


## 動作確認


電話番号は架空？の番号に書き換えてあります。

```json
{
    "valid": true,
    "number": "639455048950",
    "local_format": "09455048950",
    "international_format": "+639455048950",
    "country_prefix": "+63",
    "country_code": "PH",
    "country_name": "Philippines (Republic of the)",
    "location": "",
    "carrier": "",
    "line_type": "mobile"
}
```

## まとめ

気になるあの子に番号もらったけど、本当に実在するのか、どきどきしながら確認するのもいいかもですねｗ。

このサービスの良いところは、

## 関連情報へのリンク

- [numverify API | Free Phone Number Validation & Lookup API](https://numverify.com/)
- [apilayer/phone-number-validation: Global Phone Number Validation & Lookup JSON API. Real-time REST API supporting 232 countries](https://github.com/apilayer/phone-number-validation)
- [apilayer/numverify-API: Free global phone number validation & lookup JSON API](https://github.com/apilayer/numverify-API)
- [その電話番号は実在しますか？チェックをしてみよう](https://github.com/naoland/nemlog-54017) github
- [その電話番号は実在しますか？チェックをしてみよう](https://nemlog.nem.social/blog/54017) nemlog
