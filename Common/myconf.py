import configparser

class myconf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr