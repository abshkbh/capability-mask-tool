""" Command line utility -
    To convert a capability mask to a list of capabilities.
    To convert a list of capabilities to a capability mask.

    Capabilities correspond to values in <linux/capability.h>.
"""

import sys

# Capability name to bit position mask mapping. Corresponds to
# <linux/capability.h>.
caps_map = { 'CAP_CHOWN' : 0,
             'CAP_DAC_OVERRIDE' : 1,
             'CAP_DAC_READ_SEARCH' : 2,
             'CAP_FOWNER' : 3,
             'CAP_FSETID' : 4,
             'CAP_KILL' : 5,
             'CAP_SETGID' : 6,
             'CAP_SETUID' : 7,
             'CAP_SETPCAP' : 8,
             'CAP_LINUX_IMMUTABLE' : 9,
             'CAP_NET_BIND_SERVICE' : 10,
             'CAP_NET_BROADCAST' : 11,
             'CAP_NET_ADMIN' : 12,
             'CAP_NET_RAW' : 13,
             'CAP_IPC_LOCK' : 14,
             'CAP_IPC_OWNER' : 15,
             'CAP_SYS_MODULE' : 16,
             'CAP_SYS_RAWIO' : 17,
             'CAP_SYS_CHROOT' : 18,
             'CAP_SYS_PTRACE' : 19,
             'CAP_SYS_PACCT' : 20,
             'CAP_SYS_ADMIN' : 21,
             'CAP_SYS_BOOT' : 22,
             'CAP_SYS_NICE' : 23,
             'CAP_SYS_RESOURCE' : 24,
             'CAP_SYS_TIME' : 25,
             'CAP_SYS_TTY_CONFIG' : 26,
             'CAP_MKNOD' : 27,
             'CAP_LEASE' : 28,
             'CAP_AUDIT_WRITE' : 29,
             'CAP_AUDIT_CONTROL' : 30,
             'CAP_SETFCAP' : 31,
             'CAP_MAC_OVERRIDE' : 32,
             'CAP_MAC_ADMIN' : 33,
             'CAP_SYSLOG' : 34,
             'CAP_WAKE_ALARM' : 35,
             'CAP_BLOCK_SUSPEND' : 36,
             'CAP_AUDIT_READ' : 37,
            }

# Help message to print on invalid args or -h / --help.
help_msg = 'Utility to convert from linux capability names to mask and vice-versa.\n-c2m <caps> enter cap names separated by space to get the corresponding caps mask\n-m2c <mask> enter mask in hex or decimal to get list of capabilities\n--help print this message\nExample: python cap-mask.py -c2m CAP_WAKE_ALARM CAP_SETUID\nExample: python cap-mask.py -m2c 0x800000080\n'

# Expects a list of capabilities like ["CAP_WAKE_ALARM", "CAP_SYS_TIME",
# "CAP_AUDIT_READ"]. Returns integer mask corresponding to the list. Exits
# immediately if an invalid capability is present in |caps_list|.
def create_mask_from_caps_list(caps_list):
  mask = 0
  for cap in caps_list:
    if cap not in caps_map:
      print("Invalid cap: %s" % cap)
      sys.exit(1)
    mask |= 1 << caps_map[cap]
  return mask

# Expects integer mask and returns list of corresponding capabilities.
def create_caps_list_from_mask(mask):
  caps_list = []
  for cap, cap_bit in caps_map.items():
    if (mask & (1 << cap_bit)) > 0:
      caps_list.append(cap)
  return caps_list

def handle_args(args):
  args_len = len(args)
  if args[0] == '--help' or args[0] == '-h':
    print help_msg
  elif args[0] == '-c2m' and args_len >= 2:
    print hex(create_mask_from_caps_list(args[1:]))
  elif args[0] == '-m2c' and args_len >= 2:
    print create_caps_list_from_mask(int(args[1], 0))
  else:
    print("Invalid args\n")
    print help_msg
  return

def main():
  argv = sys.argv[1:]
  if not argv:
    print help_msg
    sys.exit(1)
  handle_args(argv)
  return

if __name__ == '__main__':
  main()
