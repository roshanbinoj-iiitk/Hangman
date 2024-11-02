from core.main import*
from core.gui import *

initial_setup()

while True:
    ch=pc_h_intro()[0]
    if ch=='1':
        pc_human()
    elif ch=='2':
        human_pc()
