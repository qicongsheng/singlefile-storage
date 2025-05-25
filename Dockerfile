FROM python:3.9.21-alpine3.20
MAINTAINER qicongsheng

ENV PORT=5083 \
    DATA_PATH=/data/singlefile \
    API_KEY=your-api-key \
    USERS=admin:admin \
    TZ=Asia/Shanghai

RUN pip install --no-cache-dir singlefile-storage -U && mkdir -p /data/singlefile

CMD ["singlefile-storage"]
