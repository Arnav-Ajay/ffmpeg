import interface.timeline.timelinefile as tf

class Timeline:

    t_id = None
    t_start_time = None
    t_end_time = None
    t_num_inputs = None
    t_input_files = []

    def __init__(self, t_id, t_start_time, t_end_time, t_num_inputs, t_input_files):

        self.t_id = t_id
        self.t_start_time = t_start_time
        self.t_end_time = t_end_time
        self.t_num_inputs = t_num_inputs
        self.t_input_files = t_input_files