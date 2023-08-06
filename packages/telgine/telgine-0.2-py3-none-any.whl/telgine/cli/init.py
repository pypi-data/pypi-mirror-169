import pathlib
import shutil
import os
import telgine


def initialize_project(project_path):
    templates_folder_path = pathlib.Path(__file__).parent.parent.joinpath('templates/project')
    generated_project_path = pathlib.Path(project_path).resolve()
    print(f'Initializing project {generated_project_path.name}')
    shutil.copytree(templates_folder_path, generated_project_path)