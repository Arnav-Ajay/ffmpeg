class Timeline:

    t_id = None
    t_start_time = None
    t_duration = None
    t_num_inputs = None
    t_input_files = []

    def __init__(self, t_id, t_start_time, t_duration, t_num_inputs, t_input_files):

        self.t_id = t_id
        self.t_start_time = t_start_time
        self.t_duration = t_duration
        self.t_num_inputs = t_num_inputs
        self.t_input_files = t_input_files