# Interval Scheduler

Implement two functions in `scheduler.py`:

1. `merge_busy(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]`: merge overlapping or touching `[start, end]` intervals.
2. `find_free_slots(busy: list[tuple[int, int]], day_start: int, day_end: int, min_duration: int) -> list[tuple[int, int]]`: return all free slots of length `>= min_duration` within `[day_start, day_end]`.
