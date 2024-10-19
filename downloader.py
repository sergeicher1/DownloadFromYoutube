import yt_dlp

def download_video_and_subtitles(video_url, save_dir, subtitle_lang):
    ydl_opts = {
        'outtmpl': f'{save_dir}/%(titles)s.%(ext)s',
        'subtitleslangs':[subtitle_lang],
        'writeautomaticsub':True,
        'format' : 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def main():
    video_url = input("Enter YouTube video URL: ").strip()
    subtitle_lang = input("Enter subtitle language (e.g., 'en'): ").strip()
    save_dir = input("Enter directory to save video and subtitles: ").strip()

    download_video_and_subtitles(video_url,save_dir, subtitle_lang)

if __name__ == "__main__":
    main()