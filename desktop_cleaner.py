from watchdog.observers import Observer
import os
import time
import datetime
import pywintypes
from connectivity_checker import connect
from watchdog.events import FileSystemEventHandler
from win10toast import ToastNotifier

dumping_folder = 'Gabbage'
folder_to_monitor = '/Users/BayoOlawumi/Desktop'
folder_to_move_latefiles = folder_to_monitor +'/' + dumping_folder
threshold_days = 5
code_location = "C:/Users/BayoOlawumi/Desktop/Masters/CamSec/Desktop_Cleaner"

os.chdir(code_location)
class TheHandler(FileSystemEventHandler):

    def on_modified(self, event):
        # Iterate through every file in the given folder to monitor
        present_time = datetime.datetime.now()
        for each_file in os.listdir(folder_to_monitor):
            # Join file name to path
            each_file_path = os.path.join(folder_to_monitor,each_file)            
            # Check if each file is a file but not folder and also not a shortcut
            if os.path.isfile(each_file_path) and os.path.splitext(each_file_path)[-1].lower() != ".lnk":
                days_spent_on_pc = self.display_days_spent(present_time, each_file_path)
                # Only extract those whose days are more than threshold
                if days_spent_on_pc > threshold_days:
                    #print(os.path.splitext(each_file_path)[-2] + " has spent " + str(days_spent_on_pc) + " days, kindly modify !")
                    self.move_longstayed_files(each_file, days_spent_on_pc)

    def move_longstayed_files(self, each_file, expended_days):
        # Ensure the folder gabbage is not being put in itself
        if each_file != dumping_folder:
            # check if the file path already exist
            incoming_file_path = folder_to_move_latefiles + '/' + each_file
            new_name = each_file
            if os.path.isfile(incoming_file_path):
                i = 1
                # Incase there are many of these duplicate files in the Gabbage folder already
                while incoming_file_path:
                    i += 1
                    new_name = os.path.splitext(folder_to_monitor + '/'+ new_name)[0] + str(i) + os.path.splitext(incoming_file_path)[-1]
                    new_name = new_name.split("/")[4]
                    incoming_file_path = os.path.isfile(folder_to_move_latefiles +"/" + new_name)


            # Real file transfer going on here
            old_path = folder_to_monitor + "/" + each_file
            new_path = folder_to_move_latefiles + "/" + new_name
            os.rename(old_path, new_path)
            print (each_file + " was successfully moved to gabbage after spending "+ str(expended_days) + " days on your desktop!")

    def display_days_spent(self, present_time, each_file_path):
        # Get the date each file was created
        created_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        # Evaluate the differences
        days_spent_on_pc = (present_time - created_date).days
        return days_spent_on_pc
        
        
toast = ToastNotifier()
if connect():
    toast.show_toast("eBayo's Automated Machine", "There is internet and your Desktop is Clean with me, Abayomi", duration=30)
else:
    toast.show_toast("eBayo's Automated Machine", "No Internet but your Desktop is Clean with me, Abayomi", duration=30)

handler = TheHandler()
observer = Observer()
observer.schedule(handler,folder_to_monitor,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
