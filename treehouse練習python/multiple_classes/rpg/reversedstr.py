class ReversedStr(str):
    def __new__(cls, *args, **kwargs):
        new_sting = str.__new__(*args, **kwargs)
        new_sting = new_sting[::-1]
        return new_sting


