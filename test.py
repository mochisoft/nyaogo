from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  items = [{
    'id':'1',
    'name':'rererer',
    'description':'ereere',
    'price':'3232',
    'quantity':'33'
    
  },{
             'id':'2',
             'name':'rererer',
             'description':'ereere',
             'price':'3232',
             'quantity':'33'

           },{
             'id':'3',
             'name':'rererer',
             'description':'ereere',
             'price':'3232',
             'quantity':'33'

           }]
  return render_template('home.html', items=items)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)