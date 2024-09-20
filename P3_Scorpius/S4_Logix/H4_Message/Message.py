# region JsonMessages

class Message:

    # region Init Function

    def __init__(self):
        pass

    # endregion

    # region MessageTr Function

    messagesTr = {

        "000": { 
            "message": ""
        },

        # region Success Messages

        "201" : {
            "message"  : "Mailiniz Onaylanmıştır. Giriş Yapabilirsiniz"
            },
        "202" : {
            "message"  : "Ekleme İşlemi Başarılı"
            },
        "203" : {
            "message"  : "Güncelleme İşlemi Başarılı"
            },
        "204" : {
            "message"  : "Silme İşlemi Başarılı"
            },

        # endregion

        # region Error Messages

        "401" : {
            "message"  : "Şifrelerini Aynı Değildi"
            },
        "402" : {
            "message"  : "Bu Email Kayıtlıdır. Farklı Bir Email Deneyiniz"
            },
        "403" : {
            "message"  : "Kayıt İşlemi Sırasında Beklenmedik Hata. Lütfen Tekrar Deneyiniz"
            },
        "404" : {
            "message"  : "Kayıt İşlemi Gerçekleştirilemedi. Lütfen Tekrar Deneyiniz"
            },
        "405" : {
            "message"  : "Böyle Bir Kullanıcı Yoktur"
            },
        "406" : {
            "message"  : "Emailiniz Henüz Onaylanmamıştır. Gönderdiğimiz Mail İle Onaylayınız"
            },
        "407" : {
            "message"  : "Hatalı Email Ya Da Şifre Girdiniz. Lütfen Tekrar Deneyiniz"
            },
        "408" : {
            "message"  : "Ekleme İşlemi Gerçekleştirilemedi"
            },
        "409" : {
            "message"  : "Güncelleme İşlemi Gerçekleştirilemedi"
            },
        "410" : {
            "message"  : "Silme İşlemi Gerçekleştirilemedi"
            },
        "411" : {
            "message"  : "Beklenmeyen Bir Hata Oluştur Kısa Bir Süre Sonra Tekrar Deneyiniz. Ya da Sistem Yöneticinizle İletişime Geçiniz"
            },
        "412" : {
            "message"  : "Token Kullanılmıştır ya da Yoktur"
            },
        "413" : {
            "message"  : "Firma Yetkilisi Üyeliğinizi Onaylamadan Giriş Yapamazsınız"
            },
        
        "414" : {
            "message"  : "Lisans Süreniz Dolmuştur. Lütfen Yenileyip Tekrar Deneyiniz"
            },

        # endregion
    }

    # endregion

# endregion