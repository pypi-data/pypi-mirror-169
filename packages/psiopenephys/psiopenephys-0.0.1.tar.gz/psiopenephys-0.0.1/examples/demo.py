import datetime as dt
from psiopenephys.client import OpenEphysClient


oe = OpenEphysClient()

# This checks to see if OpenEphys is up and running. If not, automatically
# opens the GUI.
oe.connect(auto_open=True)

time_str = dt.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
oe.set_recording_filename(f'e:/test/Test/TST045/raw/CLT045d19/CLT045d19_p_FTC_{time_str}')

# Start acquiring (but not saving).
oe.acquire()
time.sleep(1)

# Start recording.
oe.record()
time.sleep(1)

# Send a message to OpenEphys. I'm not sure where this actually ends up?
# Presumably somewhere in the file?
oe.send_message('Hello world!')

# Stop acquisition.
oe.stop()
time.sleep(1)

# Close the window.
oe.close()
