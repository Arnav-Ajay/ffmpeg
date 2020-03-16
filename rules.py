import ffmpeg

def convert_to_mono(sesh):

    j = 0

    for i in sesh.input_files:

        j += 1

        if(i.audio_c == False and i.filetype == 'mp4'):
            continue

        elif(i.audio_c == True):
            input_1 = ffmpeg.input(i.filepath)
            video = input_1["v"].filter("scale", 640, 480)
            audio = input_1["a"]
            output = ffmpeg.output(video, audio, './temp/mono_mp4' + str(j) + '.mp4', ac=1,  **{'b:a':'48k'}, max_muxing_queue_size=99000).run()

        else:
            ffmpeg.input(i.filepath).filter("scale", 640, 480).output('./temp/mono_mp4' + str(j) + '.mp4',  **{'b:v':'48k'}, max_muxing_queue_size=99000).run()

        input_i = ffmpeg.input('./temp/mono_mp4' + str(j) + '.mp4')

        i.filetype = 'mp4'
        i.filename = 'mono_mp4' + str(j) + '.mp4'
        i.filepath = './temp/mono_mp4' + str(j) + '.mp4'

    return sesh

def format_session(sesh):

    j = 0

    for i in sesh.input_files:

        j += 1

        if(i.audio_c == True and i.video_c == True):
            
            if(i.flag == 1):

                input = ffmpeg.input(i.filepath)
                audio = input['a'].output('./temp/audio' + str(j) + '.mp4', ac=1,  **{'b:a':'48k'}).run()

                i.filetype = 'mp4'
                i.filename = 'audio' + str(j) + '.mp4'
                i.filepath = './temp/audio' + str(j) + '.mp4'
                i.video_c = False
                i.flag = 0

            elif(i.flag == 2):

                input = ffmpeg.input(i.filepath)
                video = input['v'].output('./temp/video' + str(j) + '.mp4',  **{'b:v':'48k'}).run()

                i.filetype = 'mp4'
                i.filename = 'video' + str(j) + '.mp4'
                i.filepath = './temp/video' + str(j) + '.mp4'
                i.audio_c = False
                i.flag = 0

            elif(i.flag == 3):

                i.audio_c = False
                i.video_c = False
                i.flag = 0

            else:

                i.flag = 0
                print("\nDo Nothing: Default Value Selected\n")

        elif(i.audio_c == True and i.video_c == False):
            
            if(i.flag == 1):

                print("\nDo Nothing: Default Value Selected\n")
                i.flag = 0

            elif(i.flag == 2):

                print("\nVideo does not exist for file : " + i.filename + "\n")
                i.flag = 0

            elif(i.flag == 3):

                i.audio_c = False
                i.flag = 0

            else:

                i.flag = 0
                print("\nDo Nothing: Default Value Selected\n")

        elif(i.audio_c == False and i.video_c == True):
            
            if(i.flag == 1):

                print("\nAudio does not exist for file : " + i.filename + "\n")
                i.flag = 0

            elif(i.flag == 2):

                print("\nDo Nothing: Default Value Selected\n")
                i.flag = 0

            elif(i.flag == 3):

                i.video_c = False
                i.flag = 0

            else:

                print("\nDo Nothing: Default Value Selected\n")
                i.flag = 0

        else:

            print("\n File : " + i.filename + " does not have audio nor video component\n")

    return sesh

def get_dim(i):

    w = 0
    h = 0

    if i == 1:
        w = 640
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
    
        w = 320
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

    elif j == 4:

        if i == 0:   
            x = 320
            y = 0

        elif i == 1: 
            x = 0
            y = 240

        elif i == 2:
            x = 320
            y = 240

        elif i == 3:
            x = 150
            y = 150

        else:
            print('\n\nsomething went wrong\n\n')

            x = -1
            y = -1

    else:
        print('\n\nsomething went wrong\n\n')

        x = -1
        y = -1

    return (x, y)