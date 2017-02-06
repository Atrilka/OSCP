#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists
from itertools import product

if __name__ == '__main__':
  base = "/data/users/"
  users = ["g.leone", "k.barth", "anothername"]
  letters = [chr(i) for i in range(97, 123)]
  
  depth = argv[1] if len(argv) > 1 else 5
  for user in users:
    level = 1
    while level < depth:
      for combo in product(letters, repeat=level):
        combo = "".join(combo)
        path = base+user+"/"+combo
        if exists(path):
          print path
      level += 1
