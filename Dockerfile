FROM python:2

RUN apt-get update && apt-get -y install sudo && \
    useradd -m celery && echo "celery:celery" | chpasswd && adduser celery sudo && \
    pip install -U celery redis "celery[redis]"

COPY proj /home/celery/proj
USER celery
WORKDIR /home/celery/
ENV PYTHONPATH $PYTHONPATH:/home/celery/

CMD celery -A proj worker -l info