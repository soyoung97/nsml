print("NSML START!!!!!!")
import sys
print(sys.version)
import os
print(os.listdir("./"))
import nsml
print(nsml.DATASET_PATH)
#os.system('pip install --editable fairseq/.')

#with open(nsml.DATASET_PATH+'/dict.src.txt', 'r') as f:
#    print('read from dataset!')
#    print([line for line in f])

#for i in range(100):
#    nsml.report(step=i, lr=i*10, summary=True, scope=locals(), etc=2*i)

print("Executing fairseq-train!@!!!!")
os.system('pip install --upgrade torch torchvision')
#os.system('pip install Cython')
#os.system('python setup-late.py build_ext --inplace')
os.system('pip install --editable ./fairseq/.')
os.system('fairseq-train /data/soyoung_test/train --arch lstm --max-tokens 1000')
print("Execute complete!!")

