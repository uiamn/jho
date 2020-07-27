# JHO

JIS Z8301附属書Gに則ってゐないTweetを発見すると，指摘のリプライを飛ばすbot．

## Getting Started
### setup
1. Twitterのdeveloper申請をし，コンシューマキー等を取得して下さい．
2. `src/.env`を次のやうに書き替へてください．
```
CK=<取得したコンシューマキー>
CSK=<取得したコンシューマシークレットキー>
AT=<botにしたいアカウントのAccess token>
ATS=<botにしたいアカウントのAccess token secret>
```
3. 指摘したい人間をフォローして下さい．

### Docker(docker-compose)を使ってゐる場合
```
$ docker-compose up
```
上記コマンドを入力すると，初回は200件，2回目以降は以前実行した以後にツイートされたものを最大200件取得します．その後判定・リプライを行ひます．

### 使用してゐない場合
TODO

いづれの場合も，cron等で定時実行させるやうにするとよいでせう．

## License
MIT
