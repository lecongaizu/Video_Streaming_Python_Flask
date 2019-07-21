#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  layoutmodule.py
#    

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import Response
from flask import jsonify
import collections
import json
from datetime import datetime
import time 
import numpy as np
import os
import requests
import json
from datetime import timedelta
import threading
from os import listdir
from os.path import isfile, join
import uuid, sys
from flask import g
import os, sys

def layout_file():
	"""
	Documentation for get Config data from VCJ server.
	"""
	return render_template('layout.html')	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
