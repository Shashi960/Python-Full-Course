import yt_dlp

url = input("Enter YouTube video URL: ")


ydl_opts = {'format': 'best','outtmpl': '%(title)s.%(ext)s'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    print("Download Completed!")
    print("Title:", info.get('title'))
    print("Views:", info.get('view_count'))
    print("Duration (sec):", info.get('duration'))