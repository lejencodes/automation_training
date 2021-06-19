"""
You'll probably want to customize this to your own environment and needs.

For changes to take effect immediately, use Python's Develop Mode.
Develop Mode Install: "pip install -e ."  (from the top-level directory)
"""


# #####>>>>>----- REQUIRED/IMPORTANT SETTINGS -----<<<<<#####

# Default maximum time (in seconds) to wait for page elements to appear.
# Different methods/actions in base_case.py use different timeouts.
# If the element to be acted on does not appear in time, the test fails.
MINI_TIMEOUT = 2
SMALL_TIMEOUT = 6
LARGE_TIMEOUT = 10
EXTREME_TIMEOUT = 30
