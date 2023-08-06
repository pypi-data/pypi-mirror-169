import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post188"
version_tuple = (0, 5, 0, 188)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post188")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post46"
data_version_tuple = (0, 5, 0, 46)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post46")
except ImportError:
    pass
data_git_hash = "689a1184bf013548305cf21cbf22460d73d67de0"
data_git_describe = "0.5.0-46-g689a1184"
data_git_msg = """\
commit 689a1184bf013548305cf21cbf22460d73d67de0
Merge: 771a63f8 a87a94b7
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Fri Sep 30 12:15:20 2022 +0200

    Merge pull request #678 from Silabs-ArjanB/ArjanB_sdexrt
    
    Updated to latest RISC-V Debug specification. Added support for disab…

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
