from typing import Dict, List, Optional, Any, TYPE_CHECKING

from ..menu.list_manager import ListManager
from ..menu.menu import MenuSelectionType
from ..menu.text_input import TextInput
from ..menu import Menu
from ..models.subvolume import Subvolume
from ... import FormattedOutput

if TYPE_CHECKING:
	_: Any


class SubvolumeList(ListManager):
	def __init__(self, prompt: str, subvolumes: List[Subvolume]):
		self._actions = [
			str(_('Add subvolume')),
			str(_('Edit subvolume')),
			str(_('Delete subvolume'))
		]
		super().__init__(prompt, subvolumes, [self._actions[0]], self._actions[1:])

	def reformat(self, data: List[Subvolume]) -> Dict[str, Optional[Subvolume]]:
		table = FormattedOutput.as_table(data)
		rows = table.split('\n')

		# these are the header rows of the table and do not map to any User obviously
		# we're adding 2 spaces as prefix because the menu selector '> ' will be put before
		# the selectable rows so the header has to be aligned
		display_data: Dict[str, Optional[Subvolume]] = {f'  {rows[0]}': None, f'  {rows[1]}': None}

		for row, subvol in zip(rows[2:], data):
			row = row.replace('|', '\\|')
			display_data[row] = subvol

		return display_data

	def selected_action_display(self, subvolume: Subvolume) -> str:
		return subvolume.name

	def _prompt_options(self, editing: Optional[Subvolume] = None) -> List[str]:
		preset_options = []
		if editing:
			preset_options = editing.options

		choice = Menu(
			str(_("Select the desired subvolume options ")),
			['nodatacow','compress'],
			skip=True,
			preset_values=preset_options,
			multi=True
		).run()

		if choice.type_ == MenuSelectionType.Selection:
			return choice.value  # type: ignore

		return []

	def _add_subvolume(self, editing: Optional[Subvolume] = None) -> Optional[Subvolume]:
		name = TextInput(f'\n\n{_("Subvolume name")}: ', editing.name if editing else '').run()

		if not name:
			return None

		mountpoint = TextInput(f'\n{_("Subvolume mountpoint")}: ', editing.mountpoint if editing else '').run()

		if not mountpoint:
			return None

		options = self._prompt_options(editing)

		subvolume = Subvolume(name, mountpoint)
		subvolume.compress = 'compress' in options
		subvolume.nodatacow = 'nodatacow' in options

		return subvolume

	def handle_action(self, action: str, entry: Optional[Subvolume], data: List[Subvolume]) -> List[Subvolume]:
		if action == self._actions[0]:  # add
			new_subvolume = self._add_subvolume()

			if new_subvolume is not None:
				# in case a user with the same username as an existing user
				# was created we'll replace the existing one
				data = [d for d in data if d.name != new_subvolume.name]
				data += [new_subvolume]
		elif entry is not None:
			if action == self._actions[1]:  # edit subvolume
				new_subvolume = self._add_subvolume(entry)

				if new_subvolume is not None:
					# we'll remove the original subvolume and add the modified version
					data = [d for d in data if d.name != entry.name and d.name != new_subvolume.name]
					data += [new_subvolume]
			elif action == self._actions[2]:  # delete
				data = [d for d in data if d != entry]

		return data
