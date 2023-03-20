"""this is a python script that will be used to run batch submits of predicting inter-residue structures"""

import os
import sys
import subprocess
rootdir = sys.argv[1]
for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
        A3M_file = 0
        NPZ_file = 0
        for x in os.listdir(os.path.join(rootdir, subdir)):
            if x.endswith('A3M'):
                A3M_file = x
            if x.endswith('NPZ'):
                NPZ_file = x
        inpath = "/lustre/project/amaus/pos_prot_cont"+subdir+"/"+A3M_file
        outpath = "/lustre/project/amaus/pos_prot_cont"+subdir+"/"+NPZ_file
        model_path = "/lustre/project/amaus/trRosettaX/model_res2net_202108"
        subprocess.run(["/lustre/project/amaus/trRosettaX/trRosettaX/predict.py",
                        inpath, outpath, model_path, "-cpu", " 20"])