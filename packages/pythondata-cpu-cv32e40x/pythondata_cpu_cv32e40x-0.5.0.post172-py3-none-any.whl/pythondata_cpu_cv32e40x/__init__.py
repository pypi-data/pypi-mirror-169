import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post172"
version_tuple = (0, 5, 0, 172)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post172")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post30"
data_version_tuple = (0, 5, 0, 30)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post30")
except ImportError:
    pass
data_git_hash = "37b423b5c1591ab3493018eca31151b4e266949e"
data_git_describe = "0.5.0-30-g37b423b5"
data_git_msg = """\
commit 37b423b5c1591ab3493018eca31151b4e266949e
Merge: a1ca4fc1 6243bd75
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Tue Sep 27 16:25:36 2022 +0200

    Merge pull request #673 from silabs-oysteink/silabs-oysteink_wfi_timing_fix
    
    Splitting halt_wb to fix timing issues when waking from SLEEP

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
