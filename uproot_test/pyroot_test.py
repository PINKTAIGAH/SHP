import ROOT as rt
import matplotlib.pyplot as plt
import numpy as np

root_file_dir= '/home/giorgio/Desktop/ROOT_files/'
f= rt.TFile(root_file_dir + 'flat_caf_1-1637ea75-449f-467f-abd7-9e2f4f9710a7.root')
tree= f.Get('recTree;31')
leaves = tree.GetListOfLeaves()
class PyListOfLeaves(dict) :
    pass

pyl = PyListOfLeaves()

for i in range(0,leaves.GetEntries() ) :
    leaf = leaves.At(i)
    name = leaf.GetName()
    pyl.__setattr__(name,leaf)
    if name == 'rec.reco.trk.calo.2.points.dedx':
        break

nev = tree.GetEntries()
print(tree.GetLeaf('rec.reco.trk.calo.2.points.dedx').GetNdata())
list_dedx= []
list_rr= []
list_end_x= []

for entry in tree:
    entry.Show()
    #print(entry.GetLeaf('rec.reco.trk.calo.2.points.dedx').GetNdata())
    #print(entry.GetLeaf('rec.reco.trk.calo.2.points.dedx').GetLeafCounter())
    #dedx= entry.GetLeaf('rec.reco.trk.calo.2.points.dedx')
    #print(dedx)
    ##rr= entry.GetLeaf('rec.reco.trk.calo.2.points.rr').GetValue()
    #for i in dedx:
        #print(dedx.GetValue())
        

    #if dedx<5 and rr<25:
        #print(rr)
        #list_dedx.append(dedx)
        #list_rr.append(rr)

#print(len(list_end_x), len(list_dedx))
#print(list_dedx[5])
#print(nev)

#np.savetxt( 'basic.txt', np.array([list_rr,list_dedx]))