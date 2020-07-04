from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [{
    'name': "Elton's first store",
    'items': [{'name':'my item 1', 'price': 30 }],
    },
    {
    'name': "Elton's second store",
    'items': [{'name':'my item 2', 'price': 15 }],
    },
]

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
    pass
#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    pass
#get /store
@app.route('/store')
def get_stores():
    return jsonify(stores)
#post /store/<name> data: {name :}/item
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    pass
#get /store/<name>/item data: {name :}/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000, debug=True)