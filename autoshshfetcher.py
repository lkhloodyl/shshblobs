import requests
import json
import subprocess

ecid = "" # In Hex
identifier = "" # Example iPhone9,3
while True:
    r = requests.get("https://api.ipsw.me/v4/device/iphone9,3?type=ipsw")
    js = json.loads(r.text)
    firmwares = js['firmwares']
    for firmware in firmwares:
        ver = firmware['version']
        subprocess.Popen("tsschecker.exe -e %s -d %s -i %s -s --save-path blobs" % (ecid,identifier,ver),creationflags=0x08000000)
        print("Trying to download shsh blobs for iOS %s" % (ver))
