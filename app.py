from flask import Flask, request, json, make_response
from shorten import URL_Shortener

app = Flask(__name__)
shortener = URL_Shortener()

@app.route('/urls', methods=['post'])
def get_short_url():
    success = False
    status = 400

    if request.json:
        long_url = request.json['long_url']
        success, key = shortener.short(long_url)

        if success:
            status = 201
        else:
            status = 500

    res = dict()
    res['success'] = success
    res['key'] = key

    response = make_response(json.dumps(res))
    response.headers['Content-Type'] = 'application/json'
    return response, status

@app.route('/urls', methods=['get'])
def get_long_url():
    key = request.args.get('key', 'null')

    if key == 'null':
        success = False
    else:
        success, long_url = shortener.get_long_url(key)
    
    if success and long_url != None:
        status = 200
    else:
        if key == 'null':
            status = 400
        else:
            status = 500

    res = dict()
    res['success'] = success
    res['long_url'] = str(long_url)[2:-1]

    response = make_response(json.dumps(res))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'    
    response.headers['Pragma'] = 'no-cache'    

    return response, status