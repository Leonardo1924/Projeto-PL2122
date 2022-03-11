import re
import sys
from typing import List, Tuple
import time

def csvtreatment(header_line: str)-> Tuple[str,str,List[str],List[str]]:
    column_names = []
    column_operations = []
    supported_aggregation_operations = ["group","sum","media","max","min"]
    field_delimiter = re.match(r'',header_line).group(1)
    

def aggregationfuction()


def csv2json()

input_file_path = "alunos.csv"

file = open(input_file_path)
lines = file.read.spltlines()
file.close()

if len(lines) < 2 : 
    raise Exception("Not enough lines in CSV")









