#to create a single directory...
from pathlib import Path
import os

Path('/Users/valeriegalper/PycharmProjects/HellowWorld/spam').mkdir()
os.chdir('/Users/valeriegalper/PycharmProjects/HellowWorld/spam')
p = Path('spam.txt')
p.write_text('Yo Yo Maaa')
