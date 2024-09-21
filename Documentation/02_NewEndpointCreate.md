# New Endpoint Create #

Yeni bir endpoint oluşturacağınızda aşağıdaki adımları sırasıyla uygulayınız.

## 1. Yöntem Tek Metoda Sahip Endpoint Oluşturma

Oluşturacağınız endpoint sadece tek bir metoda sahipse aşağıdaki yolu izleyebilirsiniz. 

Burada HelloWorld isimli, response olarak HelloWorld çıktısı veren sadece Get metoduna sahip bir endpoint noktası oluşturacağız.

1. Öncelikle endpoint noktasının ne olacağını belirleyin. /hello-world bizim endpoint noktamız olacak.
2. Bu endpoint için kullanılacak className belirleyin. HelloWorld() olarak kullanacağız.
3. Dosya ismi de best practise olarak sınıf ismiyle aynı olabilir. HelloWorld.py


### 1 Klasör ve Dosyayı Oluştur

P2_Sirius/S2_Controllers/ altında HelloWorld isminde bir klasör oluştur.

Bu klasör altında HellWorld.py isimli dosyayı oluştur.

### 2 Dosya İçine Standat Kodları Kopyala Yapıştır ve Güncelle

Öncelike aşağıdaki kodları HelloWorld.py içine alınız.

```

# region Import Packages

import traceback

from P3_Scorpius.S4_Logix.H3_Exception.Exception import Exception
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region YourClassName Class

class YourClassName:

    # region Inıt Function

    def __init__(self):
        
        self.Exceptions = Exception()

    # endregion

    def main(self, method, **kwargs):

        # region Try

        if method == "YourMethod":

            try:
                
                return "YourMessage", 200

            # endregion

            # region Except

            except Exception as e:
                traceback.print_exc()
                return self.Exceptions.mainError("000")

            # endregion
        
        else:
            return self.Exceptions.mainError("000")


#endregion

```

İlgili alanlarda güncellemelerimizi yapalım.

YourClassName = HelloWorld
YourMethod = GET // Burada hangi metodla gelindiğinde çalışmasını istiyorsanız onu girmelisiniz.
YourMessage = "Hello World"

Metod Listesi : ["GET","POST","PATCH","DELETE","PUT", "get","post","patch","delete","put"]

Eğer bu metodlar dışında bir metod kullanmak isterseniz BluePrintQuee.py dosyası içindeki 

`self.__requestMethods = ["GET","POST","PATCH","DELETE","PUT", "get","post","patch","delete","put"]` dizisine metodu eklemeyi unutmayınız.

Güncel Haliyle Kodumuz

```

# region Import Packages

import traceback

from P3_Scorpius.S4_Logix.H3_Exception.Exception import Exception
from P3_Scorpius.S5_Session.Session import Session

# endregion

# region HelloWorld Class

class HelloWorld:

    # region Inıt Function

    def __init__(self):
        
        self.Exceptions = Exception()

    # endregion

    def main(self, method, **kwargs):

        # region Try

        if method == "GET":

            try:
                
                return "Hello World", 200

            # endregion

            # region Except

            except Exception as e:
                traceback.print_exc()
                return self.Exceptions.mainError("000")

            # endregion
        
        else:
            return self.Exceptions.mainError("000")


#endregion


```

Try içinde bu endpoint hangi logic'i işletecekse o kodlamalar yapılabilir.


### 3 EndPointClass.py Dosyasına İlgili Parametreleri Ekle


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

Bu class içine HellWorld ile alakalı eklemeyi yapalım.

```

endpointClass = {

        "Home"      : {"GET":"Home"},

        "SignUp"    : {"GET":"SignUp", "POST":"SignUp"},

        "SignIn"    : {"GET":"SignIn","POST":"SignIn"},

        "Dashboard" : {"GET":"Dashboard"},

        "SignOut"   : {"GET":"SignOut"},

        "Mail"   : {"GET":"Mail", "POST":"Mail", "PUT":"Mail", "DELETE":"Mail"},

        "HelloWorld" : {"GET":"HelloWorld"}, // Bu Satırı ekledik

    }



```

### 4 RoutePages.py Dosyasını Güncelle

Bu dosya içine yazdığımız sınıfı import ediyoruz.

``` 
# region Bluewhale Folder

from P2_Sirius.S2_Controllers.Home.Home import Home
from P2_Sirius.S2_Controllers.HelloWorld.HelloWorld import HelloWorld // Bu satır eklendi

# endregion


```

### 5 Router.py Dosyasını Güncelle

Bu sınıf içine endpointimizle alakalı parametre tanımlamalarını yapıyoruz.

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

Her bir endpoint url'i burada tanıtılır.

`"helloworld" : ["helloworld", "HelloWorld", "/hello-world"],` istediğiniz yere bu kodu ekleyebilirsiniz. 

key değerini blueprintname ile aynı vermek gerekir. 

helloworld şeklinde verdiğim ilk dizi değeri BluePrintName'e karşılık gelir. Verdiğim className'in küçük harflerle yazılmış halini veririz.

HelloWorld olarak yazılan 2. indis, kullanacağımız endpoint'in className'ine karşılık gelir.

"hello-world" : endpoint için belirlediğim urldir.

