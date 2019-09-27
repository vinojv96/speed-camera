# ---------------- User Configuration Settings for speed-cam.py ---------------------------------
#         Ver 8.4 speed-cam.py picam240 Stream Variable Configuration Settings

#######################################
#    speed-cam.py plugin settings
#######################################

# Calibration Settings
# --------------------
cal_obj_px_L2R = 80      # L2R Moving Objects, Length of a calibration object in pixels
cal_obj_mm_L2R = 4700.0  # L2R Moving Objects, Length of the calibration object in millimetres
cal_obj_px_R2L = 85      # R2L Moving Objects, Length of a calibration object in pixels
cal_obj_mm_R2L = 4700.0  # R2L Moving Objects, Length of the calibration object in millimetres

# Motion Event Settings
# ---------------------
MIN_AREA = 100         # Default= 100 Exclude all contours less than or equal to this sq-px Area
x_diff_max = 30        # Default= 30 Exclude if max px away >= last motion event x pos
x_diff_min = 1         # Default= 1  Exclude if min px away <= last event x pos
track_timeout = 0.0    # Default= 0.0 Optional seconds to wait after track End (Avoid dual tracking)
event_timeout = 0.4    # Default= 0.4 seconds to wait for next motion event before starting new track
log_data_to_CSV = True # Default= True True= Save log data as CSV comma separated values

# Camera Settings
# ---------------
WEBCAM = True          # Default = False False=PiCamera True=USB WebCamera

# Pi Camera Settings
# ------------------
CAMERA_WIDTH = 320     # Default= 320 Image stream width for opencv motion scanning default=320
CAMERA_HEIGHT = 240    # Default= 240 Image stream height for opencv motion scanning  default=240
CAMERA_FRAMERATE = 30  # Default= 30 Frame rate for video stream V2 picam can be higher

# Camera Image Settings
# ---------------------
image_font_size = 12   # Default= 15 Font text height in px for text on images
image_bigger = 3       # Default= 3 Resize saved speed image by value

# ---------------------------------------------- End of User Variables -----------------------------------------------------
