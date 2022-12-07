import youtube_dl

def youtube(link):
    with youtube_dl.YoutubeDL({}) as ydl:
        return ydl.extract_info(link,download=False)
    
