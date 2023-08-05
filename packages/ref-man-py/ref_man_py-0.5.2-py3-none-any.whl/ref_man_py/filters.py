from typing import Dict, List, Optional
import re


def year_filter(entry: Dict, min: int, max: int) -> bool:
    min = -1 if (min == "any" or not min) else min
    max = 10000 if (max == "any" or not max) else max
    return entry["year"] >= min and entry["year"] <= max


def author_filter(entry: Dict, author_names: List[str], author_ids: List[str]) -> bool:
    """Return True if any of the given authors by name or id are in the entry.

    Only one of ids or names are checked.

    """
    if author_ids:
        return any([a == x['authorId'] for a in author_ids for x in entry["authors"]])
    elif author_names:
        return any([a == x['name'] for a in author_names for x in entry["authors"]])
    else:
        return False


def num_citing_filter(entry: Dict, min: int, max: Optional[int] = None) -> bool:
    """Return True if the number of citations is greater or equal than `num`"""
    if max is not None:
        return entry["citationCount"] >= min and entry["citationCount"] < max
    else:
        return entry["citationCount"] >= min


def num_influential_count_filter(entry: Dict, min: int, max: Optional[int] = None) -> bool:
    """Return True if the influential citations is greater or equal than `num`"""
    if max is not None:
        return entry["influentialCitationCount"] >= min and entry["influentialCitationCount"] < max
    else:
        return entry["influentialCitationCount"] >= min


def venue_filter(entry: Dict, venues: List[str]) -> bool:
    """Return True if any of the given venues by regexp match are in the entry.

    The case in regexp match is ignored.

    """
    return any([re.match(x, entry["venue"], flags=re.IGNORECASE)
                for x in venues])


def title_filter(entry: Dict, title_re: str, invert: bool) -> bool:
    """Return True if the given regexp matches the entry title.

    The case in regexp match is ignored.
    Args:
        entry: A paper entry
        title_re: title regexp
        invert: Whether to include or exclude matching titles

    """
    match = bool(re.match(title_re, entry["title"], flags=re.IGNORECASE))
    return not match if invert else match
