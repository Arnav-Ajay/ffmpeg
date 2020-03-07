import ffmpeg

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

    print(input_audios)
    print(audio)
    print(overlay)
    print(str(session_num))

    if(len(input_audios)<3 and audio!=None):
        output = ffmpeg.output(overlay, audio, name, **{'b:v':'48k', 'b:a':'48k'}).run()

    elif(audio==None):
        output = ffmpeg.output(overlay, name, **{'b:v':'48k'}).run()

    else:
        for i in range(2, len(input_audios)):
            audio = ffmpeg.filter([audio, input_audios[i]], 'amix')

        output = ffmpeg.output(overlay, audio, name, **{'b:v':'48k', 'b:a':'48k'}).run()
