from google_drive.google_drive_upload import gDrive


Obj = gDrive()

#Upload a file (if file is not in current directory pass full path)
print "Uploading file on Google Drive:"
print "File ID:"
file_id = Obj.upload_File('test.txt')
print file_id

#Upload a file in a Folder (if file is not in current directory pass full path)
print
print "=========================================================="
print "Uploading file on Google Drive FOLDER:"
print "File ID:"
file_id = Obj.upload_File('test.txt',Obj.get_GDrive_Folder_ID('pradeep'))
print file_id


#Create Folder on Google Drive
print 
print "=========================================================="
print "Create Folder on Google Drive"
print "Folder ID:"
folder_id =Obj.create_GDrive_Folder('Don')
print folder_id

#Create a Folder inside another Folder
print 
print "=========================================================="
print "Create SUB Folder on Google Drive"
print "Folder ID:"
folder_id =Obj.create_GDrive_Folder('Amitabh', Obj.get_GDrive_Folder_ID('Don'))
print folder_id


#List all files
print
print "=========================================================="
print "File List (All Files in all Folders):"
Obj.get_GDrive_File_List()


#List all files in a Folder
print 
print "=========================================================="
print "File List in a Folder:"
Obj.get_GDrive_File_List(Obj.get_GDrive_Folder_ID('pradeep'))


#List all Folders
print 
print "=========================================================="
print "Folder List (including subfolders):"
Obj.get_GDrive_Folder_List()


#List all Folders in a Folder
print 
print "=========================================================="
print "Folder List in a Folder:"
Obj.get_GDrive_Folder_List(Obj.get_GDrive_Folder_ID('pradeep'))


