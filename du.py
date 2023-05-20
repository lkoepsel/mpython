# https://forum.micropython.org/viewtopic.php?t=7550
# look at tree example, it references using upysh.py
class DISK_USAGE:

    def __repr__(self):
        self.__call__()
        return ""

    def __call__(self, path=".", dlev=0, max_dlev=0, hidden=False):
        if path != ".":
                if not os.stat(path)[0] & 0x4000:
                    print('{:9} {}'.format(self.print_filesys_info(os.stat(path)[6]), path))
                else:
                    if hidden:
                        resp = {path+'/'+dir: os.stat(path+'/'+dir)[6] for dir in os.listdir(path)}
                    else:
                        resp = {path+'/'+dir: os.stat(path+'/'+dir)[6] for dir in os.listdir(path) if not dir.startswith('.')}
                    for dir in resp.keys():

                        if not os.stat(dir)[0] & 0x4000:
                            print('{:9} {}'.format(self.print_filesys_info(resp[dir]), dir))

                        else:
                            if dlev < max_dlev:
                                dlev += 1
                                self.__call__(path=dir, dlev=dlev, max_dlev=max_dlev, hidden=hidden)
                                dlev += (-1)
                            else:
                                print('{:9} {} {}'.format(self.print_filesys_info(self.get_dir_size_recursive(dir)), dir, '<dir>'))
        else:
            if hidden:
                resp = {path+'/'+dir: os.stat(path+'/'+dir)[6] for dir in os.listdir(path)}
            else:
                resp = {path+'/'+dir: os.stat(path+'/'+dir)[6] for dir in os.listdir(path) if not dir.startswith('.')}
            for dir in resp.keys():

                if not os.stat(dir)[0] & 0x4000:
                    print('{:9} {}'.format(self.print_filesys_info(resp[dir]), dir))

                else:
                    if dlev < max_dlev:
                        dlev += 1
                        self.__call__(path=dir, dlev=dlev, max_dlev=max_dlev, hidden=hidden)
                        dlev += (-1)
                    else:
                        print('{:9} {} {}'.format(self.print_filesys_info(self.get_dir_size_recursive(dir)), dir, '<dir>'))

    def print_filesys_info(self, filesize):
        _kB = 1024
        if filesize < _kB:
            sizestr = str(filesize) + " by"
        elif filesize < _kB**2:
            sizestr = "%0.1f KB" % (filesize / _kB)
        elif filesize < _kB**3:
            sizestr = "%0.1f MB" % (filesize / _kB**2)
        else:
            sizestr = "%0.1f GB" % (filesize / _kB**3)
        return sizestr

    def get_dir_size_recursive(self, dir):
        return sum([os.stat(dir+'/'+f)[6] if not os.stat(dir+'/'+f)[0] & 0x4000 else self.get_dir_size_recursive(dir+'/'+f) for f in os.listdir(dir)])
