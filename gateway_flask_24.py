import mysql.connector
from flask import Flask, request, jsonify

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



if __name__ == '__main__':
    print("START")
    app.run(host='0.0.0.0', port=5001)
