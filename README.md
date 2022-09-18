# GiNZA HTTP API

# Requirement

- [Poetry](https://github.com/python-poetry/poetry)

# Setup

```sh
$ poetry install
```

# Usage

```sh
# Execute the following command after starting a server.
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"text": "銀座でランチをご一緒しましょう。"}' http://localhost:8080/
```

```sh
# launch a develop server
$ poetry run task run_dev

# launch a product server
$ poetry run task run_prod

# kill a product server
$ poetry run task kill_prod

# test
$ poetry run task test
```