## 概要
RabbitMQでメッセージを永続化する方法を検証する


## RabbitMQ管理コンソール

- http://localhost:15672
- id/pass: guest/guest


## メッセージをキューにpublish

```bash
docker-compose run --rm app python -m mq.publish
```