# Face recognition frontend

## How to set up
``` shell
docker build -t face-recognition-frontend .
docker run -itd -p 80:80 -v /etc/letsencrypt/live/facerecognition.ddns.net/:/app/certs/ face-recognition-frontend
```