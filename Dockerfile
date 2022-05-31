FROM python:2.7-alpine
RUN apk update && apk add python python-dev libffi-dev gcc g++ make musl-dev py-pip mysql-client
RUN mkdir -p /opt/CTFd
COPY . /opt/CTFd
VOLUME [ "/opt/CTFd" ]
WORKDIR /opt/CTFd
RUN pip install -r requirements.txt
RUN for d in CTFd/plugins/*; do \
      if [ -f "$d/requirements.txt" ]; then \
        pip install -r $d/requirements.txt; \
      fi; \
    done;
EXPOSE 8000
ENTRYPOINT [ "/opt/CTFd/docker-entrypoint.sh" ]
