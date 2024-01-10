## Description

The **main.ipynb** file comprises an implementation to build graph maps for network-based datasets. The code was tested on [LANL (auth.txt.gz)](https://csr.lanl.gov/data/cyber1/).

The other notebooks are specifically used to extract graph features based on the previously calculated graph maps. Details provided below:

> features-Copy1: *In_Unique_Usr*

> features-Copy1-2: *In_Unique_Src*

> features-Copy1-3: *In_Unique_UsrSrc*

> features-Copy2: *Out_Unique_Usr, Out_Unique_Dst, Out_Unique_UsrDst*

> features-Copy4: *Out_Day_Avg_Usr, Out_Day_Avg_Dst, Out_Day_Avg_UsrDst*

## Acknowledgement

Our Python implementation is based on the algorithms presented in [this paper](https://ieeexplore.ieee.org/iel7/4275028/5699970/09335647.pdf) and [this technical report](https://drive.google.com/file/d/1JmVjjwLXy8D7zDtQjePfxPN2PX3Lu_EH/view?pli=1).
