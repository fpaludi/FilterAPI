# API REST Example

This API is used to filter countries with a life satisfaction indexes greater than a value provided by the user. In order to support extra types of filters it is necessary to add new endpoints on the views module at api folder.

## API file structure
The file structure is shown next:

FilterAPI  
│  
├── top_app.py  
├── app_config.py  
├── README.md  
├── requirements.txt  
├── api  
│   ├── data  
│   │   └── BLI_28032019144925238.csv  
│   ├── models.py  
│   ├── templates  
│   │   └── index.html  
│   └── views.py  
├── tests  
│   └── unit  
│       ├── test_models.py  
│       └── test_views.py  
├── utils  
    └── explore_data.ipynb  


## Run the application
### With Python Virtual Environment 
In order to download and run the application it is necessary to follow the next steps:

1. Installing necessary packages
```
sudo apt install git
sudo apt install python3-pip
sudo apt-get install python3-venv
```

2. Downloading application from GitHub
```
mkdir try_app
cd try_app
git clone 
```

3. Creating python virtual environment and installing dependencies
```
python3.7 -m venv venv
pip install -r requirements.txt
```

4. Testing the application:
```
python -m  pytest -v
```

5. Running the application
```
export FLASK_APP=top_app.py
flask run
```
In your favorite web browser insert one of the following:
  * http://localhost:5000 
  * http://localhost:5000/api/v1.0/countries/all
  * http://localhost:5000/api/v1.0/life_satisfaction_gt/<index>

Once you have explored all the endpoints, you can close the application by pressing CTRL+C on the terminal where the app is running

### With Docker
If you know what Docker is and you have it installed (as the installation steps can be tricky depending on the OS, they are avoided here), it is possible to run the application following the next steps:
1. Building docker image
```
docker build -t filter_app .
```
After some minutes...
2. Running docker container
```
docker run -p 5000:5000 filter_app:latest
```
3. Exploring the endpoints
  * http://localhost:5000 
  * http://localhost:5000/api/v1.0/countries/all
  * http://localhost:5000/api/v1.0/life_satisfaction_gt/<index>

