# -*- coding: utf-8 -*-
#
#    TypeAtlas Generic Utilities
#    Copyright (C) 2021 Milko Krachounov
#
#    This file is part of TypeAtlas
#
#    TypeAtlas is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TypeAtlas is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TypeAtlas.  If not, see <http://www.gnu.org/licenses/>.
#
#                                 ***
#
#    Alternatively, you may use this file (part of TypeAtlas libraries)
#    under the terms of the X11/MIT license as follows:
#
#    Permission is hereby granted, free of charge, to any person
#    obtaining a copy of this software and associated documentation
#    files (the "Software"), to deal in the Software without
#    restriction, including without limitation the rights to use,
#    copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the
#    Software is furnished to do so, subject to the following
#    conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#    OTHER DEALINGS IN THE SOFTWARE.
#

"""A library that allows one to perform complex operations on discrete ranges
of e.g. codepoints defined by set-like objects that store lists of
first and last number in a range. This is a complex library that
provides full Set interface. If you want simple operations, consider
using blockmath.

Like blocks from blockmath, the ranges are defined as their start and end,
inclusively, unlike Python's range().

For compatibility with range(), the ranges provide the Sequence interface
as well.
"""

# FIXME Too many hardcoded types, particularly RangeWrapper.

from collections.abc import Set, Iterable, Callable, Sequence, Container
from itertools import chain, islice
from typeatlas import blockmath
import re
import sys
import abc
import bisect
import numbers

from typeatlas.util import generic_type

SequenceOf = generic_type('Sequence')
IterableOf = generic_type('Iterable')
AnyStr = generic_type('AnyStr')
Optional = generic_type('Optional')


range_pattern = re.compile(r'(?s)^(.+?)(?:[:-](.+))?$')


class RangeBase(Set, Sequence):

    """The base class for discrete ranges. Use this class as a type hint.

    The ranges property defines any subranges.
    """

    __slots__ = ()

    value_type = None
    range_type = None

    ranges = ()

    def to_plain_blocks(self) -> SequenceOf[blockmath.BlockLike]:
        """Convert to blocks (plain tuples)"""
        return [(rg.start, rg.end) for rg in self.ranges]

    def to_blocks(self) -> SequenceOf[blockmath.Block]:
        """Convert to blocks (Block named tuples)"""
        return [blockmath.Block(rg.start, rg.end) for rg in self.ranges]

    def to_fontconfig(self) -> str:
        """Convert to fontconfig format."""
        return ' '.join('%x-%x' % (rg.start, rg.end) for rg in self.ranges)

    def tostring(self) -> str:
        """Convert to decimal string. This is broken for character ranges
        with spaces at the ends."""
        return ' '.join('%s-%s' % (rg.start, rg.end) for rg in self.ranges)

    def __eq__(self, other):
        ## Sequences of different types are not equal to each other, but
        ## one can enable this if they want with this code.
        #if not isinstance(other, Set) and isinstance(other, Sequence):
        #    return (len(self) == len(other) and
        #            all(x == y for x, y in zip(self, other)))

        # Make sure order is respected when comparing to e.g. inverted
        # ranges.
        if isinstance(other, _RangeStep):
            return (len(self) == len(other) and
                    all(x == y for x, y in zip(self, other)))
        return super().__eq__(other)

    def __ne__(self, other):
        ## Sequences of different types are not equal to each other, but
        ## one can enable this if they want with this code.
        #if not isinstance(other, Set) and isinstance(other, Sequence):
        #    return (len(self) != len(other) or
        #            any(x != y for x, y in zip(self, other)))

        # Make sure order is respected when comparing to e.g. inverted
        # ranges.
        if isinstance(other, _RangeStep):
            return (len(self) != len(other) or
                    any(x != y for x, y in zip(self, other)))
        return super().__ne__(other)

    def count(self, value):
        return int(bool(value in self))

    def index(self, value, start=0, stop=None):
        if value not in self:
            raise ValueError("%r not in range %r" % (value, self))

        if start in [0, None] and (stop is None or stop >= len(self)):
            return bisect.bisect_left(self, value)
        else:
            real_start = slice(start, stop).indices(len(self))[0]
            return real_start + self[start:stop].index(value)

    @abc.abstractmethod
    def successor(self, value: object) -> object:
        """Get the value after a given one, e.g. value + 1"""
        raise NotImplementedError

    @abc.abstractmethod
    def predecessor(self, value: object) -> object:
        """Get the value before a given one, e.g. value - 1"""
        raise NotImplementedError

    @abc.abstractmethod
    def sortkey(self, value: object) -> object:
        """Get the sort value for a given value"""
        raise NotImplementedError


class RangeWrapper(RangeBase):

    """A wrapper of a range. This can be used to lazily parse a range to
    avoid an expensive parsing operation until the range is really needed.
    The real real range is in the wrapped property.
    """

    __slots__ = ('wrapped', )

    @property
    def range_type(self):
        return self.wrapped.range_type

    @property
    def value_type(self):
        return self.wrapped.value_type

    @property
    def ranges(self):
        return self.wrapped.ranges

    def __init__(self, wrapped: RangeBase):
        self.wrapped = wrapped

    def __contains__(self, value):
        return value in self.wrapped

    def __iter__(self):
        return iter(self.wrapped)

    def __reversed__(self):
        return reversed(self.wrapped)

    def __len__(self):
        return len(self.wrapped)

    def __getitem__(self, index):
        return self.wrapped[index]

    def successor(self, value: object) -> object:
        return self.wrapped.successor(value)

    def predecessor(self, value: object) -> object:
        return self.wrapped.predecessor(value)

    def sortkey(self, value: object) -> object:
        return self.wrapped.sortkey(value)

    def from_iterable(self, it: Iterable) -> RangeBase:
        return self.wrapped.from_iterable(it)

    def _from_iterable(self, it: Iterable) -> Set:
        return self.wrapped._from_iterable(it)

    def to_ordinal_range(self) -> 'RangeBase':
        return self.wrapped.to_ordinal_range()

    def to_character_range(self) -> 'RangeBase':
        return self.wrapped.to_character_range()

    def __eq__(self, other):
        return self.wrapped == other

    def __ne__(self, other):
        return self.wrapped != other

    def __le__(self, other):
        return self.wrapped <= other

    def __ge__(self, other):
        return self.wrapped >= other

    def isdisjoint(self, other):
        return self.wrapped.isdisjoint(other)

    def __or__(self, other):
        return self.wrapped | other

    def __ror__(self, other):
        return other | self.wrapped

    def __and__(self, other):
        return other & self.wrapped

    def __rand__(self, other):
        return self.wrapped & other

    def __sub__(self, other):
        return self.wrapped - other

    def __rsub__(self, other):
        return other - self.wrapped

    def __repr__(self):
        return "%s(%r)" % (type(self).__name__, self.wrapped)

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)


class LazyRangeWrapper(RangeWrapper):

    """A lazy range wrapper that uses a factory to reinitialize
    the range, for example for belated parsing."""

    __slots__ = ('factory', 'args', 'kwargs')

    def __init__(self, factory: Callable, *args, **kwargs):
        self.factory = factory
        self.args = args
        self.kwargs = kwargs

    def __getattr__(self, attr):
        if attr == 'wrapped':
            self.wrapped = self.factory(*self.args, **self.kwargs)
            del self.factory, self.args, self.kwargs
            if self.wrapped is None:
                # non-strict mode
                self.wrapped = EMPTY_RANGE
            return self.wrapped

        return super().__getattr__(attr)

        #raise AttributeError('%r object has no attribute %r'
        #                        % (type(self).__name__, attr))


class EmptyRange(RangeBase):

    """An empty range. This needs to be explicit, because of the way
    ranges are defined it is impossible to define the range as empty."""

    __slots__ = ()

    def __contains__(self, value):
        return False

    def __iter__(self):
        return iter(())

    def __reversed__(self):
        return iter(())

    def __len__(self):
        return 0

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self
        raise IndexError("empty ranges are empty")

    def successor(self, value: object) -> object:
        raise TypeError("empty ranges don't have values")

    def predecessor(self, value: object) -> object:
        raise TypeError("empty ranges don't have values")

    def sortkey(self, value: object) -> object:
        raise TypeError("empty ranges don't have values")

    @classmethod
    def _from_iterable(cls, it: Iterable) -> Set:
        return frozenset(it)

    def __eq__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, (Range, MultiRange)):
            return False
        if isinstance(other, EmptyRange):
            return True
        return super().__eq__(other)

    def __ne__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, (Range, MultiRange)):
            return True
        if isinstance(other, EmptyRange):
            return False
        return super().__ne__(other)

    def __le__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, (Range, MultiRange)):
            return True
        return super().__le__(other)

    def __ge__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, (Range, MultiRange)):
            return False
        return super().__ge__(other)

    def __repr__(self):
        return 'EMPTY_RANGE'

    def to_ordinal_range(self) -> 'RangeBase':
        return self

    def to_character_range(self) -> 'RangeBase':
        return self


EMPTY_RANGE = EmptyRange()


class Range(RangeBase):

    """A basic discrete range with start and end. The start and end are
    inclusive, unlike Python's range()."""

    __slots__ = ('start', 'end')

    def __init__(self, start: object, end: object):
        self.start = start
        self.end = end

        if start not in self:
            raise ValueError("not %r <= %r" % (start, end))

    @property
    def ranges(self) -> 'SequenceOf[Range]':
        """A sequence of self"""
        return (self, )

    @property
    def range_type(self):
        return type(self)

    def __repr__(self):
        return "%s(%r, %r)" % (type(self).__name__, self.start, self.end)

    def __eq__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            return self.start == other.start and self.end == other.end
        return super().__eq__(other)

    def __ne__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            return self.start != other.start or self.end != other.end
        return super().__ne__(other)

    def __le__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            return self.start in other and self.end in other
        return super().__le__(other)

    def __ge__(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            return other.start in self and other.end in self
        return super().__ge__(other)

    def isdisjoint(self, other):
        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            if self.start in other:
                return False
            if self.end in other:
                return False
            if other.start in self:
                return False
            if other.end in self:
                return False
            return True

        return super().isdisjoint(other)

    @classmethod
    def from_blocks(cls, it: IterableOf[tuple]) -> RangeBase:
        ranges = [cls(block[0], block[1]) for block in it]
        if not ranges:
            return EMPTY_RANGE
        elif len(ranges) == 1:
            return ranges[0]
        else:
            return MultiRange(ranges)

    @classmethod
    def from_iterable(cls, it: Iterable) -> RangeBase:
        """Create the range from an iterable. If non-contiguous,
        a MultiRange may be returned."""
        return NotImplemented

    @classmethod
    def _from_iterable(cls, it: Iterable) -> Set:
        """Create a set from an iterable. This either returns a range
        or a frozenset."""
        result = cls.from_iterable(it)
        if result is NotImplemented:
            return frozenset(it)
        return result

    @classmethod
    def fromstring(cls, s: AnyStr, lazy: bool=True,
                                   strict: bool=True) -> Optional[RangeBase]:
        """Create the range from the string returned by tostring().
        If non-contiguous, a MultiRange may be returned."""
        if lazy:
            if not strict and s is None:
                return None
            if not s:
                return EMPTY_RANGE
            return LazyRangeWrapper(cls.fromstring, s,
                                    lazy=False, strict=strict)
        if not strict:
            if s is None:
                return None
            try:
                cls.fromstring(s, lazy=False, strict=True)
            except ValueError:
                return None

        if not isinstance(s, str):
            s = s.decode('utf8')

        ranges = []
        for part in s.split():
            match = range_pattern.search(part)
            if match is None:
                raise ValueError(repr(part))

            start, end = match.groups()

            start = cls.value_type(start)
            if end is None:
                ranges.append(cls(start, start))
            else:
                end = cls.value_type(end)
                ranges.append(cls(start, end))

        if not ranges:
            return EMPTY_RANGE
        if len(ranges) == 1:
            return ranges[0]
        return MultiRange(ranges)

    def __and__(self, other):

        if isinstance(other, Range):
            start = end = None
            if self.start in other:
                start = self.start
                end = other.end
            elif other.start in self:
                start = other.start
                end = self.end

            if self.end in other:
                end = self.end
                if start is None:
                    start = other.start
            elif other.end in self:
                end = other.end
                if start is None:
                    start = self.start

            if start is None or end is None:
                return EMPTY_RANGE

            return type(self)(start, end)

        if isinstance(other, EmptyRange):
            return other

        if isinstance(other, MultiRange):
            return NotImplemented

        return super().__and__(other)

    __rand__ = __and__

    def __or__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            start = end = None
            if self.start in other:
                start = other.start
                end = self.end
            elif other.start in self:
                start = self.start
                end = other.end

            if self.end in other:
                end = other.end
                if start is None:
                    start = self.start
            elif other.end in self:
                end = self.end
                if start is None:
                    start = other.start

            if start is None or end is None:
                return MultiRange([self, other])

            return type(self)(start, end)

        if isinstance(other, EmptyRange):
            return self

        if isinstance(other, MultiRange):
            return NotImplemented

        return super().__or__(other)

    __ror__ = __or__

    def __sub__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            start = end = None
            if self.start in other:
                if other.end in self:
                    start = other.successor(other.end)
                    if start not in self:
                        return EMPTY_RANGE
                    return type(self)(start, self.end)

                else:
                    return EMPTY_RANGE

                start = other.start
                end = self.end

            elif self.end in other:
                if other.start in self:
                    end = other.predecessor(other.start)
                    if end not in self:
                        return EMPTY_RANGE
                    return type(self)(self.start, end)

            elif other.start in self:
                assert other.end in self

                p1 = other.predecessor(other.start)
                p2 = other.successor(other.end)

                assert p1 in self
                assert p2 in self

                return MultiRange([type(self)(self.start, p1),
                                   type(self)(p2, self.end)])

            else:
                assert other.end not in self
                return self

        if isinstance(other, EmptyRange):
            return self

        if isinstance(other, MultiRange):
            return NotImplemented

        return super().__sub__(other)

    def __rsub__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            return type(self).__sub__(other, self)

        if isinstance(other, MultiRange):
            return NotImplemented

        if isinstance(other, EmptyRange):
            return self

        return super().__rsub__(other)


class OrdinalRange(Range):

    """A range of numbers, where the successor and predecessor are computed
    with value + 1 and value - 1."""

    __slots__ = ()

    value_type = int

    def __contains__(self, value):
        try:
            return self.start <= value <= self.end and value == int(value)
        except (TypeError, ValueError):
            return False

    def __iter__(self):
        return iter(range(self.start, self.end + 1))

    def __reversed__(self):
        return iter(range(self.end, self.start - 1, -1))

    def __len__(self):
        return self.end - self.start + 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            result = range(self.start, self.end + 1)[index]

            if len(result) == len(self) and result.step == 1:
                assert result.start == self.start, (result, self)
                return self

            if result.step == 1:
                if result.start >= result.stop:
                    return EMPTY_RANGE
                return type(self)(result.start, result.stop - 1)
            else:
                return _RangeStep(self, 1, result)

            return result

        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("range index out of range")

        value = self.start + index
        if value <= self.end:
            return value
        raise IndexError("range index out of range")

    def index(self, value, start=0, stop=None):
        if start in [0, None] and (stop is None or stop >= len(self)):
            try:
                value_int = int(value)
                value_found = (self.start <= value <= self.end and
                               value == value_int)

            except (TypeError, ValueError):
                raise ValueError("%r not in range %r" % (value, self))

            if value_found:
                return value_int - self.start
            else:
                raise ValueError("%r not in range %r" % (value, self))
        else:
            real_start = slice(start, stop).indices(len(self))[0]
            return real_start + self[start:stop].index(value)

    def successor(self, value: numbers.Real) -> numbers.Real:
        return value + 1

    def predecessor(self, value: numbers.Real) -> numbers.Real:
        return value - 1

    def sortkey(self, value: numbers.Real) -> numbers.Real:
        return value

    @classmethod
    def from_fontconfig(cls, s: AnyStr, lazy: bool=True,
                             strict: bool=False) -> Optional[RangeBase]:
        """Create the range from fontconfig character range data.
        If non-contiguous (likely), a MultiRange may be returned."""
        if lazy:
            if not strict and s is None:
                return None
            if not s:
                return EMPTY_RANGE
            return LazyRangeWrapper(cls.from_fontconfig, s,
                                    lazy=False, strict=strict)
        if not strict:
            if s is None:
                return None

            try:
                cls.from_fontconfig(s, lazy=False, strict=True)
            except ValueError:
                return None

        if not isinstance(s, bytes):
            s = s.encode('ascii')

        ranges = []
        for part in s.split():
            start, sep, end = part.partition(b'-')
            start = int(start, 16)
            if not sep:
                ranges.append(cls(start, start))
            else:
                end = int(end, 16)
                ranges.append(cls(start, end))

        if not ranges:
            return EMPTY_RANGE
        if len(ranges) == 1:
            return ranges[0]
        return MultiRange(ranges)

    @classmethod
    def from_iterable(cls, it: IterableOf[numbers.Real]) -> RangeBase:
        """Create the range from an iterable. If non-contiguous,
        a MultiRange may be returned."""
        previous = rg = None
        ranges = []
        for value in sorted(it):
            if previous != value - 1:
                rg = cls(value, value)
                ranges.append(rg)
            elif value == previous + 1:
                rg.end = value
            previous = value

        if len(ranges) == 1:
            return ranges[0]
        elif not ranges:
            return EMPTY_RANGE
        else:
            return MultiRange(ranges)

    def to_ordinal_range(self) -> 'RangeBase':
        """Get the equivalent ordinal range."""
        return self

    def to_character_range(self) -> 'RangeBase':
        """Get the equivalent character range."""
        return CharacterRange(chr(self.start), chr(self.end))


class CharacterRange(Range):

    """A range of unicode characters, where the successor and predecessor are
    computed with codepoint + 1 and codepoint - 1."""

    __slots__ = ("start_ord", "end_ord")

    value_type = str

    def __init__(self, start: str, end: str, *args, **kwargs):
        self.start_ord = ord(start)
        self.end_ord = ord(end)
        super().__init__(start, end, *args, **kwargs)

    def __contains__(self, value):
        try:
            return self.start_ord <= ord(value) <= self.end_ord
        except TypeError:
            return False

    def __iter__(self):
        return map(chr, range(self.start_ord, self.end_ord + 1))

    def __reversed__(self):
        return map(chr, range(self.end_ord, self.start_ord - 1, -1))

    def __len__(self):
        return self.end_ord - self.start_ord + 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            length = len(self)
            start, stop, step = index.indices(length)
            if stop == length and start == 0 and step == 1:
                return self

            if step == 1:
                result = range(self.start_ord, self.end_ord + 1)[index]
                if result.start >= result.stop:
                    return EMPTY_RANGE
                return type(self)(chr(result.start), chr(result.stop - 1))
            else:
                #return [chr(x) for x in result]

                if step > 0:
                    rg = self[start:stop]

                else:
                    if stop >= start:
                        return EMPTY_RANGE

                    if step == -1:
                        tail_length = 0
                    else:
                        tail_length = (start - stop - 1) % -step

                    if tail_length != 0:
                        stop += tail_length

                    rg = self[stop + 1:start + 1]

                if not rg:
                    return rg

                return _RangeStep(rg, step)

            return result

        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("range index out of range")

        value = self.start_ord + index
        if value <= self.end_ord:
            return chr(value)
        raise IndexError("range index out of range")

    def index(self, value, start=0, stop=None):
        if start in [0, None] and (stop is None or stop >= len(self)):
            try:
                value_ord = ord(value)
            except TypeError:
                raise ValueError("%r not in range %r" % (value, self))

            if self.start_ord <= value_ord <= self.end_ord:
                return value_ord - self.start_ord
            else:
                raise ValueError("%r not in range %r" % (value, self))
        else:
            real_start = slice(start, stop).indices(len(self))[0]
            return real_start + self[start:stop].index(value)

    def successor(self, value: str) -> str:
        return chr(ord(value) + 1)

    def predecessor(self, value: str) -> str:
        return chr(ord(value) - 1)

    def sortkey(self, value: str) -> int:
        return ord(value)

    @classmethod
    def from_iterable(cls, it: IterableOf[str]) -> RangeBase:
        """Create the range from an iterable. If non-contiguous,
        a MultiRange may be returned."""
        previous = rg = None
        ranges = []
        for value in sorted(it):
            value_ord = ord(value)

            if previous != value_ord - 1:
                rg = cls(value, value)
                ranges.append(rg)
            elif value_ord == previous + 1:
                rg.end = value
                rg.end_ord = value_ord

            previous = value_ord

        if len(ranges) == 1:
            return ranges[0]
        elif not ranges:
            return EMPTY_RANGE
        else:
            return MultiRange(ranges)

    def to_ordinal_range(self) -> 'RangeBase':
        """Get the equivalent ordinal range."""
        return OrdinalRange(self.start_ord, self.end_ord)

    def to_character_range(self) -> 'RangeBase':
        """Get the equivalent character range."""
        return self


class MultiRange(RangeBase):

    """A non-contiguous discrete set of multiple discrete ranges. This supports
    the same operation as the Range() as is returned whenever an operation between
    them would produce a non-contiguous range."""

    __slots__ = ('ranges', 'starts', '_length', '_offsets')

    def __init__(self, ranges: IterableOf[RangeBase]=()):
        ranges = sorted(filter(None, ranges),
                        key=lambda rg: rg.sortkey(rg.start))
        new_ranges = []
        for rg in ranges:
            if new_ranges and rg.start in new_ranges[-1]:
                new_ranges[-1] |= new_ranges[-1] | rg
            else:
                new_ranges.append(rg)

        self.ranges = tuple(new_ranges)
        self.starts = tuple(rg.sortkey(rg.start) for rg in new_ranges)

        # Lenghts and offsets are only loaded on-demand.
        # The computation of either increases the font loading time from
        # 4.3 seconds to 4.8 seconds. Not a big deal, but loading the offsets
        # increases memory usage from 115 MiB + 157 MiB to 115 MiB + 197 MiB.
        # Since offsets are used for the sequence API which is rarely used,
        # skip that.
        self._length = None
        self._offsets = None

    @property
    def offsets(self) -> SequenceOf[int]:
        """A tuple with the offsets of each range"""
        result = self._offsets
        if result is None:

            def offsets():
                length = 0
                yield length
                for rg in self.ranges:
                    length += len(rg)
                    yield length

            self._offsets = result = tuple(offsets())

        return result

    @property
    def range_type(self):
        return type(self.ranges[0])

    @property
    def value_type(self):
        return self.range_type.value_type

    def __repr__(self):
        return "%s(%r)" % (type(self).__name__, self.ranges)

    def __contains__(self, value):
        ranges = self.ranges
        starts = self.starts

        if not ranges:
            return False

        try:
            value_key = ranges[0].sortkey(value)
            i = bisect.bisect(starts, value_key) - 1

        except (TypeError, ValueError):
            return False

        if 0 <= i < len(ranges):
            return value in ranges[i]

    def __iter__(self):
        for rg in self.ranges:
            yield from rg

    def __reversed__(self):
        for rg in reversed(self.ranges):
            yield from reversed(rg)

    def __len__(self):
        result = self._length
        if result is None:
            if self._offsets is not None:
                result = self._length = self._offsets[-1]
            else:
                result = self._length = sum(len(rg) for rg in self.ranges)
        return result

    def __getitem__(self, index):
        if isinstance(index, slice):
            length = len(self)
            start, stop, step = index.indices(length)
            if stop == length and start == 0 and step == 1:
                return self

            if step == 1:
                if start >= stop:
                    return EMPTY_RANGE

                result = []

                i = bisect.bisect_right(self.offsets, start) - 1
                j = bisect.bisect_left(self.offsets, stop)

                if 0 <= i < len(self.offsets):
                    offset = self.offsets[i]
                    start -= offset
                    stop -= offset

                for rg in self.ranges[i:j]:
                    sub_length = len(rg)

                    if start < sub_length:
                        rg = rg[start:stop]
                        if rg:
                            result.append(rg)
                        start = 0
                    else:
                        start -= sub_length

                    stop -= sub_length
                    if stop < 1:
                        break
                if not result:
                    return EMPTY_RANGE
                return MultiRange(result)

            else:
                #return list(self)[index]

                if step > 0:
                    rg = self[start:stop]

                else:

                    if stop >= start:
                        return EMPTY_RANGE

                    if step == -1:
                        tail_length = 0
                    else:
                        tail_length = (start - stop - 1) % -step

                    if tail_length != 0:
                        stop += tail_length

                    rg = self[stop + 1:start + 1]

                if not rg:
                    return rg

                return _RangeStep(rg, step)

            return result

        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("range index out of range")

        ranges = self.ranges
        if ranges:
            offsets = self.offsets

            i = bisect.bisect(offsets, index) - 1
            if 0 <= i < len(ranges):
                rg = ranges[i]
                index -= offsets[i]
                if index < len(rg):
                    return rg[index]

        ## Implementation without bisect
        #for rg in self.ranges:
        #    length = len(rg)
        #    if index < length:
        #        return rg[index]
        #    index -= length
        #    if index < 0:
        #        break

        raise IndexError("range index out of range")

    def index(self, value, start=0, stop=None):
        ranges = self.ranges

        if not ranges:
            raise ValueError("%r not in range %r" % (value, self))

        if start in [0, None] and (stop is None or stop >= len(self)):
            starts = self.starts

            try:
                value_key = ranges[0].sortkey(value)
                i = bisect.bisect(starts, value_key) - 1

            except (TypeError, ValueError):
                raise ValueError("%r not in range %r" % (value, self))

            if 0 <= i < len(ranges):
                return self.offsets[i] + ranges[i].index(value)

            raise ValueError("%r not in range %r" % (value, self))

        else:
            real_start = slice(start, stop).indices(len(self))[0]
            return real_start + self[start:stop].index(value)

    def successor(self, value: object) -> object:
        return self.ranges[0].successor(value)

    def predecessor(self, value: object) -> object:
        return self.ranges[0].predecessor(value)

    def sortkey(self, value: object) -> object:
        return self.ranges[0].sortkey(value)

    def _from_iterable(self, it: Iterable) -> Set:
        if not self.ranges:
            return frozenset(it)
        result = self.ranges[0].from_iterable(it)
        if result is NotImplemented:
            return frozenset(it)
        return result

    def __eq__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, MultiRange):
            return self.ranges == other.ranges
        if isinstance(other, Range):
            return self.ranges == [other]
        return super().__eq__(other)

    def __ne__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, MultiRange):
            return self.ranges != other.ranges
        if isinstance(other, Range):
            return self.ranges != [other]
        return super().__ne__(other)

    def __le__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped
        if isinstance(other, Range):
            #return bool(self - other)
            return self <= MultiRange([other])

        if isinstance(other, MultiRange):
            pile = list(reversed(self.ranges))
            antipile = list(reversed(other.ranges))

            while pile and antipile:

                first = pile[-1]
                antifirst = antipile[-1]

                if (first.sortkey(first.start) <
                    antifirst.sortkey(antifirst.start)):

                    return False

                elif (antifirst.sortkey(antifirst.end) <
                      first.sortkey(first.start)):

                    antipile.pop()

                elif first.isdisjoint(antifirst):


                    return False

                else:

                    if (first.sortkey(first.end) <=
                        antifirst.sortkey(antifirst.end)):

                        pile.pop()

                    else:
                        modified = first - antifirst
                        if not isinstance(modified, MultiRange):
                            pile[-1] = modified
                        else:
                            # This needs to return False
                            pile[-1:] = reversed(modified.ranges)

                        antipile.pop()

            return not pile

        return super().__le__(other)

    def __ge__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            return bool(other - self)

        if isinstance(other, MultiRange):
            return type(self).__le__(other, self)

        return super().__ge__(other)

    def isdisjoint(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            first = bisect.bisect(self.starts, other.sortkey(other.start)) - 1
            end = bisect.bisect(self.starts, other.sortkey(other.end)) - 1
            return all(rg.isdisjoint(other) for rg in self.ranges[first:end + 1])

        if isinstance(other, MultiRange):
            pile1 = list(reversed(self.ranges))
            pile2 = list(reversed(other.ranges))

            while pile1 and pile2:

                first1 = pile1[-1]
                first2 = pile2[-1]

                if first1.isdisjoint(first2):
                    if first1.sortkey(first1.end) < first2.sortkey(first2.start):
                        pile1.pop()
                    else:
                        assert (first2.sortkey(first2.end) <
                                first1.sortkey(first1.start))
                        pile2.pop()
                else:
                    return False

            return True

        return super().isdisjoint(other)

    def __or__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, MultiRange):
            return type(self)(chain(self.ranges, other.ranges))

        if isinstance(other, Range):
            return type(self)(chain(self.ranges, [other]))

        if isinstance(other, EmptyRange):
            return self

        return super().__or__(other)

    __ror__ = __or__

    def __and__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            first = bisect.bisect(self.starts, other.sortkey(other.start)) - 1
            end = bisect.bisect(self.starts, other.sortkey(other.end)) - 1
            return type(self)((rg & other) for rg in self.ranges[first:end + 1])

        if isinstance(other, MultiRange):
            pile1 = list(reversed(self.ranges))
            pile2 = list(reversed(other.ranges))

            new_ranges = []

            while pile1 and pile2:

                first1 = pile1[-1]
                first2 = pile2[-1]

                if first1.isdisjoint(first2):
                    if (first1.sortkey(first1.end) <
                        first2.sortkey(first2.start)):
                        pile1.pop()
                    else:
                        assert (first2.sortkey(first2.end) <
                                first1.sortkey(first1.start))
                        pile2.pop()
                else:
                    new_ranges.append(first1 & first2)
                    if (first1.sortkey(first1.end) <
                        first2.sortkey(first2.end)):
                        pile1.pop()
                    else:
                        pile2.pop()

            if not new_ranges:
                return EMPTY_RANGE
            if len(new_ranges) == 1:
                return new_ranges[0]
            return type(self)(new_ranges)

        if isinstance(other, EmptyRange):
            return other

        return super().__and__(other)

    __rand__ = __and__

    def __sub__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, Range):
            ##first = bisect.bisect(self.starts, other.sortkey(other.start)) - 1
            ###end = bisect.bisect(self.starts, other.sortkey(other.end)) - 1
            # TODO: Rewrite
            return type(self)(chain.from_iterable((rg - other).ranges
                                                  for rg in self.ranges))

        if isinstance(other, MultiRange):
            pile = list(reversed(self.ranges))
            antipile = list(reversed(other.ranges))

            new_ranges = []

            while pile and antipile:

                first = pile[-1]
                antifirst = antipile[-1]

                if first.isdisjoint(antifirst):
                    if (first.sortkey(first.end) <
                        antifirst.sortkey(antifirst.start)):

                        new_ranges.append(first)
                        pile.pop()

                    else:
                        assert (antifirst.sortkey(antifirst.end) <
                                first.sortkey(first.start))
                        antipile.pop()
                else:
                    if (first.sortkey(first.end) <=
                        antifirst.sortkey(antifirst.end)):

                        new_ranges.append(first - antifirst)
                        pile.pop()

                    else:
                        modified = first - antifirst
                        if not isinstance(modified, MultiRange):
                            pile[-1] = modified
                        else:
                            pile[-1:] = reversed(modified.ranges)
                        antipile.pop()

            if pile:
                new_ranges.extend(pile)

            return type(self)(new_ranges)

        if isinstance(other, EmptyRange):
            return self

        return super().__sub__(other)

    def __rsub__(self, other):

        if isinstance(other, RangeWrapper):
            other = other.wrapped

        if isinstance(other, MultiRange):
            return type(self).__sub__(other, self)

        if isinstance(other, Range):
            return type(self).__sub__(MultiRange([other]), self)

        if isinstance(other, EmptyRange):
            return self

        return super().__rsub__(other)

    def to_ordinal_range(self) -> 'RangeBase':
        """Get the equivalent ordinal range."""
        return MultiRange(rg.to_ordinal_range() for rg in self.ranges)

    def to_character_range(self) -> 'RangeBase':
        """Get the equivalent character range."""
        return MultiRange(rg.to_character_range() for rg in self.ranges)


_STEP_THRESH = 10

class _RangeStep(Set, Sequence):

    """Wraps a range sliced with a step, providing a proxy that skips
    to every nth element, or reversed the range if needed.

    The stepped range is initialized using the wrapped range, the step,
    optional sequence of elements (defaulting to the wrapped range), and
    an optional set or container for the value lookup (defaulting to
    the sequence of elements.

    Since the wrapped range is only used to provide some range-like APIs,
    it is not strictly needed, so you can remove it from the code if
    reusing this class in non-range context. You can also pass None,
    at the horror of the type checkers, and it will work.
    """

    def __init__(self, wrapped: RangeBase, step: int=1,
                       items: Sequence=None, lookup: Container=None):
        if items is None:
            items = wrapped
        if lookup is None:
            lookup = items
        self.wrapped = wrapped
        self.items = items
        self.lookup = lookup
        self.step = step

    def __repr__(self):
        return '%s(%r, %r, %r)' % (type(self).__name__,
                                   self.wrapped, self.step, self.items)

    @property
    def range_type(self):
        return self.wrapped.range_type

    @property
    def value_type(self):
        return self.wrapped.value_type

    @property
    def ranges(self) -> 'SequenceOf[_RangeStep]':
        """A sequence of self"""
        return (self, )

    def __contains__(self, value):
        step = self.step
        if value not in self.lookup:
            return False
        if step == 1 or step == -1:
            return True
        if self.items.index(value) % step != 0:
            return False
        return True

    def _iter(self, direction=1):
        items = self.items
        step = self.step * direction

        if step == 1:
            return iter(items)
        if step == -1:
            return reversed(items)

        length = len(items)
        if (length - 1) % step:
            length = 1 + ((length - 1) // abs(step)) * abs(step)

        if step > 0:
            if step > _STEP_THRESH:
                return (items[i] for i in range(0, length, step))
            else:
                return islice(items, 0, None, step)
        else:
            if step > _STEP_THRESH:
                return (items[i] for i in range(length - 1, -1, step))
            else:
                return islice(reversed(items), len(items) - length, None, -step)

    def __iter__(self):
        return self._iter(1)

    def __reversed__(self):
        return self._iter(-1)

    def __len__(self):
        length = len(self.items)
        step = abs(self.step)

        return length // step + (1 if length % step else 0)

    def __getitem__(self, index):
        if isinstance(index, slice):
            # We *could* just return an effecitve sequence here, with O(n)
            # __contains__, as nobody slicing a slice of a sequence would expect,
            # but for consistency, make it a proper set.
            items = tuple(self[i] for i in range(len(self))[index])
            return type(self)(self.wrapped, 1, items, frozenset(items))

        items = self.items
        step = self.step
        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("range slice index out of range")

        if step > 0:
            return items[index * step]

        else:
            index = len(items) + index * step - 1
            if index < 0:
                raise IndexError("range slice index out of range")
            return items[index]

    def successor(self, value: object) -> object:
        return self.wrapped.successor(value)

    def predecessor(self, value: object) -> object:
        return self.wrapped.predecessor(value)

    def sortkey(self, value: object) -> object:
        return self.wrapped.sortkey(value)

    def from_iterable(self, it: Iterable) -> RangeBase:
        return self.wrapped.from_iterable(it)

    def _from_iterable(self, it: Iterable) -> Set:
        # Here, returning something entirely different from a set performance-wise
        # *would* be surprising, since this is called on set operations. While
        # we are supporting those only just in case, as a fallback, having
        # O(n) lookup performance here would be not what the caller would expect,
        # so providing a set for the lookup is more essential, even if this
        # method in itself is not.
        items = tuple(it)
        return type(self)(self.wrapped, 1, items, frozenset(items))

    def to_ordinal_range(self) -> 'RangeBase':
        return OrdinalRange.from_iterable(self)

    def to_character_range(self) -> 'RangeBase':
        return CharacterRange.from_iterable(self)

    def __eq__(self, other):
        if isinstance(other, (_RangeStep, RangeBase)):
            return (len(self) == len(other) and
                    all(x == y for x, y in zip(self, other)))
        return super().__eq__(self, other)

    def __ne__(self, other):
        if isinstance(other, (_RangeStep, RangeBase)):
            return (len(self) == len(other) and
                    all(x == y for x, y in zip(self, other)))
        return super().__eq__(self, other)

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)
