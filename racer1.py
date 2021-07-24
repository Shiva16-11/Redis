import redis
import time

r = redis.Redis()
r.flushall()

while not r.get('startFlag'):
    time.sleep(0.5)
lap = int(r.get('lapValue'))
log = []
while lap <= 10:
    x = float(r.get('startPosition'))
    while lap == int(r.get('lapValue')):
        slope = int(r.lindex('racer1slope', 0))
        c = int(r.lindex('racer1intercept', 0))
        y = slope * x + c
        print(y)
        r.lpush('racer1_locations' + str(r.get('lapValue')), y)
        lap = int(r.get('lapValue'))
        time.sleep(0.05)
        x += 1
print(log)






