
# Proje Mimarisi Genel Bakış

## 1. App.py

Uygulama `App.py` dosyası ile başlatılır.

```python
app = Flask(__name__)
```

Bu satır bir Flask örneği tanımlar. Uygulama, `FlaskStart().starter(app, __name__)` metodu kullanılarak başlatılır.

- **FlaskStart:** Bu sınıf, Flask uygulamasını başlatmak için gerekli ilk yapılandırmaları yapar.

## 2. FlaskStart.py (P3_Scorpius/S1_App/Starter/FlaskStart.py)

`FlaskStart` içindeki `PrepareSystems.starter(app)` metodu sistem düzeyinde hazırlıkları yapar.

Aşağıdaki kod satırı Flask uygulamasını yapılandırır ve başlatır:

```python
app.run(host='0.0.0.0', port=Configuration.appConfig["appPort"], use_reloader=True)
```

- **app.run():** Flask uygulamasını HTTP isteklerini dinlemeye başlatır.
- **host='0.0.0.0':** Uygulama tüm ağ arayüzlerinden erişilebilir.
- **port=Configuration.appConfig["appPort"]:** Port numarası yapılandırma ayarlarından dinamik olarak alınır.
- **use_reloader=True:** Geliştirme sırasında kod değişikliklerinden sonra uygulamayı yeniden başlatan otomatik yükleme mekanizmasını etkinleştirir.

## 3. Configuration.py (P3_Scorpius/S6_Utils/Configuration.py)

Uygulamanın yapılandırma ayarları bu dosya içinde tanımlanır. Port numarası gibi ayarlar çalışma ortamına göre güncellenir.

## 4. PrepareSystems.py (P3_Scorpius/S1_App/Prepare/PrepareSystems.py)

Bu dosya, sistem hazırlıklarından sorumludur. Veritabanı bağlantısı, önbellek yapılandırması gibi gereksinimler burada işlenir.

## 5. Run.py (P3_Scorpius/S1_App/Run.py)

Uygulamanın ana giriş noktası `Run.py` dosyasıdır. Tüm endpoint'ler burada import edilip kaydedilir. Bu dosya, `FlaskStart` ve gerekli diğer modülleri kullanarak uygulamanın başlatılmasını sağlar.

```python
from P3_Scorpius.S1_App.Router.RoutePages import *
```

## 6. EndPointClass.py (P3_Scorpius/S1_App/EndPointClass.py)

Bu sınıf, HTTP metodlarını ve bu metodlara karşılık gelen sınıfları map eder. `endpointClass` sözlüğü URL yollarını sınıf metodları ile eşleştirir.

```python
endpointClass = {
    "Home": {"GET": "Home"},
    "SignUp": {"GET": "SignUp", "POST": "SignUp"},
    "SignIn": {"GET": "SignIn", "POST": "SignIn"},
    "Dashboard": {"GET": "Dashboard"},
    "SignOut": {"GET": "SignOut"},
    "Mail": {"GET": "Mail", "POST": "Mail", "PUT": "Mail", "DELETE": "Mail"},
}
```

Bu sözlük HTTP metodlarını (örn. `GET`, `POST`) ilgili sınıf isimleri ile eşleştirir. Örneğin, `Home` endpoint'ine yapılan bir `GET` isteği `Home` sınıfına yönlendirilir.

## 7. RoutePages.py (P3_Scorpius/S1_App/Router/RoutePages.py)

Bu dosya, uygulamadaki tüm endpoint sınıflarını import eder. Her endpoint sınıfı burada listelenmelidir.

## 8. FlaskStart Yapılandırması

`FlaskStart` sınıfı içindeki yapılandırma, logging, middleware yapılandırması ve güvenlik ayarları gibi sistem düzeyindeki görevleri içerir. Bu görevler, uygulamanın sorunsuz ve güvenli çalışmasını sağlamak için kritiktir.
