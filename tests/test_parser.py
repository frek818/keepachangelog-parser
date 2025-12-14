from keepachangelog_parser import parser

from .util import as_dict


def test_out_of_the_box():
    text = """# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Initial commit

"""

    want = {
        "changelog": {
            "intro": [
                "# ",
                "Changelog",
                "\n",
                "All notable changes to this project will be documented in this file.",
                "\n",
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/),",
                "\n",
                "and this project adheres to [Semantic "
                "Versioning](https://semver.org/spec/v2.0.0.html).",
                "\n",
            ],
            "releases": [
                {
                    "change_types": [
                        {
                            "change_type": "Added",
                            "entries": [{"description": "Initial commit"}],
                        }
                    ],
                    "version": "Unreleased",
                }
            ],
        }
    }
    changelog_document = parser.ChangeLogDocument()("changelog")
    got = changelog_document.parse_string(text)
    assert as_dict(got) == want


def test_one_release():
    text = """# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- *docs/*:New Stuff [ADO#123](https://github.com/frek818/keepachangelog-parser)

## [1.0.0] - 2025-01-01



### Added
- Initial 



### Fixed
- *docs/*:New Stuff [ADO#123](https://github.com/frek818/keepachangelog-parser)

[Unreleased]: <https://www.dido.com/diff?from=refs/tags/1.0.0&to=refs/heads/develop>
[1.0.0]: <https://www.dido.com/diff?from=sdfjalsie&to=refs/tags/1.0.0>

"""
    want = {
        "changelog": {
            "intro": [
                "# ",
                "Changelog",
                "\n",
                "All notable changes to this project will be documented in this file.",
                "\n",
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/),",
                "\n",
                "and this project adheres to [Semantic "
                "Versioning](https://semver.org/spec/v2.0.0.html).",
                "\n",
            ],
            "references": [
                {
                    "link": "https://www.dido.com/diff?from=refs/tags/1.0.0&to=refs/heads/develop",
                    "version": "Unreleased",
                },
                {
                    "link": "https://www.dido.com/diff?from=sdfjalsie&to=refs/tags/1.0.0",
                    "version": "1.0.0",
                },
            ],
            "releases": [
                {
                    "change_types": [
                        {
                            "change_type": "Added",
                            "entries": [
                                {
                                    "description": "*docs/*:New Stuff",
                                    "link": {
                                        "href": "https://github.com/frek818/keepachangelog-parser",
                                        "text": "ADO#123",
                                    },
                                }
                            ],
                        }
                    ],
                    "version": "Unreleased",
                },
                {
                    "change_types": [
                        {
                            "change_type": "Added",
                            "entries": [{"description": "Initial"}],
                        },
                        {
                            "change_type": "Fixed",
                            "entries": [
                                {
                                    "description": "*docs/*:New Stuff",
                                    "link": {
                                        "href": "https://github.com/frek818/keepachangelog-parser",
                                        "text": "ADO#123",
                                    },
                                }
                            ],
                        },
                    ],
                    "release_date": "2025-01-01",
                    "version": "1.0.0",
                },
            ],
        }
    }
    doc = parser.ChangeLogDocument()("changelog")
    got = doc.parse_string(text)
    assert as_dict(got) == want


def test_multiple_releases():
    sample = """# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Initial 

## [1.1.0] - 2025-01-02
### Added
- *docs/*:New Stuff [ADO#123](https://github.com/frek818/keepachangelog-parser)

## [1.0.0] - 2025-01-01
### Changed
- *docs/*:New Stuff [ADO#123](https://github.com/frek818/keepachangelog-parser)


[Unreleased]: <https://www.dido.com/diff?from=refs/tags/1.1.0&to=refs/heads/develop>
[1.1.0]: <https://www.dido.com/diff?from=refs/tags/1.0.0&to=refs/tags/1.1.0>
[1.0.0]: <https://www.dido.com/diff?from=sdfjalsie&to=refs/tags/1.0.0>

"""
    want = {
        "changelog": {
            "intro": [
                "# ",
                "Changelog",
                "\n",
                "All notable changes to this project will be documented in this file.",
                "\n",
                "The format is based on [Keep a "
                "Changelog](https://keepachangelog.com/en/1.0.0/),",
                "\n",
                "and this project adheres to [Semantic "
                "Versioning](https://semver.org/spec/v2.0.0.html).",
                "\n",
            ],
            "references": [
                {
                    "link": "https://www.dido.com/diff?from=refs/tags/1.1.0&to=refs/heads/develop",
                    "version": "Unreleased",
                },
                {
                    "link": "https://www.dido.com/diff?from=refs/tags/1.0.0&to=refs/tags/1.1.0",
                    "version": "1.1.0",
                },
                {
                    "link": "https://www.dido.com/diff?from=sdfjalsie&to=refs/tags/1.0.0",
                    "version": "1.0.0",
                },
            ],
            "releases": [
                {
                    "change_types": [
                        {
                            "change_type": "Added",
                            "entries": [{"description": "Initial"}],
                        }
                    ],
                    "version": "Unreleased",
                },
                {
                    "change_types": [
                        {
                            "change_type": "Added",
                            "entries": [
                                {
                                    "description": "*docs/*:New Stuff",
                                    "link": {
                                        "href": "https://github.com/frek818/keepachangelog-parser",
                                        "text": "ADO#123",
                                    },
                                }
                            ],
                        }
                    ],
                    "release_date": "2025-01-02",
                    "version": "1.1.0",
                },
                {
                    "change_types": [
                        {
                            "change_type": "Changed",
                            "entries": [
                                {
                                    "description": "*docs/*:New Stuff",
                                    "link": {
                                        "href": "https://github.com/frek818/keepachangelog-parser",
                                        "text": "ADO#123",
                                    },
                                }
                            ],
                        }
                    ],
                    "release_date": "2025-01-01",
                    "version": "1.0.0",
                },
            ],
        }
    }
    doc = parser.ChangeLogDocument()("changelog")
    got = doc.parse_string(sample)
    assert as_dict(got) == want


def test_ChangeTypeHeading():
    change_type = parser.ChangeTypeHeading()
    assert change_type.parse_string("### Added").as_list() == ["Added"]
    assert change_type.parse_string("### Changed").as_list() == ["Changed"]
    assert change_type.parse_string("### Removed").as_list() == ["Removed"]
    assert change_type.parse_string("### Fixed").as_list() == ["Fixed"]


def test_ReleaseHeading():
    text = "## [1.25.0] - 2025-12-10\n"
    want = {"release_heading": {"release_date": "2025-12-10", "version": "1.25.0"}}
    release_heading = parser.ReleaseHeading()("release_heading")
    got = release_heading.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_ChangeTypeSection():
    text = """### Added
- *keepachangelog.com*: hello world. [abc](https://dev.azure.com/)
- *api.keepachangelog.com*: Added something cool. [ADO#435](https://gitbug.com/)
"""
    want = {
        "change_section": {
            "change_type": "Added",
            "entries": [
                {
                    "description": "*keepachangelog.com*: hello world.",
                    "link": {"href": "https://dev.azure.com/", "text": "abc"},
                },
                {
                    "description": "*api.keepachangelog.com*: Added something cool.",
                    "link": {"href": "https://gitbug.com/", "text": "ADO#435"},
                },
            ],
        }
    }
    cts = parser.ChangeTypeSection()("change_section")
    got = cts.parse_string(text)
    assert as_dict(got) == want


def test_UnreleasedSection():
    text = """## [Unreleased]
### Added
- asdf [fancy](https://www.ford.com/escort) 

"""
    want = {
        "unreleased": {
            "change_types": [
                {
                    "change_type": "Added",
                    "entries": [
                        {
                            "description": "asdf",
                            "link": {
                                "href": "https://www.ford.com/escort",
                                "text": "fancy",
                            },
                        }
                    ],
                }
            ],
            "version": "Unreleased",
        }
    }
    unreleased = parser.UnreleasedSection()("unreleased")
    got = unreleased.parse_string(text)
    assert as_dict(got) == want


def test_UnreleasedSection_greedy():
    text = """## [Unreleased]
### Added
- Initial world

### Security
- Initial world

"""
    text = """## [Unreleased]
### Added
- Initial    asdf 


"""
    want = {
        "unreleased": {
            "change_types": [
                {
                    "change_type": "Added",
                    "entries": [{"description": "Initial    asdf"}],
                }
            ],
            "version": "Unreleased",
        }
    }
    unreleased = parser.UnreleasedSection()("unreleased")
    got = unreleased.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_Link():
    want = {
        "link": {
            "text": "onward & upward",
            "href": "https://www.keepachangelog.com/vroom",
        }
    }
    link = parser.Link()("link")
    got = link.parse_string("[onward & upward](https://www.keepachangelog.com/vroom)")
    assert as_dict(got) == want


def test_UnreleasedReference():
    text = "[Unreleased]: <https://one-two-three.com/>"
    want = {
        "reference": {
            "link": "https://one-two-three.com/",
            "version": "Unreleased",
        },
    }
    link = parser.UnreleasedReference()("reference")
    got = link.parse_string(text)
    assert as_dict(got) == want


def test_ReleaseReference():
    text = "[1.2.3]: <https://one-two-three.com/>"
    want = {"reference": {"link": "https://one-two-three.com/", "version": "1.2.3"}}

    link = parser.ReleaseReference()("reference")
    got = link.parse_string(text)
    assert as_dict(got) == want


def test_ChangeEntry():
    change_entry = parser.ChangeEntry()("change_entry")

    got = change_entry.parse_string(
        "- hello world the sky is falling [VROOM#123](https://www.keepachangelog.com)\n"
    )
    assert as_dict(got) == {
        "change_entry": {
            "description": "hello world the sky is falling",
            "link": {"text": "VROOM#123", "href": "https://www.keepachangelog.com"},
        }
    }

    got = change_entry.parse_string("- hello\n")
    assert as_dict(got) == {"change_entry": {"description": "hello"}}

    got = change_entry.parse_string("- hello world the sky is falling\n")
    assert as_dict(got) == {
        "change_entry": {"description": "hello world the sky is falling"}
    }


def test_ChangeEntries():
    text = """- abc def
- cba fed [xyz](http://www.lmnop.com)
"""
    want = {
        "entries": [
            {"description": "abc def"},
            {
                "description": "cba fed",
                "link": {"href": "http://www.lmnop.com", "text": "xyz"},
            },
        ]
    }
    change_entries = parser.ChangeEntries()("entries")
    got = change_entries.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_ReleaseSection():
    text = """## [1.2.3] - 2025-11-12
### Added
- milk to cart
"""
    want = {
        "release_section": {
            "change_types": [
                {"change_type": "Added", "entries": [{"description": "milk to cart"}]}
            ],
            "release_date": "2025-11-12",
            "version": "1.2.3",
        }
    }
    release_section = parser.ReleaseSection()("release_section")
    got = release_section.parse_string(text)
    assert as_dict(got) == want


def test_ReleaseReferencesSection():
    text = """
[Unreleased]: <https://www.unreleased.com>
[1.0.0]: <https://www.released.com/1.0.0>

"""
    want = {
        "release_references": [
            {"link": "https://www.unreleased.com", "version": "Unreleased"},
            {"link": "https://www.released.com/1.0.0", "version": "1.0.0"},
        ]
    }
    release_references = parser.ReleaseReferencesSection()("release_references")
    got = release_references.parse_string(text)
    assert as_dict(got) == want


def test_UnifiedReleases():

    text = """
## [Unreleased]      
### Added
- Initial commit


## [123.456.789] - 2025-01-02    

### Added

- Initial commit
"""
    want = {
        "unified_releases": [
            {
                "change_types": [
                    {
                        "change_type": "Added",
                        "entries": [{"description": "Initial " "commit"}],
                    }
                ],
                "version": "Unreleased",
            },
            {
                "change_types": [
                    {
                        "change_type": "Added",
                        "entries": [{"description": "Initial " "commit"}],
                    }
                ],
                "release_date": "2025-01-02",
                "version": "123.456.789",
            },
        ]
    }
    unified_releases = parser.UnifiedReleases()("unified_releases")
    got = unified_releases.parse_string(text)
    assert as_dict(got) == want
