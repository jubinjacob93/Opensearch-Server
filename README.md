
# Wiki-searcher

The goal of this project is to create a small web-application that offers a somewhat different way to search for information on wikipedia. The application would be running on a web server on http://*.wiki-search.com

Depending on the subdomain used, the web service will return the results of the appropriate search on wikipedia.


## Deployment

To deploy this project run

```bash
  pip install Flask
  C:\path\to\app>set FLASK_APP=wikisearcher.py
```

Testing this may also require an update to your hosts file for each use case, for example to search for the queries 'dog', 'apple' and 'ordinary', the host folder was updated as shown below:
```
	127.0.0.1       wiki-search.com 
	127.0.0.1       dogs.wiki-search.com
	127.0.0.1       ordinary.wiki-search.com
	127.0.0.1       apple.wiki-search.com

```

## API used

```
MediaWiki API 
URL = "https://en.wikipedia.org/w/api.php"

```