# SPDX-FileCopyrightText: 2022-present Paths.py Contributors
#
# SPDX-License-Identifier: MIT

import os
import shutil

from pathlib import Path
from typing import List


class Utils:
    """Utility methods used by toyboxpy."""

    @classmethod
    def lookInFolderFor(cls, folder: str, wildcard: str) -> List[str]:
        # -- We use this here instead of just simply os.path.exists()
        # -- because we want the test to be case-sensitive on all platforms,
        # -- so we list what the match are and let glob give us the paths.
        paths_found = []
        looking_in = Path(folder)

        for p in looking_in.glob(wildcard):
            as_string = str(p)
            if len(as_string) > 4:
                as_string = as_string[len(folder) + 1:-4]
                paths_found.append(as_string)

        return paths_found

    @classmethod
    def backup(cls, from_folder: str, to_folder: str):
        if os.path.exists(from_folder):
            shutil.move(from_folder, to_folder)

    @classmethod
    def restore(cls, from_folder: str, to_folder: str):
        if os.path.exists(to_folder):
            shutil.rmtree(to_folder)

        if os.path.exists(from_folder):
            shutil.move(from_folder, to_folder)

    @classmethod
    def delete(cls, folder: str):
        if os.path.exists(folder):
            shutil.rmtree(folder)

    @classmethod
    def softlinkFromTo(cls, source: str, dest: str):
        if not os.path.exists(source):
            raise RuntimeError('Local toybox folder ' + source + ' cannot be found.')

        os.makedirs(dest, exist_ok=True)

        for file_or_dir in os.listdir(source):
            if file_or_dir[0] == '.':
                continue

            os.symlink(os.path.join(source, file_or_dir), os.path.join(dest, file_or_dir))

    @classmethod
    def copyFromTo(cls, source: str, dest: str):
        if not os.path.exists(source):
            raise RuntimeError('Local toybox folder ' + source + ' cannot be found.')

        shutil.copytree(source, os.path.join(dest, ''))
