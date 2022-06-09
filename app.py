from flask import Flask , jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

animals = [
    "dog" , "cat","elephant" , "lion", "flamingo" , "eagle" , "owl"
]

@app.get('/api/animals')
def animals_get():
    args = request.args
    animals_Id = int(args.get('animalList'))
    if animals_Id == None:
        return jsonify(animals) , 200
    else:
        return jsonify (animals[animals_Id]), 200

@app.post('/api/animals')
def animals_post():
    animals_data = request.json['snake']
    print(animals_data)
    if not animals_data.get('animals'):
        return jsonify ('Missing required field : animals') , 422
    

@app.patch('/api/animals')
def animals_patch():
    animal_Update = animals_data.get('animals')
    print(animal_Update)
    animal_Update = {
        "golden retriever" , "cat","elephant" , "lion", "flamingo" , "eagle" , "owl"
}
    animals_data = animal_Update

@app.delete('/api/animals')
def animals_delete():
    animals.remove("cat")
    return  jsonify(animals) , 200

