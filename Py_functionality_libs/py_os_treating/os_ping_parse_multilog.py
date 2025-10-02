#!/usr/bin/env python3

import platform
import subprocess


def ping_site(site_name):
    hostname = site_name
    param = "-n" if platform.system().lower() == "windows" else "-c"

    # Run ping and capture output
    result = subprocess.run(
        ["ping", param, "4", hostname], capture_output=True, text=True
    )

    # result.stdout contains the ping output
    print("Captured Logs:\n", result.stdout)
    return result.stdout


def main():
    assert "Lost = 0" in ping_site("google.com")


if __name__ == "__main__":
    main()
