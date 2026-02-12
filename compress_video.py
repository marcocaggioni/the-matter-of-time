import subprocess
import os

# Input and output paths
input_video = r".\Time exhibit NYE2026_reduced.mp4"
output_video = r".\Time exhibit NYE2026_reduced.mp4"

# Check if input file exists
if not os.path.exists(input_video):
    print(f"Error: {input_video} not found")
    exit(1)

# Get original file size
original_size = os.path.getsize(input_video) / (1024 * 1024)
print(f"Original size: {original_size:.2f} MB")
print("Compressing video further...")

# Temporary output file
temp_output = r".\Time exhibit NYE2026_temp.mp4"

# More aggressive compression settings
command = [
    "ffmpeg",
    "-i", input_video,
    "-vf", "scale=640:360",   # Further reduce to 360p
    "-c:v", "libx264",        # Use H.264 codec
    "-preset", "veryfast",    # Faster encoding
    "-b:v", "300k",           # Further reduce video bitrate to 300 kbps
    "-r", "24",               # Reduce frame rate to 24fps
    "-c:a", "aac",            # Audio codec
    "-b:a", "32k",            # Further reduce audio bitrate to 32 kbps
    "-y",                     # Overwrite output file
    temp_output
]

# Run FFmpeg
try:
    result = subprocess.run(command, check=True)
    
    # Replace original with compressed version
    os.replace(temp_output, output_video)
    
    # Get new file size
    compressed_size = os.path.getsize(output_video) / (1024 * 1024)
    
    print(f"\n✓ Compression complete!")
    print(f"Original size: {original_size:.2f} MB")
    print(f"Compressed size: {compressed_size:.2f} MB")
    print(f"Reduction: {((original_size - compressed_size) / original_size * 100):.1f}%")
    print(f"\nOutput file: {output_video}")
    
except subprocess.CalledProcessError as e:
    print(f"Error: FFmpeg failed to compress the video")
    print("Make sure FFmpeg is installed and available in your PATH")
except FileNotFoundError:
    print("Error: FFmpeg is not installed or not found in PATH")
    print("Please install FFmpeg: https://ffmpeg.org/download.html")

