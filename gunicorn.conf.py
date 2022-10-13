from bin.port import load_port

pythonpath = "./"

workers = 3

worker_class = "uvicorn.workers.UvicornWorker"

_port = load_port()
print("Gunicorn running on " 
    + '\033[32m' + f"http://localhost:{_port}" + '\033[0m')

bind = f"127.0.0.1:{_port}"

pidfile = "prod.pid"

daemon = True

proc_name = "ginza_http_api"

accesslog = "./log/access.txt"
errorlog = "./log/error.txt"
