from flask import Flask, request, render_template, jsonify, Blueprint
import requests
from requests.auth import HTTPBasicAuth

api_key = '85b7a821-fdff-4dfa-b066-57bcc6f74f0f'
api_pass = '2a5e88fc-cdae-45dc-b646-d7fb2fa9a08a'

app = Flask(__name__)

@app.route('/get_cnc_ipv4', methods=['GET', 'POST'])
def get_cnc_ipv4():

    search = "https://api.xforce.ibmcloud.com/xfti/c2server/ipv4"
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    cnc_ipv4 = response#["data"][0]#[x for x in response["data"]]

    # What the response looks like
    # {
    #     "FeedCategory": "Botnet Command and Control Server",
    #     "FeedType": "IPv4",
    #     "Version": "0000000010",
    #     "CreationDate": "2019-08-20T07:26:00.000Z",
    #     "IndicatorCount: "2",
    #     "data": ["127.0.0.1", "..."]
    # }

    # Returns info back to the AJAX call
    return jsonify(cnc_ipv4)

if __name__ == '__main__':
    app.run()