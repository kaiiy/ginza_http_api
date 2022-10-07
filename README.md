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
