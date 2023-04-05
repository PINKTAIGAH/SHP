import ROOT as rt
import matplotlib.pyplot as plt
import numpy as np

root_file_dir= '/home/giorgio/Desktop/ROOT_files/'
f= rt.TFile(root_file_dir + 'reco2-1cf8343b-b547-4ec5-9de8-da9ee53d258d.root')
tree= f.Get('Events')






list_dedx= []
list_rr= []
list_end_x= []

for entry in tree:
    rr= entry.GetLeaf('anab::Calorimetrys_pandoraCalo__Reco2./anab::Calorimetrys_pandoraCalo__Reco2.obj/anab::Calorimetrys_pandoraCalo__Reco2.obj.fdEdx')
    print(rr)
        

    #if dedx<5 and rr<25:
        #print(rr)
        #list_dedx.append(dedx)
        #list_rr.append(rr)

#print(len(list_end_x), len(list_dedx))
#print(list_dedx[5])
#print(nev)

#np.savetxt( 'basic.txt', np.array([list_rr,list_dedx]))