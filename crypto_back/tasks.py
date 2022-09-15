# Celery
from celery import shared_task, app
# Celery-progress
from celery_progress.backend import ProgressRecorder
# Task imports
import time

# Celery Task
@app.shared_task(bind=True)
def ProcessDownload(self, seconds):
	print('Task started')
	# Create the progress recorder instance
	# which we'll use to update the web page
	progress_recorder = ProgressRecorder(self)
	res = 0
	print('Start')
	for i in range(seconds):
		# Sleep for 1 second
		time.sleep(1)
		res += i
		# Print progress in Celery task output
		print(i + 1)
		# Update progress on the web page
		progress_recorder.set_progress(i + 1, seconds, description="Calculating...")
	print('End')

	return result
