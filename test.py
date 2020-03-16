import ffmpeg

input1 = ffmpeg.input("./files/WB4.webm")
video = input1["v"].filter("scale", 640, 480)

output = ffmpeg.output(video, "./scaletest.mp4").run()
print("\n\n\n")
#to_mp4 = input1.output("./mp4.mp4").run()

input2 = ffmpeg.probe("./files/Zoom.webm")

print(input2)