FROM alpine
MAINTAINER Emily Smith
RUN apk -U add python
RUN mkdir -p /app
ADD renamer.sh /app/renamer.sh
ADD renamer.py /app/renamer.py
RUN chmod 755 /app
ENTRYPOINT [ "/bin/sh", "/app/renamer.sh"]
