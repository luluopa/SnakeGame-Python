class JsonNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("Json file could not be found [did you pass the wrong path?]")
        pass