# -*- coding: utf-8 -*-
"""Jailbreaking_Starter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kCtX-QBSwv5wlrkZ0fSMMHGWJXqQjZaE
"""

!pip install fschat
!pip install openai==0.28

import os
os.environ['OPENAI_API_KEY'] = "API-KEY"
from KOV import startKOV

startKOV("advbench_subset.csv", "lmsys/vicuna-7b-v1.5")

