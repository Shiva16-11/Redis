import redis
import time

r = redis.StrictRedis()

r.set('startFlag', 0)
r.set('lapValue', 1)
r.hmset('racer1_locations', {"racer_id": "1"})
r.hmset('racer2_locations', {"racer_id": "2"})

r.rpush('slope', 10, 11)

r.rpush('intercept', 10, 11)
r.set('startPosition', (
        r.get('intercept')[1] - r.get('intercept')[0])/(r.get('slope')[1] - r.get('slope')[1]))

slope = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [9, 10]]
intercept = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [9, 10]]
lap_value = 1
distance = 0
output = []
while lap_value <= 10:
    index = 0
    if distance > 10:
        r.set('lapValue', int(r.get('lapValue')) + 1)
        r.rpush('slope', slope.pop())
        r.rpush('intercept', intercept.pop())
        r.set('startPosition', (
            (float(r.lindex('intercept', 1)) - float(r.lindex('intercept', 0))) / (
                float(r.lindex('slope', 1)) - float(r.lindex('slope', 0)))))

        lap_value = int(r.get('lapValue'))
        distance = 0

    time.sleep(1)
    while lap_value == int(r.get('lapValue')) and distance <= 10:
        try:
            d = r.hget('racer1_locations').get('lap')[index]
            D = r.get('racer2_locations').get('lap')[index]
            distance = d - D
            output.append(lap_value, d, D, distance)
            index += 1
        except:
            pass

print(output)








