from json import loads, dumps

class Config:
    def __init__(self,source: str) -> None:
        self.source = source
        self.data = self.__load()
        self.source_urls = self.data["source_urls"]
        self.ignore = self.data["ignore"]

    def save(self,payload: dict):
        with open(self.source,"w") as file:
            file.write(dumps(payload))

    def __load(self) -> dict:
        with open(self.source) as file:
            return(loads(file.read()))

config = Config("config.json")