[app]
title = PyCalc Mobile
package.name = pycalc_mobile
package.domain = org.example
version = 0.1
source.dir = .
source.include_exts = py,kv,png,jpg,json

requirements = python3,kivy,requests,certifi,charset-normalizer,idna,urllib3

android.permissions = INTERNET

# Optional archs:
# android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
