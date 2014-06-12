import flask, flask.views
import foursquare
import os
import functools

app = flask.Flask(__name__)





class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		selection =  str(flask.request.form['TeamName'])
		print selection
		

app.add_url_rule('/', view_func=Main.as_view('main'), methods=['GET', 'POST'])		


app.debug = True
app.run()