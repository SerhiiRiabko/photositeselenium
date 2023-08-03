class ConfigObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update_dict(self):
        pass

    def get_dict(self):
        pass
