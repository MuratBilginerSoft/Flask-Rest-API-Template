# region Import Packages

# endregion

# region ResendConfirmMailHtml Class

class ResendConfirmMailHtml():

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
        <body style="margin: 0; padding: 0; overflow: hidden; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center;padding-top: 50px;">

            <div style="color: #000; font-family: Roboto; font-size: 14px; font-style: normal;font-weight: 400; line-height: 150%; display: flex; flex-direction: column; justify-content: center; width: 65%; padding: 10px; z-index: 100;">

            <p>Dear</p>

            <p>Welcome to Prowth, your go-to SaaS tool for revolutionizing growth strategies and data-driven decision-making! We're excited to have you on board and provide you with the power to identify growth opportunities effortlessly using advanced analytics without any coding.</p>

            <p style='font-weight: bold;'>To ensure the security of your account and enable seamless access to Prowth, we kindly ask you to verify your email address by clicking the button below:</p>
            
            <div style="display: flex; justify-content: center; align-items: center; cursor: pointer; border: none; border-radius: 8px; background-color: rgba(82, 52, 178, 1); height: 36px; width: 145px; color: white; margin-top: 10px; margin-bottom: 10px; border:none;">
                <a href="{link}" style="color: white; text-decoration: none; margin:auto; margin-left:30px; margin-top:10px">Verify Your Email</a>
            </div>


            <p>Once you click the link, your email will be verified, and you'll gain full access to our platform. With Prowth, you can:</p>

            <p><span style='font-weight: bold;'>Uncover Growth Insights: </span>Leverage advanced analytics to identify growth opportunities tailored to your needs.</p>

            <p><span style='font-weight: bold;'>Data-Driven Decision-Making: </span>Empower yourself with actionable insights to make informed decisions that drive your business forward.</p>

            <p><span style='font-weight: bold;'>No Coding Required: </span>Tailor your growth strategy based on real-time data, enabling you to optimize and fine-tune your approach.
            </p>

            <p><span style='font-weight: bold;'>Personalized Growth Strategy: </span>Empower yourself with actionable insights to make informed decisions that drive your business forward.</p>

            <p>We understand the value of data privacy and security. Rest assured that your information is protected with top-notch measures and won't be shared with any third parties.</p>
            
            <p>If you encounter any questions, need assistance, or have feedback on your Prowth experience, don't hesitate to reach out to our dedicated customer support team at product@prowth.co</p>

            <p>Thank you for choosing Prowth! Let's embark on a growth-driven journey together.</p>

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
        </html>"""

        self.__htmlContent = self.__htmlContent.encode(
            'ascii', errors='replace').decode()

        return self.__htmlContent

    # endregion

# endregion