from flask import Flask
import requests

URL="https://en.wikipedia.org/w/api.php"

app = Flask(__name__)

#configuring the server name as required
app.config['SERVER_NAME'] = "wiki-search.com:5000"

@app.route("/")
def home():
    return 'Enter you query as the subdomain.'

@app.route('/', subdomain="<SEARCHPAGE>")

#function that searches for the URL
def url_search(SEARCHPAGE):
    if SEARCHPAGE is None:
        return 'Enter you search query as the subdomain'

    title_data = requests.get(URL, params={
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": SEARCHPAGE}).json()

    #creating a list named titles and appending the titles of every search result into it
    titles = []
    for title in title_data['query']['search']:
        titles.append(title['title'])

    #creating a list named urls to which the url of every title is appended
    urls = []
    for title in titles:
        url_data = requests.get(URL, params={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "info",
            "inprop": "url"}).json()


        for key in url_data['query']['pages']:
            urls.append(url_data['query']['pages'][key]['fullurl'])

    #creating a dictionary that contains the links appended as a list to the key named links
    results={"links":urls}
    return results

if __name__ == '__main__':
    app.run(debug=True,port=5000)

