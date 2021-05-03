import random
import redis


# class Redis(object):
#     def __init__(self, host = 'localhost', port = 6379)

random.seed(444)

hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

r = redis.Redis(db = 1)
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute()


# add values to hash in redis

def hash_demo(r):
    """Create a hash value."""
    record = {
        "name": "Shivanshu",
        "description": "Beginner tutorial",
        "e-mail": "shivanshu1611",
        "github": "https://github.com/hackersandslackers"
    }
    r.hmset('business', record)

# add values to list

def list_values_demo(r):
    """Push and pop items from a list."""
    # Add single string to a new list.
    r.lpush('my_list', 'A')
    

    # Push second string to list from the right.
    r.rpush('my_list', 'B')
    

    # Push third string to list from the right.
    r.rpush('my_list', 'C')
   

    # Remove 1 instance from the list where the value equals 'C'.
    r.lrem('my_list', 1, 'C')
   

    # Push a string to our list from the left.
    r.lpush('my_list', 'C')
   

    # Pop first element of our list and move it to the back.
    r.rpush('my_list', r.lpop('my_list'))

# working with sets
def set_values_demo(r):
    """Execute unions and intersects between sets."""
    # Add item to set 1
    r.sadd('my_set_1', 'Y')
    

    # Add item to set 1
    r.sadd('my_set_1', 'X')
    

    # Add item to set 2
    r.sadd('my_set_2', 'X')
    

    # Add item to set 2
    r.sadd('my_set_2', 'Z')
    


   