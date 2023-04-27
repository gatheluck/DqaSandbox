# DQA Sandbox

![stable](https://img.shields.io/badge/stable-v0.1.3-blue)
[![tests](https://github.com/cvpaperchallenge/Ascender/actions/workflows/lint-and-test.yaml/badge.svg)](https://github.com/cvpaperchallenge/Ascender/actions/workflows/lint-and-test.yaml)
[![MIT License](https://img.shields.io/github/license/cvpaperchallenge/Ascender?color=green)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-blue)](https://github.com/python/mypy)

## Project Organization

```
    ├── .github/           <- Settings for GitHub.
    │
    ├── data/              <- Datasets.
    │
    ├── environments/       <- Provision depends on environments.
    │
    ├── models/            <- Pretrained and serialized models.
    │
    ├── notebooks/         <- Jupyter notebooks.
    │
    ├── outputs/           <- Outputs.
    │
    ├── src/               <- Source code. This sould be Python module.
    │
    ├── tests/             <- Test codes.
    │
    ├── .flake8            <- Setting file for Flake8.
    ├── .dockerignore
    ├── .gitignore
    ├── LICENSE
    ├── Makefile           <- Makefile used as task runner.
    ├── poetry.lock        <- Lock file. DON'T edit this file manually.
    ├── poetry.toml        <- Setting file for Poetry.
    ├── pyproject.toml     <- Setting file for Project. (Poetry, Black, isort, Mypy)
    └── README.md          <- The top-level README for developers.

```

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://github.com/docker/compose)

**NOTE**: Example codes in the README.md are written for `Docker Compose v2`. However, Ascender also should work under `Docker Compose v1`. If you are using `Docker Compose v1`, just replace `docker compose` in the example code by `docker-compose`.

## Prerequisites installation

Here, we show example prerequisites installation codes for Ubuntu. If prerequisites  are already installed your environment, please skip this section. If you want to install in another environment, please follow the officail documentations.

- Docker and Docker Compose: [Install Docker Engine](https://docs.docker.com/engine/install/)
- NVIDIA Container Toolkit (nvidia-docker2): [Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

### Install Docker and Docker Compose

```bash
# Set up the repository
$ sudo apt update
$ sudo apt install ca-certificates curl gnupg lsb-release
$ sudo mkdir -p /etc/apt/keyrings
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker and Docker Compose
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

If `sudo docker run hello-world` works, installation succeeded.

## Embedding

At 2023/04/28, OpenAPI recommends to use `text-embedding-ada-002`.

About `text-embedding-ada-002`:
- Tokenizer: cl100k_base
- Max input tokens: 8191
- Output Dimensions: 1536

## References

- [Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Question Answering over Docs](https://python.langchain.com/en/latest/use_cases/question_answering.html)
- [近傍探索を使ってブログ内検索してみる](https://michimani.net/post/programming-serach-blog-posts-by-nearest-neighbor-search/)
- [ChatGPT APIの運用で必須のツール: LangChainの使い方まとめ (1)](https://qiita.com/sakasegawa/items/d01dafdf0c77da133f24)
- [ChatGPT APIとFaissを使って長い文章から質問応答する仕組みを作ってみる](https://qiita.com/sakasegawa/items/16714fa132e874cab069#embeddingsqa%E3%81%AE%E5%AE%9F%E8%A3%85-bertjapanesetokenizer%E3%82%92%E4%BD%BF%E3%81%86)
- [ベクトル検索ライブラリ Faiss を試す](https://note.com/npaka/n/nb766e344a4fc)
