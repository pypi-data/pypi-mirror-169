from keyscraper.dynamicscraper import DSFormat, DSInfo, DriverOptions, DynamicScraper
from keyscraper.utils import ImageGrabber
from keygim.imageUtils import BasicUtils, ImageUtils
import datetime, sys, os
class KeyGoogleImages:
    def help():
        print("KeyGoogleImages:")
        print("\t[1] LinkFormatter")
        print("\t[2] GoogleImageDownloader")
        print("")
    class LinkFormatter:
        FORMAT_STRING = "https://www.google.com/search?q={}&tbm=isch"
        FORMAT_LARGE = "&tbs=isz:l"
        def help():
            print("KeyGoogleImages.LinkFormatter:")
            print("\t[1] __init__(self, stringList)")
            print("\t[2] fetch_links(self, large = False)")
            print("")
        def __init__(self, stringList):
            self.stringList = BasicUtils.verify_type(stringList, [list])
        def __format_string(self, string, large = False):
            return self.FORMAT_STRING.format(string) + (self.FORMAT_LARGE if (large) else "")
        def fetch_links(self, large = False):
            large = BasicUtils.verify_type(large, [bool,int])
            return [
                self.__format_string(string, large) for string in self.stringList        
            ]
    class GoogleImageDownloader:
        __DRIVERS = { 0 : "Google Chrome", 1 : "Mozilla Firefox" }
        MODE_CHROME  = list(__DRIVERS.keys())[0]
        MODE_FIREFOX = list(__DRIVERS.keys())[1]
        SCRAPED = []
        class Retry:
            PATIENCE = 15
            def __init__(self): self.reset_SOT()
            def reset_SOT(self): self.SOT = datetime.datetime.now()
            def retry(self, link):
                if (((type(link) != str) or (link[:11] == "data:image/") or (link[:17] == "https://encrypted")) and \
                    ((datetime.datetime.now() - self.SOT).total_seconds() < self.PATIENCE)):
                    return False
                self.reset_SOT()
                return True
        RET = Retry()
        def help():
            print("KeyGoogleImages.GoogleImageDownloader:")
            print("\t[1] __init__(self, search_strings, mode = 0, driver_path = None)")
            print("\t\t#default mode -> Google Chrome")
            print("\t[2] configure(self, **kwargs)")
            print("\t\tavailable parameters:")
            print("\t\t(1) \"folder_name\"")
            print("\t\t(2) \"hide_window\"")
            print("\t\t(3) \"wait_load\"")
            print("\t\t(4) \"search_large\"")
            print("\t\t(5) \"save_search\"")
            print("\t\t(6) \"item_wait\"")
            print("\t\t(7) \"images_per_page\"")
            print("\t\t(8) \"verbose\"")
            print("\t\t(9) \"url_timeout\"")
            print("\t\t(10) \"load_timeout\"")
            print("\t[3] download(self)")
            print("\t[4] cleanup(self)")
            print("")
        def __init__(self, search_strings, mode = 0, driver_path = None):
            (self.search_strings, self.mode, self.driver_path) = (
                BasicUtils.verify_type(search_strings, [list]),
                BasicUtils.verify_mode(BasicUtils.verify_type(mode, [int]), list(self.__DRIVERS.keys())),
                BasicUtils.verify_type(driver_path, [type(None),str])
            )
            self.parameters = {
                "folder_name" : None,
                "hide_window" : False,
                "wait_load" : True,
                "search_large" : False,
                "save_search" : False,
                "item_wait" : 1,
                "images_per_page" : 10,
                "verbose" : True,
                "url_timeout" : 60,
                "load_timeout" : 30
            }
        def __get_mode_scraper(self):
            return (DynamicScraper.MODE_FILE if (self.parameters["save_search"]) else DynamicScraper.MODE_READ)
        def __get_mode_driver(self):
            if (self.mode == self.MODE_CHROME):
                return DriverOptions.MODE_CHROME
            elif (self.mode == self.MODE_FIREFOX):
                return DriverOptions.MODE_FIREFOX
            raise Exception("Mode Error: driver must be either Chrome or Firefox\n")
        def __scrape_page(self, webpage):
            f_item = DSFormat(xpath = "(//img[contains(@class, 'rg_i Q4LuWd')])", click = True, multiple = True)
            f_attr = [DSFormat(
                xpath = "//div[contains(@class, 'tvh9oe BIB1wf')]//img[contains(@class, 'n3VNCb')]", 
                retry = self.RET.retry, nickname = "url", relative = False, extract = "src", 
                callback = KeyGoogleImages.GoogleImageDownloader._format_link
            )]
            info = DSInfo(f_site = webpage, f_page = "", f_item = f_item, f_attr = f_attr)
            driver = DriverOptions(
                mode = self.__get_mode_driver(), 
                path = self.driver_path, 
                window = not self.parameters["hide_window"]
            )
            DynamicScraper(info, driver, mode = self.__get_mode_scraper(), 
                buttonPath = "//input[contains(@class, 'mye4qd')][last()]", 
                itemWait = self.parameters["item_wait"]).scrape(
                start = 1,
                pages = 1,
                perPage = self.parameters["images_per_page"]
            )
        def __get_folder(self, page_number):
            return (
                BasicUtils.verify_folder(self.parameters["folder_name"]) if (self.parameters["folder_name"] != None) else \
                    "./{}/".format(self.search_strings[page_number].strip("/")[:50])
            )
        def __download_images(self, page_number):
            for index, page in enumerate(KeyGoogleImages.GoogleImageDownloader.SCRAPED):
                if (self.parameters["verbose"]):
                    sys.stdout.write(f"\rDownloading {index + 1}...")
                ImageGrabber(
                    BasicUtils.verify_filename(
                        "".join([
                            BasicUtils.verify_folder(self.__get_folder(page_number), True), 
                            self.search_strings[page_number].strip("/"),
                            self.__format_format(page)  
                        ]),
                        overwrite = False
                    ),
                    progressBar = self.parameters["verbose"],
                    url_timeout = self.parameters["url_timeout"]
                ).retrieve(directlink = page, timeout = self.parameters["load_timeout"])
                if (self.parameters["verbose"]):
                    sys.stdout.flush()
            if (self.parameters["verbose"]):
                print("")
        def __clear_list(self):
            KeyGoogleImages.GoogleImageDownloader.SCRAPED = []
        def _format_link(link):
            if (link != None):
                KeyGoogleImages.GoogleImageDownloader.SCRAPED.append(link)
            return link
        def __format_format(self, page):
            if (page[:11] == "data:image/"):
                first11 = page.split("/")[1][:11].lower()
                first12 = page.split("/")[1][:12].lower()
                if (("jpeg;base64" in first11) or ("jpg;base64" in first11)):
                    foundType = ".jpg"
                elif ("png;base64" in first11):
                    foundType = ".png"
                elif ("webp;base64" in first11):
                    foundType = ".webp"
                elif ("bmp;base64" in first11):
                    foundType = ".bmp"
                elif ("gif;base64" in first11):
                    foundType = ".gif"
                elif (("tif;base64" in first11) or ("tiff;base64" in first11)):
                    foundType = ".tiff"
                elif ("x-icon;base64" in first12):
                    foundType = ".ico"
                else:
                    foundType = ".jpg"
            else:
                last10 = page[-10:].lower()
                if ("png" in last10):
                    foundType = ".png"
                elif ("webp" in last10):
                    foundType = ".webp"
                elif (("jpg" in last10) or ("jpeg" in last10)):
                    foundType = ".jpg"
                elif ("ico" in last10):
                    foundType = ".ico"
                elif ("gif" in last10):
                    foundType = ".gif"
                elif ("bmp" in last10):
                    foundType = ".bmp"
                elif ("tif" in last10):
                    foundType = ".tiff"
                else:
                    foundType = ".jpg"
            return foundType
        def __modify(self, key, value):
            if (key == "folder_name"):
                self.parameters[key] = BasicUtils.verify_type(value, [type(None),str])
            elif (key in ["item_wait", "url_timeout", "load_timeout"]):
                self.parameters[key] = max(0, BasicUtils.verify_type(value, [float,int]))
            elif (key == "images_per_page"):
                self.parameters[key] = max(1, BasicUtils.verify_type(value, [int]))
            else:
                self.parameters[key] = bool(BasicUtils.verify_type(value, [bool,int]))
        def configure(self, **kwargs):
            for key, value in kwargs.items():
                if (isinstance(key, str)):
                    key = key.lower()
                    if (key in list(self.parameters.keys())):
                        self.__modify(key, value)
        def download(self):
            pages = KeyGoogleImages.LinkFormatter(self.search_strings).fetch_links(self.parameters["search_large"])
            self.__clear_list()
            for index, page in enumerate(pages):
                if (self.parameters["verbose"]):
                    print(f"On page {index + 1}: {self.search_strings[index]}")
                self.__scrape_page(page)
                self.__download_images(index)
                self.__clear_list()
        def cleanup(self):
            for page_number in range(len(self.search_strings)):
                folder = self.__get_folder(page_number)
                if (os.path.exists(folder)):
                    ImageUtils.ImageCorruptDisposer(folder).parse().dispose()
                else:
                    print(f"Warning: path {folder} does not exist.")
if (__name__ == "__main__"):
    """
    search_strings = ["idiot"]
    searcher = GoogleImageDownloader(search_strings, driver_path = "./chromedriver.exe")
    searcher.configure(
        search_large = True,
        save_search = True,
        hide_window = True,
        images_per_page = 20
    )
    searcher.download()
    """
    """
    LinkFormatter.help()
    GoogleImageDownloader.help()
    """
    """
    search_string = ["anime wallpaper"]
    downloader = GoogleImageDownloader(
        search_strings = search_string, 
        mode = GoogleImageDownloader.MODE_CHROME, 
        driver_path = "./chromedriver.exe"
    )
    downloader.configure(
        hide_window = True,
        images_per_page = 100,
        search_large = True,
        load_timeout = 10,
        url_timeout = 30,
        folder_name = "background_templates"
    )
    downloader.download()
    """
    