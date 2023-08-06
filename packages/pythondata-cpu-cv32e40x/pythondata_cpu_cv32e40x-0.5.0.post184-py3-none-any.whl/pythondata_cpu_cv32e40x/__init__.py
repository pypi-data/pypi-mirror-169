import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.5.0.post184"
version_tuple = (0, 5, 0, 184)
try:
    from packaging.version import Version as V
    pversion = V("0.5.0.post184")
except ImportError:
    pass

# Data version info
data_version_str = "0.5.0.post42"
data_version_tuple = (0, 5, 0, 42)
try:
    from packaging.version import Version as V
    pdata_version = V("0.5.0.post42")
except ImportError:
    pass
data_git_hash = "707899d0ee31c6ae904c984dac3fa4a029e472b6"
data_git_describe = "0.5.0-42-g707899d0"
data_git_msg = """\
commit 707899d0ee31c6ae904c984dac3fa4a029e472b6
Merge: 9b33f911 4f7bd710
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Sep 28 11:48:44 2022 +0200

    Merge pull request #669 from silabs-oysteink/silabs_oysteink_wfe
    
    Implemented custom WFE instruction

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
