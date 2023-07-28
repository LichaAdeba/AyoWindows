import requests
import json 
import time

client=requests.session()
def getdata(i):
    url ="https://newsapi.org/v2/everything?q=tesla&from=2022-12-22&sortBy=publishedAt&apiKey=487329e075044488a60f31e03daa5761"
    response = client.get(url)
    jsonobject = json.loads(response.content)
    articles = jsonobject['articles']
    for article in articles:
        print(article['title'])
if __name__=='__main__':
    starttime = time.time()
    for i in range (100):
        getdata(i) 
    finishtime= time.time() 
    programtime = finishtime-starttime 
    print(str(programtime))
