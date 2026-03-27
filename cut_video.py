from moviepy import VideoFileClip

# 1. Load your video (ensure the file is in this folder)
clip = VideoFileClip("input.mp4")

# 2. Cut from 5 seconds to 15 seconds
# You can use (start_second, end_second)
trimmed = clip.subclipped(5, 15)

# 3. Save it
trimmed.write_videofile("output_cut.mp4")

print("Done! Check output_cut.mp4")
