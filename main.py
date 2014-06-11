import flask, flask.views
import foursquare
import os
import functools

app = flask.Flask(__name__)





class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	

app.add_url_rule('/', view_func=Main.as_view('main'))		


app.debug = True
app.run()