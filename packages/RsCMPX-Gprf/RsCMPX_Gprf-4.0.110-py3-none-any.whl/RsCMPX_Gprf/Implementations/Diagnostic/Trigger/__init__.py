from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerCls:
	"""Trigger commands group definition. 17 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .NrMmw import NrMmwCls
			self._nrMmw = NrMmwCls(self._core, self._cmd_group)
		return self._nrMmw

	@property
	def wcdma(self):
		"""wcdma commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Wcdma import WcdmaCls
			self._wcdma = WcdmaCls(self._core, self._cmd_group)
		return self._wcdma

	@property
	def wlan(self):
		"""wlan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wlan'):
			from .Wlan import WlanCls
			self._wlan = WlanCls(self._core, self._cmd_group)
		return self._wlan

	@property
	def add(self):
		"""add commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_add'):
			from .Add import AddCls
			self._add = AddCls(self._core, self._cmd_group)
		return self._add

	def clone(self) -> 'TriggerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TriggerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
