import ffmpeg

def convert_to_mono(sesh):

    j = 0

    for i in sesh.input_files:

        j += 1

        if(i.audio_c == False and i.filetype == 'mp4'):
            continue

        elif(i.audio_c == True):
            ffmpeg.input(i.filepath).output('./temp/mono_mp4' + str(j) + '.mp4', ac=1,  **{'b:a':'48k'}).run()

        else:
            ffmpeg.input(i.filepath).output('./temp/mono_mp4' + str(j) + '.mp4',  **{'b:v':'48k'}, max_muxing_queue_size=9000).run()

        input_i = ffmpeg.input('./temp/mono_mp4' + str(j) + '.mp4')

        i.filetype = 'mp4'
        i.filename = 'mono_mp4' + str(j) + '.mp4'
        i.filepath = './temp/mono_mp4' + str(j) + '.mp4'

    return sesh

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