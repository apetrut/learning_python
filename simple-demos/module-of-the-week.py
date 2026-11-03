import contextlib


for one_line in open("/etc/passwd"):
    print(len(one_line), end=' ')

# OR

with open('/etc/passwd') as f:
  for one_line in open("/etc/passwd"):
      print(len(one_line), end=' ')

class MyCM:
    def __enter__(self):
        print('\tNow in __enter__')

    def __exit__(self, type, value, tb):
        print('\tNow in __exit__')

with MyCM() as m:
    print('hello')

with open('my_file.txt', 'w') as f:
    f.write('hello world\n')
    rs = contextlib.redirect_stdout(f)

    with rs:
        print('hello world')