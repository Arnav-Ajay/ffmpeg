import ffmpeg
import json

import interface.fileinterface as fi
import interface.sessioninterface as si

sess_num = 0
output_filename = './output/session' + str(sess_num) + '.mp4'

def get_data(s_id):

    f = open('./data.json')
    data = json.load(f)

    session_files = []

    for i in range(0, data["session" + str(s_id)]["num_input"]):

        name = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["filename"]
        path = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["filepath"]
        ty = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["filetype"]
        st = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["start_time"]
        d = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["duration"]
        ac = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["audio_c"]
        vc = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["video_c"]

        input_file = fi.FileInterface(name, path, ty, st, d, ac, vc)

        session_files.append(input_file)

    session = si.SessionInterface(data["session" + str(s_id)]["num_input"], session_files, data["session" + str(s_id)]["duration"])

    return session

def convert_to_mono(sesh):

    j = 0

    for i in sesh.input_files:

        j += 1

        if(i.audio_c == False and i.filetype == 'mp4'):
            continue

        elif(i.audio_c == True):
            ffmpeg.input(i.filepath).output('./temp/mono_mp4' + str(j) + '.mp4', ac=1).run()

        else:
            ffmpeg.input(i.filepath).output('./temp/mono_mp4' + str(j) + '.mp4', max_muxing_queue_size=9000).run()

        input_i = ffmpeg.input('./temp/mono_mp4' + str(j) + '.mp4')

        i.filetype = 'mp4'
        i.filename = 'mono_mp4' + str(j) + '.mp4'
        i.filepath = './temp/mono_mp4' + str(j) + '.mp4'

    return sesh

def get_audio_comp(i, delay):

    input_i = ffmpeg.input(i.filepath)

    if(i.video_c == True and i.audio_c == True):
        return input_i['a'].filter('adelay', delay)

    else:
        return input_i.filter('adelay', delay)

def get_video_comp(i, num_inputs, offset):

    input_i = ffmpeg.input(i.filepath)

    size = get_dim(num_inputs)


    #    if video component present in input file
    if(i.video_c == True and i.audio_c == True):
        return input_i['v'].filter('scale', size[0], -1).filter('setdar', '16/9').setpts('PTS' + offset)

    #    if audio component present in input file
    else:
        return input_i.filter('scale', size[0], -1).filter('setdar', '16/9').setpts('PTS' + offset)

def get_dim(i):

    w = 0
    h = 0

    if i == 1:
        w = 1280
        h = -1
   
    elif i == 2:  
        w = 320
        h = -1
   
    elif i == 3:  
        w = 320
        h = -1
   
    elif i == 4: 
        w = 320
        h = -1

    else:
        print("\n\nPlease add more conditions\nnum of input files is greater than 4\n\nedit in preprocess.py\n\n")
    
        w = -1
        h = -1

    return (w, h)

def get_cord(i, j):
    x=0
    y=0
    
    if j == 1:
        x = 320
        y = 240

    elif j == 2:

        if i == 0:      
            x = 320
            y = 0
       
        elif i == 1:
            x = 180
            y = 240

        else:
            print('\n\nsomething went wrong\n\n')
   
            x = -1
            y = -1

    elif j == 3:

        if i == 0:   
            x = 320
            y = 0
   
        elif i == 1: 
            x = 0
            y = 240
   
        elif i == 2:
            x = 320
            y = 240

        else:
            print('\n\nsomething went wrong\n\n')
   
            x = -1
            y = -1

    else:
        print('\n\nsomething went wrong\n\n')
   
        x = -1
        y = -1

    return (x, y)