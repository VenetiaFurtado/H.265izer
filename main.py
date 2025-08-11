import os
import time
import yaml
import subprocess
from pathlib import Path

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def is_h265(file_path):
    # Simple check using ffprobe
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
         '-show_entries', 'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1',
         str(file_path)],
        capture_output=True,
        text=True
    )
    return 'hevc' in result.stdout  # hevc == h265

def convert_to_h265(input_path, ffmpeg_path):
    output_path = input_path.with_suffix('.h265.mp4')
    cmd = [
        ffmpeg_path, '-y', '-i', str(input_path),
        '-c:v', 'libx265', '-c:a', 'copy', str(output_path)
    ]
    print(f"Converting {input_path} -> {output_path}")
    subprocess.run(cmd)

def scan_and_convert(config):
    count = 0
    for root, _, files in os.walk(config['input_folder']):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
                filepath = Path(root) / file
                if not is_h265(filepath):
                    convert_to_h265(filepath, config['ffmpeg_path'])
                    count += 1
                    if count >= config['max_conversions_per_run']:
                        return

def main():
    while True:
        config = load_config()
        scan_and_convert(config)
        print(f"Sleeping for {config['scan_interval_minutes']} minutes")
        time.sleep(config['scan_interval_minutes'] * 60)

if __name__ == '__main__':
    main()
