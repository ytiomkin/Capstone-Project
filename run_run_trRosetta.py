"""this is a python script that will be used to run batch submits of generating
flexible protein structures using trRosetta"""

import os
import sys
import subprocess
rootdir = sys.argv[1]
for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
        npz_file = 0
        fasta_file = 0
        for x in os.listdir(os.path.join(rootdir, subdir)):
            if x.endswith('npz'):
                npz_file = x
            if x.endswith('fasta'):
                fasta_file = x
        fasta_file = "/lustre/project/amaus/pos_prot_cont/"+subdir+"/"+fasta_file
        npz_file = "/lustre/project/amaus/pos_prot_cont/"+subdir+"/"+npz_file
        outpath = "/lustre/project/amaus/pos_prot_cont/"+subdir
        subprocess.run(["/lustre/project/amaus/trRosettaX/trRosettaX/run_trRosetta.py", "-npz",
                        npz_file, "-fasta", fasta_file, "-o", outpath, "-n", "5", "-cpu", "20"])
