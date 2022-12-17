# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import json,datetime

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):
		f = open('data.json','r')
		data = json.load(f)
		f.close()
		return jsonify(data)
	
	if(request.method == 'POST'):
		req_data = json.loads(request.data)

		data = {
			"url": req_data["url"],
			"last_updated": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
		}
		
		with open("data.json", "w") as outfile:
			outfile.write(json.dumps(data, indent=4))

		return jsonify({'data': data})



# driver function
if __name__ == '__main__':
	app.run(debug = False)
