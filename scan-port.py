import socket
import argparse

BANNER = r"""
  #####                                  ######                       ##
 ##   ##                                       ##  ##                      ##
 #         ####     ####    #####              ##  ##   ####    ######    #####
  #####   ##  ##       ##   ##  ##   ######    #####   ##  ##    ##  ##    ##
      ##  ##        #####   ##  ##             ##      ##  ##    ##        ##
 ##   ##  ##  ##   ##  ##   ##  ##             ##      ##  ##    ##        ## ##
  #####    ####     #####   ##  ##            ####      ####    ####        ###
"""

def scan_port(host: str, port: int, timeout: float = 5.0) -> bool:
    """Return True if the TCP port is open on the host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0

def main() -> None:
    print(BANNER)

    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="Target host or IP address")
    parser.add_argument("port", type=int, help="Port to check")
    args = parser.parse_args()

    if scan_port(args.host, args.port):
        print(f"Port {args.port} open on {args.host}")
    else:
        print(f"Port {args.port} closed on {args.host}")

if __name__ == "__main__":
    main()
