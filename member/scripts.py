import streamlink

def twitchLink(link):
    streams = streamlink.streams(link)
    best = streams["best"].to_url()
    return best
