# container-images

## streamdeck

Used Python library: https://github.com/abcminiuser/python-elgato-streamdeck

```
docker buildx build --platform linux/amd64 -t ghcr.io/vice-industries/streamdeck:latest streamdeck
docker push ghcr.io/vice-industries/streamdeck:latest
```
