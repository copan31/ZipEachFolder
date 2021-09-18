# coding: utf-8

from pathlib import Path
import argparse
import shutil
import traceback

class ZipEachFolder():

    def __init__(self, input_path, output_path):
        """ Zip each folder under the input path, and save it under the output path
        :type input_path: Path
        :param input_path: A specific path (path obj)
        :type output_path: Path
        :param output_path: A specific path (path obj)
        :return: None
        """
        assert isinstance(input_path, Path)
        assert isinstance(output_path, Path)
        self.input_path = input_path
        self.output_path = output_path

    def exec(self):
        # get folders under the specific path
        folder_list = [x for x in self.input_path.iterdir() if x.is_dir()]

        # zip each folder
        for folder_path in folder_list:
            assert isinstance(folder_path, Path)
            try:
                print(f'[Try zip] {folder_path}')
                shutil.make_archive(self.output_path / folder_path.name, 'zip', folder_path)
                print(f'Zip {folder_path} success. Moved in {self.output_path}')
            except:
                print(f'Zip {folder_path} failed.')
                print(traceback.format_exc())

if __name__ == '__main__':
    # get args
    parser = argparse.ArgumentParser(description="Zip each folders under the specific path")
    parser.add_argument("--input_path", help="Specify the path")
    parser.add_argument("--output_path", help="Specify the path")
    args = parser.parse_args()

    # set init path
    input_path = Path(args.input_path) if args.input_path else Path.cwd()
    output_path = Path(args.output_path) if args.output_path else Path.cwd()

    zip_each_folder = ZipEachFolder(input_path, output_path)
    zip_each_folder.exec()



