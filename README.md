# CsCan-Scanner
Crawl sitemap, collect JS files, extract versions and check local CVE database in one command.

CsCan – Web Asset & CVE Scanner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Lightweight, fully-open-source tool that:
-Crawls sitemap.xml (or your own URL list)
-Harvests JavaScript files
-Extracts library versions from URLs, headers, source-maps & code
-Checks them against a local CVE dump (no API calls required)
-Reports vulnerable dependencies in seconds
-Auto clear cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| Feature            | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| **Sitemap-first**  | Auto-discovers every `<loc>` in robots.txt → sitemap.xml      |
| **Custom lists**   | add your custom link.txt file                                 |
| **JS hunter**      | Collects `<script src="…">` as absolute URLs                  |
| **Version mining** | CDN paths, comment headers, `*.version`, source-maps, regex   |
| **Offline CVE**    | Ships with `cve.json` (NVD dump); zero external calls         |
| **Coloured CLI**   | Green = clean, orange = version, red = CVE                    |
| **Pure Python 3**  | Only `requests` & `colorama` dependencies                     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
