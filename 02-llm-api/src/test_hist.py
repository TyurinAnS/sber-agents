from typing import List

hst_max = 5
hst: List[str] = []

hst.append('prompt')
for i in range(1,20):
    hst.append('mess'+str(i))
    print(hst[0:4] + hst[4:][-hst_max:])
