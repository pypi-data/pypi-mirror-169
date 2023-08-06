import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post176"
version_tuple = (0, 5, 0, 176)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post176")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post34"
data_version_tuple = (0, 5, 0, 34)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post34")
except ImportError:
    pass
data_git_hash = "9b33f911ca30927e18209a7eefc40884dd3c69c0"
data_git_describe = "0.5.0-34-g9b33f911"
data_git_msg = """\
commit 9b33f911ca30927e18209a7eefc40884dd3c69c0
Merge: 35def5a2 f6cd2b72
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Sep 28 08:34:14 2022 +0200

    Merge pull request #674 from Silabs-ArjanB/ArjanB_priondi
    
    Clarified relative priority of NMIs, interrupts, debug, exceptions

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
