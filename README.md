# GiNZA HTTP API

# Usage

```sh
# Execute the following command after starting a server.
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"text": "銀座でランチをご一緒しましょう。"}' http://localhost:8080/
```

```sh
# launch a develop server
$ ./bin/run_develop.sh

# launch a product server
$ ./bin/run_product.sh

# kill a product server
$ ./bin/kill_product.sh

# test
$ pytest
```

# Setup

```sh
$ python3 -m venv venv
$ . ./venv/bin/activate.fish
$ pip3 install -r requirements.txt
```

# Dependencies

- [GiNZA](https://github.com/megagonlabs/ginza)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [Gunicorn](https://github.com/benoitc/gunicorn)

```sh
$ pip3 install \
    ginza ja_ginza_electra \
    fastapi \
    uvicorn[standard] \
    gunicorn
```