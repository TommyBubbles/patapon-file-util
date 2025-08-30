from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import sys
import ast
import argparse
import re

sys.path.insert(0, ".\\src")
from patapon.filedata.patapon_data_class import PataponDataClass


def num_to_word(number: int):
    zero_to_ten = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    return zero_to_ten[number]


def get_func_arg_value_as_string(ast_tree: ast.Call, keyword_values: list[str]) -> str | bytes:
    for keyword in ast_tree.keywords:
        if keyword.arg in keyword_values:
            if isinstance(keyword.value, ast.Constant):
                if type(keyword.value.value) is str:
                    return "\"" + keyword.value.value + "\""
                elif type(keyword.value.value) is int:
                    return str(keyword.value.value)
                elif type(keyword.value.value) is float:
                    return str(keyword.value.value)
                elif type(keyword.value.value) is bytes:
                    return keyword.value.value
            elif isinstance(keyword.value, ast.Subscript) and isinstance(keyword.value.value, ast.Name):
                if keyword.value.value.id == 'list':
                    return "[]"
            elif isinstance(keyword.value, ast.Name):
                return keyword.value.id
    return ""



def create_test_file(package_file_path: str, test_input_files: list[str], template_file_path: str, template_directory: str = './templates') -> None:
    package_folder, package_file_name = os.path.split(package_file_path)
    
    jinja_env = Environment(
        loader=FileSystemLoader(template_directory),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True
    )

    template = jinja_env.get_template(template_file_path)
    
    # TODO: capture variables from package file to pass to template
    classes = []
    with open(package_file_path, "r") as file:
        tree = ast.parse(file.read())

        for item in tree.body:
            class_args = []

            if isinstance(item, ast.ClassDef):
                pattern = re.compile("(?=([A-Z][a-z]*|[0-9]+))+")
                func_base_name = "_".join(pattern.findall(item.name))

                field_defaults = []
                for sub_item in item.body:
                    if isinstance(sub_item, ast.AnnAssign) and isinstance(sub_item.value, ast.Call):
                        default_value = get_func_arg_value_as_string(sub_item.value, ["default", "default_factory"])
                        class_default = False

                        for class_info_prev in classes:
                            if class_info_prev["name"] == default_value:
                                default_value = class_info_prev["func_base_name"]
                                class_args.append({"name": class_info_prev["func_base_name"], "type": class_info_prev["name"]})
                                class_default = True
                                break
                        
                        default_info = {
                            "value": default_value,
                            "isclass": class_default
                        }
                        field_defaults.append(default_info)
                        
                class_info = {
                    "name": item.name,
                    "func_base_name": func_base_name.lower(),
                    "field_defaults": field_defaults,
                    "class_args": class_args
                }
                classes.append(class_info)

    # TODO: capture input file information to pass to template
    files = []
    for i in range(len(test_input_files)):
        file_number = num_to_word(i+1)
        file = {
            "func_name": "file_" + file_number,
            "class_name": "TestFile" + file_number.title(),
            "file_path": "\"" + test_input_files[i] + "\""
        }
        files.append(file)

    # apply variables to template
    vars = {
        "classes": classes,
        "package_name": package_file_name.split('.')[0],
        "files": files
    }
    new_test_file_str = template.render(**vars)

    # create testing folder
    # test_folder = os.path.abspath(package_folder).replace("src", "test")
    # os.makedirs(test_folder, exist_ok=True)

    # create new testing file
    # new_test_file_path = os.path.join(test_folder, "test_" + package_file_name)
    new_test_file_path = ".\\test\\tools\\test_" + package_file_name
    with open(new_test_file_path, 'w') as file:
         file.write(new_test_file_str)


if __name__ == '__main__':
    # capture commandline arguments
    parser = argparse.ArgumentParser(description="CLI arguments")
    parser.add_argument("package_file_path")
    parser.add_argument("--inputs", "-i", nargs='*', dest="test_input_files")
    parser.add_argument("--file", "-f", default='test_filedata.template', dest="template_file_path")
    parser.add_argument("--dir", "-d", default='./test/tools/templates', dest="template_directory")
    args = parser.parse_args()

    create_test_file(args.package_file_path, args.test_input_files, args.template_file_path, args.template_directory)
