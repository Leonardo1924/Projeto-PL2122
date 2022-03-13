from dataclasses import field
from optparse import Values
import re
import string
import sys
from typing import List, Tuple
import time
from unicodedata import numeric

def csvtreatment(header_line: str)-> Tuple[str,str,List[str],List[str]]:
    column_names = []
    column_operations = []
    supported_aggregation_operations = ["group","sum","media","max","min"]
    field_delimiter = re.match(r'-------',header_line).group(1)
    
    if field_delimiter == ",":
        operations_separator = "::"
        captures = re.findall(r'-------',header_line)


    for capture in captures:
        num_clauses = len(list(filter(None,capture)))
        column_names.append(capture[0])
        if num_clauses == 1:
            column_operations.append("none");
        elif num_clauses == 2:
            if capture[1] == "::":
                column_operations.append(["group"])

# falta acabar esta parte.

def aggregationfuction(column_name: str,
                            values: List[str],
                            operations:List[str],
                            row_number:int,
                            last_column:bool) -> List[str]:
    operation_results=[]
    try:
        numeric_values = [float(value) for value in values]
        for i, operation in enumerate(operations):
            if operation == "group":
                operation_result = f'\t\t"{column_name}": {numeric_values}'
            if operation == "sum":
                operation_result = f'\t\t"{column_name}": {sum(numeric_values)}'
            elif operation == "media":
                operation_result = f'\t\t"{column_name}": {sum(numeric_values)/len(numeric_values)}'
            elif operation == "min":
                operation_result = f'\t\t"{column_name}": {min(numeric_values)}'
            elif operation == "max":
                operation_result = f'\t\t"{column_name}": {max(numeric_values)}'

            operation_results.append(operation_result + 
            ("" if last_column and i==len(operations)-1 else ","))

        return operation_results
    except ValueError:
        raise ValueError(f"That's no numeric element in row {str(row_number)} and it should!!")

def csv2json(csv_lines: List[str],
                            field_delimiter: str,
                            operations_separator: str,
                            column_names: List[str],
                            column_operations: List[str]) -> str:
    
    string_list = []

    string_list.append("[")
    for i, line in enumerate(csv_lines):
        string_list.append("\t{")
        fields = line.split(field_delimiter)

        if len(fields) != len(column_names):
            raise AttributeError(
                f"Row {str(i+2)} does not have the same number of columns!! See header!!")
        
        for j, field in enumerate(fields):
            if field:
                if column_operations[j] == "none":
                    string_list.append(f'\t\t"{column_names[j]}": "{field}"' +
                    ("," if (len(list(filter(None,fields[j:]))) > 1 ) else "")) #check if it's not he last non-empty field
                elif column_operations[j] == "cast":
                    try:
                        numeric_value = float(field)
                        string_list.append(f'\t\t"{column_names[j]}": {numeric_value}' +
                        ("," if (len(list(filter(None,fields[j:]))) > 1 ) else ""))
                    except ValueError:
                        raise ValueError(f"Row {str(i + 2)}: {field} can't be casted to a numeric value")
                else:
                    values = re.match(r'\((.+?)\)',field) # extract values inside the parenthesis
                    if not values:
                        raise AttributeError(f"Row {str(i + 2)} group column has incorrect format")

                    values = values.group(1).split(operations_separator)

                    if len(values) > 0:
                        string_list = string_list + aggregationfuction(column_names[j],values,column_operations[j],i+2,len(list(filter(None,fields[j:]))) == 1)

        if(i == len(csv_lines)-1):
            string_list.append("\t}")
        else:
            string_list.append("\t},")

    string_list.append("]")
    return '\n'.join(string_list)

if len(sys.argv) == 1:
    input_file_path = "input/alunos.csv"
    output_file_path = f"output/alunos.json"
elif len(sys.argv) == 2:
    input_file_path = f"input/{sys.argv[1]}"
    output_file_path = f"output/alunos.json"
elif len(sys.argv) == 3:
    input_file_path = f"input/{sys.argv[1]}"
    output_file_path = f"output/{sys.argv[2]}"
else:
    raise ValueError("Wrong number of arguments.\n Help Manual: python main.py [input_file_name] [output_file_name]")

#Let's read the file
file = open(input_file_path)
lines = file.read.spltlines()
file.close()

if len(lines) < 2 : 
    raise Exception("Not enough lines in CSV")

#How much time to process the file
start = time.time()
field_delimiter, operations_separator, csv_columns_names, csv_column_operations = csvtreatment(lines[0])
json_txt = csv2json(lines[1:],field_delimiter,operations_separator,csv_columns_names,csv_column_operations)
end = time.time()

#Write to json
output_file = open(output_file_path,"w")
output_file.write(json_txt)
output_file.close()

print(f"Time for processing the csv:{end - start}s")






