# mini-RAG

This is a minimal implementation of the RAG model for question answering

## Requirments

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [href](https://www.anaconda.com/download/success)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8

```
3) Activate the environment:
```bash
$ conda activate mini-rag
```


#### (Optional) Setup you command line for better readability
``` bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```


## Installation
### Install the required packages

```bash
$ pip install -r requirments.txt
```

### Setup the requirment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

