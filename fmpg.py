import ffmpeg

import rules as r
import preprocess as p

session_number = 5
base = './files/background.png'

output_filename = './output/session' + str(session_number) + '.mp4'


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

session_data = r.convert_to_mono(data)
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

#    if there is only one input file, no need to overlay
if(session_data.num_input==1):

    #    if input file has only video component
    if(len(input_audios)==0):
        output = ffmpeg.output(input_videos[0], output_filename, **{'b:v':'48k'}).run()

    #    if input file has only audio component
    elif(len(input_videos)==0):
        output = ffmpeg.output(input_audios[0], output_filename, **{'b:a':'48k'}).run()


    else:
        output = ffmpeg.output(input_videos[0], input_audios[0], output_filename, **{'b:v':'48k', 'b:a':'48k'}).run()


#    for more than one input files
else:
    overlay = ffmpeg.overlay(base_image, input_videos[0], x=0, y=0, eof_action='pass')
    n = len(input_videos)
    n-=1
    for i in range(1, len(input_videos)):

        cord = r.get_cord(i-1, n)
        overlay = ffmpeg.overlay(overlay, input_videos[i], x=cord[0], y=cord[1], eof_action='pass')

    #    for num of input audios less than 3; returns audio
    audio = p.check_num_audios(input_audios)

    p.create_output(input_audios, audio, overlay, session_number, output_filename)


p.empty_temp()