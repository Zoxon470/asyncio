# Asynchronous email sending

Script for sending a large number of mails asynchronously.

In this script I use smtp server from gmail.

PS I've written this script for practice myself that understand how to work asynchrony.

PSS Maybe current script will be useful for my purposes.

## Run

```.bash
$ pipenv shell
$ python main.py --USERNAME example@gmail.com --PASSWORD mypassword --SUBJECT 'Test subject' --MESSAGE 'Test message'
```

If you wanna see available parameters, write on the terminal follow:

```.bash
$ python main.py -h
``` 

## Run via docker

Build image via follow command:

```.bash
$ docker build --no-cache -f docker/Dockerfile -t email-sender . 
```

Run email sender via follow command:

```bash
$ docker run --rm email-sender --USERNAME example@gmail.com --PASSWORD mypassword --SUBJECT 'Test subject' --MESSAGE 'Test message'
```

Available parameters

| Parameters    | Description   |    Default value  |
| :---         |     :---      |          :--- |   
| `-h, --help`  | show this help message and exit  |               |
| `-H HOST, --HOST HOST`  | Email host | **smtp.gmail.com**        |
| `-u USERNAME, --USERNAME USERNAME`  | Email host username |      |
| `-p PASSWORD, --PASSWORD PASSWORD`  | Email host password |      |
| `-P PORT, --PORT PORT`  | Email host port | **465**              |
| `-f FILE_PATH, --FILE_PATH`  | Email list | **emails.txt**       |
| `-s SUBJECT, --SUBJECT SUBJECT`  | Email subject | **H!**        |
| `-m MESSAGE, --MESSAGE MESSAGE`  | Email message | **Hello, World**  |
