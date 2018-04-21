import requests
from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG']=True


@app.route('/pokemon/<query>')
def get_name(query):
    try :
        link = 'http://pokeapi.co/api/v2/pokemon/'+str(query)
        r=requests.get(link)
        if r.status_code!=200:
            return_string = "Your query couldn't be found!! Please try again with a real pokemon."
        else:
            a=r.json()
            name = a['name']
            url = a['forms'][0]["url"]
            ID = eval(url.split("-form")[1].strip('/'))
            if query.isdigit():                
                statement = """<html> 
                <body>
                <h1>The Pokemon with id """+query+" is "+name+"""
                </h1>
                </body>
                </html>"""
                
            elif not query.isdigit():
                statement = """<html>
                <body>
                <h1>"""+name+" has id "+str(ID)+"""
                </h1>
                </body>
                </html>"""

            return statement

    except :
        return "Your request could not be processed."


if __name__ == "__main__":
	app.run()