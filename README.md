# Flask-Rest-API-Template

1. `python -m venv P6_VirtualEnv`
2. `source P6_VirtualEnv/Scripts/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r P5_PyModules/Requirements.txt`

## Database İşlemleri

P4_Orion>App>A1_CreateFolder.py dosyasını açınız.

Örneğin migrationla yönetmek istediğiniz 3 adet database olsun.

DevDb, TestDb, ProdDb isimlerine sahip olsun.

DevDb > migrations
TestDb > migrationsTest
ProdDb > migrationsProd

değerlerini aşağıdaki gibi diziye ekleyin.

`migrationFolderList = ["P4_Orion/migrations", "P4_Orion/migrationsPro"]`

Bu klasörleri oluşturmak için terminalde

`python P4_Orion/App/A1_CreateFolder.py` komutunu çalıştınız.

P4_Orion içinde bu klasörler oluşmuş olmalı.

Burada başlangıçta migrationsDev klasörü için migrations klasörünü ürettik. Diğer DB'ler için klasör isimlerini aynen yazıyoruz.


P4_Orion/App/A4_DbConfig.py dosyasını açınız.


`self.__dataBases = ['devdb', 'proddb',]` kodu bulup kullanacağınız databaseleri sırayla ekleyiniz.

`self.__migrationFolderList = ["migrationsDev", "migrationsPro",]` bu kodu bulup klasör isimlerini verdiğiniz database sırasına göre veriniz. devdb için klasörü migrationsDev olarak tutulsun, proddb için migrationsPro olara tutulsun istiyoruz. Burada migrations kısmını standart tutarak geri kalan kısmını istediğiniz ismi verebilirsiniz. 

Ancak 1. database klasörü hariç diğer klasörlere ne isim verdiyseniz başlangıçtaki oluşturma kısmında da aynı isimler verilmeli.

Aşağıdaki kod bölümünü bulup database bilgilerinizi giriniz.

``` 
    self.__host = ''
    self.__userName = ''
    self.__password = ""
    
```


MySQL database'i için connection string kısmı aşağıdaki gibi olmalı.

`DbConfig.dbUrl = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(user=self.__userName, pw=self.__password, url=self.__host, db=self.__database)`


Bu işlemleri tamamladıktan sonra tablolarınızı oluşturacak Class'ları, P4_Orion/Entity klasörü içinde oluşturunuz.

Örneğin,

Authentications.py isimli bir dosya ile

''' 

# region Import Packages

from App.A3_ModelBase import *

# endregion

# region Authentication Table

class Authentications(BaseModel, db.Model):

    __tablename__ = "authentications"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(300), unique=True)
    Email = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(300))
    Token = db.Column(db.String(300))
    ConfirmStatus = db.Column(db.Integer)
    CreatedBy = db.Column(db.String(300))
    CreatedAt = db.Column(db.String(30))
    ChangedBy = db.Column(db.String(300))
    ChangedAt = db.Column(db.String(30))
    Revision = db.Column(db.Integer)
    DeleteFlag = db.Column(db.Integer)

    def __init__(self, UserId, Email, Password, Token, ConfirmStatus, CreatedBy, CreatedAt, ChangedBy, ChangedAt, Revision, DeleteFlag):

        self.UserId = UserId
        self.Email = Email
        self.Password = Password
        self.Token = Token
        self.ConfirmStatus = ConfirmStatus
        self.CreatedBy = CreatedBy
        self.CreatedAt = CreatedAt
        self.ChangedBy = ChangedBy
        self.ChangedAt = ChangedAt
        self.Revision = Revision
        self.DeleteFlag = DeleteFlag

# endregion


'''

Bu tabloyu sisteme tanıtmak için, P4_Orion/App/A2_EntityHub.py dosyası içine ekleyiniz.

`from Entity.Authentications import *`

Eklediğiniz her class'ı buraya eklemeniz gerekli.

## Database Migration

`cd P4_Orion` ile klasöre geçiş yapınız.

Başlangıçta her database'in migration dosyalarının oluşması için sırayla bu adımları her database için gerçekleştiriniz.

`python3 Manage.py db init`
`python3 Manage.py db migrate`
`python3 Manage.py db upgrade`

Bu işlemler sırasında her defasında hangi database için işlem yapacağınızı soracaktır. Burada ilgili database'in self.__databases'daki tanımlı sırasına göre indis değerini girebilirsiniz.

devdb için 0 proddb için 1 indis değerlerini vereceğiz.

En son hangi database için işlem yaptıysanız onun klasörünün ismi migrations olarak kalır. Diğer klasörler databaseler için verdiğiniz klasör isimlerine dönerler.

## Yeni Tablo(lar) Ekleme ve Migration

Yeni bir tablo class'ı eklediğinizde bunu database'e işlemek için aşağıdaki adımları gerçekleştiriniz.

İlgili class'ı ya da class'ları A2_EntityHub içine import ediniz.

`python3 Manage.py db migrate`
`python3 Manage.py db upgrade`

İndis değeri olarak hangi database için işlem yapılacaksa onu giriniz.

Bu yönetim şekli sayesinde, tabloları ilk anda tüm databaselere migrate etmenize gerek kalmadan çalışabilirsiniz.



## Tabloyu Models İçine Taşıma

P4_Orion Katmanında oluşturduğunuz class'ı proje içinde kullanabilmek için P2_Sirius/S1_Models/M3_Entities içine taşımalısınız.

Taşıdıktan sonra import tanımını aşağıdaki gibi güncelleyiniz.

`from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import *` 

Metod olarak en altına aşağıdaki metodu ekleyiniz.

``` 

def _to_dict(self):
        
    return {prop: getattr(self, prop) for prop in dir(self) if not prop.startswith('_') and not callable(getattr(self, prop))}


```

Sonuç olarak şöyle bir dosya olmalı.

```

# region Import Packages

from P2_Sirius.S1_Models.M2_EntityBase.EntityBase import *

# endregion

# region Authentication Table

class Authentications(BaseModel, db.Model):

    __tablename__ = "authentications"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.String(300), unique=True)
    Email = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(300))
    Token = db.Column(db.String(300))
    ConfirmStatus = db.Column(db.Integer)
    CreatedBy = db.Column(db.String(300))
    CreatedAt = db.Column(db.String(30))
    ChangedBy = db.Column(db.String(300))
    ChangedAt = db.Column(db.String(30))
    Revision = db.Column(db.Integer)
    DeleteFlag = db.Column(db.Integer)

    def __init__(self, UserId, Email, Password, Token, ConfirmStatus, CreatedBy, CreatedAt, ChangedBy, ChangedAt, Revision, DeleteFlag):

        self.UserId = UserId
        self.Email = Email
        self.Password = Password
        self.Token = Token
        self.ConfirmStatus = ConfirmStatus
        self.CreatedBy = CreatedBy
        self.CreatedAt = CreatedAt
        self.ChangedBy = ChangedBy
        self.ChangedAt = ChangedAt
        self.Revision = Revision
        self.DeleteFlag = DeleteFlag

    def _to_dict(self):
        
        return {prop: getattr(self, prop) for prop in dir(self) if not prop.startswith('_') and not callable(getattr(self, prop))}
# endregion

```

