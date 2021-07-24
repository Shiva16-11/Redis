import redis
import time

r = redis.Redis()

while not r.get('startFlag'):
    time.sleep(0.5)
lap = int(r.get('lapValue'))
log = []
while lap <= 10:
    x = r.get('startPosition')
    slope = r.get('slope')[0]
    c = r.get('intercept')[0]
    y = slope * x + c
    log.append((slope, c, lap))
    dic = r.get('racer1_locations')
    dic['lap'].append(y)
    r.set('racer1_locations', dic)
    lap = r.get('lapValue')
print(log)






