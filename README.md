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

Directory Structure:
	
	├── data.json				#    Json file containing data of each session.
	├── files				#    Directory containing all input files
	│   ├── background.png
	│   ├── LR1.mp4
	│   ├── LR2.mp4
	│   ├── LR3.webm
	│   ├── LR4.webm
	│   ├── LR5.webm
	│   ├── LR6.webm
	│   ├── LR7.webm
	│   ├── vid1.mp4
	│   ├── vid2.mp4
	│   ├── WB1.mp4
	│   ├── WB2.mp4
	│   ├── WB3.webm
	│   └── Zoom.webm
	├── fmpg.py				#    FFMPEG-Python Implementation
	├── interface				#    Directory containing File and Session Interface
	│   ├── fileinterface.py
	│   └── sessioninterface.py
	├── output				#   Directory containing all output files 
	│   ├── session1.mp4
	│   ├── session2.mp4
	│   ├── session3.mp4
	│   ├── session4.mp4
	│   ├── session5.mp4
	│   ├── session6.mp4
	│   ├── session7.mp4
	│   ├── session8.mp4
	│   └── session9.mp4
	├── preprocess.py			#    Support python file for fmpg.py
	├── README.md
	├── rules.py				#    Contains rules/format of how each vid/audio should be
	├── temp				#   Directory containing all temp files, these get generated and deleted during run time
	└── test.py
