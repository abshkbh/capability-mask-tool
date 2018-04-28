This is a command line utility to help with linux capabilities. It helps:
- To convert a capability mask to a list of capabilities.
- To convert a list of capabilities to a capability mask.

Capabilities correspond to values in <linux/capability.h>

Example: python cap-mask.py -c2m CAP_WAKE_ALARM CAP_SETUID
Example: python cap-mask.py -m2c 0x800000080\n'
