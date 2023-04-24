import whisper
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE
import argparse
import os
import requests
import json
import base64
#import gradio as gr
from pathlib import Path
#import pysrt
#import pandas as pd
import re
import time

from googletrans import Translator

