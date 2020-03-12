import ffmpeg
import json
import os

import rules as r

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
        f = data["session" + str(s_id)]["input_files"]["file" + str(i+1)]["flag"]

        input_file = fi.FileInterface(name, path, ty, st, d, ac, vc, f)

        session_files.append(input_file)

    session = si.SessionInterface(data["session" + str(s_id)]["num_input"], session_files, data["session" + str(s_id)]["duration"])

    return session

def get_audio_comp(i, delay):

    input_i = ffmpeg.input(i.filepath)

    flag = i.flag

    if(flag == 0 or flag == 1):

        if(i.video_c == True and i.audio_c == True):
            return input_i['a'].filter('adelay', delay)

        else:
            return input_i.filter('adelay', delay)

    elif(flag == 2 or flag == 3):

        return None

    else:
        return None

def get_audio_comp_test(i):

    input_i = ffmpeg.input(i.filepath)

    flag = i.flag

    if(flag == 0 or flag == 1):

        if(i.video_c == True and i.audio_c == True):
            return input_i['a']

        else:
            return input_i

    elif(flag == 2 or flag == 3):

        return None

    else:
        return None

def get_video_comp(i, num_inputs, offset):

    input_i = ffmpeg.input(i.filepath)

    size = r.get_dim(num_inputs)

    flag = i.flag

    if(flag == 0 or flag == 2):
        #    if video component present in input file
        if(i.video_c == True and i.audio_c == True):
            return input_i['v'].filter('scale', size[0], -1).filter('setdar', '16/9').setpts('PTS' + offset)

        #    if audio component present in input file
        else:
            return input_i.filter('scale', size[0], -1).filter('setdar', '16/9').setpts('PTS' + offset)

    elif(flag == 1 or flag == 3):

        return None

    else:
        return None

def get_video_comp_test(i, num_inputs):

    input_i = ffmpeg.input(i.filepath)

    size = r.get_dim(num_inputs)

    flag = i.flag

    if(flag == 0 or flag == 2):
        #    if video component present in input file
        if(i.video_c == True and i.audio_c == True):
            return input_i['v'].filter('scale', size[0], -1).filter('setdar', '16/9')

        #    if audio component present in input file
        else:
            return input_i.filter('scale', size[0], -1).filter('setdar', '16/9')

    elif(flag == 1 or flag == 3):

        return None

    else:
        return None

def check_num_audios(input_audios):

    if(len(input_audios)==0):
        print("No audio component present\n")
        return None
    elif(len(input_audios)==1):
        audio = input_audios[0]
    else:
        audio = ffmpeg.filter([input_audios[0], input_audios[1]], 'amix')

    return audio

def create_output(input_audios, audio, overlay, session_num, name):

    if(len(input_audios)<3 and audio!=None):
        output = ffmpeg.output(overlay, audio, name, **{'b:v':'48k', 'b:a':'48k'}).run()

    elif(audio==None):
        output = ffmpeg.output(overlay, name, **{'b:v':'48k'}).run()

    else:
        for i in range(2, len(input_audios)):
            audio = ffmpeg.filter([audio, input_audios[i]], 'amix')

        output = ffmpeg.output(overlay, audio, name, **{'b:v':'48k', 'b:a':'48k'}).run()

def create_sub_output(overlay, id, name, sub_input):

    name = './temp/sub_op' + str(id) + '.mp4'

    output = ffmpeg.output(overlay, name, **{'b:v':'48k'}).run()

    sub_input.append(name)

    return sub_input

def empty_temp():

    cmd = "rm ./temp/*"

    os.system(cmd)