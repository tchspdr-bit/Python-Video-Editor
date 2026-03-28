from moviepy import VideoFileClip

# 1. Load your video (ensure the file is in this folder)
clip = VideoFileClip("clean_video_ALTERED.mp4")

# 1. Trim VIDEO from 5 to 15
video_trimmed = clip.subclipped(5, 15)

# 2. Trim AUDIO from 6 to 16 (Pulls the audio forward by 1 second)
audio_trimmed = clip.audio.subclipped(5, 15)

# 3. Combine and save (keep fps=30 to stabilize it)
final_clip = video_trimmed.with_audio(audio_trimmed)
final_clip.write_videofile("output_cut.mp4", fps=30, audio_codec="aac", audio_fps=44100)
print("Done! Check output_cut.mp4")
