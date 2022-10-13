# GiNZA HTTP API

# Requirements

- poetry
- task

# Setup

```sh
$ poetry install
```

# Usage

```sh
$ task dev
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"text": "銀座でランチをご一緒しましょう。"}' http://localhost:8080/
```

# Customization

```sh
#  change a port
$ echo "PORT=45000" > .env
```