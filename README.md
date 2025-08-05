# Meduza PGP Verifier

This is a lightweight FastAPI web app to verify PGP-signed messages in English or Portuguese.

## Features

- Paste signed message or upload `.asc` file
- Verifies using GPG installed on your machine
- Accepts multilingual output (`Good signature` or `Assinatura válida`)

## Requirements

- Python 3.9+
- `gpg` installed on your system
- FastAPI, Uvicorn

## Run locally

```bash
uvicorn main:app --reload --port 8000
```

Then open your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## File structure

```
project/
│
├── main.py
├── templates/
│   ├── form.html
│   └── result.html
└── static/
```

## License

MIT License
