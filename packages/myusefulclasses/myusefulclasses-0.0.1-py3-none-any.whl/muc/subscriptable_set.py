# This file is part of MyUsefulClasses.
# 
# MyUsefulClasses is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# MyUsefulClasses is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MyUsefulClasses. If not, see <http://www.gnu.org/licenses/>.
from functools import wraps
from collections.abc import Iterable


class SubscriptableSetException(Exception):

	def __init__(self):
		super().__init__()
		

class NotIndexableError(SubscriptableSetException):

	def __init__(self, obj):
		self.obj = obj
		
	def __str__(self):
		return "The item '%s' is not an integer or does not have an __index__ method."%str(obj)
		

class OperationError(SubscriptableSetException):

	def __init__(self, obj):
		self.obj = obj
		
	def __str__(self):
		return "The object '%s' of type '%s' can not be cast to SubscriptableSet."%(obj.__repr__(), obj.__class__.__name__)


class SubscriptableSet(set):
	"""This set can contains only integer values or objects which have an __index__ method. It is subscriptable: the subscription operator used with an integer value num will return that item 
	of the set whose value (if it's an integer) or whose value as returned by its __index__ method equals num.
	
	Raises:
		NotIndexableError: raised when one attempts to add to the set an object which is neither an integer nor returns an integer from its __index__ method.
	"""

	def __new__(cls, *args, **kwargs):
		obj = set.__new__(cls, *args, **kwargs)
		return obj

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for item in self:
			self._check_is_indexable(item)

	def _is_indexable(self, item) -> bool:
		if type(item) == int:
			return True
		index_method = getattr(item, "__index__", None)
		return callable(index_method)
		
	def _check_is_indexable(self, item):
		if not self._is_indexable(item):
			raise NotIndexableError(item)
			
	def __getitem__(self, index: int) -> object:
		"""Returns the item of the set whose index is ``index``, else None"""

		if type(index) != int:
			try:
				index = int(index)
			except TypeError:
				raise
		
		for item in self:
			if int(item) == index:
				return item
		return None
		
	def is_index_unique(self, item) -> bool:
		"""Returns True if there is not element in the set that has the same index value of ``item``."""

		#since we have already checked that item is indexable, we can just use it in __getitem__ and check that the returned value is different from None:
		return self.__getitem__(item) == None
	
	def add(self, new_item) -> bool:
		"""Adds a new item to the set. If the item is not indexable, it raises a NotIndexableException. If the item is indexable, but there is another item in the set with the same index value, 
		it does nothing and returns False. Otherwise, it successfully adds the item and returns True"""
		self._check_is_indexable(new_item)
		if not self.is_index_unique(new_item):
			return False
		super().add(new_item)
		return True
		
	def pop(self, index) -> object:
		"""Searchs an item in the set, either by itself or by its index. If no item is found, returns None and nothing happens; if it is found, it is removed from the set and returned by the 
		function."""
		item = self.__getitem__(index)

		#the method discard ensures us that if item == None (and therefore doesn't exist in the set) no modification will be applied and no error will be raised:
		self.discard(item)						

		return item

	
	def must_be_set(method):		
		@wraps(method)
		def check_is_set(_self, _other):
			if not isinstance(_other, set):
				raise TypeError(_other.__class__)
			return method(_self, _other)
		return check_is_set

	def cast_return(method):
		"""This decorator makes sure that, when an operation between the instance and another set is performed, the returned set is cast to SubscriptableSet.
		
		Raises:
			OperationError: raised if the other set can not be cast to a SubscriptableSet.
		"""
		
		@wraps(method)
		def cast_to_subscriptable_set(_self, _other):
			ret_set = method(_self, _other)
			try:
				return _self.__class__(ret_set)
			except NotIndexableError:
				raise OperationError(_other)
		
		return cast_to_subscriptable_set

	def cast_other(method):
		"""This decorator makes sure that, when an operation between the instance and another set is performed, the other set is cast to SubscriptableSet.
		
		Raises:
			OperationError: raised if the other set can not be cast to a SubscriptableSet.
		"""
		
		@wraps(method)
		def cast_to_subscriptable_set(_self, _other):
			if _other.__class__ != _self.__class__:
				try:
					_other = _self.__class__(_other)
				except NotIndexableError:
					raise OperationError(_other)
			ret_set = method(_self, _other)
			return ret_set
		
		return cast_to_subscriptable_set
			
	def raises_operation_error(method):
		@wraps(method)
		def raise_operation_error(_self, _other):
			try:
				return method(_self, _other)
			except NotIndexableError:
				raise OperationError(_other)
		
		return raise_operation_error

	@raises_operation_error
	def update(self, other: Iterable):
		for item in other:
			self.add(item)

	@raises_operation_error
	def union(self, other: Iterable):
		"""Similar to set.union, but the elements of other whose indexes are already in self will not be included."""
		new_set = SubscriptableSet()
		for item in self:
			new_set.add(item)
		for item in other:
			new_set.add(item)
		return new_set
	
	@cast_return
	@cast_other
	def __or__(self, other: set):
		if not isinstance(other, set):
			raise TypeError(other.__class__)
		return self.union(other)
	
	@cast_return
	@must_be_set
	@cast_other
	def __ror__(self, other):
		return self.union(other)
	
	def __ior__(self, other):
		return self.update(other)
	
	@cast_return
	@cast_other
	def simmetric_difference(self, other: Iterable):
		return super().simmetric_difference(other)
	
	def simmetric_difference_update(self, other: set):
		sim_diff = self.simmetric_difference(other)
		self.update(sim_diff)
		
	@cast_return
	@cast_other
	def __xor__(self, other: set):
		return self.simmetric_difference(other)
	
	@must_be_set
	def __ixor__(self, other):
		self.simmetric_difference_update(other)
	
	@cast_return
	@cast_other
	def __rxor__(self, other):
		return self.simmetric_difference(other)
	
	@cast_return
	def intersection(self, other: Iterable):
		"""Returns the intersection of two SubscriptableSets."""
	
		return {item for item in self if item in other}

	def intersection_update(self, other: Iterable):
	
		#intersection_update operation will eliminate any element which (or whose index) is in the self set
		super().intersection_update(other)
	
	@cast_return
	def __and__(self, other):
		return super().__and__(other)
	
	@cast_return
	def __rand__(self, other):
		return super().__rand__(other)
	
	@must_be_set
	def __iand__(self, other):
		self.intersection_update(other)
				
	@cast_return
	def __sub__(self, other):
		return super().__sub__(other)
	
	@cast_return
	def difference(self, other):
		return super().difference(other)
	
	def difference_update(self, other):
		for item in other:
			self.pop(item)
	
	
	@cast_return
	def __rsub__(self, other):
		return super().__rsub__(other)
	
	def __isub__(self, other):
		return super().__isub__(other)
	
	def clear(self):
		super().clear()
	
	def copy(self):
		new_set = SubscriptableSet()
		for item in self:
			new_set.add(item)
		return new_set

	@property
	def indexes(self):
		"""Returns the indexes of all the items in the set, sorted by increasing value"""
		indexes = [int(item) for item in self]
		indexes = sorted(indexes)
		return tuple(indexes)
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
