# Project Architecture Anlamak #

# 1 App.py

Proje App.py dosyasından start olur.

`app = Flask(__name__)` bir flask nesnesi tanımlanır.

`FlaskStart().starter(app, __name__)` FlaskStart class'ı ile uygulama ayağa kaldırılır.

FlaskStart içinde uygulamanın ihtiyaç duyduğu ilk config ayarlamaları yapılır.

# 2 FlaskStart.py (P3_Scorpius/S1_App/Starter/FlaskStart.py)

`self.PrepareSystems.starter(app)` sistem hazırlıkları PrepareSystems sınıfı içinde yapılır.

`app.run(host='0.0.0.0', port=Configuration.appConfig["appPort"], use_reloader=True)` 

Bu kod satırı, bir Flask uygulamasını başlatmak için kullanılıyor ve Flask uygulamasının hangi IP adresinde ve hangi portta dinleyeceğini belirliyor. Ayrıca use_reloader=True argümanıyla Flask'ın uygulamayı otomatik olarak yeniden başlatma mekanizmasını aktif hale getiriyor.

app.run(): Flask uygulamasını başlatmak için kullanılan fonksiyon. Bu fonksiyon çalıştığında Flask uygulaması belirtilen adreste ve portta HTTP isteklerini dinlemeye başlar.

host='0.0.0.0': Flask uygulamasının dış dünyaya açık olmasını sağlar. Yani, bu ayarla uygulama sadece localhost'ta (127.0.0.1) değil, sunucuya bağlı tüm ağ arayüzlerinden erişilebilir hale gelir. Genelde sunucu ortamlarında kullanılır.

port=Configuration.appConfig["appPort"]: Flask uygulamasının dinleyeceği port numarasını belirler. Burada Configuration.appConfig["appPort"] ifadesi, port numarasının dinamik olarak bir konfigürasyon dosyasından veya yapılandırma ayarlarından alındığını gösterir.

use_reloader=True: Flask uygulaması üzerinde yapılan kod değişikliklerini otomatik olarak algılayıp, uygulamayı yeniden başlatır. Bu özellikle geliştirme ortamında faydalıdır, çünkü kodda yapılan değişiklikler sonrasında sunucuyu elle yeniden başlatmaya gerek kalmaz.

# 3 Configuration.py (P3_Scorpius/S6_Utils/Configuration.py)

Uygulama configuration bilgileri bu dosya içinde belirlenir.

Bu dosyadaki bilgiler çalışma ortamına göre güncellenir.


### appConfig


```

appConfig = {
        
        "staticFolder"      : "P1_Assets",
        "secretKey"         : "FlaskTemplate",
        "userFolderPath"    : os.path.join(os.getcwd(),"P1_Assets","Users"),
        "appPort"           : 6001,
        "rootUrl" : "http://localhost:6001",
    }


```

Burada scretKey'i kendi projenize göre güncelleyebilirsiniz.

Bir kullanıcı bazlı klasörleme yapacaksanız, userFolderPath değişkenini kullanabilir ve oluşacağı yeri burada tanımlayabilirsiniz.
Standart tanımlaması Kök dizinde P1_Assets içinde Users ismiyle oluşmuş klasöre işaret eder.

Burada farklı klasörleme sistemleri ve pathleri kullanacaksınız key değerlerini verip değişken pathlerine atama yapabilirsiniz.

appPort: Uygulamanın hangi porttan ayağa kaldırılacağını belirleriz. İstediğiniz port değerini verebilirsiniz.

rootUrl: rootUrl uygulamanın ayağa kalktığı url'in ismidir. 


### folderNames


```

folderNames ={

        "Log" : "Log",
        "Temp"    : "Temp",
        "Image"   : "Image",
    }


```

Uygulama içinde başlangıçta oluşturulması istenen Klasör isimleri bu değişkenle tutuluyor. İstediğiniz key ile istediğiniz kadar klasör ismi ekleyebilirsiniz. 


### dbConfig



```
dbConfig = {
        
        "dbType": "MySQL",
        "database": "devdb",
        "host": "prowthdb.mysql.database.azure.com",
        "user": "muratbilginer",
        "password": "Tj_G{z=<4$'3qg-#",
        "port": "3306",
        "dbUrl" : None
    }

```

Database bilgileri dbConfig değişkeni ile tutulur. 

dbType hangi veri tabanı sistemini kullanıyorsanız onu yazmalısınız. 

Ortamına göre database ismi güncellenmelidir.


### mailConfig


```
mailConfig = {

        "email"     : "mbilginer@brainytech.net",
        "password"  : "nqybvwitviwpefnw",
        "server"    : "smtp.yandex.com.tr",
        "port"      : 465,
    }

```

Uygulamanız üzerinde mail gönderme işlemi yapacaksınız mailConfig bilgileriyle gönderim yapacağınız mailin smtp ayarlarını girebilirsiniz.


# 4 PrepareSystem.py (P3_Scorpius/S1_App/SystemConfig/PrepareSystem.py)

Sistem ayarlamalarının app flask nesnesine aktarılıp uygulamanın ayağa kalkması için router yapısına aktardığı kısımdır. Buradaki bilgiler Router ile işlendikten sonra BluePrint yapısı kurulur ve FlaskStart.py içindeki PrepareSystem class'ı işini tamamlamış olur uygulama hazır hale gelmiştir.

Buradaki bilgilerle uygulama Run edilir.

`app.config['DEBUG'] = True` 

bu komut eğer dev ortamında True prod ortamında False olması tavsiye edilir. Anlamı True verdiğinizde uygulama üzerinde herhangi bir dosyada bir güncelleme yaptığınzıda projeyi baştan başlatma gereksinimi duymadan güncel kodlarla yenide ayağa kaldırır.

False verilmesi durumunda değişikliklerin uygulanabilmesi için uygulamanın durdurulup yeniden başlatılması gerekir.

`dbUrl = self.HeroKits.setDbUrl(Configuration().dbConfig["dbType"], Configuration().dbConfig["database"], Configuration().dbConfig["host"], Configuration().dbConfig["user"], Configuration().dbConfig["password"])`

Bu komut SQLAlchemy'nin kullanacağı DbConnection bilgilerini oluşturur ve dbUrl isimli değişkene atar.

Burada bu işlem yapılırken HeroKits sınıfı içinde bulunan setDbUrl fonksiyonu kullanılır.


İlgili fonksiyon

```
def setDbUrl(self, databaseType, databaseName, host=None, userName=None, password=None):

        dbUrl = None

        if databaseType == "SQLite":

            dbUrl = self.dbUrl = 'sqlite:///{}'.format(databaseName)

        elif databaseType == "MySQL":

            dbUrl = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(user=userName, pw=password, url=host, db=databaseName)
    
        return dbUrl

```

Bu fonksiyon dbType'a göre gönderilen parametrelerle kullanılacak dbUrl değişkenini oluşturur.


`Configuration().dbConfig["dbUrl"] = dbUrl` burada oluşturulan dbUrl uygulama boyunca her yerde istenildiğinde kullanılabilmesi için başlangıçta Configuration.py içinde bulunan dbConfig değişkeni içindeki dbUrl key'ine bir değer olarak atanır.

Kullanılmak istediğinde buradan çağrılabilir.

Yoksa bu değişkeni her kullanacağınız yer de tekrar üretmeniz gerekirdi.


```

app.config['SQLALCHEMY_DATABASE_URI'] = dbUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.static_folder = Configuration().appConfig["staticFolder"]
app.secret_key = Configuration().appConfig["secretKey"] 

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 1600 * 1000 * 1000

```

app.config['SQLALCHEMY_DATABASE_URI'] = dbUrl: Bu satır, Flask-SQLAlchemy eklentisi için veritabanı bağlantı URL'sini ayarlıyor. dbUrl, veritabanına bağlanmak için gerekli olan URL'yi içerir (örneğin, PostgreSQL, MySQL veya SQLite gibi bir veritabanı). Bu URL, veritabanı türü, kullanıcı adı, parola, sunucu adresi ve veritabanı adını içerir.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False: Flask-SQLAlchemy, veri modellerindeki değişiklikleri izleyebilir. Ancak bu izleme işlemi ekstra bellek tüketimine neden olabilir. Bu satır, performans optimizasyonu amacıyla bu özelliği kapatıyor (yani, veri modeli değişiklikleri izlenmiyor).

app.static_folder = Configuration().appConfig["staticFolder"]: Bu satır, Flask uygulamasının statik dosyalarının (CSS, JavaScript, resimler gibi) nerede bulunacağını belirler. Configuration().appConfig["staticFolder"] ifadesi, statik dosya yolunun dinamik olarak bir yapılandırma ayarından alındığını gösteriyor.

app.secret_key = Configuration().appConfig["secretKey"]: Flask uygulamalarında gizli anahtar, güvenlik amacıyla kullanılır. Bu gizli anahtar, oturum verilerini ve bazı güvenlik işlevlerini (örneğin CSRF koruması) şifrelemek için kullanılır. Burada secretKey, yapılandırma dosyasından alınan bir değer.

CORS(app, resources={r"/*": {"origins": "*"}}): Bu satır, Flask uygulamasında CORS (Cross-Origin Resource Sharing) özelliğini etkinleştiriyor. CORS, bir web uygulamasının farklı bir kaynak (domain, port veya protokol) üzerinden yapılan istekleri kabul etmesini sağlar. Burada tüm yollar (/*) için origins="*" kullanılarak, uygulamanın herhangi bir kaynaktan gelen istekleri kabul etmesi sağlanıyor.

app.config['CORS_HEADERS'] = 'Content-Type': CORS isteklerinde kabul edilecek özel başlıkları belirler. Burada Content-Type başlığına izin veriliyor, yani isteklerde bu başlık bulunursa kabul edilecektir.

app.config['MAX_CONTENT_LENGTH'] = 1600 * 1000 * 1000: Bu satır, Flask uygulamasının kabul edebileceği maksimum içerik boyutunu ayarlıyor. 1600 * 1000 * 1000 bayt (yaklaşık 1.6 GB) olarak belirlenmiş. Bu genellikle büyük dosya yüklemelerini kontrol etmek için kullanılır.


`db.init_app(app)`

Bu satır, Flask-SQLAlchemy eklentisinin uygulama ile birlikte başlatılmasını sağlar. db.init_app(app), veritabanı bağlantısının Flask uygulamasıyla entegre olmasını sağlar.

`self.Routers.main(app)` router ayarlarına başlayabilmek için Routers sınıfının main fonksiyonuna oluşturduğumuz app flask nesnesi verilerek başlatılır.


# 5. Router.py (P3_Scorpius/S1_App/Router/Router.py)

Bu class uygulama için oluşturulacak blueprint yapısının parametrelerini belirlediğimiz yerdir. 

Burası bir endpointin istenen class'a gidip logic'ini çalıştırabilmesi için en önemli yerdir.


```

# ["BluePrintName", "ClassName", "routeUrl"]

bluePrintParameter =  {

    "home" : ["home", "Home", "/"],
    "signup" : ["signup", "SignUp", "/auth/signup"],
    "signin" : ["signin", "SignIn", "/auth/signin"],
    "dashboard" : ["dashboard", "Dashboard", "/dashboard"],
    "confirm" : ["confirm", "Confirm", "/confirm"],
    "signout" : ["signout", "SignOut", "/auth/signout"],

    "site"  : ["site", "Site", "/sites"],
    "sitedata"  : ["sitedata", "Site", "/site"],
    "siteadd"   : ["siteadd", "Site", "/site/add"],
    "siteupdate" : ["siteupdate", "Site", "/site/update/<id>"],
    "sitedelete" : ["sitedelete", "Site", "/site/delete/<id>"],
    "sitedetail" : ["sitedetail", "Site", "/site/detail/<id>"],

}



```

Her endpoint noktası için bluePrintParameter dictionary'si içine ilgili tanımlamalar eklenmelidir.

/ root url'i home class'ı ile ele alacağımızı varsayarak buna ait blueprint yapısını oluşturmak istediğimizde,

`"home" : ["home", "Home", "/"],`

bu endpoint yakalayacka dictionary'i key'ini belirliyoruz. Burada küçük harfle yazıyoruz keyleri.

0. indis blueprintName : home
1. indis ClassName : Home bu Url'e gelen istekler ana dağıtıcı olarak hangi class'a gidecek bunun ismini veriyoruz.
2. indis endpoint Url : Bu işlem hangi url'e geldiğinde gerçekleşecek bu endpoint noktasını belirliyoruz.


```

for data in bluePrintParameter.values():

    bluePrint = BluePrintQuee(data[0])
    bluePrint.createBluePrint(data[0], data[2], data[1])

    app.register_blueprint(bluePrint.BluePrintBps)


```

Elimizdeki parametre üzerinde bir döngü kurup register_blueprint yapısının kurulmasını sağlıyoruz.

Burada registerblueprint kuyruğunu BluePrintQuee class'ı sayesinde yaparız. Bu class aşağıda anlatılmıştır.

İlgili blueprint nesnesi için BluePrintQuee'ye değişkeni gönderilip bir blueprint nesnesi oluşturulur.

Sonra bu sınıf içindeki createBluePrint fonksiyonu kullanılarak, buraya gönderilen Class ve Url bilgileri ile blueprint kurulur.


`app.register_blueprint(bluePrint.BluePrintBps)` son olarak blueprint kuyruğuna ilgili endpoint bu kod parçası ile eklenir. Böylece / endpointine gelen bir istek flask tarafından karşılanıp ilgili class'ına gönderilip işlemler yapılıp bir response'un dönmesi sağlanır.


# 6 BluePrintQuee.py (P3_Scorpius/S1_App/Router/BluePrintQuee.py)

`self.BluePrintBps = Blueprint(bluePrintName, __name__)`  bir blueprint yapısına dahil olacak bir endpoint parçası oluşturmak isterseniz. Bir Flask'in içinde bulunan BluePrint class'ı kullanılır. bluePrintName ve __name__ parametreleri gönderdiğimzide bizim için app_register'a eklenecek bir blueprint parçacığı oluşturur.

Bu komut ile bunu sağlıyoruz. 

`self.__requestMethods = ["GET","POST","PATCH","DELETE","PUT", "get","post","patch","delete","put"]` burada request ile gelecek isteklerde kabul edilecek metodların bir listesini oluşturduk. Bu liste üzerinde kontrol sağlayıp istediğimiz metodlar harici bir yöntemle istek gelmiş ise bu isteği işleme almadan decline edeceğiz.


```

def createBluePrint(self, bluePrintName, endPointName, className, **kwargs):
    @self.BluePrintBps.route(f"{endPointName}", methods=self.__requestMethods)
    def page(id = None, productId = None, token=None):

        return self.Starters.start(className, bluePrintName=bluePrintName, id=id, productId=productId, token=token, **kwargs)

```

self: Bu metot, bir sınıfın içinde tanımlı olduğundan, metot çağrılırken sınıfın örneğine erişimi sağlar.
bluePrintName: Blueprint'in adını temsil eder.
endPointName: Blueprint'in hangi URL yolunda (endpoint) tanımlanacağını belirtir.
className: Blueprint'te çalıştırılacak sınıfın adını belirler.
**kwargs: Dinamik ek parametreler alabilir. Bu, ek esneklik sağlar ve istenilen herhangi bir sayıda parametreyi fonksiyona iletebilirsin.

### Rota Tanımlama

`@self.BluePrintBps.route(f"{endPointName}", methods=self.__requestMethods)`

self.BluePrintBps.route(): Bu satır, Flask blueprint'ine bir rota (endpoint) ekler.

f"{endPointName}": Rota URL'si olarak endPointName değişkeni kullanılıyor, yani bu değişken dinamik olarak rota URL'sini belirler.

methods=self.__requestMethods: Rota için HTTP metodları belirleniyor (örneğin GET, POST, vs.). Bu da self.__requestMethods değişkeninden alınıyor.

Bu decorator (@), page fonksiyonunu rota ile eşleştirir. Yani, bir kullanıcı endPointName URL'sine bir istek gönderdiğinde bu fonksiyon tetiklenecek.


### Rota Fonksiyonu

`def page(id=None, productId=None, token=None):`

Bu, yukarıdaki rota için tanımlanmış fonksiyondur. id, productId, ve token parametreleri varsayılan olarak None değerine sahiptir, yani bu parametreler rota ile birlikte istekte gönderilirse bu değerler kullanılır, aksi takdirde None olacaktır.

### İşlem Yapma

`return self.Starters.start(className, bluePrintName=bluePrintName, id=id, productId=productId, token=token, **kwargs)`

self.Starters.start(): Bu satır, Starters adında bir nesnenin start metodunu çağırır.

Bu metoda className, bluePrintName, id, productId, token ve **kwargs iletilir.

Bu, belirli bir sınıfı (className) ve blueprint'i (bluePrintName) başlatmak için çağrılan fonksiyon gibi görünüyor.

kwargs sayesinde ekstra parametreler de bu metoda dinamik olarak iletilebiliyor.

# 7 Run.py (P3_Scorpius/S1_App/Run/Run.py)

Bu class ilgili endpointe istek geldiğinde hangi isteği hangi class işleyecekse oraya yönlendirir. 

Aynı zamanda Logic'in çalışmaya başlamadan önceki son adımı olduğu için database ile alakalı işlem tanımları, değişkenler burada verilir.

```
userId =  Session.userId // Kullanıcı endpointi kullanabilmesi için mutlaka tanımlı olmalıdır. Kullanıcı UserId gelen tokenden yakalanır. Uygulama boyunca bu userId'ye ihtiyacımız olacağı için Session sınıfının userId global değişkenine atanır.

self.AlchemyEngines.createEngine() // Bu Database üzerinde çalışacak bir Engine yaratır. Standart engine budur.
self.AlchemyEngines.snapEngine() // Bir de herhangi bir anda kullanılıp kapatılacak snapEngine aynı şekilde yaratılır.

methot = request.method.upper() // request ile gelen metod upper yöntemi ile tüm harfleri büyük hale getirilir.

className = str(EndPointClass.endpointClass[className][methot]) // Endpoint'lerin classlarının olduğu EndpointClass isminde bir sınıfımız mevcuttur. Detaylarına aşağıdan bakınız. Bu kod ile beraber gidilecek Class yakalanmış olur. 


classOne = getattr(sys.modules[__name__], className)() // Yakalanan className bir string olduğu için bunun bir Class gibi işleme sokulabilmesi için öncelikle bu kod parçacığı ile bir Class'a dönüştürülür ve bir nesne türetilir.

/*

Önreğin className = "Home" olarak geldi. 

getattr(sys.modules[__name__], className) bu kod onu Home class'ına döndürür. Kullanılan () sayesinde Home() şeklini alır ve ondan bir nesne türetilmesi sağlanır.

*/


return classOne.main(methot, userId = userId, **kwargs) // Her endpoint logic'i işletecek Class'ın main metodu vardır ve metodlara göre dağıtıum bu main metodu üzerinden gerçekleşir. Bu kod parçacığı sayesinde Endpoint class'ının main metodunun ihtiyaç duyduğu parametreler gönderilir ve main işletilir.


```

Bu class içinde tanımlanan aşağıdaki kod parçasının dosyasının detaylarını aşağıda okuyunuz.

`from P3_Scorpius.S1_App.Router.RoutePages import *`

# 8 EndPointClass (P3_Scorpius/S1_App/EndPointClass.py)

Bu class bir endpointClass isminde dictionary'e sahiptir. 

ClassName'leri key kabul edip içinde metot isimleriyle hangi class'lara gideceğinin tanımı yapılır.


```
 endpointClass = {

        "Home"      : {"GET":"Home"},

        "SignUp"    : {"GET":"SignUp", "POST":"SignUp"},

        "SignIn"    : {"GET":"SignIn","POST":"SignIn"},

        "Dashboard" : {"GET":"Dashboard"},

        "SignOut"   : {"GET":"SignOut"},

        "Mail"   : {"GET":"Mail", "POST":"Mail", "PUT":"Mail", "DELETE":"Mail"},

    }

```

Burada Home className ile gelen bir sogulama yapıldığında karşılığı olan {"GET":"Home"} değer yakalanır. Sonra bunun içinde o anki gelen metodun eşleşmesi yapılarak istek hangi Class'a gidecek bu çekilir.

Burada endpointlerin hangi metodlara sahip ise bu metodlar eklenmelidir. Home için Get'den başka metodla gelinirse yanıt verecek bir architecture yoktur bunun için sadece Get metodu işlenmiştir.

Mail'e bakarsanız GET, POST, PUT, DELETE gibi metodlarla gelen işlemlere karşılık verebileceğini görüyoruz.

Her yazdığınız endpoint için buraya tanımlanması yapılmalıdır.


# 9 RoutePages.py (P3_Scorpius/S1_App/Router/RoutePages.py)

Endpoint için oluşturduğunuz class'ların ana dağıtıcı dosyasını bu dosya içinde import etmelisiniz. Burada listelenen tüm endpoint class'ları 
Run.py içinde bu dosya yardımı ile toplu halde çağrılır ve kullanıma alınır.

