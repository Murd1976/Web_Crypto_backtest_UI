# Celery
from celery import shared_task, app
# Celery-progress
from celery_progress.backend import ProgressRecorder
# Task imports
import time
from .main_web import BackTestApp

# Celery Task
@app.shared_task(bind=True)
def ProcessDownload(self, text_buf, name):
	print('Task started')
	# Create the progress recorder instance
	# which we'll use to update the web page
#	progress_recorder = ProgressRecorder(self)

	ui_utils = BackTestApp()
	ui_utils.my_rep.progress_recorder = ProgressRecorder(self)
	res = 0
	print('Start')
#	for i in range(seconds):
		# Sleep for 1 second
#		time.sleep(1)
#		res += i
#		progress_recorder.set_progress(i+1, seconds, description="Calculating...")
		
		# Print progress in Celery task output
	print(ui_utils.my_rep.cur_progress)
		
		# Update progress on the web page
	

	ui_utils.run_report(text_buf, 'local', name)
#	progress_recorder.set_progress(ui_utils.my_rep.cur_progress, ui_utils.my_rep.bar_len, description="Calculating...")
	print(ui_utils.my_rep.cur_progress)
	print('End')

	return res
