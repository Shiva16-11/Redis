import redis
import time

from redis import ConnectionPool

pool = ConnectionPool(host='127.0.0.1', port=6379, db=0,  decode_responses=True)
r = redis.StrictRedis(connection_pool=pool)
r.flushall(asynchronous=False)

while not r.get('startFlag'):
    continue

lap = int(r.lindex('lapValue', 0))
log = []
print("Racer1 initialised")
while lap <= 10:
    x = float(r.get('startPosition'))
    while lap == int(r.lindex('lapValue', 0)):
        slope = int(r.lindex('racer1slope', 0))
        c = int(r.lindex('racer1intercept', 0))
        y = slope * x + c
        # print(y)
        r.lpush('racer1_locations' + str(r.lindex('lapValue', 0)), y)
        # print('racer1_locations' + str(r.lindex('lapValue', 0)))
        lap = int(r.lindex('lapValue', 0))
        time.sleep(0.05)
        x += 1
    print("slope = {}, intercept = {} for lap = {} racer_name = {}".format(slope, c, lap, "Racer1"))
    lap = int(r.lindex('lapValue', 0))
print("Exit")






