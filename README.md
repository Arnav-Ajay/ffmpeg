# ffmpeg

Clone the git repository:
    git clone 

Install the following:

	pip3 install ffmpeg-python --user
	sudo apt-get install libavdevice57
	sudo apt-get install ffmpeg

To Run:

	from inside the project directory, type:
		python3 fmpg.py


ffmpeg
	|
	|-Files				directory containing all input files
	|	|-vid1.mp4		
	|	|-vid2.mp4
	|	|-LR3.webm
	|	.
	|	.
	|-Interface			directory containing File and Session Interface files 
	|	|-FileInter.py
	|	|-Session.py
	|
	|-data.json			Json file containing data of each session.
	|
	|-fmpg.py			FFMPEG-Python Implementation
	|
	|-preprocess.py		Support python file for fmpg.py
	|
	|-rules.py			Contains rules/format of how each vid/audio should be
	|
    |-temp             Contains temp files. these get generated and deleted during run-time
    |
	|-Output			directory containing all output files
		|-output.mp4
