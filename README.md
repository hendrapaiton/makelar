# makelar

Web Proxy for Python Web Crawler and Ethical Hacking



## Installation

Before install the python library for project, first we must clone this repository.

```python
git clone https://github.com/hendrapaiton/makelar.git
```

Make virtual environment for python projects

```python
python3 -m virtualenv venv
source ./venv/bin/activate # for linux
.\venv\Scripts\activate    # for windows
```

Then install the python library consist of scrapy and requests

```python
pip install -r requirements.txt
```



## Proxy List Web Scraping

Web scraping with scrapy using proxy spider available

```python
scrapy crawl proxy
```

And you can look in main project directory there is [proxy.txt](proxy.txt)
with ip address and port number of proxy available inside



## Testing the proxy from the list

After we have proxy list now we can testing the proxy

```python
python testing.py
```


### Happy Proxying!
