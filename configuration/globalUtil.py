import yaml,os
filename = os.path.join(os.path.dirname(__file__),'settings.yaml').replace("\\","/")


class GlobalSetting:
    def __init__(self,env="SIT"):
        self.env = env

    @staticmethod
    def get_value(self):
        config = yaml.safe_load(open(filename))
        return config

if __name__ == '__main__':
    default_config = GlobalSetting.get_value('')
    print default_config['Jenkins']['username']
    print os.path.join(os.path.dirname(__file__))

