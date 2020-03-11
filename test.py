import ffmpeg

import rules as r
import preprocess as p
import interface.timeline.timeline as t
import interface.timeline.timelinefile as tf

def check_started(i, j):

    for k in j.files_input:
        
        if(i>k.start_time and i< (k.start_time + k.duration)):

            return True

        else:

            return False

def check_num_running(i):

    count = 0

    for j in session_data.input_files:

        if(i >= j.start_time and i < (j.start_time + j.duration)):

            count += 1

    return count

def get_running_files(i):

    files = []

    for j in session_data.input_files:

        if(i >= j.start_time and i < (j.start_time + j.duration)):

            files.append(j)

    return files


session_number = 1

session_data = p.get_data(session_number)

#session_data = r.convert_to_mono(data)

time_interval = []
for i in session_data.input_files:

    if i.start_time not in time_interval:
        time_interval.append(i.start_time)
    
    if (i.start_time + i.duration) not in time_interval:
        time_interval.append((i.start_time + i.duration))

time_interval.sort()

id = 0
ID = 0
files = []
timeline_files = []
timeline_intervals = []

for i in range(0, (len(time_interval) - 1)):

    #    timeline id
    id += 1

    #    timeline start time
    start_1 = time_interval[i]

    #    timeline num files
    count = check_num_running(time_interval[i])

    print("\n" + str(count))

    #    corresponding files
    files = get_running_files(time_interval[i])

    #    timeline end time
    end_1 = time_interval[i + 1]


    for j in files:

        ID += 1

        st = start_1 - j.start_time

        d = end_1 - start_1

        input_trim = ffmpeg.input(j.filepath, ss=st, t=d).output("./temp/trim" + str(ID) + ".mp4").run()

        timeline_file = tf.TimelineFile(st, d, j)

        timeline_files.append(timeline_file)

    timeline = t.Timeline(id, start_1, end_1, count, timeline_files)

    timeline_intervals.append(timeline)

id = 0

#for i in timeline_files:

#    id += 1

#    input_trim = ffmpeg.input(i.input_file.filepath, ss=i.file_start_time, t=i.file_duration).output("./temp/trim" + str(id) + ".mp4").run()

#for i in timeline.t_input_files:

#    print(i.input_file.filename)


#for i in timeline_intervals:

#    print(i.t_id)
#    print(i.t_start_time)
#    print(i.t_end_time)
#    print(i.t_num_inputs)
#    print(i.t_id)

#    for j in i.t_input_files:

#        id += 1

#        input_trim = ffmpeg.input(j.input_file.filepath, ss=j.file_start_time, t=j.file_duration).output("./temp/trim" + str(id) + ".mp4").run()


#        print(j.input_file.filename)