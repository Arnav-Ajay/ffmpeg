import ffmpeg

import rules as r
import preprocess as p

import interface.timeline as t
import interface.fileinterface as fi

#    Change the session number to select a perticular session
session_number = 11

#    Initializing some key varialbles
output_vid = None
offset_time = None
delay_margin = None
delay = ''

time_interval = []
files = []
timeline_files = []
timeline_intervals = []
input_audios = []
input_videos = []
sub_input = []
final_input = []

file_id = 0
timeline_id = 0
sub_op_id = 0

#    path to background image
base = './files/background.png'

trim_output_filetype = ".mp4"
trim_output_filename = "trim" + str(file_id) + ".mp4"
trim_output_filepath = "./temp/trim" + str(file_id) + ".mp4"
sub_op_filepath = './temp/sub_op' + str(sub_op_id) + '.mp4'
output_filename = './output/session' + str(session_number) + '.mp4'
vid_output_filename = './temp/vid_output.mp4'

#    returns no of files running at a perticular time
def check_num_running(i):

    count = 0

    for j in session_data.input_files:

        if(j.video_c == True):

            if(i >= j.start_time and i < (j.start_time + j.duration)):

                count += 1

    return count

#    returns a list of files running at a perticular time
def get_running_files(i):

    files = []

    for j in session_data.input_files:

        if(j.video_c == True):

            if(i >= j.start_time and i < (j.start_time + j.duration)):

                files.append(j)

    return files

#    fetch data from json file to session and file object
data = p.get_data(session_number)

#    uncomment for debugging purpose
#for i in data.input_files:

#    print(i.filename)


#    convert the audio files to have channel : mono, filetype : mp4
mono_data = r.convert_to_mono(data)

#    uncomment for debugging purpose
#for i in mono_data.input_files:

#    print(i.filename)

session_data = r.format_session(mono_data)

#    uncomment for debugging purpose
#for i in session_data.input_files:

#    print(i.filename)
#    print(i.start_time)
#    print(i.duration)
#    print(i.duration + i.start_time)
#    print(i.audio_c)
#    print(i.video_c)   

for i in session_data.input_files:

    #    Creating timeline from start and end time of each input file
    if(i.video_c == True):

        if(i.start_time not in time_interval):
            time_interval.append(i.start_time)

        end = i.start_time + i.duration

        if(end not in time_interval):
            time_interval.append(end)

    elif(i.video_c == False and i.audio_c == False):
        session_data.input_files.remove(i)
        print("\n N  file : " + i.filename)


    #    for the following case:
    #    if that file is starting before any other file or if it is ending 
    #    after any other file, then we need to consider it.
    elif(i.video_c == False and i.audio_c == True):

        end = i.start_time + i.duration
        print("\n Ao end time of file : " + i.filename + "is " + str(end))

        #    returns the greatest end time and smallest start time from session data
        large = p.get_greatest_et(session_data)
        small = p.get_smallest_st(session_data)

        #    compare with current files start and end time
        if(i.start_time == small):

            if(i.start_time not in time_interval):
                time_interval.append(i.start_time)

        if(end == large):

            print("\n Ai end time of file : " + i.filename + "is " + str(end))

            if(i.start_time + i.duration) not in time_interval:
                time_interval.append(end)

    else:
        print("\n else  file : " + i.filename)

    #    Separating Audio component from input files
    offset_time = i.start_time
    delay_margin = offset_time * 1000
    delay = str(delay_margin)

    if(i.audio_c == True):
        audio = p.get_audio_comp(i, delay)

        if(audio!=None):
            input_audios.append(audio)

    #    if input file has neither of the components, i.e an error file, then
    if(i.video_c == False and i.audio_c == False):

        print("Input File " + i.filename + " does not have both video and audio component")

#    uncomment for debugging purpose
#print(time_interval)

time_interval.sort()

#print(time_interval)
#print(input_audios)

#    Trim each video occuring in a time interval, and add all the files to timeline interface
for i in range(0, (len(time_interval) - 1)):

    timeline_id += 1

    start_1 = time_interval[i]
    end_1 = time_interval[i + 1]

    #    num of files in a perticular time interval
    count = check_num_running(time_interval[i])

    #    corresponding files in a perticular time interval
    files = get_running_files(time_interval[i])

    #print(files)

    if(files == []):

        timeline = t.Timeline(timeline_id, start_1, (end_1 - start_1), 0, None)

        timeline_intervals.append(timeline)

    else:

        #    adding timeline files to timeline object
        for j in files:

            file_id += 1

            trim_output_filetype = ".mp4"
            trim_output_filename = "trim" + str(file_id) + ".mp4"
            trim_output_filepath = "./temp/trim" + str(file_id) + ".mp4"

            #    start time and duration of input file in a time interval
            d = end_1 - start_1
            st = start_1 - j.start_time

            #    trim file by setting start time and duration
            input_1 = ffmpeg.input(j.filepath, ss=st, t=d).output(trim_output_filepath).run()
       
            timeline_file = fi.FileInterface(trim_output_filename, trim_output_filepath, trim_output_filetype, st, d, j.audio_c, j.video_c, j.flag)

            #    uncomment for debugging purpose
            #print("\n" + timeline_file.filename)
            #print(timeline_file.filepath)
            #print(timeline_file.filetype)
            #print(timeline_file.start_time)
            #print(timeline_file.duration)
            #print(timeline_file.audio_c)
            #print(timeline_file.video_c)
            #print(timeline_file.flag)
            
            timeline_files.append(timeline_file)

        if(timeline_files != []):

            timeline = t.Timeline(timeline_id, start_1, d, count, timeline_files)
            timeline_intervals.append(timeline)

        #    Empty timeline files list to add files of next interval
        timeline_files = []

#    merge files belonging to same time interval
for i in timeline_intervals:

    sub_op_id += 1

    base_image = ffmpeg.input(base, loop=1, framerate=48, t=i.t_duration).filter('scale', 640, 480)

    #    Seperating video from input files
    if(i.t_input_files == None):

        input_videos = None
     
    else:

        for j in i.t_input_files:

            if(j.video_c == True):
                video = p.get_video_comp(j, i.t_num_inputs)

                if(video!=None):
                    input_videos.append(video)

    #    if no file is running in a time interval,
    #    create empty background of time interval's duration
    if(input_videos == None):

        sub_op_filepath = './temp/sub_op' + str(sub_op_id) + '.mp4'

        output = ffmpeg.output(base_image, sub_op_filepath).run()

        sub_input.append(sub_op_filepath) 

    #   else output or overlay
    elif(len(input_videos) == 1):

        sub_op_filepath = './temp/sub_op' + str(sub_op_id) + '.mp4'

        output = ffmpeg.output(input_videos[0], sub_op_filepath, **{'b:v':'48k'}).run()
     
        sub_input.append(sub_op_filepath)

    #    for more than one input files
    else:
        overlay = ffmpeg.overlay(base_image, input_videos[0], x=0, y=0, eof_action='pass')
        n = len(input_videos)
        n-=1
        for i in range(1, len(input_videos)):

            #    returns coordinates for overlaying the video component
            cord = r.get_cord(i-1, n)
            overlay = ffmpeg.overlay(overlay, input_videos[i], x=cord[0], y=cord[1], eof_action='pass')

        #    returns a list of overlaied output files of each time interval
        sub_input = p.create_sub_output(overlay, sub_op_id, sub_op_filepath, sub_input)
        
    input_videos = []

#    setting each overlaid file to have the same format
for i in sub_input:

    input_i = ffmpeg.input(i).filter('setdar', '16/9')

    final_input.append(input_i)

#    concating different overlaid video components
if(len(final_input) == 1):
    
    final_vid = ffmpeg.output(final_input[0], vid_output_filename, **{'b:v':'48k'}).run()
    output_vid = ffmpeg.input(vid_output_filename)

elif(len(final_input) >= 2):
    output_vid = ffmpeg.concat(final_input[0], final_input[1], v=1, n=2)

if(len(final_input) > 2):
    for i in range(2, len(final_input)):        

        output_vid = ffmpeg.concat(output_vid, final_input[i])

#    Generating final output
#    for only one input file
if(session_data.num_input==1):

    #    if input file has no audio component
    if(len(input_audios)==0):
        output = ffmpeg.output(output_vid, output_filename, **{'b:v':'48k'}).run()

    #    if input file has no video component
    elif(output_vid == None):
        output = ffmpeg.output(input_audios[0], output_filename, **{'b:a':'48k'}).run()

    else:
        output = ffmpeg.output(output_vid, input_audios[0], output_filename, **{'b:v':'48k', 'b:a':'48k'}).run()

else:

    #    for num of input audios less than 3; returns audio
    audio = p.check_num_audios(input_audios)

    #    Merges audio and combines with the concated video component to generate output file
    p.create_output(input_audios, audio, output_vid, session_number, output_filename)

#    empty temp directory
p.empty_temp()