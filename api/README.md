# Shoes api 
## Run
```
pip3 install -r requirements.txt
export FLASK_APP=shoes_api
flask run
```

### Docker
```
cd api
docker build -t shoes_api .
docker run -v ./shoes_api:/app/shoes_api --network host -d shoes_api
```
