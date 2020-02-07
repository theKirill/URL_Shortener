from flask import Flask, render_template, redirect, request, json, make_response, Response
from shorten import URL_Shortener

app = Flask(__name__)
shortener = URL_Shortener()

@app.route('/urls', methods=['post'])
def get_short_url():
    if request.json:
        long_url = request.json['long_url']
        success, code = shortener.short(long_url)

        if success:
            content = "{"+"'Location':'/urls/{}'".format(code)+"}"
            status=201
        else:
            content = "{'msg': 'Error'}"
            status=500

    return Response(content, status=status, mimetype='application/json')

@app.route('/urls', methods=['get'])
def get_long_url():
    code = request.args.get('code', 'null')
    success, long_url = shortener.get_long_url(code)
    
    if success:
        response = "{'success': True,"+"'long_url': '{}',".format(long_url) + "'short_url': '{}'".format("http://127.0.0.1:5000/urls/{}".format(code))+"}"
        status = 200
    else:
        response = "{'msg':'Error'}"
        status=500
    
    return Response(response, status=status, mimetype='application/json')