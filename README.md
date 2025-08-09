# YT_Down 🎥⬇️

A Python-based command-line YouTube downloader that supports both single videos and playlists, with customizable video quality options.  
Built with **yt-dlp** for fast, reliable downloads and a simple interactive interface.

---

## Features
- **Download Single Videos or Playlists**  
- **Custom Video Quality Selection** – Choose from `480p`, `720p`, `1080p`, or `Best available`.
- **Resumable Downloads** – Continue partially downloaded files.

---

## 📦 Requirements

Install Python 3.7 or higher and the following Python packages:

```bash
pip install -r requirements.txt
```

This program **requires [FFmpeg](https://ffmpeg.org/)** for video/audio processing.

### 🖥️ Installing FFmpeg

#### **Windows**
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
2. Extract the files.
3. Add the `bin` folder to your Windows PATH environment variable.

#### **Linux (Debian/Ubuntu)**
```bash
sudo apt update
sudo apt install ffmpeg
```

#### **Linux (Arch)**
```bash
sudo pacman -S ffmpeg
```

#### **macOS**
```bash
brew install ffmpeg
```

---

## ▶️ Usage

Clone repo:
```bash
git clone https://github.com/namz182/yt_down.git
```
Run the script:
```bash
python yt_down.py
```

1. Enter the **YouTube video or playlist URL** when prompted.
2. Select the desired **video quality**:
    - `1` → 480p  
    - `2` → 720p  
    - `3` → 1080p  
    - `4` → Best available  
3. If a playlist is detected:
    - The program will display its title and total number of videos.
    - You can choose a **starting index** to download from a specific video onwards.
4. Downloads will be saved inside the `Downloads/` directory.
5. After completion, choose whether to download another or exit.

---

## 📂 Output Structure
```
YT_DOWN/
│── SingleVideo.mp4
│── PlaylistName/
│   ├── Video1.mp4
│   ├── Video2.mp4
│   └── ...
```

---

## ⚙️ Example

**Downloading a playlist starting from video 3 at 720p:**
```
Enter YouTube video or playlist URL: https://www.youtube.com/playlist?list=xxxx
Choose the video quality:
1. 480p
2. 720p
3. 1080p
4. Best available
Enter your choice (1-4): 2
Detected as a playlist: MyPlaylist with 10 videos.
Enter the starting index (1 to 10) [default is 1]: 3
Downloading: 15.20 MB / 50.00 MB (30.40%)
...
Download complete!
```

---

## 🛠️ Built With
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – The backend for downloading videos.
- [pyfiglet](https://pypi.org/project/pyfiglet/) – ASCII art for the CLI.
- [FFmpeg](https://ffmpeg.org/) – Required for video/audio merging and processing.

---

## 👨‍💻 Developer
**Mainza Namangani** – Micho Technologies  
🌐 [Portfolio Website](https://mainza-namangani.rf.gd)  
📦 Version: `V4.8.25`
