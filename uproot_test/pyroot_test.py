import ROOT as rt
import matplotlib.pyplot as plt
import numpy as np

root_file_dir= '/home/giorgio/Desktop/ROOT_files/'
Tfile= rt.TFile.Open(root_file_dir + 'flat_caf_0-833995dc-14a2-47e7-9a95-91e25102b7ef.root')
TTree= Tfile.Get('recTree;29/rec.reco.trk.calo.2.ke')

for i, event in enumerate(TTree):
    e= event
    print(e)