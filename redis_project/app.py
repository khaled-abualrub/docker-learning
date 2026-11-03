import os
from flask import Flask
import redis

app = Flask(__name__)

# 1. Environment-driven configuration (DevOps best practice)
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

# 2. Connect to the Redis database client
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

@app.route('/count')
def count():
    # 3. Atomic increment: increases the counter by 1 every time the route is hit
    visits = r.incr('visit_count')
    return f"This page has been visited {visits} times."

if __name__ == '__main__':
    # 4. Bind to 0.0.0.0 so Docker can map and expose the port externally
    app.run(host='0.0.0.0', port=5000)