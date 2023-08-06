import json
import codecs
import os
import shutil
from .folder_utils import FolderUtils

class FileUtils:
    def write_json_file(self, file_path, write_mode, json_object, stringify=None, log=False):
        write_object = json_object
        directory = '/'.join(file_path.split('/')[:-1])
        FolderUtils().create_folder(directory)
        
        try:
            if log:
                print(f'File saved in - {file_path}')
                
            if stringify is None:
                with open(file_path, write_mode, encoding="utf8") as f:
                        json.dumps(write_object)
                        return f
            else:
                to_save = json.dumps(write_object, ensure_ascii=False, indent=4, sort_keys=True, default=str)
                with codecs.open(file_path, write_mode, encoding='utf-8') as f:
                    f.write(to_save)
                    return f
        
        except Exception as e:
            print("Failed to write to - {}\n{}".format(file_path))
            print(e)

    def load_json_file(self, file_path):
        try:
            if os.path.isfile(file_path):
                return json.load(open(file_path, encoding='utf-8'))
            return None
        except Exception as e:
            print("Failed to read file - {}".format(file_path))
            print(e)

    def write_file_from_array(self, file_path, write_mode, file_content):
        try:
            with open(file_path, write_mode) as f:
                f.writelines(file_content)
                f.close()
        except Exception as e:
            print("Failed to write to - {}\n{}".format(file_path, file_content))
            print(e)

    def load_rows_from_file(self, file_path, limit=None, row_contain=None):
        file_content = open(file_path, "r")
        if limit == None:
            return file_content
        else:
            rows = []
            i = 0
            for line in file_content:
                if i + 1 < limit:
                    clean_line = line.strip()
                    if row_contain is not None and row_contain in clean_line:
                        if line[0] == '/':
                            rows.append(clean_line[1:-1])
                        else:
                            rows.append(clean_line)
                    
                        i += 1
                else: break
            
            return rows

    def create_windows_shortcut(path, name, target='', url=True):    
        if url:
            shortcut = open(path + '/' + name + '.url', 'w')
            shortcut.write('[InternetShortcut]\n')
            shortcut.write('URL=%s' % target)
            shortcut.close()

    def remove_files_from_path(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))