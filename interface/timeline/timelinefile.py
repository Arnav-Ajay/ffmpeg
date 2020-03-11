class TimelineFile:

    file_start_time = None
    file_duration = None
    input_file = None

    def __init__(self, file_start_time, file_duration, input_file):

        self.file_start_time = file_start_time
        self.file_duration = file_duration
        self.input_file = input_file
