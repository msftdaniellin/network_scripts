import importlib
from rq import Worker, Queue, Connection
from redis import Redis

# Connect to Redis
redis_conn = Redis(host='localhost', port=6379, db=0)

# Function to dynamically import and execute a function
def run_function(full_function_name, *args, **kwargs,):
    try:
        # Split the full function name into module and function
        module_name, function_name = full_function_name.rsplit('.', 1)
        # Dynamically import the module
        module = importlib.import_module(module_name)
        # Get the function from the module
        func = getattr(module, function_name)
        # Execute the function and return the result
        return func(*args, **kwargs)
    except Exception as err:
        return (False, {'error': f'Failed to execute {full_function_name} due to {err}'})

if __name__ == '__main__':
    # Connect to the Redis queue
    with Connection(redis_conn):
        # Create a worker to listen to the 'default' queue
        worker = Worker([Queue('default')])
        print('Worker is listening for jobs...')
        worker.work()