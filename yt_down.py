import os
import yt_dlp
import pyfiglet

# ===================== Progress hook function =================
def progress_hook(d):
    if d['status'] == 'downloading':
        total_size_mb = d.get('total_bytes', 0) / (1024 * 1024)  
        downloaded_size_mb = d.get('downloaded_bytes', 0) / (1024 * 1024)  
        percentage = (downloaded_size_mb / total_size_mb) * 100 if total_size_mb > 0 else 0
        print(f"\rDownloading: {downloaded_size_mb:.2f} MB / {total_size_mb:.2f} MB ({percentage:.2f}%)", end='')
    elif d['status'] == 'finished':
        print("\nDownload complete!")

ydl_opts = {
    'continuedl': True,                   # Resume partial downloads
    'ignoreerrors': True,                 # Ignore errors during playlist downloads
    'progress_hooks': [progress_hook],    # Attach the progress hook
    'quiet': True,                    # Don't suppress progress
    'no_warnings': True,               # Suppress warnings
}

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_playlist_info(url):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                return info.get('title', 'Playlist'), len(info['entries'])
    except Exception as e:
        print(f"Error fetching playlist information: {e}")
    return None, None

def download_video_or_playlist(video_url, output_dir, quality, start_index=1, is_playlist=False):
    if quality == "best":
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
    else:
        ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'

    if is_playlist:
        ydl_opts['outtmpl'] = os.path.join(output_dir, 'yt_down %(playlist_index)s: %(title)s.%(ext)s')
        ydl_opts['playliststart'] = start_index
    else:
        ydl_opts['outtmpl'] = os.path.join(output_dir, 'yt_down %(title)s.%(ext)s')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")
    except yt_dlp.utils.DownloadError:
        print("Error: Invalid URL or download failed. Please check the link and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    GREEN = "\033[92m"
    RED = "\033[31m"
    RESET = "\033[0m"

    dev = f"""
               {GREEN}
                    BY  
                        Micho Technologies | Mainza Namangani
                        https://mainza-namangani.rf.gd 
                        V4.8.25   
    {RESET}
    """
    print("=" * 70)
    txt = pyfiglet.figlet_format('YouTube_Down')
    print(f"{RED}{txt}{RESET}")
    print(dev)
    print("=" * 70)

    user_downloads = os.path.join(os.path.expanduser("~"), "Downloads", "YT_DOWN")
    ensure_directory_exists(user_downloads)

    while True:
        video_url = input("\nEnter YouTube video or playlist URL: ").strip()
        if not video_url:
            print("Error: URL cannot be empty. Please try again.")
            continue

        print("\nChoose the video quality:")
        print("1. 480p")
        print("2. 720p")
        print("3. 1080p")
        print("4. Best available")
        quality_choice = input("Enter your choice (1-4): ").strip()

        quality_map = {
            "1": "480",
            "2": "720",
            "3": "1080",
            "4": "best"
        }
        quality = quality_map.get(quality_choice, "720")

        playlist_title, total_items = get_playlist_info(video_url)
        if total_items:
            print(f"{GREEN}Detected as a playlist: {playlist_title} with {total_items} videos.{RESET}")
            try:
                start_index = input(f"Enter the starting index (1 to {total_items}) [default is 1]: ").strip()
                start_index = int(start_index) if start_index else 1
                if start_index < 1 or start_index > total_items:
                    print(f"{RED}Invalid input. Defaulting to index 1.{RESET}")
                    start_index = 1
            except ValueError:
                print("Invalid input for starting index. Defaulting to index 1.")
                start_index = 1

            playlist_dir = os.path.join(user_downloads, playlist_title)
            ensure_directory_exists(playlist_dir)
            download_video_or_playlist(video_url, playlist_dir, quality, start_index, is_playlist=True)
        else:
            print(f"{GREEN}Detected as a single video.{RESET}")
            download_video_or_playlist(video_url, user_downloads, quality, is_playlist=False)

        try:
            choice = int(input("Enter 1 to download another video or playlist, or 0 to exit: "))
            if choice == 0:
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Exiting...")
            break

if __name__ == "__main__":
    main()
