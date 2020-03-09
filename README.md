# ffmpeg

Clone the git repository:

	git clone https://github.com/Arnav-Ajay/ffmpeg.git

Install the following:

	pip3 install ffmpeg-python --user
	sudo apt-get install libavdevice57
	sudo apt-get install ffmpeg

To Run:

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

# Run this using your Video/Audio Files

Place all input files in ffmpeg/files/ directory.

Make the required changes in ffmpeg/data.json file

Change background images from fmpg.py

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
			"video_c" : true
		    },
		    "file2" : {
			"filename" : "WB1.mp4",
			"filepath" : "./files/WB1.mp4",
			"filetype" : "mp4",
			"start_time" : 45,
			"duration" : 261,
			"audio_c" : false,
			"video_c" : true
		    },
		    "file3" : {
			"filename" : "vid1.mp4",
			"filepath" : "./files/vid1.mp4",
			"filetype" : "mp4",
			"start_time" : 15,
			"duration" : 30,
			"audio_c" : true,
			"video_c" : true
		    },
		    "file4" : {
			"filename" : "vid2.mp4",
			"filepath" : "./files/vid2.mp4",
			"filetype" : "mp4",
			"start_time" : 20,
			"duration" : 30,
			"audio_c" : true,
			"video_c" : true
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
	    
