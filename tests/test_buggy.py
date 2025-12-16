from keepachangelog_parser import parser

from .util import as_dict


def test_fulL_doc_buggy_case():
    text = """
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- easy. [ADO#398442](https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442)

## [1.1.0] - 2025-01-01
### Added
- peazy [ADO#123](https://github.com/frek818/keepachangelog-parser)

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
                            "type": "Added",
                            "entries": [
                                {
                                    "description": "easy.",
                                    "link": {
                                        "href": "https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442",
                                        "text": "ADO#398442",
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
                            "type": "Added",
                            "entries": [
                                {
                                    "description": "peazy",
                                    "link": {
                                        "href": "https://github.com/frek818/keepachangelog-parser",
                                        "text": "ADO#123",
                                    },
                                }
                            ],
                        }
                    ],
                    "release_date": "2025-01-01",
                    "version": "1.1.0",
                },
            ],
        }
    }
    doc = parser.ChangeLogDocument()("changelog")
    got = doc.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_buggy_unreleased_section_trailing_newlines():
    text = """## [Unreleased]



### Changed
- habla espanol [si](https://www.arriba.com)

### Added






- habla espanol [si](https://www.arriba.com)


- habla espanol [si](https://www.arriba.com)

### Removed
- habla espanol [si](https://www.arriba.com)


- habla espanol [si](https://www.arriba.com)
### Fixed
- habla espanol [si](https://www.arriba.com)
- habla espanol
- habla espanol [si](https://www.arriba.com)


"""
    want = {
        "section": {
            "change_types": [
                {
                    "type": "Changed",
                    "entries": [
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                    ],
                },
                {
                    "type": "Added",
                    "entries": [
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                    ],
                },
                {
                    "type": "Removed",
                    "entries": [
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                    ],
                },
                {
                    "type": "Fixed",
                    "entries": [
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                        {
                            "description": "habla espanol",
                        },
                        {
                            "description": "habla espanol",
                            "link": {
                                "href": "https://www.arriba.com",
                                "text": "si",
                            },
                        },
                    ],
                },
            ],
            "version": "Unreleased",
        },
    }
    unreleased_sectipn = parser.UnreleasedSection()("section")
    got = unreleased_sectipn.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_buggy_unreleased_section_no_trailing_newlines():
    text = """## [Unreleased]
### Added
- *www.keepachangelog.ca*: Added `/paynow` vanity URL. [ADO#398442](https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442)"""

    want = {
        "section": {
            "change_types": [
                {
                    "type": "Added",
                    "entries": [
                        {
                            "description": "*www.keepachangelog.ca*: "
                            "Added `/paynow` "
                            "vanity URL.",
                            "link": {
                                "href": "https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442",
                                "text": "ADO#398442",
                            },
                        }
                    ],
                }
            ],
            "version": "Unreleased",
        }
    }
    unreleased_sectipn = parser.UnreleasedSection()("section")
    got = unreleased_sectipn.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_unifiedreleases():
    text = """ 
## [Unreleased]
### Added
- easy. [ADO#398442](https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442)

## [1.1.0] - 2025-01-01
### Added
- peazy [ADO#123](https://github.com/frek818/keepachangelog-parser)
"""
    want = {
        "unified": [
            {
                "change_types": [
                    {
                        "type": "Added",
                        "entries": [
                            {
                                "description": "easy.",
                                "link": {
                                    "href": "https://dev.azure.com/keepachangelog/keepachangelog/_workitems/edit/398442",
                                    "text": "ADO#398442",
                                },
                            },
                        ],
                    },
                ],
                "version": "Unreleased",
            },
            {
                "change_types": [
                    {
                        "type": "Added",
                        "entries": [
                            {
                                "description": "peazy",
                                "link": {
                                    "href": "https://github.com/frek818/keepachangelog-parser",
                                    "text": "ADO#123",
                                },
                            },
                        ],
                    },
                ],
                "release_date": "2025-01-01",
                "version": "1.1.0",
            },
        ],
    }
    unified_release = parser.UnifiedReleases()("unified")
    got = unified_release.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_buggy_changetypesection():
    text = """### Added
- milk to cart



"""
    want = {
        "change_type_section": {
            "type": "Added",
            "entries": [{"description": "milk to cart"}],
        }
    }
    change_type_section = parser.ChangeTypeSection()("change_type_section")
    got = change_type_section.parse_string(text, parse_all=True)
    assert as_dict(got) == want


def test_buggy_unreleasedsection_multiple_changetypesections():

    text = """## [Unreleased]

### Added
- milk to cart



### Changed          
- diaper


### Security

- hacked
"""

    want = {
        "unreleased_section": {
            "change_types": [
                {
                    "type": "Added",
                    "entries": [{"description": "milk to cart"}],
                },
                {"type": "Changed", "entries": [{"description": "diaper"}]},
                {"type": "Security", "entries": [{"description": "hacked"}]},
            ],
            "version": "Unreleased",
        }
    }
    unreleased_section = parser.UnreleasedSection()("unreleased_section")
    got = unreleased_section.parse_string(text, parse_all=True)
    assert as_dict(got) == want
