import requests
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

lab_credentials = {'win' : 'bX8wvDRLPaCNIzaAjH'}

boxcar_url = 'https://new.boxcar.io/api/notifications'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		title = request.form['m_title']
		message = request.form['m_message']
		people = request.form['person']

		if people is list:
			for person in people:
				params = {'user_credentials': lab_credentials[person],
						'notification[title]': title,
						'notification[long_message]' : message}
				r = requests.post(boxcar_url, params)
		else:
			params = {'user_credentials': lab_credentials[people],
						'notification[title]': title,
						'notification[long_message]' : message}
			r = requests.post(boxcar_url, params)

		return redirect('/')

	else:

		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)