"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if(len(intervals)==0):
            return True
        intervals.sort(key=lambda x:x.start)
        l = intervals[0].start
        r = intervals[0].end
        for a in intervals[1:]:
            if a.start < r:  # Overlap detected (using < instead of >)
                return False  # Conflict found
            else:
                l = a.start
                r = a.end
        
        return True  # No conflicts