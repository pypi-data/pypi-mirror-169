# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2019-2022 Colin B. Macdonald
# Copyright (C) 2020 Andrew Rechnitzer
# Copyright (C) 2020 Vala Vakilian
# Copyright (C) 2020 Dryden Wiebe
# Copyright (C) 2021 Elizabeth Xiao

"""Plom tools for scribbling fake answers on PDF files."""

import base64
import importlib.resources as resources
import json
from pathlib import Path
import random

import fitz

import plom.create
import plom.create.fonts
from plom.create import paperdir as _paperdir
from plom.create import with_manager_messenger


possible_answers = [
    "I am so sorry, I really did study this... :(",
    "I know this, I just can't explain it",
    "Hey, at least its not in Comic Sans",
    "Life moves pretty fast. If you don't stop and look around once in a while, "
    "you could miss it.  -- Ferris Bueler",
    "Stupid is as stupid does.  -- Forrest Gump",
    "Of course, it is very important to be sober when you take an exam.  "
    "Many worthwhile careers in the street-cleansing, fruit-picking and "
    "subway-guitar-playing industries have been founded on a lack of "
    "understanding of this simple fact.  -- Terry Pratchett",
    "The fundamental cause of the trouble in the modern world today is that "
    "the stupid are cocksure while the intelligent are full of doubt.  "
    "-- Bertrand Russell",
    "Numbers is hardly real and they never have feelings\n"
    "But you push too hard, even numbers got limits.  -- Mos Def",
    "I was doin' 150 miles an hour sideways\n"
    "And 500 feet down at the same time\n"
    "I was lookin' for the cops, 'cuz you know\n"
    "I knew that it, it was illegal  -- Arlo Guthrie",
    "But there will always be science, engineering, and technology.  "
    "And there will always, always be mathematics.  -- Katherine Johnson",
    "Is 5 = 1?  Let's see... multiply both sides by 0.  "
    "Now 0 = 0 so therefore 5 = 1.",
    "I mean, you could claim that anything's real if the only basis for "
    "believing in it is that nobody's proved it doesn't exist!  -- Hermione Granger",
]


# Customizable data
blue = [0, 0, 0.75]
name_font_size = 26
answer_font_size = 18


def scribble_name_and_id(
    pdf_doc, student_number, student_name, *, pagenum=0, seed=None
):
    """Write name/number on coverpage of fitz pdf_doc.

    Arguments:
        pdf_doc (fitz.Document): an open pdf file, we'll modify it
            implicitly but not close it.
        student_number (str)
        student_name (str)

    Keyword Args:
        pagenum (int): which page is the coverpage, default 0 (1st page).
        seed (None/int): seed the random number generator with this value.
            Default of None means don't.  This can be used to ensure the
            same digit images are chosen each time, useful for testing.

    Returns:
        None: but modifies the open document as a side effect.
    """
    # load the digit images
    digit_array = json.loads(resources.read_text(plom.create, "digits.json"))
    # array is organized in blocks of each digit with this many samples of each
    num_samples = len(digit_array) // 10
    assert len(digit_array) % 10 == 0

    if seed is not None:
        random.seed(seed)

    # insert digit images into rectangles - some hackery required to get correct positions.
    id_page = pdf_doc[pagenum]
    width = 28
    border = 8
    for n, digit in enumerate(student_number):
        rect1 = fitz.Rect(
            220 + border * n + width * n,
            265,
            220 + border * n + width * (n + 1),
            265 + width,
        )
        # uu-encoded png
        uuImg = digit_array[int(digit) * num_samples + random.randrange(num_samples)]
        img_BString = base64.b64decode(uuImg)
        id_page.insert_image(rect1, stream=img_BString, keep_proportion=True)
        # TODO - there should be an assert or something here after insert?

    fontname, ttf = "ejx", "ejx_handwriting.ttf"
    rect = fitz.Rect(220 + random.randrange(0, 16), 345, 600, 450)
    with resources.path(plom.create.fonts, ttf) as fontfile:
        excess = id_page.insert_textbox(
            rect,
            student_name,
            fontsize=name_font_size,
            color=blue,
            fontname=fontname,
            fontfile=str(fontfile),  # remove str once PyMuPDF >= 1.19.5
            align=0,
        )
    assert excess > 0
    del id_page


def scribble_pages(pdf_doc, exclude=(0, 1)):
    """Scribble on most pages of fitz pdf_doc.

    Arguments:
        pdf_doc (fitz.Document): an open pdf file, we'll modify it
            implicitly but not close it.

    Returns:
        None: but modifies the open document as a side effect.

    By default exclude pages 0 and 1 (the ID page and DNM page in our demo data).
    """
    # In principle you can put other fonts in plom.create.fonts
    # Can also use "helv" (or "Helvetica"?) and `None` for the fontfile
    # fontname, ttf = random.choice(...)
    fontname, ttf = "ejx", "ejx_handwriting.ttf"

    # Write some random answers on the pages
    for page_index, pdf_page in enumerate(pdf_doc):
        answer_rect = fitz.Rect(
            100 + 30 * random.random(), 150 + 20 * random.random(), 500, 500
        )
        answer_text = random.choice(possible_answers)

        if page_index in exclude:
            continue
        with resources.path(plom.create.fonts, ttf) as fontfile:
            excess = pdf_page.insert_textbox(
                answer_rect,
                answer_text,
                fontsize=answer_font_size,
                color=blue,
                fontname=fontname,
                fontfile=str(fontfile),  # remove str once PyMuPDF >= 1.19.5
                align=0,
            )
            assert excess > 0


def fill_in_fake_data_on_exams(paper_dir, classlist, outfile, which=None):
    """Fill-in exams with fake data for demo or testing.

    Arguments:
        paper_dir (str/pathlib.Path): Directory containing the blank exams.
        classlist (list): list of dicts with keys `id` and `name`.
            See also Issue #1646: maybe will use `student_number` someday.
        outfile (str/pathlib.Path): write results into this concatenated PDF file.

    Keyword Arguments:
        which (iterable): By default we scribble on all exams or specify
            something like ``which=range(10, 16)`` here to scribble on a
            subset. (default: `None`)
    """
    # Customizable data
    extra_page_probability = 0.2
    extra_page_font_size = 18

    paper_dir = Path(paper_dir)
    outfile = Path(outfile)

    print("Annotating papers with fake student data and scribbling on pages...")
    if which:
        papers_paths = sorted([paper_dir / f"exam_{i:04}.pdf" for i in which])
    else:
        papers_paths = sorted(paper_dir.glob("exam_*.pdf"))

    # those with an ID number
    named_papers_paths = list(paper_dir.glob("exam_*_*.pdf"))
    # extract student numbers used in prenaming
    used_ids = [f.stem.split("_")[-1] for f in named_papers_paths]
    # get those students not used in the the prename
    available_classlist = [x for x in classlist if x["id"] not in used_ids]
    random.shuffle(available_classlist)

    # A complete collection of the pdfs created
    all_pdf_documents = fitz.open()

    for index, f in enumerate(papers_paths):
        if f in named_papers_paths:
            print(f"{f.name} - prenamed paper - scribbled")
        else:
            x = available_classlist.pop()
            # TODO: Issue #1646: check for "student_number" fallback to id
            student_number = x["id"]
            student_name = x["name"]
            print(f"{f.name} - scribbled using {student_number} {student_name}")

        # TODO: could do `with fitz.open(f) as pdf_document:`
        pdf_document = fitz.open(f)

        if f not in named_papers_paths:
            # TODO: use spec.IDpage
            scribble_name_and_id(pdf_document, student_number, student_name)

        # TODO: should match the ID page and DNM pages from spec settings
        scribble_pages(pdf_document)

        # delete last page from the first test
        if index == 0:
            pdf_document.delete_page(-1)
            print(f"Deleting last page of test {f}")

        # We then add the pdfs into the document collection
        all_pdf_documents.insert_pdf(pdf_document)
        pdf_document.close()

        # For a comprehensive test, we will add some extrapages with low probability
        if random.random() < extra_page_probability:
            # folder_name/exam_XXXX.pdf or folder_name/exam_XXXX_YYYYYYY.pdf,
            test_number = f.stem.split("_")[1]
            if f in named_papers_paths:
                # exam_XXXX_YYYYYYY.pdf
                student_number = f.stem.split("_")[2]

            print(
                f"  making an extra page for test {test_number} and id {student_number}"
            )
            all_pdf_documents.insert_page(
                -1,
                text=f"EXTRA PAGE - t{test_number} Q1 - {student_number}",
                fontsize=extra_page_font_size,
                color=blue,
            )

    all_pdf_documents.save(outfile)
    all_pdf_documents.close()
    print(f'Assembled in "{outfile}"')


def make_garbage_pages(pdf_file, number_of_garbage_pages=2):
    """Randomly generates and inserts garbage pages into a PDF document.

    Used for testing.

    Arguments:
        pdf_file (pathlib.Path): a pdf file we add pages to.

    Keyword Arguments:
        number_of_garbage_pages (int): how many junk pages to add (default: 2)
    """
    green = [0, 0.75, 0]

    doc = fitz.open(pdf_file)
    print("Doc has {} pages".format(len(doc)))
    for _ in range(number_of_garbage_pages):
        garbage_page_index = random.randint(-1, len(doc))
        print(f"Insert garbage page at garbage_page_index={garbage_page_index}")
        doc.insert_page(
            garbage_page_index, text="This is a garbage page", fontsize=18, color=green
        )
    doc.saveIncr()
    doc.close()


def make_colliding_pages(paper_dir, outfile):
    """Build two colliding pages - last pages of papers 2 and 3.

    Arguments:
        paper_dir (str/pathlib.Path): Directory containing the blank exams.
        outfile (pathlib.Path): modify this pdf file, appending the
            colliding pages.

    Purely used for testing.
    """
    paper_dir = Path(paper_dir)
    outfile = Path(outfile)

    all_pdf_documents = fitz.open(outfile)
    # Customizable data
    colliding_page_font_size = 18

    papers_paths = sorted(paper_dir.glob("exam_*.pdf"))
    for file_name in papers_paths[1:3]:  # just grab papers 2 and 3.
        pdf_document = fitz.open(file_name)
        test_length = len(pdf_document)
        colliding_page_index = random.randint(-1, len(all_pdf_documents))
        print(
            "Insert colliding page at colliding_page_index={}".format(
                colliding_page_index
            )
        )
        all_pdf_documents.insert_pdf(
            pdf_document,
            from_page=test_length - 1,
            to_page=test_length - 1,
            start_at=colliding_page_index,
        )
        pdf_document.close()
        excess = all_pdf_documents[colliding_page_index].insert_textbox(
            fitz.Rect(100, 100, 500, 500),
            "I was dropped on the floor and rescanned.",
            fontsize=colliding_page_font_size,
            color=blue,
            fontname="helv",
            fontfile=None,
            align=0,
        )
        assert excess > 0

    all_pdf_documents.saveIncr()
    all_pdf_documents.close()


def splitFakeFile(outfile):
    """Split the scribble pdf into three files"""

    outfile = Path(outfile)
    print("Splitting PDF into 3 in order to test bundles.")
    originalPDF = fitz.open(outfile)
    length = len(originalPDF) // 3

    doc1 = fitz.open()
    doc2 = fitz.open()
    doc3 = fitz.open()

    doc1.insert_pdf(originalPDF, from_page=0, to_page=length)
    doc2.insert_pdf(originalPDF, from_page=length + 1, to_page=2 * length)
    doc3.insert_pdf(originalPDF, from_page=2 * length + 1)

    doc1.save(outfile.with_name(outfile.stem + "1.pdf"))
    doc2.save(outfile.with_name(outfile.stem + "2.pdf"))
    doc3.save(outfile.with_name(outfile.stem + "3.pdf"))
    doc1.close()
    doc2.close()
    doc3.close()
    originalPDF.close()


@with_manager_messenger
def make_scribbles(basedir=Path("."), *, msgr):
    """Fake exam writing by scribbling on the pages of the blank exams.

    After Plom exam PDF files have been generated, this can be used to
    scribble on them to simulate random student work.  Note this tool does
    not upload those files, it just makes some PDF files for you to play with
    or for testing purposes.

    Args:
        server (str): the name and port of the server.
        password (str): the "manager" password.
        basedir (str/pathlib.Path): the blank tests (for scribbling) will
            be taken from `basedir/papersToPrint`.  The pdf files with
            scribbles will be created in `basedir`.  Defaults to current
            directory.

    Keyword Args:
        msgr (plom.Messenger/tuple): either a connected Messenger or a
            tuple appropriate for credientials.

    1. Read in the existing papers.
    2. Create the fake data filled pdfs
    3. Do some things to make the data unpleasant:

       * delete the last page of the first test.
       * Randomly add some extra pages
    """
    basedir = Path(basedir)
    outfile = basedir / "fake_scribbled_exams.pdf"
    classlist = msgr.IDrequestClasslist()

    fill_in_fake_data_on_exams(basedir / _paperdir, classlist, outfile)
    make_garbage_pages(outfile)
    make_colliding_pages(basedir / _paperdir, outfile)
    splitFakeFile(outfile)
    outfile.unlink()
