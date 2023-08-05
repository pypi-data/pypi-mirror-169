# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2018-2022 Colin B. Macdonald
# Copyright (C) 2018-2020 Andrew Rechnitzer
# Copyright (C) 2020 Dryden Wiebe

from multiprocessing import Pool
from pathlib import Path
import shutil
import tempfile

from tqdm import tqdm

from plom.finish import start_messenger
from plom.finish.examReassembler import reassemble


def _parfcn(y):
    """Parallel function used below, must be defined in root of module. Reassemble a pdf from the cover and question images.

    Leave coverfname as None to omit it (e.g., when totalling).

    Args:
        y : arguments to testReassembler.reassemble
    """
    reassemble(*y)


def download_page_images(msgr, tmpdir, outdir, short_name, t, sid):
    """Reassembles a test with a filename that includes the directory and student id.

    Args:
        msgr (ManagerMessenger): the messenger to the plom server.
        tmpdir (pathlib.Path): where to store the temporary files.
        outdir (pathlib.Path): where to put the reassembled test.
        short_name (str): the name of the test.
        t (int/str): test number.
        sid (str): student id.

    Returns:
        tuple (outname, short_name, sid, None, rnames): descriptions below.
            outname (str): the full name of the file.
            short_name (str): same as argument.
            sid (str): sane as argument.
            None: placeholder for the coverpage which is not used here
            id_pages: pages flagged as id_pages, empty
            question_pagess: we pass all pages here
            dnm_pages: pages flagged as do-not-mark, empty
    """
    fnames = msgr.RgetOriginalFiles(t)  # uses deprecated filesystem access
    outname = outdir / f"{short_name}_{sid}.pdf"
    return (outname, short_name, sid, None, [], fnames, [])


def main(server=None, pwd=None):
    msgr = start_messenger(server, pwd)
    try:
        shortName = msgr.getInfoShortName()

        outdir = Path("reassembled_ID_but_not_marked")
        outdir.mkdir(exist_ok=True)
        tmpdir = Path(tempfile.mkdtemp(prefix="tmp_images_", dir=Path.cwd()))
        print(f"Downloading to temp directory {tmpdir}")

        identifiedTests = msgr.getIdentified()
        pagelists = []
        for t in identifiedTests:
            if identifiedTests[t][0] is not None:
                dat = download_page_images(
                    msgr, tmpdir, outdir, shortName, t, identifiedTests[t][0]
                )
                pagelists.append(dat)
            else:
                print(">>WARNING<< Test {} has no ID".format(t))
    finally:
        msgr.closeUser()
        msgr.stop()

    N = len(pagelists)
    print("Reassembling {} papers...".format(N))
    with Pool() as p:
        r = list(tqdm(p.imap_unordered(_parfcn, pagelists), total=N))

    print(">>> Warning <<<")
    print(
        "This still gets files by looking into server directory. In future this should be done over http."
    )
    shutil.rmtree(tmpdir)


if __name__ == "__main__":
    main()
