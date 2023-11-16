import mysql.connector
from flask import Flask, request, jsonify



class Program_Flask():

    def __init__(self):
        self.program_ID = 1
        self.program_name = "Najlepszy Alarm Domowy !"
        self.status = 0
        self.last_update = "12:33 12.12.2022" 


    def return_hello(self):
        return "Siemanko !!!"
































app = Flask(__name__)
"""
db = mysql.connector.connect(
    host = "192.168.1.77",
    user = "maczo1928all",
    passwd = "Pomidor13",
    database = "siemanko_test"
)
"""


#mycursor = db.cursor()



@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json  # Odczytaj dane JSON z żądania
    print("Otrzymane dane:", data)
    
    plant = data["plant"]
    temp = data["temp"]
    wilg = data["wilg"]
    gleba = data["gleba"]    

    mycursor.execute(f"INSERT INTO plant_0{plant} (temp, wilg, gleba) VALUES (%s,%s,%s)", (temp,wilg,gleba))
    db.commit()


    return jsonify(message="Dane odebrane przez serwer")
