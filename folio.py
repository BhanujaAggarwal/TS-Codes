import math
import enum
class Range() :
    lo = int()
    hi = int()
    def __init__(self) :
        self.lo = 0
        self.hi = 0

    def __init__(self,e) :
        self.lo = 0
        self.hi = e

    def __init__(self, a, b) :
        self.lo = math.min(a,b)
        self.hi = math.max(a,b)

    def reset(self) :
        self.lo = 0
        self.hi = 0
    def rStrech(self) :
        self.hi += 1

    def rStrech(self,n) :
        self.hi += n

    def lStrech(self) :
        self.lo += 1

    def lStrech(self,n) :
        self.lo += n

    def strech(self) :
        self.lo -= 1
        self.hi += 1

    def strech(self,n) :
        self.lo -= n
        self.hi += n

    def squeeze(self) :
        self.lo += 1
        self.hi -= 1
        if self.lo > self.hi :
            self.reset()

    def squeeze(self,n) :
        self.lo += n
        self.hi -= n
        if self.lo > self.hi :
            self.reset()

    def shift(self,n) :
        self.lo += n
        self.hi += n

    def length(self) :
        return self.hi - self.lo +1

    def toString(self) :
        return "[" + self.lo + "," + self.hi +"]"

    def contains(self,x) :
        return self.lo <= x and x <= self.hi

    def contains(self,r) :
        return self.lo <= r.lo and r.high <= self.hi

    def equals(self,r) :
        return self.lo == r.low and self.hi == r.high

    def isDisjoint(self,r) :
        return self.lo > r.high or self.hi < r.lo

    def isOverlapping(self,r) :
        return not(self.isDisjoint(r))

    def lessThan(self,r) :
        return self.lo < r.lo

    relation =enum.Enum('relation' ,'SUBSET , SUPERSET, LESSOVERLAP, MOREOVERLAP, TOUCHINGL, TOUCHINGR , LESSDISJOINT,MOREDISJOINT,SAME')

    def classify (r) :
        if self.hi == r.lo :
            return relation.TOUCHINGR
        if self.lo == r.hi :
            return realtion.TOUCHINGL
        if self.equals(r) :
            return relation.SAME
        if self.contains(r) :
            return relation.SUPERSET
        if r.contains(self) :
            return relation.SUBSET
        if self.isDisjoint(r) :
            if self.lo > r.hi :
                return relation.MOREDISJOINT
            else :
                return relation.LESSDISJOINT
        if self.lessThan(r) :
            return relation.LESSOVERLAP
        return relation.MOREOVERLAP

    def merge(Self,r) :
        if self.isDisjoint(r) :
            return Range()
        a = math.min(self.lo , r.lo)
        b = math.max(self.hi , r.hi)
        return Range(a,b)

    def common(self,r):
        if self.isDisjoint(r):
            return Range()
        es = []
        es.append(self.lo)
        es.append(self.hi)
        es.append(r.lo)
        es.append(r.hi)
        es.sort()
        return Range(es[1],es[2])
