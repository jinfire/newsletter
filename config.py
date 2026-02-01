class Config:
    SMTP_SERVERS = {
        "naver":{
            "email":"oinqkvs@naver.com",
            "password":"qpdknvi319",
            "smtpName":"smtp.naver.com",
            "smtpPort":465,
        }
    }

    @classmethod
    def get_smtp_config(cls, provider:str):
        return cls.SMTP_SERVERS.get(provider)