import glob
import hashlib
import sys
import time
from rich.console import Console
from rich.progress import track

dirname = sys.argv[1]

results = {}

c = Console()

with c.status(f'Hashing files in {dirname}...') as status:
    for one_filename in glob.glob(f'{dirname}/*'):

        try:
            digest = hashlib.file_digest(open(one_filename, 'rb'), 'sha1')
            results[one_filename] = digest.hexdigest()
        except Exception as e:
            pass

        time.sleep(0.1)
        status.update()

for key, value in results.items():
    print(f'{key}: {value}')


# with track

for one_filename in track(glob.glob(f'{dirname}/*')):

        try:
            digest = hashlib.file_digest(open(one_filename, 'rb'), 'sha1')
            results[one_filename] = digest.hexdigest()
        except Exception as e:
            pass

        time.sleep(0.1)

for key, value in results.items():
    print(f'{key}: {value}')