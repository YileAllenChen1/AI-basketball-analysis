import os
import sys
import cv2

from PIL import Image

from src.config import shooting_result
from src.app_helper import getVideoStream, get_image, detectionAPI

video_path = 'Giannis_Antetokounmpo_short.mp4'
stream = getVideoStream(video_path)