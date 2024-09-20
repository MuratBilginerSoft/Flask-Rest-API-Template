# region Proje Kütüphaneleri

from flask import Flask

from App.A4_DbConfig import DbConfig
from App.A3_ModelBase import *
from App.A2_EntityHub import *

# endregion

# region Flask Sınıfından Bir Proje Yarat

app = Flask(__name__)

# endregion

# region Flask App Variables

index = int(input("Enter the index of the database you want to connect to: "))

if index < 0 or index > 3:
    raise Exception("Invalid database index")

DbConfigs = DbConfig(index)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = DbConfig.dbUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.static_folder = "P1_Assets"
app.secret_key = "CheckerMan"

#endregion

# region DB Create

db.init_app(app) # App üzerinde çalışacak bir SqlAlchemy DB Modeli Yaratıldı.

# endregion

# region Projeyi Baslat

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6001, use_reloader=True)

# endregion