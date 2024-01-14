FROM python:3.12.1-bookworm

WORKDIR /workspace

# install poetry via pip
RUN pip install poetry

CMD ["tail", "-f", "/dev/null"]