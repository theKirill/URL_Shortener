from flask import Flask, render_template, redirect, request, json, make_response, Response
from shorten import URL_Shortener

app = Flask(__name__)
shortener = URL_Shortener()

@app.route('/urls', methods=['post'])
def get_short_url():
    if request.json:
        long_url = request.json['long_url']
        success, id = shortener.short(long_url)

        if success:
            response = "{" + "'success': True, 'id': '{}'".format(id) + "}"
            status = 201
        else:
            response = "{'success': False}"
            status = 500
            
        return Response(response, status = status, mimetype = 'application/json')

    return Response("{'success': False}", status = 400, mimetype = 'application/json')

@app.route('/urls', methods=['get'])
def get_long_url():
    id = request.args.get('id', 'null')
    success, long_url = shortener.get_long_url(id)
    
    if success:
        response = "{'success': True, " + "'long_url': '{}'".format(long_url) + "}"
        status = 200
    else:
        response = "{'success': False}"
        status = 500
    
    return Response(response, status = status, mimetype = 'application/json')