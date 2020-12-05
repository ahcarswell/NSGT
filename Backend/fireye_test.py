import hashlib
import hmac
import http.client
import email
import urllib
import time

ACCEPT_VERSION = '2.5'


def get_headers(prv, pub, query):
    time_stamp = email.Utils.formatdate(localtime=True)
    new_data = query + ACCEPT_VERSION + 'application/json' + time_stamp
    hashed = hmac.new(prv, new_data, hashlib.sha256)
    headers = {
        'Accept': 'application/json',
        'Accept-Version': ACCEPT_VERSION,
        'X-Auth': pub,
        'X-Auth-Hash': hashed.hexdigest(),
        'Date': time_stamp
    }
    return headers


def data(url, query, pub, prv):
    headers = get_headers(prv, pub, query)
    load_data(url, query, headers)


def load_data(url, query, headers):
    con = http.client.HTTPSConnection(url)
    con.request('GET', query, '', headers)
    resp = con.getresponse()

    chunk = ""
    response=""
    while True:
        chunk=resp.read(50000)
        if chunk:
            response+=chunk
        else:
            break

    status = resp.status
    if status == 204:
        print ("Status:204 SearchResultNotFound")
    else:
        print (response)


def data_ioc(url,public_key, private_key):
    print ("iocs Response:")
    #30 days back start date
    startDate = int(time.time()) - 2592000
    endDate = int(time.time())
    ioc_query = '/view/iocs?'+'startDate='+str(startDate)+'&endDate='+str(endDate)
    return data(url, ioc_query,  public_key, private_key)


def data_text_search_simple(url, public_key, private_key):
    print ("text_search_simple Response:")
    # simple text search
    params = {
        'text': 'Stack-Based Buffer Overflow Vulnerability',
        'limit': '10',
        'offset': '0'
    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    data(url, text_search_query,  public_key, private_key)


def data_text_search_filter(url, public_key, private_key):
    print ("text_search_filter Response:")
    # filter text search
    params = {
        'text': 'malware',
        'filter': 'threatScape:cyberEspionage,cyberCrime&riskRating:HIGH,LOW&language:english',
        'sortBy': 'title:asc,reportId:desc',
        'limit': '10',
        'offset': '5'
    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    print('text_search_query', text_search_query)
    data(url, text_search_query,  public_key, private_key)

    params = {
        'text': 'malware',
        'filter': 'cveId:~\'CVE\''

    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    data(url, text_search_query,  public_key, private_key)


def data_text_search_title(url, public_key, private_key):
    print ("text_search_title Response:")
    # title phrase search
    params = {
        'text': 'title:"Software Stack 3.1.2"'
    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    data(url, text_search_query,  public_key, private_key)


def data_text_search_wildcard(url, public_key, private_key):
    print ("text_search_wildcard Response:")
    # wild card text search
    params = {
        'text': 'zero-day*',
        'limit': '10',
        'offset': '0'
    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    data(url, text_search_query,  public_key, private_key)


def data_text_search_sensitive_reports(url, public_key, private_key):
    print ("text_search_sensitive_reports Response:")
    params = {
        'text': 'title:"Latin American"',
        'customerIntelOnly': True
    }
    text_search_query = '/search/text?' + urllib.urlencode(params)
    data(url, text_search_query,  public_key, private_key)


def data_advanced_search_filter_indicators(url, public_key, private_key):
    print ("advanced_search_filter_indicators Response:")
    # Indicator field md5
    advanced_search_query = '/search/advanced?query=md5=~8512835a95d0fabfb&fileIdentifier=[Victim;Attacker]'
    data(url, advanced_search_query,  public_key, private_key)


def data_basic_search(url, public_key, private_key):
    print ("basic_search Response:")
    #Query for search
    basic_search_query = '/search/basic?ip=66.34.253.56'
    data(url, basic_search_query,  public_key, private_key)


if __name__ == '__main__':
    #API-Host
    url = 'api.isightpartners.com'

    #User keys
    public_key = 'PUBLIC_KEY'
    private_key = 'PRIVATE_KEY'