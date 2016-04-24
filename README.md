    .____                 _             _             
    |  _ \  _____   _____| | ___  _ __ (_)_ __   __ _
    | | | |/ _ \ \ / / _ \ |/ _ \| '_ \| | '_ \ / _` |
    | |_| |  __/\ V /  __/ | (_) | |_) | | | | | (_| |
    |____/ \___| \_/ \___|_|\___/| .__/|_|_| |_|\__, |
    .                            |_|            |___/
    ======================================================
    .____            _       _     _           _                      _       
    / ___|  ___ __ _| | __ _| |__ | | ___     / \   _ __  _ __  ___  (_)_ __  
    \___ \ / __/ _` | |/ _` | '_ \| |/ _ \   / _ \ | '_ \| '_ \/ __| | | '_ \
    .___) | (_| (_| | | (_| | |_) | |  __/  / ___ \| |_) | |_) \__ \ | | | | |
    |____/ \___\__,_|_|\__,_|_.__/|_|\___| /_/   \_\ .__/| .__/|___/ |_|_| |_|
    .                                              |_|   |_|                  
    ===========================================================================
    .____        _   _                 
    |  _ \ _   _| |_| |__   ___  _ __  
    | |_) | | | | __| '_ \ / _ \| '_ \
    |  __/| |_| | |_| | | | (_) | | | |
    |_|    \__, |\__|_| |_|\___/|_| |_|
    .      |___/                       
    ====================================

Course code for Building Scalable Apps with Google App Engine in Python class:
- [https://www.udacity.com/course/viewer#!/c-ud858/l-3850178979/e-1728658601/m-1759808537](https://www.udacity.com/course/viewer#!/c-ud858/l-3850178979/e-1728658601/m-1759808537)

# Creating AppEngine Project

- Go here: [https://console.developers.google.com](https://console.developers.google.com)
- Select Create project
- Click Edit to view the Project ID field
- Choose a unique project id
    - **udacity-course-1205**
- Give your project a name (doesn't have to be unique)
    - **Udacity Course**
- Click Create

# Set Up Development Environment
- python 2.7
- Google App Engine SDK for Python
    - [Baixar SDK](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

```bash
$ unzip google_appengine_1.9.31.zip
```

```bash
$ sudo joe ~/.bashrc

# Add the following lines to the end of the file
PATH=$PATH:/home/leonardo/Work/udacity.com/developing-scalable-apps-in-python/google_appengine/
export PATH

$ . ~/.bashrc

# check
$ echo $PATH
```

# Hello, World!

## helloworld.py

```python
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
```

## app.yaml

```python
version: 1
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /.*
  script: helloworld.app
```
**Testing the Application**
```bash
$ dev_appserver.py helloworld/
```

# Overview of Endpoints Code

```python
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

# If the request contains path or querystring arguments,
# you cannot use a simple Message class.
# Instead, you must use a ResourceContainer class
REQUEST_GREETING_CONTAINER = endpoints.ResourceContainer(
    # Classe de request.
    message_types.VoidMessage,
    name=messages.StringField(1),
    period=messages.StringField(2)
)

package = 'Hello'

class Hello(messages.Message):
    # Classe de resposta herdeira de messages.Message
    greeting = messages.StringField(1)

@endpoints.api(name='helloworldendpoints', version='v1')
class HelloWorldApi(remote.Service):

    # Cada método da API deve ser "decorado" com @endpoints.method
    # e retornar um objeto "messages.Message"
    @endpoints.method(
        message_types.VoidMessage, #Request
        Hello, #Return
        path = "sayHello",
        http_method='GET',
        name = "sayHello")
    def say_hello(self, request):
        return Hello(greeting="Hello World")

    @endpoints.method(
        REQUEST_GREETING_CONTAINER, #Request
        Hello, #Return
        path = "greetByPeriod",
        http_method = "get",
        name = "greetByPeriod")
    def greet_by_period(self, request):
        greet = "Good {}, {}".format(request.period, request.name)
        return Hello(greeting=greet)

APPLICATION = endpoints.api_server([HelloWorldApi])
```

**Deploying**

- Ref.: https://cloud.google.com/appengine/docs/python/gettingstartedpython27/uploading

```bash
appcfg.py -A udacity-course-1205 -V v1 update helloworld/
```

Ir para:
* https://udacity-course-1205.appspot.com

**API Explorer Page**

*Obs: não funciona localmente. Tem que fazer o deploy.*

Ir para:
- https://udacity-course-1205.appspot.com/_ah/api/explorer


# Write the endpoints functions

# Use the API explorer

# Conference Central APp

# Referências

- [Primer on Python Decorators](https://realpython.com/blog/python/primer-on-python-decorators/)
- [Protocol RPC field classes](https://cloud.google.com/appengine/docs/python/tools/protorpc/messages/fieldclasses)
- [Google Scafolding](https://github.com/GoogleCloudPlatform/appengine-endpoints-helloendpoints-python)
    - Hello World com autenticação
