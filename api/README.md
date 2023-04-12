# Shoes api 
## Run
```
pip3 install -r requirements.txt
export FLASK_APP=shoes_api
flask run
```

### Docker
```
docker build -t shoes_api .
docker run -p 5000:5000 shoes_api
```
