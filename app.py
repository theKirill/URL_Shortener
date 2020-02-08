from flask import Flask, request, json, make_response
from shorten import URL_Shortener

app = Flask(__name__)
shortener = URL_Shortener()

@app.route('/urls', methods=['post'])
def get_short_url():
    res = "{'success': False}"
    status = 400

    if request.json:
        long_url = request.json['long_url']
        success, id = shortener.short(long_url)

        if success:
            res = "{" + "'success': True, 'id': '{}'".format(id) + "}"
            status = 201
        else:
            status = 500

    response = make_response(json.dumps(res))
    response.headers['Content-Type'] = 'application/json'
    return response, status

@app.route('/urls', methods=['get'])
def get_long_url():
    id = request.args.get('id', 'null')

    if id == 'null':
        success = False
    else:
        success, long_url = shortener.get_long_url(id)
    
    if success:
        res = "{'success': True, " + "'long_url': '{}'".format(long_url) + "}"
        status = 200
    else:
        res = "{'success': False}"
        if id == 'null':
            status = 400
        else:
            status = 500

    response = make_response(json.dumps(res))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'    
    response.headers['Pragma'] = 'no-cache'    

    return response, status