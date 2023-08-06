import collections

VersionInfo = collections.namedtuple(
    "VersionInfo", ["major", "minor", "micro", "release_level"]
)

version_info = VersionInfo(major=0, minor=3, micro=5, release_level="beta")
__version__ = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
