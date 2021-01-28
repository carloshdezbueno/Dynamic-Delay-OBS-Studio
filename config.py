import os
import logging

# author and license information
AUTHOR = 'Carlos Hernandez-Bueno Regojo'
AUTHOR_EMAIL = 'carlos.hdezbueno@gmail.com'
LICENSE = 'see license.md file for details'

# log configuration
DEBUG = True
LOG_LEVEL = logging.DEBUG

# App configuration
RECORDING_OBS_IP = 'localhost'
STREAMING_OBS_IP = 'localhost'

RECORDING_OBS_PORT = 4444
STREAMING_OBS_PORT = 4445

DELAY_SCENE = 'Delay'
REMOVE_DELAY_SCENE_TRANSITION = 'removeDelayTransition'
ADD_DELAY_SCENE_TRANSITION = 'Transition'

AUDIO_SOURCE_1 = 'Cascos'
AUDIO_SOURCE_2 = 'Altavoces'
AUDIO_SOURCE_3 = 'Mic/Aux'