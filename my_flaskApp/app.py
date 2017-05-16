from flask import Flask , jsonify, request, render_template

app = Flask(__name__)


list_stores = [
    {
        "name" : "store1",
        "items" : {
                    "item1": {
                        "item_name" : "item1",
                        "item_desciption" : "this is item 1"
                        },
                    "item2": {
                        "item_name" : "item2",
                        "item_desciption" : "this is item 2"
                        }
                    }
    },
    {
        "name" : "store2",
        "items" : {
                    "item1": {
                        "item_name" : "item1_2",
                        "item_desciption" : "this is item 1_2"
                        },
                    "item2": {
                        "item_name" : "item2_2",
                        "item_desciption" : "this is item 2_2"
                        }
                    }
    }
]

@app.route('/')
def fun():
    return "hello world"


@app.route('/stores')
def test():
    return jsonify(list_stores)

@app.route('/stores', methods = ['POST'])
def addstore():
    request_data = request.get_json()

    list_stores.append(request_data)
    return jsonify(list_stores)

@app.route('/stores/<string:name>')
def get_storeDetails(name):
    for store in list_stores:
        if store['name'] == name:
            return jsonify(store)

@app.route("/stores/<string:storename>/items")
def get_itemdetails(storename):
    for store in list_stores:
        if store['name'] == storename:
            return jsonify(store['items'])

@app.route("/stores/<string:storename>/items", methods = ['POST'])
def update_items(storename):
    request_data = request.get_json()
    for store in list_stores:
        if store['name'] == storename:
            new_item = {
                "item_desciption" : request_data["item_desciption"],
                "item_name" : request_data["item_name"]
            }

            store['items']['item3']= new_item

            return jsonify(list_stores)
    return jsonify({'message':'store not found'})

app.run(port=5000)