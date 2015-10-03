# coding: utf-8
__author__ = 'mancuniancol'
# from shutil import rmtree
#
#
# path = "C:\Users\Ruben\AppData\Roaming\Kodi\cache\movies/Edge of Tomorrow (2014)"
# rmtree(path)
text = "Edge of tomorrow webdl"

keyWords = {"Cam": ["camrip", "cam"],
            "Telesync": ["ts", "telesync", "pdvd"],
            "Workprint": ["wp", "workprint"],
            "Telecine": ["tc", "telecine"],
            "Pay-Per-View Rip": ["ppv", "ppvrip"],
            "Screener": ["scr", "screener", "dvdscr", "dvdscreener", "bdscr"],
            "DDC": ["ddc"],
            "R5": ["r5", "r5.line", "r5 ac3 5 1 hq"],
            "DVD-Rip": ["dvdrip", "dvd-rip"],
            "DVD-R": ["dvdr", "dvd-full", "full-rip", "iso rip", "lossless rip", "untouched rip", "dvd-5 dvd-9"],
            "HDTV": ["dsr", "dsrip", "dthrip", "dvbrip", "hdtv", "pdtv", "tvrip", "hdtvrip", "hdrip"],
            "VODRip": ["vodrip", "vodr"],
            "WEB-DL": ["webdl", "web dl", "web-dl"],
            "WEBRip": ["web-rip", "webrip", "web rip"],
            "WEBCap": ["web-cap", "webcap", "web cap"],
            "BD/BRRip": ["bdrip", "brrip", "blu-ray", "bluray", "bdr", "bd5", "bd"]}
quality = "480p"
textQuality = ""
for key in keyWords:
    for keyWord in keyWords[key]:
        if ' ' + keyWord + ' ' in ' ' + text + ' ':
            print keyWord
            quality = "480p"
            textQuality += " [COLOR FFF4AE00]%s[/COLOR]" % key
print textQuality
