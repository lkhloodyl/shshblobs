# shshblobs
This python script will allow you to save shsh blobs for your device. Works with Python 2.7 100% Did not test it for Python 3 but it should work fine.

## Requirements
You need to download the latest tsschecker release from here:
```
https://github.com/encounter/tsschecker/releases
```
JSON and requests for python2:
```
pip install requests
pip install json
```
JSON and requests for python3:
```
pip3 install requests
pip3 install json
```

## How to find ECID and Model Identifier?
Using iTunes go to your device's summary and click on the labels under "Capacity" until you find the ECID and Model Identifier.
If your ECID is not a combination of numbers and letters then you need to convert it to hex
You can use this website to convert
```
http://www.binaryhexconverter.com/decimal-to-hex-converter
```
