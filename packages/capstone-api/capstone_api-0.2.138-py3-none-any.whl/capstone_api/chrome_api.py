import re
import subprocess
import time
from configparser import ConfigParser
from pathlib import Path

from bs4 import BeautifulSoup


class ChromeAPI(object):
    """Wrapper for chrome-cli"""

    def __init__(self, delay=0):
        """Configs"""
        if delay:
            self.delay = int(delay)
        else:
            capstone_api_ini = Path(Path.home(), '.config/capstone_api.ini')
            if capstone_api_ini.exists():
                config = ConfigParser()
                config.read(capstone_api_ini)
                chrome = dict(config["chrome"].items())
                self.delay = chrome["delay"]
            else:
                self.delay = 0

    def openTab(self, url):
        """Open url in new tab"""
        cmd = f'chrome-cli open "{url}"'
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        time.sleep(2)
        tab = re.search(r'Id: (?P<tab>\d+)', out).groupdict('tab').get('tab')
        return tab

    def getSrc(self, tab):
        """Get tab source"""
        cmd = f'chrome-cli source -t {tab}'
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        return BeautifulSoup(out, 'html5lib')

    def execJS(self, js, tab):
        """Execute JavaScript"""
        cmd = f'chrome-cli execute \'{js}\' -t {tab}'
        subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
        # c.print(out)
        return


