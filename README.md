# Video Converter (H.265)

A background application that:  
- Scans through a folder and its sub-folders to find **non-H.265** video files.  
- Converts them to **H.265** using [FFmpeg](https://ffmpeg.org/).  
- Uses a user-configurable **YAML** file to:  
  - Select the folder to scan.  
  - Set how often to check the folder for video files.  
  - Choose how many files to convert at a time.  
- Runs inside a container with all dependencies pre-installed (e.g., FFmpeg).

---

## Features
- **Automated Scanning** – Recursively checks your chosen folder for new non-H.265 videos.  
- **Smart Conversion** – Converts videos without altering the originals’ folder structure.  
- **Customizable Settings** – All behavior is set in `config.yaml`.  
- **Portable** – Works in Docker, no need to manually install FFmpeg or Python packages.

---

## Getting Started

### **Step 1: Build the Docker image**
```bash
docker build -t video-converter .
```
### **Step 2: Run the container**
Replace ```~/testVideos``` with the path to your video folder.
```bash
docker run --rm -v ~/testVideos:/videos video-converter
```
### Configuration
- **Target folder** to scan for videos.
- **Scan interval** (how often to check for new files).
- **Batch size** (how many videos to process at once).
  
The ```config.yaml``` file can be edited before running:
```bash
folder: "/videos"
scan_interval: 3600    # seconds
batch_size: 2          # number of files to convert per run
```
### Dependencies
All dependencies (including FFmpeg) are installed inside the Docker image.
No additional setup required on the host machine.
