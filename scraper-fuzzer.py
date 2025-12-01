import json,requests,os,time,bs4,urllib.parse,re,sys,subprocess
import xml.etree.ElementTree as ET
from colorama import Fore
base_url = input(Fore.BLUE + "Target url (ex. https://google.com/) >> ")
custom_file = input(Fore.BLUE + "Are you have target links file? >> ")
url = base_url + "sitemap.xml"
print(Fore.GREEN + "Checking sitemap file...")
time.sleep(2)
check_sitemap = requests.get(url)
if check_sitemap.status_code == 200:
    print(Fore.GREEN + "Sitemap Found ! >>",Fore.YELLOW + url)
    st_urls = requests.get(url)
    ro = ET.fromstring(st_urls.content)
    urls = {os.path.dirname(loc.text)+"/" for loc in ro.iter()
        if loc.text and loc.text.endswith(".xml")}
    open("sitemap.txt","w",encoding="utf-8").write("\n".join(sorted(urls)))
    print(Fore.GREEN + "Sitemap.xml is Scraped!")
else:
    print(Fore.RED + "Sitemap not Found ! Exiting >>")
    time.sleep()
    os._exit(0)
os.system(f"cat {custom_file} sitemap.txt > urls.txt")
#################################################################
time.sleep(2)
os.system("clear")
print(Fore.BLUE + "Wait scraping js files...")
js = set()
results = []
for u in open("urls.txt"):
    for s in bs4.BeautifulSoup(requests.get(u.strip()).text,"html.parser").find_all("script"):
        if s.get("src"): js.add(urllib.parse.urljoin(u.strip(),s["src"]))
open("js_found.txt","w").write("\n".join(sorted(js)))
print(Fore.GREEN + "Succesfully scrape !!")
time.sleep(2)
os.system("clear")
#################################################################
print(Fore.BLUE + "Checking versions js files...")
PATTERNS = {
    "jquery": [
        r'jquery[/@-](\d+\.\d+\.\d+)',
        r'jquery.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*jQuery\s+v(\d+\.\d+\.\d+)',
        r'\$\.fn\.jquery\s*=\s*[\'"](\d+\.\d+\.\d+)',
        r'window\.jQuery\.fn\.jquery\s*=\s*[\'"](\d+\.\d+\.\d+)',
    ],
    "bootstrap": [
        r'bootstrap[/@-](\d+\.\d+\.\d+)',
        r'bootstrap.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\!?\s*Bootstrap\s+v(\d+\.\d+\.\d+)',
        r'Bootstrap\.VERSION\s*=\s*[\'"](\d+\.\d+\.\d+)',
    ],
    "vue": [
        r'vue[/@-](\d+\.\d+\.\d+)',
        r'Vue\.js\s+v(\d+\.\d+\.\d+)',
        r'Vue\.version\s*=\s*[\'"](\d+\.\d+\.\d+)',
        r'__VUE_VERSION__\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*Vue\.js\s+v(\d+\.\d+\.\d+)',
    ],
    "react": [
        r'react[/@-](\d+\.\d+\.\d+)',
        r'ReactVersion\s*=\s*[\'"](\d+\.\d+\.\d+)',
        r'react.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'__REACT_VERSION__\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*React\s+v(\d+\.\d+\.\d+)',
    ],
    "angular": [
        r'angular[/@-](\d+\.\d+\.\d+)',
        r'angular.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*Angular(JS)?\s+v(\d+\.\d+\.\d+)',
        r'window\.angular\.version\s*=\s*{[^}]*full\s*:\s*[\'"](\d+\.\d+\.\d+)',
    ],
    "lodash": [
        r'lodash[/@-](\d+\.\d+\.\d+)',
        r'__lodash_version__\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*@license\s+lodash (\d+\.\d+\.\d+)',
        r'_\._VERSION\s*=\s*[\'"](\d+\.\d+\.\d+)',
    ],
    "gsap": [
        r'gsap[/@-](\d+\.\d+\.\d+)',
        r'gsap.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*GSAP\s+v(\d+\.\d+\.\d+)',
        r'gsap\.version\s*=\s*[\'"](\d+\.\d+\.\d+)',
    ],
    "axios": [
        r'axios[/@-](\d+\.\d+\.\d+)',
        r'axios.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*axios (\d+\.\d+\.\d+)',
    ],
    "moment": [
        r'moment[/@-](\d+\.\d+\.\d+)',
        r'moment.*version[\'"]?\s*[:=]\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\!?[\s]*Moment\.js (\d+\.\d+\.\d+)',
    ],
    "chart.js": [
        r'chart\.js[/@-](\d+\.\d+\.\d+)',
        r'Chart\.version\s*=\s*[\'"](\d+\.\d+\.\d+)',
        r'/\*\s*Chart\.js v(\d+\.\d+\.\d+)',
    ],
}
js_file = "js_found.txt"
results = set()
for url in map(str.strip, open(js_file, encoding="utf-8")):
    try:
        text = requests.get(url, timeout=10).text
    except Exception:
        continue
    for prod, patterns in PATTERNS.items():
        for pat in patterns:
            for m in re.finditer(pat, text, re.I):
                results.add((prod, m.group(1)))
json.dump([{"product": p, "version": v} for p, v in results],
          open("all_versions.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(Fore.GREEN + "Successfully version scan !!")
os.system("clear")
#################################################################
print(Fore.BLUE + "Checking versions vuln...")
os.system("python3 cve_checker.py")
time.sleep(2)
#################################################################



    
