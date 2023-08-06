import os
import json
from pathlib import Path
import plac


@plac.opt('indent', "format files with that indent level", type=int)
@plac.opt('sort_keys', "decide whether jpf should sort the keys", type=bool)
@plac.opt('file', "format file under given path unaffected by its suffix", type=Path)
def format(indent=4, sort_keys=False, file=None):
    if file != None:
        with open(file, 'r') as f:
            try:
                content = json.load(f)
            except:
                raise ValueError(f'Could not parse json from given file {file}.')
        with open(file, 'w') as f:
            f.write(json.dumps(content, indent=indent, sort_keys=sort_keys))
    for subdir, dirs, files in os.walk("."):
        for file in files:
            if file.endswith('.json'):
                path = os.path.join(subdir, file)
                with open(path, 'r') as f:
                    try:
                        content = json.load(f)
                    except:
                        continue
                with open(path, 'w') as f:
                    f.write(json.dumps(content, indent=indent, sort_keys=sort_keys))


def main():
    plac.call(format)
