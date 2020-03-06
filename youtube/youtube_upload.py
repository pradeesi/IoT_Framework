from subprocess import PIPE, Popen
import inspect, os

YouTube_Script_Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
YouTube_Script_File_Path =  os.path.join(YouTube_Script_Dir, 'master_script.py')


#====================================================================================
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
#====================================================================================


#====================================================================================
def upload_Video_On_YouTube(file_Path, file_Title, file_Privacy_Status="private", file_Description="", search_Keywords="""'abc'"""):
	
	upload_Command = r"python " + YouTube_Script_File_Path + \
					r" --file=" + file_Path + \
					r" --title=" + file_Title + \
					r" --description=" + file_Description + \
					r" --keywords=" + search_Keywords + \
					r" --privacyStatus=" + file_Privacy_Status
					
	upload_Output = cmdline(upload_Command)
	
	print upload_Output
#====================================================================================	

