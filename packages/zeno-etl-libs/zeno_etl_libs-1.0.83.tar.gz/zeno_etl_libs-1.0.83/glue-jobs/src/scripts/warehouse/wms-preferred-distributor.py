# -*- coding: utf-8 -*-
"""
Created on Wed May 4 11:52:28 2022

@author: akshay.bhutada@zeno.health

Purpose:
"""

import os
import sys
import argparse

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from calendar import monthrange


sys.path.append('../../../..')

from zeno_etl_libs.db.db import DB, MongoDB, MSSql
from zeno_etl_libs.helper.aws.s3 import S3
from zeno_etl_libs.logger import get_logger, send_logs_via_email
from zeno_etl_libs.helper.email.email import Email

mg_db = MongoDB()
mg_client = mg_db.open_connection("generico-crm")

db = mg_client['generico-crm']
collection = db["wmsDataSyncToS3"].find()


dist_list = pd.DataFrame(list(collection))

dist_list








