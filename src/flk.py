
from flask import Flask, render_template, request
import pickle
import pymongo

from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.optimizers import Adam



app = Flask(__name__)

    
 
  

@app.route("/", methods=['GET', 'POST'])
def get_data():
    temp = request.get_json()
    print('Recieved from client: ',temp)
    for i in range(len(temp)):
        temp[i] = float(temp[i])

    client='mongodb+srv://username:<password>@cluster0.vgt8rtj.mongodb.net/test'
    db= "ML_database"
    dbconnection= "customers"
    myclient = pymongo.MongoClient(client)

    mydb = myclient[db]

    mycon = mydb[dbconnection]
    score = []
    data = mycon.find({'name':'lightGBM'})
   
    for i in data:
        lgb_pickled_model = pickle.loads(i['lightGBM'])
      
        score.append(i["score"])
    
    data = mycon.find({'name':'naive_bayes'})

    for i in data:
        nb_pickled_model = pickle.loads(i['naive_bayes'])
        score.append(i["score"])


    data = mycon.find({'name':'neural_network'})

    for i in data:
        nn_pickled_model = pickle.loads(i['neural_network'])
        score.append(i["score"])
        
    nn_loaded = model_from_json(nn_pickled_model)
    adm = Adam(learning_rate=0.01)
    nn_loaded.compile(loss='binary_crossentropy', optimizer= adm, metrics=['accuracy'])
    return str(lgb_pickled_model.predict([temp])[0])+","+str(nb_pickled_model.predict([temp])[0])+","+str(int(nn_loaded.predict([temp])[0][0]))+","+str(score) # return model prdection




app.run(host="0.0.0.0",debug=True, port=5000)










