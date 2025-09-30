## 1. Out of memory？

Further possibilities to reduce memory consumption are:

- using a smaller encoder such as mitb3 or mitb4 instead of mitb5
- disabling FD (imnet_feature_dist_lambda=0)
- using a smaller crop size

Even though these changes will most probably reduce the mIoU (as shown in the ablations in the paper), they might be a starting point to get DAFormer running your GPU. Further, switching to a less demanding window manager (e.g. xfce) can sometimes give the few extra MB of GPU memory that are missing.
