# coding: utf-8
__author__ = 'mancuniancol'


class UnTangle():
    movie = "MOVIE"
    tvShow = "SHOW"
    anime = "ANIME"
    keywords = ['en 1080p', 'en 720p', 'en dvd', 'en dvdrip', 'en hdtv', 'en bluray', 'en blurayrip',
                'en web', 'en rip', 'en ts screener', 'en screener', 'en cam', 'en camrip', 'pcdvd', 'bdremux',
                'en ts-screener', 'en hdrip', 'en microhd', '1080p', '720p', 'dvd', 'dvdrip', 'hdtv', 'bluray',
                'blurayrip', 'web', 'rip', 'ts screener', 'screener', 'cam', 'camrip', 'ts-screener', 'hdrip',
                'brrip', 'blu', 'webrip', 'hdrip', 'bdrip', 'microhd', 'ita', 'eng', 'esp', "spanish espanol",
                'castellano', '480p', 'bd', 'bdrip', 'hi10p', 'sub', 'x264', 'sbs', '3d', 'br', 'hdts', 'dts',
                'dual audio', 'hevc', 'aac', 'batch', 'h264', 'gratis', 'descargar'
                ]

    class info():
        def __init__(self, title="", folder="", rest="", type="", cleanTitle="",
                     year="", quality="", detailQuality="", height="",
                     width="", language=""):
            self.title = title
            self.folder = folder
            self.rest = rest
            self.type = type
            self.cleanTitle = cleanTitle
            self.year = year
            self.quality = quality
            self.detailQuality = detailQuality
            self.height = height
            self.width = width
            self.language = language

    @staticmethod
    def normalize(name, onlyDecode=False):
        from unicodedata import normalize
        import types
        if type(name) == types.StringType:
            unicode_name = name.decode('unicode-escape')
        else:
            try:
                unicode_name = name.encode('latin-1').decode('utf-8')  # to latin-1
            except:
                unicode_name = name
        normalize_name = unicode_name if onlyDecode else normalize('NFKD', unicode_name)
        return normalize_name.encode('ascii', 'ignore')

    @staticmethod
    def uncodeName(name):  # Convert all the &# codes to char, remove extra-space and normalize
        from HTMLParser import HTMLParser
        name = name.replace('<![CDATA[', '').replace(']]', '')
        name = HTMLParser().unescape(name)
        return name

    @staticmethod
    def unquoteName(name):  # Convert all %symbols to char
        from urllib import unquote
        return unquote(name).decode("utf-8")

    @staticmethod
    def safeName(value):  # Make the name directory and filename safe
        import re
        value = UnTangle.normalize(value)  # First normalization
        value = UnTangle.unquoteName(value)
        value = UnTangle.uncodeName(value)
        value = UnTangle.normalize(
            value)  # Last normalization, because some unicode char could appear from the previous steps
        value = value.lower().replace('_', ' ')
        # erase keyword
        value = re.sub('^\[.*?\]', '', value)  # erase [HorribleSub] for ex.
        # check for anime
        value = re.sub('- ([0-9][0-9][0-9][0-9]) ', ' \g<1>', value + " ")
        value = re.sub('- ([0-9]+) ', '- ep\g<1>', value + " ")
        value = value.replace(" episode ", " - ep")
        # check for qualities
        value = value.replace("1920x1080", "1080p")
        value = value.replace("1280x720", "720p")
        value = value.replace("853x480", "480p")
        value = value.replace("848x480", "480p")
        value = value.replace("704x480", "480p")
        value = value.replace("640x480", "480p")
        keys = {'"': ' ', '*': ' ', '/': ' ', ':': ' ', '<': ' ', '>': ' ', '?': ' ', '|': ' ',
                "'": '', '.': ' ', ')': ' ', '(': ' ', '[': ' ', ']': ' ', '-': ' '}
        for key in keys.keys():
            value = value.replace(key, keys[key])
        value = ' '.join(value.split())
        return value.replace('s h i e l d', 'shield').replace('c s i', 'csi')

    @staticmethod
    def checkQuality(text=""):
        # quality
        keyWords = {"Cam": ["camrip", "cam"],
                    "Telesync": ["ts", "telesync", "pdvd"],
                    "Workprint": ["wp", "workprint"],
                    "Telecine": ["tc", "telecine"],
                    "Pay-Per-View Rip": ["ppv", "ppvrip"],
                    "Screener": ["scr", "screener", "screeener", "dvdscr", "dvdscreener", "bdscr"],
                    "DDC": ["ddc"],
                    "R5": ["r5", "r5.line", "r5 ac3 5 1 hq"],
                    "DVD-Rip": ["dvdrip", "dvd-rip"],
                    "DVD-R": ["dvdr", "dvd-full", "full-rip", "iso rip", "lossless rip", "untouched rip",
                              "dvd-5 dvd-9"],
                    "HDTV": ["dsr", "dsrip", "dthrip", "dvbrip", "hdtv", "pdtv", "tvrip", "hdtvrip", "hdrip"],
                    "VODRip": ["vodrip", "vodr"],
                    "WEB-DL": ["webdl", "web dl", "web-dl"],
                    "WEBRip": ["web-rip", "webrip", "web rip"],
                    "WEBCap": ["web-cap", "webcap", "web cap"],
                    "BD/BRRip": ["bdrip", "brrip", "blu-ray", "bluray", "bdr", "bd5", "bd"],
                    "MicroHD": ["microhd"],
                    "FullHD": ["fullhd"],
                    }
        color = {"Cam": "FFF4AE00",
                 "Telesync": "FFF4AE00",
                 "Workprint": "FFF4AE00",
                 "Telecine": "FFF4AE00",
                 "Pay-Per-View Rip": "FFD35400",
                 "Screener": "FFD35400",
                 "DDC": "FFD35400",
                 "R5": "FFD35400",
                 "DVD-Rip": "FFD35400",
                 "DVD-R": "FFD35400",
                 "HDTV": "FFD35400",
                 "VODRip": "FFD35400",
                 "WEB-DL": "FFD35400",
                 "WEBRip": "FFD35400",
                 "WEBCap": "FFD35400",
                 "BD/BRRip": "FFD35400",
                 "MicroHD": "FFD35400",
                 "FullHD": "FFD35400",
                 }
        quality = "480p"
        detailQuality = ""
        for key in keyWords:
            for keyWord in keyWords[key]:
                if ' ' + keyWord + ' ' in ' ' + text + ' ':
                    quality = "480p"
                    detailQuality += " [COLOR %s][%s][/COLOR]" % (color[key], key)

        if "480p" in text:
            quality = "480p"
            detailQuality += " [COLOR FF2980B9][480p][/COLOR]"
        if "720p" in text:
            quality = "720p"
            detailQuality += " [COLOR FF5CD102][720p][/COLOR]"
        if "1080p" in text:
            quality = "1080p"
            detailQuality += " [COLOR FFF4AE00][1080p][/COLOR]"
        if "3d" in text:
            quality = "1080p"
            detailQuality += " [COLOR FFD61515][3D][/COLOR]"
        if "4k" in text:
            quality = "2160p"
            detailQuality += " [COLOR FF16A085][4K][/COLOR]"
        return quality, detailQuality

    @staticmethod
    def width(quality="480p"):
        result = 720
        if '480p' in quality:
            result = 720
        elif '720p' in quality:
            result = 1280
        elif '1080p' in quality:
            result = 1920
        elif '2160p' in quality:
            result = 2160
        return result

    @staticmethod
    def height(quality="480p"):
        result = 480
        if '480p' in quality:
            result = 480
        elif '720p' in quality:
            result = 720
        elif '1080p' in quality:
            result = 1080
        elif '2160p' in quality:
            result = 3840
        return result

    @staticmethod
    def findLanguage(value=""):
        language = ""  # It is english or unknown
        if "spa" in value or "spanish" in value or "espanol" in value:
            language = " Español "
        return language

    @staticmethod
    def exceptionsTitle(title=""):
        value = title + " "
        if "csi " in value:
            title = title.replace("csi", "CSI Crime Scene Investigation")
        return title

    @staticmethod
    def _cleanTitle(value=''):
        keywordsCleanTitle = ['version', 'extendida', 'extended', 'edition', 'hd', 'unrated', 'version',
                              'special', 'edtion', 'uncensored', 'fixed', 'censurada', 'episode', 'ova', 'complete'
                              ]
        for keyword in keywordsCleanTitle:  # checking keywords
            value = (value + ' ').replace(' ' + keyword.title() + ' ', ' ')
        return value.strip()

    @staticmethod
    def __formats__(value=""):
        import re
        formats = [' ep[0-9]+', ' s[0-9]+e[0-9]+', ' s[0-9]+ e[0-9]+', ' [0-9]+x[0-9]+',
                   ' [0-9][0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]',
                   ' [0-9][0-9] [0-9][0-9] [0-9][0-9]', ' season [0-9]+', ' season[0-9]+', ' s[0-9][0-9]',
                   ' temporada [0-9]+ capitulo [0-9]+', ' temporada[0-9]+', ' temporada [0-9]+',
                   ' seizoen [0-9]+ afl [0-9]+',
                   ' temp [0-9]+ cap [0-9]+', ' temp[0-9]+ cap[0-9]+',
                   ]
        for format in formats:  # search if it is a show
            sshow = re.search(format, value)  # format shows
            if sshow is not None:
                break
        return sshow

    @staticmethod
    def __keyWords__(value=""):
        pos = 0
        title = value
        rest = ""
        while pos != -1:  # loop until doesn't have any keyword in the title
            value = title + ' '
            for keyword in UnTangle.keywords:  # checking keywords
                pos = value.find(' ' + keyword + ' ')
                if pos > 0:
                    title = value[:pos]
                    rest = value[pos:].strip() + ' ' + rest
                    break
        return title, rest

    @staticmethod
    def formatTitle(rawTitle='', fileName='', type=""):
        import re
        fileName = rawTitle if fileName == '' else fileName
        pos = rawTitle.rfind("/")
        rawTitle = rawTitle if pos < 0 else rawTitle[pos:]  # extract info from URL
        rawTitle = UnTangle.safeName(rawTitle) + ' '  # ASCII encode
        fileName = UnTangle.safeName(fileName) + ' '  # ASCII encode
        quality, detailQuality = UnTangle.checkQuality(fileName)  # find quality
        language = UnTangle.findLanguage(rawTitle)  # find language
        # check type
        if type == UnTangle.anime:
            rawTitle += " ep00"
        if type == UnTangle.tvShow:
            rawTitle += " s0e00"
        # start processing
        sshow = UnTangle.__formats__(rawTitle)
        if sshow is None:
            # it is a movie
            type = UnTangle.movie
            rawTitle += ' 0000 '  # checking year
            syear = re.search(' [0-9][0-9][0-9][0-9] ', rawTitle)
            year = syear.group(0).strip()
            pos = rawTitle.find(year)
            if pos > 0:
                title = rawTitle[:pos].strip()
                rest = rawTitle[pos + 5:].strip().replace('0000', '')
            else:
                title = rawTitle.replace('0000', '')
                rest = ''
            title, restAdd = UnTangle.__keyWords__(title)
            rest += ' ' + restAdd
            title = title.title().strip().replace('Of ', 'of ').replace('De ', 'de ')
            cleanTitle = UnTangle._cleanTitle(title.replace('0000', ''))
            title += ' (' + year.strip() + ')' if '0000' not in year else ''
            year = year.replace('0000', '')
            folder = title
        else:
            # it is a show
            rest = rawTitle.strip()  # original name
            episode = sshow.group(0)
            # clean title
            for keyword in UnTangle.keywords:  # checking keywords
                rawTitle = rawTitle.replace(' ' + keyword + ' ', ' ')
            title = rawTitle[:rawTitle.find(episode)].strip()
            title = title.strip()
            episode = episode.replace('temporada ', 's').replace(' capitulo ', 'e')
            episode = episode.replace('temp ', 's').replace(' cap ', 'e')
            episode = episode.replace('seizoen ', 's').replace(' afl ', 'e')

            if 'x' in episode:
                episode = 's' + episode.replace('x', 'e')

            if 's' in episode and 'e' in episode and 'season' not in episode:  # force S00E00 instead S0E0
                temp_episode = episode.replace('s', '').split('e')
                episode = 's%02de%02d' % (int(temp_episode[0]), int(temp_episode[1]))

            if 's' not in episode and 'e' not in episode:  # date format
                date = episode.split()
                if len(date[0]) == 4:  # yyyy-mm-dd format
                    episode = episode.replace(' ', '-')  # date style episode talk shows
                else:  # dd mm yy format
                    if int(date[2]) > 50:
                        date[2] = '19' + date[2]
                    else:
                        date[2] = '20' + date[2]
                    episode = date[2] + '-' + date[1] + '-' + date[0]

            episode = episode.replace(' ', '')  # remove spaces in the episode format
            title = UnTangle.exceptionsTitle(title)
            # finding year
            rawTitle = title + ' 0000 '
            syear = re.search(' [0-9][0-9][0-9][0-9] ', rawTitle)
            year = syear.group(0).strip()
            pos = rawTitle.find(year)
            if pos > 0:
                title = rawTitle[:pos].strip()
            title = rawTitle.replace('0000', '')
            year = year.replace('0000', '')
            # the rest
            title = title.title().strip().replace('Of ', 'of ').replace('De ', 'de ')
            folder = title  # with year
            cleanTitle = UnTangle._cleanTitle(title.replace(year, '').strip())  # without year
            title = folder + ' ' + episode.upper()
            type = "SHOW"
            if bool(re.search("EP[0-9]+", title)):
                type = "ANIME"
        # common return
        return UnTangle.info(title=title, folder=folder, rest=rest, type=type, cleanTitle=cleanTitle,
                             year=year, quality=quality, detailQuality=detailQuality, height=UnTangle.height(quality),
                             width=UnTangle.width(quality), language=language)


a = UnTangle.formatTitle("[horriblesubs] The Seminarian 2010 1080p BluRay x264-MELiTE")

print a.cleanTitle, a.__dict__
print a.type
