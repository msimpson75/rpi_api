from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/time-tracker', methods=['POST'])
def json_example():
	request_data = request.get_json()

	activity = request_data['data']['currentTracking']['activity']['name']

	rawTime = request_data['data']['currentTracking']['startedAt']

	time = rawTime

	return '''
            The activity is: {}
            The time started is: {}'''.format(activity, time)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
