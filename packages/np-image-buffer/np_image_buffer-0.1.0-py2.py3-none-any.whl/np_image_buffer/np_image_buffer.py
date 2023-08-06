from __future__ import annotations
from collections.abc import Sequence
import numpy as np

class ImageBuffer(Sequence):
    """ Manages an image circular buffer with a certain capacity and element type.
    Args:
        shape (tuple[int, int, int]):
            A 3-element tuple representing the shape of the circular buffer (Z, Y, X)
        dtype (np.dtype, optional):
            Desired type of buffer elements.
        allow_overwrite (bool, optional):
            If False, throw an IndexError when trying to append to an
            already full buffer.
            Default: True
    """
    __slots__ = [
        "__array",
        "__unwrap_buffer",
        "__unwrap_buffer_is_dirty",
        "__full_capacity",
        "__allow_overwrite",
        "__head",
        "__tail"
    ]
    
    def __init__(self, shape: tuple[int, int, int], dtype: np.dtype, allow_overwrite: bool = True) -> None:
        self.__array = np.zeros(shape=shape, dtype=dtype)
        self.__unwrap_buffer = np.zeros(shape=shape, dtype=dtype)
        self.__unwrap_buffer_is_dirty = False
        self.__full_capacity = self.__array.shape[0]
        self.__allow_overwrite = allow_overwrite
        self.__head = 0
        self.__tail = 0
    
    def clear(self) -> None:
        """Clears buffer, resetting indexes.
        """
        self.__head = 0
        self.__tail = 0
        self.__array.fill(0)
        self.__unwrap_buffer.fill(0)
    
    def put(self, value: np.ndarray) -> None:
        """Alias for compatibility with queue-style containers.
        """
        self.append(value)
    
    def append(self, value: np.ndarray) -> None:
        """Append an image to the buffer.
        """
        if self.full:
            if not self.__allow_overwrite:
                raise IndexError(
                    "Append to a full RingBuffer with overwrite disabled."
                )
            if self.__full_capacity == 0:
                return  # Mimick behavior of deque(maxlen=0)
            self.__tail += 1

        self.__unwrap_buffer_is_dirty = True
        self.__array[self.__head % self.__full_capacity] = value
        self.__head += 1
        self._fix_indices()

    def appendleft(self, value) -> None:
        """Append an image to the buffer's tail.
        """
        if self.full:
            if not self.__allow_overwrite:
                raise IndexError(
                    "Append to a full RingBuffer with overwrite disabled."
                )
            if self.__full_capacity == 0:
                return  # Mimick behavior of deque(maxlen=0)
            self.__head -= 1

        self.__unwrap_buffer_is_dirty = True
        self.__tail -= 1
        self._fix_indices()
        self.__array[self.__tail] = value

    # --------------------------------------------------------------------------
    #   extend
    # --------------------------------------------------------------------------

    def extend(self, values: np.ndarray) -> None:
        """Extend the buffer with a list of images.
        """
        lv = len(values)
        if len(self) + lv > self.__full_capacity:
            if not self.__allow_overwrite:
                raise IndexError(
                    "RingBuffer overflows, because overwrite is disabled."
                )
            if self.__full_capacity == 0:
                return  # Mimick behavior of deque(maxlen=0)

        self.__unwrap_buffer_is_dirty = True
        if lv >= self.__full_capacity:
            self.__array[...] = values[-self.__full_capacity :]
            self.__head = self.__full_capacity
            self.__tail = 0
            return

        ri = self.__head % self.__full_capacity
        sl1 = np.s_[ri : min(ri + lv, self.__full_capacity)]
        sl2 = np.s_[: max(ri + lv - self.__full_capacity, 0)]
        # fmt: off
        self.__array[sl1] = values[: sl1.stop - sl1.start]  # pylint: disable=no-member
        self.__array[sl2] = values[sl1.stop - sl1.start :]  # pylint: disable=no-member
        # fmt: on
        self.__head += lv
        self.__tail = max(self.__tail, self.__head - self.__full_capacity)
        self._fix_indices()

    def extendleft(self, values) -> None:
        """Extend the ring buffer with a list of values from the left side.
        """
        lv = len(values)
        if len(self) + lv > self.__full_capacity:
            if not self.__allow_overwrite:
                raise IndexError(
                    "RingBuffer overflows, because overwrite is disabled."
                )
            if self.__full_capacity == 0:
                return  # Mimick behavior of deque(maxlen=0)

        self.__unwrap_buffer_is_dirty = True
        if lv >= self.__full_capacity:
            self.__array[...] = values[: self.__full_capacity]
            self.__head = self.__full_capacity
            self.__tail = 0
            return

        self.__tail -= lv
        self._fix_indices()
        li = self.__tail
        sl1 = np.s_[li : min(li + lv, self.__full_capacity)]
        sl2 = np.s_[: max(li + lv - self.__full_capacity, 0)]
        # fmt: off
        self.__array[sl1] = values[:sl1.stop - sl1.start]  # pylint: disable=no-member
        self.__array[sl2] = values[sl1.stop - sl1.start:]  # pylint: disable=no-member
        # fmt: on
        self.__head = min(self.__head, self.__tail + self.__full_capacity)

    # --------------------------------------------------------------------------
    #   pop
    # --------------------------------------------------------------------------

    def pop(self):
        if len(self) == 0:
            raise IndexError("Pop from an empty RingBuffer.")
        self.__unwrap_buffer_is_dirty = True
        self.__head -= 1
        self._fix_indices()
        return self.__array[self.__head % self.__full_capacity]

    def popleft(self):
        if len(self) == 0:
            raise IndexError("Pop from an empty RingBuffer.")
        self.__unwrap_buffer_is_dirty = True
        res = self.__array[self.__tail]
        self.__tail += 1
        self._fix_indices()
        return res

    # --------------------------------------------------------------------------
    #   Properties
    # --------------------------------------------------------------------------

    @property
    def full(self) -> bool:
        return len(self) == self.__full_capacity

    @property
    def unwrap_address(self) -> int:
        """Get the fixed memory address of the internal unwrap buffer, used when
        the ring buffer is completely full.
        """
        return self.__unwrap_buffer[:].__array_interface__["data"][0]

    @property
    def current_address(self) -> int:
        """Get the current memory address of the array behind the buffer.
        """
        return self[:].__array_interface__["data"][0]

    @property
    def dtype(self) -> np.dtype:
        return self.__array.dtype

    @property
    def shape(self) -> tuple[int, int, int]:
        return self.__array.shape

    @property
    def maxlen(self) -> int:
        return self.__full_capacity

    # --------------------------------------------------------------------------
    #   _unwrap
    # --------------------------------------------------------------------------

    def _unwrap(self) -> np.ndarray:
        """Copy the data from this buffer into unwrapped form.
        """
        return np.concatenate(
            (
                self.__array[self.__tail : min(self.__head, self.__full_capacity)],
                self.__array[: max(self.__head - self.__full_capacity, 0)],
            )
        )

    # --------------------------------------------------------------------------
    #   _unwrap_into_buffer
    # --------------------------------------------------------------------------

    def _unwrap_into_buffer(self) -> np.ndarray:
        """Copy the data from this buffer into unwrapped form to the unwrap
        buffer at a fixed memory address. Only call when the buffer is full.
        """
        if self.__unwrap_buffer_is_dirty:
            # print("Unwrap buffer was dirty")
            np.concatenate(
                (
                    self.__array[self.__tail : min(self.__head, self.__full_capacity)],
                    self.__array[: max(self.__head - self.__full_capacity, 0)],
                ),
                out=self.__unwrap_buffer,
            )
            self.__unwrap_buffer_is_dirty = False
        else:
            # print("Unwrap buffer was clean")
            pass

    # --------------------------------------------------------------------------
    #   _fix_indices
    # --------------------------------------------------------------------------

    def _fix_indices(self):
        """Enforce our invariant that 0 <= self.__tail < self.__full_capacity.
        """
        if self.__tail >= self.__full_capacity:
            self.__tail -= self.__full_capacity
            self.__head -= self.__full_capacity
        elif self.__tail < 0:
            self.__tail += self.__full_capacity
            self.__head += self.__full_capacity

    # --------------------------------------------------------------------------
    #   Dunder methods
    # --------------------------------------------------------------------------

    def __array__(self):
        """Numpy compatibility
        """
        # print("__array__")
        if self.full:
            self._unwrap_into_buffer()
            return self.__unwrap_buffer
        else:
            return self._unwrap()

    def __len__(self):
        return self.__head - self.__tail

    def __getitem__(self, item):

        # --------------------------
        #   ringbuffer[slice]
        #   ringbuffer[tuple]
        #   ringbuffer[None]
        # --------------------------

        if isinstance(item, (slice, tuple)) or item is None:
            if self.full:
                # print("  --> __unwrap_buffer[item]")
                self._unwrap_into_buffer()
                return self.__unwrap_buffer[item]

            # print("  --> _unwrap()[item]")
            return self._unwrap()[item]

        # ----------------------------------
        #   ringbuffer[int]
        #   ringbuffer[list of ints]
        #   ringbuffer[np.ndarray of ints]
        # ----------------------------------
        item_arr = np.asarray(item)

        if not issubclass(item_arr.dtype.type, np.integer):
            raise TypeError("RingBuffer indices must be integers.")

        if len(self) == 0:
            raise IndexError(
                "RingBuffer list index out of range. The RingBuffer has "
                "length 0."
            )

        if not hasattr(item, "__len__"):
            # Single element: We can speed up the code
            # Check for `List index out of range`
            if item_arr < -len(self) or item_arr >= len(self):
                raise IndexError(
                    "RingBuffer list index %s out of range. The RingBuffer "
                    "has length %s." % (item_arr, len(self))
                )

            if item_arr < 0:
                item_arr = (self.__head + item_arr) % self.__full_capacity
            else:
                item_arr = (item_arr + self.__tail) % self.__full_capacity

        else:
            # Multiple elements
            # Check for `List index out of range`
            if np.any(item_arr < -len(self)) or np.any(item_arr >= len(self)):
                idx_under = item_arr[np.where(item_arr < -len(self))]
                idx_over = item_arr[np.where(item_arr >= len(self))]
                idx_oor = np.sort(np.concatenate((idx_under, idx_over)))
                raise IndexError(
                    "RingBuffer list indices %s out of range. The RingBuffer "
                    "has length %s." % (idx_oor, len(self))
                )
            idx_neg = np.where(item_arr < 0)
            idx_pos = np.where(item_arr >= 0)

            if len(idx_neg) > 0:
                item_arr[idx_neg] = (self.__head + item_arr[idx_neg]) % self.__full_capacity
            if len(idx_pos) > 0:
                item_arr[idx_pos] = (item_arr[idx_pos] + self.__tail) % self.__full_capacity

        # print("  --> __array[item_arr]")
        return self.__array[item_arr]

    def __iter__(self):
        # print("__iter__")
        if self.full:
            self._unwrap_into_buffer()
            return iter(self.__unwrap_buffer)
        else:
            return iter(self._unwrap())

    def __repr__(self):
        return "<RingBuffer of {!r}>".format(np.asarray(self))