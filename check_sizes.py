# the translation files can only be a certain size, so this script compares the sizes against those from the official translation mod

# In KB
official_sizes = {
    "al.yml": 37355,
    "bb.yml": 45206,
    "ca.yml": 51256,
    "dc.yml": 16474,
    "di.yml": 2759,
    "eh.yml": 53930,
    "es.yml": 4468,
    "fontimage.bar": 238720,
    "fontinfo.bar": 41988,
    "gumi.yml": 63155,
    "hb.yml": 85635,
    "he.yml": 60740,
    "jm.yml": 278809,
    "lk.yml": 39752,
    "lm.yml": 56446,
    "md_m": 4096,
    "mu.yml": 42887,
    "nm.yml": 52969,
    "po.yml": 32927,
    "sys.yml": 159601,
    "title.yml": 25725,
    "tr.yml": 27327,
    "tt.yml": 156381,
    "wi.yml": 23154,
    "wm.yml": 13944
}

import os
for f in os.listdir("msg"):
    fn = os.path.join("msg", f)
    new_size = os.stat(fn).st_size
    old_size = official_sizes[f]
    if new_size > old_size:
        print("{} is {}% too big ({} extra bytes)".format(f, 100-int((old_size/new_size)*100), new_size-old_size))