# on my machine, i ran this with:  
#   python3.13 -B extend.py ../moot/optimize/[comp]*/*.csv
#   python3.13 -B extend.py /workspaces/ezr/data/optimize/misc/auto93.csv > ./extend /workspaces/ezr/data/optimize/misc/auto93.csv
import sys,random,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# 将父级目录添加到 sys.path
sys.path.append(parent_dir)

from ezr import the, DATA, csv, dot

def show(lst):
  return print(*[f"{word:6}" for word in lst], sep="\t")

def myfun(train):
  d    = DATA().adds(csv(train))
  x    = len(d.cols.x)
  size = len(d.rows)
  dim  = "small" if x <= 5 else ("med" if x < 12 else "hi")
  size = "small" if size< 500 else ("med" if size<5000 else "hi")
  return [dim, size, x,len(d.cols.y), len(d.rows), train[17:]]

random.seed(the.seed) #  not needed here, but good practice to always take care of seeds
show(["dim", "size","xcols","ycols","rows","file"])
show(["------"] * 6)
[show(myfun(arg)) for arg in sys.argv if arg[-4:] == ".csv"]
