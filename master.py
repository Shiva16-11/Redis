import datetime
import redis
import time
import random
from redis import ConnectionPool

pool = ConnectionPool(host='127.0.0.1', port=6379, db=0,  decode_responses=True)
r = redis.StrictRedis(connection_pool=pool)

r.lpush('lapValue', 1)
r.lpush('racer1_locations' + str(r.lindex('lapValue', 0)), "0")
r.lpush('racer2_locations' + str(r.lindex('lapValue', 0)), "0")

r.lpush('racer1slope', 10)
r.lpush('racer2slope', 11)
r.lpush('racer1intercept', 10)
r.lpush('racer2intercept', 11)
print()
r.set('startPosition', -1)
r.set('startFlag', 0)

lap_value = 1
distance = 0

output = []
while lap_value <= 10:

    if distance > 10:

        temp = int(r.lindex('lapValue', 0)) + 1
        r.lpush('lapValue', temp)
        time.sleep(1)
        slope_racer1 = random.randint(1, 100)
        slope_racer2 = random.randint(1, 100)
        # avoid m1 == m2
        while slope_racer1 == slope_racer2:
            slope_racer2 = random.randint(1, 100)
        r.lpush('racer1slope', slope_racer1)
        r.lpush('racer2slope', slope_racer2)
        intercept_racer1 = random.randint(2, 120)
        intercept_racer2 = random.randint(1, 150)
        r.lpush('racer1intercept', intercept_racer1)
        r.lpush('racer2intercept', intercept_racer2)
        try:
            value = (float(r.lindex('racer2intercept', 0)) - float(r.lindex('racer1intercept', 0))) / (
                float(r.lindex('racer1slope', 0)) - float(r.lindex('racer2slope', 0)))
        except Exception as e:
            print(e)
            value = 0
        r.set('startPosition', value)
        lap_value = int(r.lindex('lapValue', 0))

        distance = 0

    while lap_value == int(r.lindex('lapValue', 0)) and distance <= 10:

        try:

            d = r.lindex('racer1_locations' + str(r.lindex('lapValue', 0)), 0)
            D = r.lindex('racer2_locations' + str(r.lindex('lapValue', 0)), 0)
            print("Location of racer1 in lap {}".format(d))
            print("Location of racer2 in lap {}".format(D))
            distance = abs(float(d) - float(D))
            output.append((lap_value, d, D, abs(distance), datetime.datetime.now()))
            print("distance between racers in lap {} is {}".format(lap_value, abs(distance)))

        except Exception as e:
            if int(r.lindex('lapValue', 0)) > 10:
                break
            print(e, datetime.datetime.now())
            time.sleep(3)
            continue
    if int(r.lindex('lapValue', 0)) > 10:
        break

print(output)









