import configparser

config = configparser.RawConfigParser()
config.read('../Configurations/app_config.ini')


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get('app_data', 'base_url')

    @staticmethod
    def get_user_creds():
        return config.get('user_data', 'email'), config.get('user_data', 'password')

    @staticmethod
    def get_browser_id():
        return config.get("browser_data", "browser_id")

    @staticmethod
    def get_photo_link():
        return config.get("icon_link_data", "link_photo")
