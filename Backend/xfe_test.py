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

@app.route('/get_mal_hash', methods=['GET', 'POST'])
def get_mal_hash():

    mal_hash = request.args.get('hash')
    search = "https://api.xforce.ibmcloud.com/malware/{}".format(mal_hash)
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    mal_ip = response["malware"]["origins"]["CnCServers"]["rows"][0]["ip"]

    # Returns info back to the AJAX call
    return jsonify(mal_ip)

@app.route('/get_mal_fam', methods=['GET', 'POST'])
def get_mal_fam():

    mal_family = request.args.get('family')
    search = "https://api.xforce.ibmcloud.com/malware/family/{}".format(mal_family)
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    mal_hashes = response["malware"]

    # Returns info back to the AJAX call
    return jsonify(mal_ip)

@app.route('/get_ips', methods=['GET', 'POST'])
def get_ips():

    ### IP Report ###
    ip = request.args.get('ip')
    search = "https://api.xforce.ibmcloud.com/ipr/{}".format(ip)
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    ip_report = response["history"]

    ### Botnet IPs ###
    search = "https://api.xforce.ibmcloud.com//xfti/bots/ipv4"
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    bot_ip4 = response

    search = "https://api.xforce.ibmcloud.com//xfti/bots/ipv6"
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    bot_ip6 = response

    ### Malware IPs ###
    search = "https://api.xforce.ibmcloud.com/ipr/malware/{}".format(ip)
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    ip_report = response["malware"]

    ### Crytocurrency IPs ###
    search = "https://api.xforce.ibmcloud.com/xfti/cryptomining/ipv4"
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    crypto_ipv4 = response

    search = "https://api.xforce.ibmcloud.com/xfti/cryptomining/ipv6"
    response = requests.get(search, auth=HTTPBasicAuth(api_key, api_pass)).json()
    crypto_ipv6 = response

    # Returns info back to the AJAX call
    return jsonify(mal_ip)

if __name__ == '__main__':
    app.run()