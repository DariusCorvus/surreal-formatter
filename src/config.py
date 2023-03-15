class Config:
    tabsize: int = 2
    LEN_WHERE: int = 5
    LEN_AND: int = 3

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance
