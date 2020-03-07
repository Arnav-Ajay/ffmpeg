import preprocess as p
import ffmpeg

session_number = 7
base = './files/background.png'


#    initiating key variables
offset_time = None
offset = ''
delay_margin = None
delay = ''
input_videos = []
input_audios = []
j=0

data = p.get_data(session_number)
print(data.input_files[0].filename)

session_data = p.convert_to_mono(data)
print(session_data.input_files[0].filename)

for i in session_data.input_files:

    offset_time = i.start_time
    delay_margin = offset_time * 1000
    offset = '+' + str(offset_time) + '/TB'
    delay = str(delay_margin)
    j += 1

    if(i.audio_c == True):
        audio = p.get_audio_comp(i, delay)
        input_audios.append(audio)

    if(i.video_c == True):
        video = p.get_video_comp(i, len(session_data.input_files), offset)
        input_videos.append(video)

     #    if input file has neither of the components, i.e an error file, then
    if(i.video_c == False and i.audio_c == False):
        print("Input File " + i.filename + " does not have both video and audio component")

#    you can overlay a video on a video only, so convert image to video.
base_image = ffmpeg.input(base, loop=1, framerate=48, t=session_data.duration).filter('scale', 640, 480)
