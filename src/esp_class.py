import mysql.connector


db = mysql.connector.connect(
    host = "192.168.0.157",
    user = "maczo1928all",
    passwd = "Pomidor13",
    database = "siemanko_test"
)


mycursor = db.cursor()


mycursor.execute(f"INSERT INTO plant_01 (temp, wilg, gleba) VALUES (%s,%s,%s)", ("1221231","1adsda2","1q12123"))
db.commit()





class Esp_Menager:


    def __init__(self):
        self.description = "This class is responsible for returning ESP measure values"

    def __str__(self):
        return "Kurwa siemanko"

    def return_curent_temp(self):
        return


