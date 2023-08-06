import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post186"
version_tuple = (0, 5, 0, 186)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post186")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post44"
data_version_tuple = (0, 5, 0, 44)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post44")
except ImportError:
    pass
data_git_hash = "771a63f8583d15b7b3b95a35a0432c77cb8c08cb"
data_git_describe = "0.5.0-44-g771a63f8"
data_git_msg = """\
commit 771a63f8583d15b7b3b95a35a0432c77cb8c08cb
Merge: 707899d0 ee44ba7c
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Sep 29 09:25:39 2022 +0200

    Merge pull request #677 from silabs-oivind/rvfi_trace_performance_fix
    
    Fix performance issue in rvfi_sim_trace and enable it by default.

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
