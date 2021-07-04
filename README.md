# Webhook-Tester

An application that helps the user to create a unique webhook endpoint and show the data dumped into it in a user-friendly manner. Every hit on the created endpoint is recorded and displayed for the user to inspect the data.

The endpoints and its relevant data are destroyed exactly an hour from when it is created, the reason being these are short-lived endpoints purely used for testing purposes.

Web app is powered by Django, Celery and Redis.

Web App Supports
1. Creating short-lived webhook unique endpoints.
2. Inspecting the data posted to these webhooks.



#### Database Setup
Web App uses Sqlite DB that comes by default with Django, so no need for any extra setup.

#### Setup Dependencies

Run below command from project home after creating a virtual environment.

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.
Major requirements are Django, Celery, Redis

#### Running the server

Below setup is for linux machine. Run below command from project home/src, make sure you have virtual env set up done and you have installed all dependencies using above command.

To run the Django server, execute:

```
python manage.py runserver
```

The application runs on `http://127.0.0.1:5000/` by default.

Along with the application server we need to run celery, celery beat and Redis. Run each of below commands in a new terminal.

Run Redis in a terminal. Then make sure to update redis connection(host & port) settings in src/webhook_tester/settings.py file.

```
redis-server
```


Run celery worker in a terminal from project home/src.

```
celery -A webhook_tester worker -l info
```


Run celery beat in a terminal from project home/src.

```
celery -A webhook_tester worker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```


## Testing
To run the tests, run below command from project home/src/core

```
python tests.py
```

All tests are kept in that file and should be maintained as updates are made to app functionality.


## Home Page

1. Home page has a button to create new webhook endpoints.
2. Home page also shows the list of created webhook endpoints from recent to oldest, which have the number of hits info and time left to expire info.
3. Click the endpoint to go to the endpoint detail page. 

## End Point Detail Page

1. At the top it shows the endpoint url that can be used to post data to the webhook, it also displays the time left to expire.
2. There is a button at the top to copy the web hook URL.
3. After that we see a list of detailed info i.e Query params, Body, Headers that different post calls had, sorted from most recent to oldest.
4. Use below query params with the details page to get more filtered information.
    * past_mins=10, gives the info about all post calls made in past 10 mins
    * last_hits=5, gives the info about the recent 5 post calls. 

### Getting Started

* Base URL: This Web App is at hosted in at [Webhook-Tester](http://4eb84d4511fe.ngrok.io/web-hook/get-list/). 
* The Web App can be run locally at `http://127.0.0.1:8000/`
