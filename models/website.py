from pexpect import TIMEOUT
from requests import get
from models.banner import Banner


class Website:
    """A simple model of a website"""

    TIMEOUT = 5

    def __init__(self, domain: str, url="", html="", banner=Banner.UNKNOWN):
        self.domain = domain
        self.url = url
        self.html = html
        self.banner = banner


    def crawl(self):
        try:
            response = get("https://" + self.domain, timeout=5)
            status_code = response.status_code
            html = response.text
        except:
            try:
                response = get("http://" + self.domain, timeout=5)
                status_code = response.status_code
                html = response.text
            except:
                status_code = 408
                html = ""

        match (status_code):
            case 403:
                banner = Banner.FORBIDDEN
            case 404:
                banner = Banner.NOT_FOUND
            case 408:
                banner = Banner.TIMEOUT
            case _:
                banner = Website.__find_banner(html)

        self.banner = banner


    @staticmethod
    def __find_banner(html) -> Banner:
        if html == "":
            return Banner.UNKNOWN

        lines = html.split("\n")

        tags = []

        for line in lines:
            if line.find("<script") > -1:
                tags.append(line)

        for line in tags:
            found_banner = Website.__read_tag(line)
            if found_banner != Banner.UNKNOWN:
                return found_banner

        return Banner.UNKNOWN
        

    @staticmethod
    def __read_tag(s: str) -> Banner:
        if s.__contains__('id="Cookiebot"'):
            return Banner.COOKIEBOT
        elif s.__contains__("static.clickskeks.at"):
            return Banner.CLICKSKEKS
        else:
            return Banner.UNKNOWN
