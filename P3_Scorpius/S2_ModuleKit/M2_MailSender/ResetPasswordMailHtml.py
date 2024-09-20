# region Import Packages

# endregion

# region ResetPasswordMailHtml Class

class ResetPasswordMailHtml():

    # region Init

    def __init__(self) -> None:

        self.__htmlContent = None
    
    # endregion

    # region Starter

    def starter(self, link):

        self.__htmlContent = f"""

            <!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title></title>

            </head>
            <body style="margin: 0; padding: 0; overflow: hidden; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center;padding-top: 50px; ">

                <div style='color: #000; font-family: Roboto; font-size: 14px; font-style: normal;font-weight: 400; line-height: 150%; display: flex; flex-direction: column; justify-content: center; width: 65%;padding: 20px; z-index: 100;'>

                    <p>Hello</p>

                    <p>We received a password reset request for your Prowth account. Your security is our top priority, and we are happy to assist you in regaining access to your account.</p>

                    <p style='font-weight: bold;'>If you did not request a password reset, you can safely ignore this email. Only a person with access to your email can reset your account password.</p>

                    <p>To proceed with the password reset, please click on the link below:</p>

                    <div style="display: flex; justify-content: center; align-items: center; cursor: pointer; border: none; border-radius: 8px; background-color: rgba(82, 52, 178, 1); height: 36px; width: 145px; color: white; margin-top: 10px; margin-bottom: 10px; border:none;">
                        <a href="{link}" style="color: white; text-decoration: none;">Reset Password</a>
                    </div>

                    <p>If you encounter any issues during the password reset process or have any concerns, please don't hesitate to reach out to our support team at support@prowth.com. We are here to help you.</p>

                    <p>Thank you for choosing Prowth as your growth analytics SaaS tool. We are committed to providing you with the best experience and ensuring the security of your account.</p>

                    <p style='font-weight: bold;'>Best regards,</p>
                    <p style='font-weight: bold; margin-top: -15px;'>The Prowth Team</p>

                    <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 10px;'>

                        <img src="https://i.hizliresim.com/7ywv7qv.png"/>

                        <p style='color:#3E4E8C;'>Operate and identify growth opportunities by using </p>
                        
                        <p style='color:#3E4E8C; margin-top: -20px;'>advanced analytics without coding</p>

                        <p style='color:#3E4E8C;'>Do you need support?  Contact us via <a href='mailto:product@prowth.co'>product@prowth.co</a></p>

                        <div style='display: flex;'>

                            <img src="https://i.hizliresim.com/2rjw894.png"/>

                        </div>
                    </div>
                </div>
            </body>
            </html>
        """

        self.__htmlContent = self.__htmlContent.encode(
            'ascii', errors='replace').decode()

        return self.__htmlContent

    # endregion

# endregion