import interface.fileinterface as fi

class SessionInterface:

    num_input = None
    input_files = []
    duration = None

    def __init__(self, num_input, input_files, duration):

        self.num_input = num_input
        self.input_files = input_files
        self.duration = duration