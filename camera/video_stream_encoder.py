import inspect, os
from subprocess import PIPE, Popen
from datetime import datetime

camera_Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
ffmpeg_File_Path =  os.path.join(camera_Dir, 'ffmpeg')

from settings.parseSettings import get_Settings
Camera_Settings = get_Settings('CAMERA')

Video_Dir_Path = Camera_Settings['VIDEO_DIR']
Frame_Height = Camera_Settings['VIDEO_FRAME_HEIGHT']
Frame_Width = Camera_Settings['VIDEO_FRAME_WIDTH']
Frame_Per_Second = Camera_Settings['VIDEO_FRAME_PER_SECOND']
Bit_Rate = Camera_Settings['VIDEO_BITRATE']


YouTube_Settings = get_Settings('YOUTUBE')
Stream_Name = YouTube_Settings['LIVE_STREAM_NAME_KEY']
 

#====================================================================================
def cmdline(command):
	process = Popen(args=command,stdout=PIPE,shell=True)
	return process.communicate()[0]
#====================================================================================



#====================================================================================
# UNDER TESTING (DO NOT USE)
#def encode_video_Stream_To_mkvFile(file_Title):
	
#	encode_Video_Command = r"raspivid -o - -t 10000 -w 1280 -h 720 -fps 25 -b 4000000 -g 50 | " + ffmpeg_File_Path + r" -r 25 -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy " + file_Title
#	#Add Executable permission to ffmpeg file
#	cmdline(r"chmod a+x " + ffmpeg_File_Path)
#	process = Popen(args=encode_Video_Command,stdout=PIPE,shell=True)
#	time.sleep(20)
#	os.killpg(os.getpgid(process.pid), signal.SIGINT)
#====================================================================================	


#====================================================================================
def stream_Video_To_YouTube_Channel():
	
	youtube_Streaming_Command = r"raspivid -o - -t 0 -w " + Frame_Width  + r" -h " + Frame_Height  + r" -fps " + Frame_Per_Second  + r" -b " + Bit_Rate + r" | " + ffmpeg_File_Path + r" -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/" + Stream_Name

	#Add Executable permission to ffmpeg file
	cmdline(r"chmod a+x " + ffmpeg_File_Path)

	#Start Streaming
	encode_Output = cmdline(youtube_Streaming_Command)
#====================================================================================	


#====================================================================================
def stream_Video_To_VLC():
	#VLC should be installed on Raspberry Pi (sudo apt-get install vlc)
	#VLC can't be executed with root privileges
	#VLC crashes with high resolution streaming (go with default values in command)
	#Viewing URL will be "http://raspbeery_IP:8160"
	
	vlc_Streaming_Command = """raspivid -o - -t 0 -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264"""

	#vlc_Streaming_Command = r"raspivid -o - -t 0 -w " + Frame_Width  + r" -h " + Frame_Height  + r" -fps " + Frame_Per_Second  + r" -b " + Bit_Rate + r" | " + "cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264"
	
	#Start Streaming
	encode_Output = cmdline(vlc_Streaming_Command)
#====================================================================================	


#====================================================================================
def capture_MP4_Video(File_Name, Capture_Duration_in_Sec):	
		
	#Add Executable permission to ffmpeg file
	cmdline(r"chmod a+x " + ffmpeg_File_Path)
		
	#Capture H.264 VIDEO
	h264_File_Path = os.path.join(Video_Dir_Path, File_Name + r".h264")	
	h264_Video_Capture_Cmd = r"raspivid -o " + h264_File_Path + r" -t " + str(int(Capture_Duration_in_Sec) * 1000) + r" -h " + Frame_Height  + r" -w " + Frame_Width  + r" -fps " + Frame_Per_Second  + r" -b " + Bit_Rate
	cmdline(h264_Video_Capture_Cmd)
	
	#Convert Captured VIDEO to MP4 Format
	mp4_File_Path = os.path.join(Video_Dir_Path, File_Name + r".mp4")
	mp4_Encode_Cmd = ffmpeg_File_Path + r" -r " + Frame_Per_Second + r" -i " + h264_File_Path + r" -vcodec copy " + mp4_File_Path
	cmdline(mp4_Encode_Cmd)
	
	#Remove temporary H.264 Video File
	os.remove(h264_File_Path)
	
	return mp4_File_Path
#====================================================================================



