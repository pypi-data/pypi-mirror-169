"""
"""
__docformat__ = "restructuredtext"
# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("nlptutti")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

from maskword.maskfactory import (
    mask_name,
    mask_ctznum,
)

#__all__ = ["get_cer",
#           "get_wer"]