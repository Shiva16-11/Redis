import redis
import time
import random

r = redis.StrictRedis()

r.set('startFlag', 0)
r.set('lapValue', 1)
r.lpush('racer1_locations' + str(r.get('lapValue')), "0")
r.lpush('racer2_locations' + str(r.get('lapValue')), "0")

r.lpush('racer1slope', 10)
r.lpush('racer2slope', 11)
r.lpush('racer1intercept', 10)
r.lpush('racer2intercept', 11)
print()
r.set('startPosition', -1)

# slope = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [9, 10]]
# intercept = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [9, 10]]
lap_value = 1
distance = 0

output = []
while lap_value <= 10:
    index = 0
    if distance > 10:
        r.set('lapValue', int(r.get('lapValue')) + 1)
        slope_racer1 = random.randint(1, 100)
        slope_racer2 = random.randint(1, 100)
        while slope_racer1 == slope_racer2:
            slope_racer2 = random.randint(1, 100)
        r.rpush('racer1slope', slope_racer1)
        r.rpush('racer2slope', slope_racer2)
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

        lap_value = int(r.get('lapValue'))
        print(distance)
        distance = 0

    time.sleep(1)
    while lap_value == int(r.get('lapValue')) and distance <= 10:
        try:
            print(lap_value, distance)
            d = r.lindex('racer1_locations' + str((r.get('lapValue'))), 0)
            D = r.lindex('racer2_locations' + str((r.get('lapValue'))), 0)
            distance = abs(float(d) - float(D))
            output.append((lap_value, d, D, distance))
            index += 1
        except Exception as e:
            print(e)
            break

print(output)








