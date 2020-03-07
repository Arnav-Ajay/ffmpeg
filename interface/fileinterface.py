class FileInterface:

    filename = ''
    filepath = ''
    filetype = ''
    start_time = None
    duration = None
    audio_c = None
    video_c = None

    def __init__(self, filename, filepath, filetype, start_time, duration, audio_c, video_c):
        self.filename = filename
        self.filepath = filepath
        self.filetype = filetype
        self.start_time = start_time
        self.duration = duration
        self.audio_c = audio_c
        self.video_c = video_c
