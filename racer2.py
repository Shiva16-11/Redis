import redis
import time

r = redis.StrictRedis(db=1, charset="utf-8", decode_responses=True)
r.flushall()

while not r.get('startFlag'):
    time.sleep(0.5)
lap = int(r.get('lapValue'))
log = []
print("Racer2 Initialised")
while lap <= 10:
    x = float(r.get('startPosition'))
    while lap == int(r.get('lapValue')):
        slope = int(r.lindex('racer2slope', 0))
        c = int(r.lindex('racer2intercept', 0))
        y = slope * x + c
        # print(y)
        r.lpush('racer2_locations' + str(r.get('lapValue')), y)
        print("lap value is", lap)
        lap = int(r.get('lapValue'))
        print("lap value from redis", int(r.get('lapValue')))
        time.sleep(0.05)
        x += 1
print(log)






