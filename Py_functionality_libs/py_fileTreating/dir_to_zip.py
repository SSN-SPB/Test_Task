#!/usr/bin/env python3

import os
import zipfile


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )


def main():
    with zipfile.ZipFile("dist.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipdir("D:\\Personal\\PythonCodes\\Py_functionality_libs", zipf)


if __name__ == "__main__":
    main()
