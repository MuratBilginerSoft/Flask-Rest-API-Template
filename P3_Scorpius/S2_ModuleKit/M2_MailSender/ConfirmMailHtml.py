# region Import Packages

# endregion

# region ConfirmMailHtml Class

class ConfirmMailHtml:

    # region Init

    def __init__(self) -> None:

        self.__htmlContent = None

    # endregion

    # region Starter

    def starter(self, link, name, surname):

        self.__htmlContent = f"""

        <!DOCTYPE html>
        <html lang='tr'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <title></title>
        </head>

        <body style="margin: 0; padding: 0; overflow: hidden; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center;padding-top: 50px;">

            <div style="color: #000; font-family: Roboto; font-size: 14px; font-style: normal;font-weight: 400; line-height: 150%; display: flex; flex-direction: column; justify-content: center; width: 65%; padding: 10px; z-index: 100;">

            <p>Degerli Kullanicimiz;</p>

            <p>Posa Turkey Panel uyeliginizi tamamlamak icin lutfen emailinizi onaylayiniz.</p>

            <p style='font-weight: bold;'>Hesabinizin guvenligini saglamak ve Posa Turkey'e sorunsuz erisim saglamak icin, asagidaki dugmeye tiklayarak e-posta adresinizi dogrulamanizi rica ederiz</p>
            
            <div style="display: flex; justify-content: center; align-items: center; cursor: pointer; border: none; border-radius: 8px; background-color: rgba(82, 52, 178, 1); height: 36px; width: 145px; color: white; margin-top: 10px; margin-bottom: 10px; border:none;">
                <a href="{link}" style="color: white; text-decoration: none; margin:auto; margin-left:30px; margin-top:10px">Email'i Onayla</a>
            </div>

            <p>Herhangi bir sorunla karsilasirsaniz, yardima ihtiyaciniz varsa veya Posa Turkey deneyiminizle ilgili geri bildiriminiz varsa, product@posapanel.com adresinden ozel musteri destek ekibimize ulasmaktan cekinmeyin.</p>

            <p>Posa Turkey'i sectiginiz icin tesekkur ederiz! Gelin birlikte buyume odakli bir yolculuga cikalim.</p>

            <p style='font-weight: bold;'>Saygilarimizla</p>
            <p style='font-weight: bold; margin-top: -15px;'>Posa Turkey Team</p>

            <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 10px;'>

                <img src="https://i.hizliresim.com/211yhwp.png"/>

                <p style='color:#3E4E8C;'>Destege mi ihtiyaciniz var?  Bizimle iletisime geciniz<a href='mailto:product@prowth.co'>product@posapanel.com</a></p>

                <div style='display: flex;'>

                    <img src="https://i.hizliresim.com/2rjw894.png"/>

                </div>
        
            </div>
            </div>
        </body>
        </html>"""

        self.__htmlContent = self.__htmlContent.encode('ascii', errors='replace').decode('ascii')
        
        return self.__htmlContent

    # endregion

# endregion
