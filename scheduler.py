from typing import List, Tuple

Interval = Tuple[int, int]


def merge_busy(intervals: List[Interval]) -> List[Interval]:
    """Merge overlapping or adjacent [start, end] intervals."""
    # TODO: handle empty input, sort by start, merge overlaps
    raise NotImplementedError


def find_free_slots(
    busy: List[Interval],
    day_start: int,
    day_end: int,
    min_duration: int,
) -> List[Interval]:
    """Return free gaps inside [day_start, day_end] with length >= min_duration."""
    # TODO: clamp busy intervals to [day_start, day_end] and collect gaps
    raise NotImplementedError
