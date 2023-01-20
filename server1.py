import redis
import random

with redis.Redis() as redis_server1:
    redis_server1.lpush("queue", random.randint(0,10))