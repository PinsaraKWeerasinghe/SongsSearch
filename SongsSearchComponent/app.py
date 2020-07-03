import splitter
import classifiere

from flask import Flask,redirect,url_for,render_template,request,json
#from sinling import SinhalaTokenizer
import requests
app = Flask(__name__,template_folder='template')


@app.route('/search',methods=['GET'])
def admin():
    text=request.args['text']
    searchResults=json.dumps(getSearchResults(text))
    return searchResults


def getSearchResults(text):
    tokenList,query=splitter.process_word(text)
    result=classifiere.classify_query(tokenList,100,text)
    print(query)
    print(result["total"]["total"])
    fields=[]
    for field in result.keys():
        if result[field]==True:
            fields.append(field)

    print(fields)

    if(query==" " or query==""):
        reqJson={
            "query": { "match_all": {} },
            "size":result["total"]["total"]
        }  
    elif(result["total"]["rating"]==True):
        reqJson={  
            "query": { 
                "multi_match" : { 
                    "query": query, 
                    "fields": fields 
                } 
            },
            "size":result["total"]["total"],
            "sort":[{
                "views":{"order":"desc"}
            }
            ]
        }
        
    else:
        reqJson={  
            "query": { 
                "multi_match" : { 
                    "query": query, 
                    "fields": fields 
                } 
            },
            "size":result["total"]["total"]
        }
    

    response=requests.get("http://localhost:9200/esmap_v5/_search",json=reqJson)
    return response.json()