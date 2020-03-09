# ffmpeg-python

Developed/Tested on Elementary OS 5.1 Hera
Python 3.6

Worked/Tested with .mp4 and .webm files

Clone the git repository:

	git clone https://github.com/Arnav-Ajay/ffmpeg.git

Install the following:

	pip3 install ffmpeg-python --user
	sudo apt-get install libavdevice57
	sudo apt-get install ffmpeg

To Run:

	Create 3 empty folders inside the project directory, 'files', 'output', 'temp'.

	Place all input files in ffmpeg/files/ directory.

	Make the required changes in ffmpeg/data.json file

Change background image from:
	
	ffmpeg/fmpg.py, line 7
	
Select a perticular session by it's ID:

	ffmpeg/fmpy.py, line 6

from inside the project directory, type:
		
	python3 fmpg.py

# Directory Structure
	
	├── data.json				#    Json file containing data of each session.
	├── files				#    Directory containing all input files
	│   ├── background.png
	│   ├── vid1.mp4
	│   ├── vid2.mp4
	├── fmpg.py				#    FFMPEG-Python Implementation
	├── interface				#    Directory containing File and Session Interface
	│   ├── fileinterface.py
	│   └── sessioninterface.py
	├── output				#   Directory containing all output files 
	│   ├── session1.mp4
	├── preprocess.py			#    Support python file for fmpg.py
	├── README.md
	├── rules.py				#    Contains rules/format of how each vid/audio should be
	├── temp				#   Directory containing all temp files, these get generated and deleted during run time

# data.json Format:

	{
	    "session1": {
		"num_input" : 4,
		"input_files": {
		    "file1" : {
			"filename" : "LR1.mp4",
			"filepath" : "./files/LR1.mp4",
			"filetype" : "mp4",
			"start_time" : 0,
			"duration" : 240,
			"audio_c" : true,
			"video_c" : true,
            "flag" : 0
		    },
		    "file2" : {
			"filename" : "WB1.mp4",
			"filepath" : "./files/WB1.mp4",
			"filetype" : "mp4",
			"start_time" : 45,
			"duration" : 261,
			"audio_c" : false,
			"video_c" : true,
            "flag" : 0
		    },
		    "file3" : {
			"filename" : "vid1.mp4",
			"filepath" : "./files/vid1.mp4",
			"filetype" : "mp4",
			"start_time" : 15,
			"duration" : 30,
			"audio_c" : true,
			"video_c" : true,
            "flag" : 2
		    },
		    "file4" : {
			"filename" : "vid2.mp4",
			"filepath" : "./files/vid2.mp4",
			"filetype" : "mp4",
			"start_time" : 20,
			"duration" : 30,
			"audio_c" : true,
			"video_c" : true,
            "flag" : 1
		    }
		},
		"duration" : 306
	    }
	    "session2":{
	    	.
	    	.
	    	.
	    },
	    .
	    .
	    .
	}

# Preprocess.py

	get_data() : Fetches data from json file to File and Session Object
	
	get_audio_component() : Seperates Audio Component from input files
	
	get_video_component() : Seperates Video Component from input files
	
	check_num_audios() : Return mixed audio for no. of audios < 3. This is the first step of mixing audios together
	
	create_output() : Creates output for more than 1 input files
	
	empty_temp() : Deletes all files in Temp folder
	
# Rules.py

	convert_to_mono() : Converts all webm files and files containing audio to mono, mp4 format.

	get_dim() : Size of input file differs based of no. of inputs.
	
	get_cord() : Position of input file differs based of no. of inputs.
	
# Fmpg.py

	P.get_data()
	
	R.convert_to_mono()
	
	P.get_audio_component()
	
	P.get_video_component()
	
	R.get_cord()

	P.check_num_audios()
	
	P.create_output()
		
		R.get_dim()
		
	P.empty_temp()

# Attributes of File Object

	filename : Name of File (String),
	filepath : Path of File (String),
	filetype : File Extension (String),
	start_time : Time at which the video/ audio starts (in Seconds),
	duration : Total duration of input file (in Seconds),
	audio_c : Tells if input file has audio component (Boolean),
	video_c : Tells if input file has Video component (Boolean),
    flag : Ranges from 0 to 3. indicates which component to choose (Number)
			0 : No changes
			1 : Only audio component needed
			2 : Only video component needed
			3 : Skip file altogether(not required)

	
# Attributes of Session Object

	num_inputs : Number of input files (Number),
	input_files : list of input files (File Object),
	duration : Total duration of session (in Seconds)

