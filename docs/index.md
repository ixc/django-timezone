# Overview

Helper functions for working with `datetime` objects without caring if they are
timezone aware or not. If `USE_TZ=True`, timezone aware objects will be
returned and localised to the current or default timezone.

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

Install the app into your virtualenv:

    (venv)$ pip install -e git+ssh://git@github.com/ixc/django-timezone.git#egg=django-timezone

## Usage

The following functions are provided:

    date(when=None, tz=None)
        Return a naive `date` object for `when` in `tz`. Shortcut for
        `localize(when, tz).date()`.

    datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0,
             tzinfo=None)
        Return an aware or naive `datetime` object. Naive objects will be
        converted to the current timezone.

    get(tz=None)
        Return a `tzinfo` object. The default for `tz` is the current timezone.
        The `tz` argument can be a `tzinfo` object or a string. For example,
        "Australia/Sydney".

    jstime(when=None)
        Return a `datetime` object represented as a JavaScript timestamp
        (milliseconds since 1970).

    localize(when=None, tz=None)
        Return `when`, localised (if aware) or converted (if naive) to `tz`.
        The default for `when` is `now()`. The default for `tz` is the
        current timezone. The `tz` argument can also be given as a string. For
        example, "Australia/Sydney".

    midnight(when=None)
        Return an aware or naive `datetime` object for 12:00 AM on `when`,
        which defaults to now in the current timezone.

    now(tz=None)
        Return an aware or naive `datetime` object for now in `tz`. The default
        for `tz` is the current timezone. The `tz` argument can also be given
        as a string. For example, "Australia/Sydney".

    time(when=None, tz=None)
        Return a naive `time` object for `when` in `tz`. Shortcut for
        `localize(when, tz).time()`.

## HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to preview your
documentation as you are writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
