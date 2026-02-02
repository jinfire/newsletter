class Config:
    SMTP_SERVERS = {
        "naver":{
            "email":"oinqkvs@naver.com",
            "password":"P4CXHMQWKQ85",
            "smtpName":"smtp.naver.com",
            "smtpPort":587,
        }
    }

    @classmethod
    def get_smtp_config(cls, provider:str):
        return cls.SMTP_SERVERS.get(provider)