import requests
from bs4 import BeautifulSoup
from typing import Union
from fastapi import FastAPI
import re
import uvicorn

app = FastAPI(title="Direct Download",
              version="0.0.1",
              terms_of_service=
              "Use It Only For Personal Project Else I Need To Delete The Api",
              contact={
                "name": "CYCNO",
                "url": "https://github.com/CYCNO",
              },
              docs_url='/')


@app.get('/mediafire')
def mediafire(link: Union[str, None] = None):
  try:
    down_link = str(link)
    mid = down_link.split('/', 5)
    if mid[3] == "view":
      mid[3] = "file"
      down_link = '/'.join(mid)
      print(down_link)
    r = requests.get(down_link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"class": "input popsok"}).get("href")
    a = str(a_href)
    id = link.split('/', 5)[4]
    a_byte = soup.find("a", {"class": "input popsok"}).get_text()
    a_name = soup.find("div", {"class": "dl-btn-label"}).get_text()
    details = soup.find("ul", {"class": "details"})
    li_items = details.find_all('li')[1]
    some = li_items.find_all("span")[0].get_text().split()
    dat = list(some)
    down = a_byte.replace(" ", "").strip()
    time = dat[1]
    date = dat[0]
    byte = down.split("(", 1)[1].split(")", 1)[0]
    name = a_name.replace(" ", "").strip()
    return {
      "status": "true",
      "data": {
        "file": {
          "url": {
            'directDownload': a,
            "original": link,
          },
          "metadata": {
            "id": id,
            "name": name,
            "size": {
              "readable": byte
            },
            "DateAndTime": {
              "time": time,
              "date": date
            }
          }
        }
      }
    }

  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"


@app.get('/gdrive')
def gdrive(link: Union[str, None] = None):
  try:
    down = link.split('/', 6)
    url = f'https://drive.google.com/uc?export=download&id={down[5]}'
    session = requests.Session()

    response = session.get(url, stream=True)

    # Get the headers from the response
    headers = response.headers
    # Get the Content-Disposition header
    content_disp = headers.get('content-disposition')

    # Extract the filename from the content disposition header using regex
    filename = None
    if content_disp:
      match = re.search(r'filename="(.+)"', content_disp)
      if match:
        filename = match.group(1)

    # Get the Content-Length header
    content_length = headers.get('content-length')

    # Get the Last-Modified header
    last_modified = headers.get('last-modified')

    # Get the Content-Type header
    content_type = headers.get('content-type')

    return {
      "status": "true",
      "data": {
        "file": {
          "url": {
            'directDownload': url,
            "original": link,
          },
          "metadata": {
            "id":
            down[5],
            "name":
            filename if filename else 'No filename provided by the server.',
            "size": {
              "readable":
              f'{round(int(content_length) / (1024 * 1024), 2)} MB' if
              content_length else 'No content length provided by the server.',
              "type":
              content_type
              if content_type else 'No content type provided by the server.'
            },
            "DateAndTime":
            last_modified if last_modified else
            'No last modified date provided by the server.',
          }
        }
      }
    }

  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get('/anonfiles')
def anonfiles(link: Union[str, None] = None):
  try:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"id": "download-url"}).get("href")
    a = str(a_href)
    id = link.split('/', 4)[3]
    jsondata = requests.get(
      f'https://api.anonfiles.com/v2/file/{id}/info').json()
    jsondata['data']['file']['url']['directDownload'] = a
    del jsondata['data']['file']['url']['full']

    return jsondata
  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get('/filechan')
def filechan(link: Union[str, None] = None):
  try:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"id": "download-url"}).get("href")
    a = str(a_href)
    id = link.split('/', 4)[3]
    jsondata = requests.get(
      f'https://api.filechan.org/v2/file/{id}/info').json()
    jsondata['data']['file']['url']['directDownload'] = a
    del jsondata['data']['file']['url']['full']

    return jsondata
  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get('/letsupload')
def letsupload(link: Union[str, None] = None):
  try:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"id": "download-url"}).get("href")
    a = str(a_href)
    id = link.split('/', 4)[3]
    jsondata = requests.get(
      f'https://api.letsupload.cc/v2/file/{id}/info').json()
    jsondata['data']['file']['url']['directDownload'] = a
    del jsondata['data']['file']['url']['full']

    return jsondata
  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get('/megaupload')
def megaupload(link: Union[str, None] = None):
  try:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"id": "download-url"}).get("href")
    a = str(a_href)
    id = link.split('/', 4)[3]
    jsondata = requests.get(
      f'https://api.megaupload.nz/v2/file/{id}/info').json()
    jsondata['data']['file']['url']['directDownload'] = a
    del jsondata['data']['file']['url']['full']

    return jsondata
  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get('/myfile')
def myfile(link: Union[str, None] = None):
  try:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    a_href = soup.find("a", {"id": "download-url"}).get("href")
    a = str(a_href)
    id = link.split('/', 4)[3]
    jsondata = requests.get(
      f'https://api.myfile.is/v2/file/{id}/info').json()
    jsondata['data']['file']['url']['directDownload'] = a
    del jsondata['data']['file']['url']['full']

    return jsondata
  except:
    return "{'status': 'false', 'message': 'Invalid Link'}"

uvicorn.run(app, host='0.0.0.0')
