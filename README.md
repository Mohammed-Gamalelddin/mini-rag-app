# mini-rag-app

This is a minimal implementation of the RAG model

## Requirements

- Python 3.10 or later

### Install Python using Miniconda

1. Download and install MiniConda from [here] (https://www.anaconda.com/docs/getting-started/installation)
2. Create a new enviornment using the following command:

```bash
$conda create -n mini-rag-app python=3.8
```

3)Activate the envoirnment:

```bash
$conda activate mini-rag-app
```

## Installation

```bash
$ pip install -r requirements.text
```

### Setup the enviornment variables

```bash
$ cp .env.example .env
```

Set your enviornment variable in `.env` file. Like `OPENAI_API_KEY`

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
