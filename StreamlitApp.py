import os
import json
import pandas as pd
import traceback
import streamlit as st
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging
from langchain.callbacks import get_openai_callback
