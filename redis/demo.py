import redis
import secrets
import string
import random
import string

#dbsize
#flushall

#Strings
#set (ex), get, del
#mset, mget
#exists, expire, ttl, persist
#incr, decr

#Lists
#rpush, lpush, llen
#lpop, rpop
#lrange

#Hashes
#hset, hget, hgetall, hmset, hmget
#hdel, hexists

#Set
#sadd, smembers, sismember, srem, scard, sdiff, spop, smove

#Atomic: multi, exec, discsard, watch

def generate_interleaved_string():
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    result = ''
    for i in range(4):
        if i % 2 == 0:
            result += random.choice(consonants)
        else:
            result += random.choice(vowels)
    return result

def generate_random_course():
    characters = string.digits
    course_number = ''.join(secrets.choice(characters) for _ in range(3)) 
    course_topic = generate_interleaved_string()
    course_name = f'{course_topic}-{course_number}'
    instructor = generate_interleaved_string()
    students_enrolled = random.randint(10, 100)
    price = round(random.uniform(10, 20), 2)
    rating = round(random.uniform(1, 5), 2)
    return course_name, instructor, students_enrolled, price, rating

def load_courses_to_redis():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for idx in range(1,1001):
        course_entry = generate_random_course()
        key = f'course:{idx}'
        value = ','.join(str(item) for item in course_entry)
        #print(value)
        r.set(key,value, ex=60)
    

#print(generate_random_course())
#load_courses_to_redis()