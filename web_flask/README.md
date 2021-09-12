## Web Flask
Using a web framework

### 0-hello_route.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
* You must use the option `strict_slashes=False` in your route definition


### 1-hbnb_route.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
* You must use the option `strict_slashes=False` in your route definition


### 2-c_route.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable 
   (replace underscore _ symbols with a space )
* You must use the option `strict_slashes=False` in your route definition


### 3-python_route.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable 
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
* You must use the option `strict_slashes=False` in your route definition


### 4-number_route.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable 
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer
* You must use the option `strict_slashes=False` in your route definition


### 5-number_template.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable 
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer
   * `/number_template/<n>`: display a HTML page only if `n` is an integer:
      * `H1` tag: “Number: `n`” inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition


### 6-number_odd_or_even.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
   * `/`: display “Hello HBNB!”
   * `/hbnb`: display “HBNB”
   * `/c/<text>`: display “C ” followed by the value of the `text` variable 
   (replace underscore _ symbols with a space )
   * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
      * The default value of `text` is “is cool”
   * `/number/<n>`: display “`n` is a number” only if `n` is an integer
   * `/number_template/<n>`: display a HTML page only if `n` is an integer:
      * `H1` tag: “Number: `n`” inside the tag `BODY`
   * `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer:
        * `H1` tag: “Number: `n` is even|odd” inside the tag BODY

* You must use the option `strict_slashes=False` in your route definition

### 7-states_list.py
A script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* After each request you must remove the current SQLAlchemy Session
  * Declare a method to handle `@app.teardown_appcontext`
  * Call in this method `storage.close()`
* Routes:
  * `/states_list`: display a HTML page: (inside the tag`BODY`)
    * H1 tag: “States”
    * UL tag: with the list of all State objects present in DBStorage sorted by name
* You must use the option strict_slashes=False in your route definition


### 8-cities_by_states.py
A script that starts a Flask web application:
* Your web application must be listening on 0.0.0.0, port 5000
* You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
* To load all cities of a State:
  * If your storage engine is DBStorage, you must use cities relationship
  * Otherwise, use the public getter method cities
* After each request you must remove the current SQLAlchemy Session:
  * Declare a method to handle @app.teardown_appcontext
  * Call in this method storage.close()
* Routes:
  * /cities_by_states: display a HTML page: (inside the tag BODY)

