class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:  # if key exist
            return self[item]  # 像範例的 jso.language = 'Python'
        except KeyError:  # if item doesn't a valid key
            return super().__getattribute__(item)
            #  fall back to dict version of getattribute to see if there is a actual attribute