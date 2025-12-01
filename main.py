from colorama import Fore
import time,sys,os
os.system("clear")
os.system("rm -rf urls.txt")
os.system("rm -rf sitemap.txt")
os.system("rm -rf all_urls.txt")
os.system("rm -rf alive_pages.txt")
os.system("rm -rf js_found.txt")
os.system("rm -rf clean_versions.json")
os.system("rm -rf tmp.csv")
os.system("rm -rf cve_report.json")
os.system("rm -rf all_versions.json")
def slow_print(text: str, delay: float = 0.03, newline: bool = True):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

print(r"""
            |\---/|
            | ,_, |
             \_`_/-..----.
            ___/ `   ' ,""+ \ 
           (__...'   __\    |`.___.';
            (_,...'(_,.`__)/'.....+
""")
slow_print(Fore.CYAN + "   CsScan.py | The powerfull web scanner")
slow_print(Fore.YELLOW + "          Version : v0.1(Beta)")
os.system("python3 scraper-fuzzer.py")


