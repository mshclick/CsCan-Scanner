import json
CVE_FILE = "cve.json"
VER_FILE = "all_versions.json"
OUT_FILE = "cve_report.json"
data = json.load(open(CVE_FILE, encoding="utf-8"))
vers = json.load(open(VER_FILE))
report = []
for cve_entry in data.get("cve", []):  
    cve_id = cve_entry.get("id", "")
    desc   = cve_entry.get("descriptions", [{}])[0].get("value", "").lower()
    for v in vers:
        prod, ver = v["product"], v["version"]
        if prod.lower() in desc and ver in desc:
            metrics = cve_entry.get("metrics", {})
            score = "N/A"
            if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:
                score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
            elif "cvssMetricV30" in metrics and metrics["cvssMetricV30"]:
                score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]
            print(f"{prod} {ver} → {cve_id}  (CVSS: {score})")
            report.append({"product": prod, "version": ver, "cve": cve_id, "cvss": score})
json.dump(report, open(OUT_FILE, "w"), indent=2)
print(f"{len(report)} CVE found")
