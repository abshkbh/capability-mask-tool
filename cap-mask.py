import sys

# Capability name to bit position mask.
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

help_msg = 'Utility to convert from linux capability names to mask and vice-versa.\n-c2m <caps> enter cap names separated by space to get the corresponding caps mask\n-m2c <mask> enter mask in hex or decimal to get list of capabilities\n--help print this message'


def handle_args(args):
  args_len = len(args)
  if args[0] == '--help' or args[0] == '-h':
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
