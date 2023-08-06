from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtACls:
	"""ExtA commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: TriggerInstance, default value after init: TriggerInstance.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extA", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_triggerInstance_get', 'repcap_triggerInstance_set', repcap.TriggerInstance.Nr1)

	def repcap_triggerInstance_set(self, triggerInstance: repcap.TriggerInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TriggerInstance.Default
		Default value after init: TriggerInstance.Nr1"""
		self._cmd_group.set_repcap_enum_value(triggerInstance)

	def repcap_triggerInstance_get(self) -> repcap.TriggerInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import SourceCls
			self._source = SourceCls(self._core, self._cmd_group)
		return self._source

	def clone(self) -> 'ExtACls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ExtACls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
