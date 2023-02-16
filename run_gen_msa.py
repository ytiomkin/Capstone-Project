"""this is a python script that will be used to run batch submits of generating MSA documents"""

import os
import sys
import subprocess
rootdir = sys.argv[1]
for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
        A3M_file = 0
        fasta_file = 0
        for x in os.listdir(os.path.join(rootdir, subdir)):
            if x.endswith('A3M'):
                A3M_file = x
            if x.endswith('fasta'):
                fasta_file = x
        inpath = "/lustre/project/amaus/pos_prot_cont"+subdir+"/"+fasta_file
        outpath = "/lustre/project/amaus/pos_prot_cont"+subdir+"/"+A3M_file
        hhbin_path = "/lustre/project/amaus/hhsuite-bin/bin"
        hhdb_path = "/lustre/project/amaus/uniclust30_2018_08/uniclust30_2018_08"
        subprocess.run(["/lustre/project/amaus/trRosettaX/trRosettaX/generate_msa.py",
                        inpath, outpath, hhbin_path, hhdb_path])
