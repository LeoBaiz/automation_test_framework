from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver_path():
    return ChromeDriverManager().install()