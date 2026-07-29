# YouTube Video Downloader

A simple Python application to download YouTube videos in the highest available quality using **yt-dlp**. The application uses **Tkinter** to allow the user to choose a download location.

## Features

- Download YouTube videos
- Supports YouTube Shorts
- Downloads the highest available video quality
- Automatically merges video and audio into an MP4 file
- Select download folder using a file dialog
- Simple command-line interface

---

## Requirements

- Python 3.10 or later
- yt-dlp
- FFmpeg

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jebez-sharon/python-mini-projects.git
cd python-mini-projects/Youtube_video_downloader
```

### 2. Install Python dependencies

```bash
pip install yt-dlp
```

### 3. Install FFmpeg

Download FFmpeg from:

https://www.gyan.dev/ffmpeg/builds/

Download the **ffmpeg-git-essentials** (or latest Essentials) build.

Extract the archive and add the **bin** folder to your system PATH.

Verify the installation:

```bash
ffmpeg -version
```

If FFmpeg is installed correctly, it will display the version information.

---

## Running the Application

Run the program using:

```bash
python youtube_downloader.py
```

Enter the YouTube video URL when prompted.

Choose a folder where the video should be saved.

The application will download the highest available quality video.

---

## Supported URLs

- Standard YouTube videos
- YouTube Shorts

Examples:

```
https://www.youtube.com/watch?v=XXXXXXXXXXX

https://www.youtube.com/shorts/XXXXXXXXXXX
```

---

## Technologies Used

- Python
- Tkinter
- yt-dlp
- FFmpeg

---

## Project Structure

```
Youtube_video_downloader/
│
├── youtube_downloader.py
├── README.md
└── requirements.txt
```

---

## Notes

- FFmpeg must be installed and added to your system PATH.
- yt-dlp is used instead of pytube because it is actively maintained and supports the latest YouTube changes.
- The highest available resolution depends on the quality uploaded by the video creator.

---

## License

This project is for educational purposes.