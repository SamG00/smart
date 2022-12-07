import streamlink
import urllib.request


def twitchLink(link):
    streams = streamlink.streams(link)
    best = streams["best"].to_url()
    return best
