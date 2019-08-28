from wit import Wit
from newsapi import NewsApiClient

newsapiKey = ""
witAccess = ""

newsclient = NewsApiClient(newapiKey)
witClient = Wit(access_token = witAccess)

#witResponse = witClient.message("What are the top sports news from India")

def witResponse(message):
    response = witclient.message(message)
    entities = response['entities']
    output = {'newsCategory':None,'location':None}
    for entity in entities:
        #print(entities[entity])
        output[entity]= entities[entity][0]['value']
    return output

#witResponse("Give me latest technology news from India")
newsClient

def getNews(query):
    
    try:
        location=query['location'].lower()
        category = query['category'].lower()
        headlines = newsClient.get_top_headline(q='{}'.format(location),category,pages_size=5)
        
        for item in headlines['articles']:
            element = {
                    'title':item['title'],
                    'image_url':item['urlToimage'],
                    'buttons':[{
                            'type':'web_url',
                            'title':'Read More',
                            'url':item['url']
                            }]
                    }
            elements.append(elemnts)
    except:
        element = {
                'title':'Sorry! I am still learning',
                'image_url':''
                'buttons':[{
                        }]
                }