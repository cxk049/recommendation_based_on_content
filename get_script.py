import pandas as pd
import bccdl

def get_subtitle():
    subtitles = []

    return subtitles


def get_video():
    pass


def vid2pic():
    pass


def ocr_method():
    pass


def get_ocr_subtitle(bvid):
    video = get_video(bvid)
    pics = vid2pic(video)
    subtitles = []
    for pic in pics:
        txt = ocr_method(pic)
        subtitles.append(txt)
    return subtitles


def vid2voi():
    pass


def voice2text():
    voi = vid2voi()
    texts = []
    return texts


def main(bvid):
    script = get_subtitle(bvid)
    if script is None:
        script_ocr = get_ocr_subtitle(bvid)
        script_voi = voice2text(bvid)
    return script, script_ocr, script_voi


if __name__ == 'main':
    main()
