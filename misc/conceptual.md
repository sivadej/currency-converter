### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript<p>
_Python and JS are completely different languages with different syntax. Python uses whitespace for blocking while JS uses curly braces. Var definitions are automatically implied in Python, as opposed to needing to use ``let`` or ``const`` or ``var`` in JS. JS is run client-side, typically on the browser. Python is run server-side. Traditionally, Python has been more catered towards stats and data science while JS is more for front-end web development, however both are quite popular in back-end development these days._

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.<p>
  _Check if the key exists before doing anything else with a null check: `if 'c' in dictionary` or `dictionary.get('c')`

- What is a unit test?<p>
  _Tests the output of a single function_

- What is an integration test?<p>
  _Tests involving data passed between functions or external calls_

- What is the role of web application framework, like Flask?<p>
_Provides a way to serve web pages to the end user, acting as a web server with additional functionality._

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?<p>
  _If the app is using URL placeholders, information can be passed in a route URL._

- How do you collect data from a URL placeholder parameter using Flask?<p>
_You can use a `<name>` placeholder in the URL. For example, getting an id route from the URL could look like:_
`@app.route('/home/user/<id>')`<br>
`def user_home(id):`

- How do you collect data from the query string using Flask?<p>
_Assuming the query string contains<br>
`?message="Hello"`<br>
You would put this in your route def:<br>
`message = request.args.get('message')`

- How do you collect data from the body of the request using Flask?<p>
`request.data`

- What is a cookie and what kinds of things are they commonly used for?<p>
_Cookies save state on the client. Stored as key-value pairs. Sent from browser to server for every request to the same domain. Expiration can be set._

- What is the session object in Flask?<p>
_Flask sessions contain info for the current browser. It preserves data types, and are signed so users can't modify data._

- What does Flask's `jsonify()` do?<p>
_Returns a JSON object that can be useful in utilizing http requests from other functions or apps_

- What was the hardest part of this past week for you?<p>
_Understanding the GET/POST/etc flow when using Jinja templates and redirects in Flask._

- What was the most interesting?<p>
_Learning about web scraping with Python_