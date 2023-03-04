from instagrapi import Client
from flask import Flask, request, jsonify
from config import cookies
import random
app = Flask(__name__)

@app.route('/login-insta', methods=['POST'])
def handle_post_request():
    # Check if the request has JSON data
    if request.method=='POST':
        json_data = request.get_json()
        print(json_data)
        try:
            cl=Client()
            cl.set_country(json_data['country'])
            cl.set_timezone_offset(int(json_data['timeoffset']) * 60 * 60)  # Los Angeles UTC (GMT) -7 hours == -25200 seconds
            cl.login(json_data['instaUserName'],json_data['instaPassword'])
            a=cl.get_settings()
            a['cookies']=random.choice(cookies)
            return {'Status': 'Success','message':a}
        except Exception as err:
            # Return a JSON error response
            return {'Status': 'Fail','message': str(err)}
    else:
        # Return an error response
        return {'error': 'Invalid request'}, 400
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
