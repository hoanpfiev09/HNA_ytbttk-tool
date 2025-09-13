
# This module downloads YouTube videos using yt-dlp.
# Input: YouTube URL
# Output: Path to downloaded video file
# Constraints: Must handle errors, support retries, and log events.


def download_video(url: str) -> str:
    import yt_dlp
    import logging
    from pathlib import Path

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Define the output directory and file name
    output_dir = Path("downloads")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "%(title)s.%(ext)s"

    # Set up yt-dlp options
    ydl_opts = {
        'format': 'best',
        'outtmpl': str(output_file),
        'noplaylist': True,
        'retries': 3,
        'retry_sleep': 5,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            logger.info(f"Downloaded video: {url}")
            return str(output_file)
    except Exception as e:
        logger.error(f"Error downloading video: {e}")
        raise