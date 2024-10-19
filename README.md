Here’s an extended `README.md` file tailored for a GitHub public repository based on your `yt_dlp` program for downloading videos and subtitles:

---

# YouTube Video & Subtitle Downloader

A Python script that allows you to download YouTube videos along with automatic subtitles using `yt_dlp`. This tool is easy to use and supports selecting the subtitle language for better accessibility.

## Features

- Downloads the best quality video from a YouTube URL.
- Automatically downloads subtitles in the desired language (if available).
- Supports automatic subtitles if no manual subtitles are available.
- Simple to configure and run from the command line.

## Prerequisites

- **Python 3.6+**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **yt-dlp**: The script uses the `yt_dlp` Python library to handle video downloads and subtitles.

### Installing yt-dlp

You can install `yt-dlp` via `pip`:

```bash
pip install yt-dlp
```

For more information, visit the [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp).

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Run the script:

   ```bash
   python downloader.py
   ```

   You'll be prompted to enter:
   - YouTube video URL
   - Subtitle language (e.g., `en` for English)
   - The directory to save the video and subtitle file

3. After running the script, the video and its corresponding subtitle file will be saved in the directory you specify.

### Example

```bash
Enter YouTube video URL: https://www.youtube.com/watch?v=example
Enter subtitle language (e.g., 'en'): en
Enter directory to save video and subtitles: ./downloads
```

The downloaded video and subtitle file (if available) will be saved in the `./downloads` directory.

## Code Explanation

The core functionality is wrapped inside the `download_video_and_subtitles` function, which accepts the video URL, save directory, and subtitle language as inputs.

```python
def download_video_and_subtitles(video_url, save_dir, subtitle_lang):
    ydl_opts = {
        'outtmpl': f'{save_dir}/%(titles)s.%(ext)s',
        'subtitleslangs': [subtitle_lang],
        'writeautomaticsub': True,
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
```

- **outtmpl**: Defines the naming convention and location for the saved files.
- **subtitleslangs**: Specifies the desired subtitle language.
- **writeautomaticsub**: Downloads automatically generated subtitles if no manual subtitles are available.
- **format**: Chooses the best available video format.

## Requirements

- Python 3.6 or higher
- yt-dlp

Install all requirements via `pip`:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
yt-dlp
```

## Customization

You can modify the script to:
- Change the video format (e.g., download audio-only).
- Automatically organize downloaded files based on categories (e.g., video type, language).

For more advanced configurations, check the `yt-dlp` options: [yt-dlp Options](https://github.com/yt-dlp/yt-dlp#usage-and-options).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and create a pull request, or open an issue.

---

Feel free to modify the repository name and add any specific project details or features that you plan to implement in the future.
