pythonpath = "./"

workers = 3

worker_class = "uvicorn.workers.UvicornWorker"

bind = "127.0.0.1:8080"

pidfile = "prod.pid"

daemon = True

proc_name = "ginza_http_api"

accesslog = "./log/access.txt"
errorlog = "./log/error.txt"
