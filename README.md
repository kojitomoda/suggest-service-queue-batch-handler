# suggest-service-queue-batch-handler

## 環境
- Python 3.12.4
- aws-sam-cli 1.125.0

## ローカル実行方法
イメージビルド
```
sam build
```

ローカル実行
```
sam local invoke QueuePusherFunction
```


## デプロイ
aws ssoの設定
```
aws sso login
```
docker imageの build
```
sam build
```
デプロイ
```
sam deploy
```

