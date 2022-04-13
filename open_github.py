
# a function to open a Github file

from __future__ import annotations
from yaml import safe_load
from ansible.release import __codename__
def main():
    with open('.github/RELEASE_NAMES.yml') as f:
        releases = safe_load(f.read())
    # Why this format?  The file's sole purpose is to be read by a human when they need to know
    # which release names have already been used.  So:
    # 1) It's easier for a human to find the release names when there's one on each line
    # 2) It helps keep other people from using the file and then asking for new features in it
    for name in (r.split(maxsplit=1)[1] for r in releases):
        if __codename__ == name:
            break
    else:
        print('.github/RELEASE_NAMES.yml: Current codename was not present in the file')
        
        
if __name__ == '__main__':
    main()

