"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_cy_interface import AnimationCyInterface
from apysc._display.y_interface_base import YInterfaceBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_suffix_attr_interface import (
    VariableNameSuffixAttrInterface,
)
from apysc._validation import arg_validation_decos


class CyInterface(
    YInterfaceBase,
    VariableNameSuffixAttrInterface,
    AnimationCyInterface,
    RevertInterface,
    AttrLinkingInterface,
):
    @final
    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize _y attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_y"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="y")
        self._y = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_attr_linking_setting(self) -> None:
        """
        Append y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._y, attr_name="y")
        self._append_attr_to_linking_stack(attr=self._y, attr_name="y")

    @property
    @add_debug_info_setting(module_name=__name__)
    def y(self) -> Int:
        """
        Get a center y-coordinate.

        Returns
        -------
        y : Int
            Center y-coordinate.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> circle.y = ap.Int(120)
        >>> circle.y
        Int(120)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_y_if_not_initialized()
        y: ap.Int = value_util.get_copy(value=self._y)
        return y

    @y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def y(self, value: Int) -> None:
        """
        Update a center y-coordinate.

        Parameters
        ----------
        value : Int
            Center y-coordinate value.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa
        """
        self._y = value
        self._y._append_incremental_calc_substitution_expression()
        self._append_y_update_expression()

        self._append_y_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_y_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(value=self._y)
        expression: str = f"{self.variable_name}.cy({value_str});"
        ap.append_js_expression(expression=expression)

    @final
    def _update_y_and_skip_appending_exp(self, *, y: Union[int, Int]) -> None:
        """
        Update y-coordinate and skip appending an expression.

        Parameters
        ----------
        y : int or Int
            Y-coordinate value.
        """
        if isinstance(y, Int):
            y_: Int = y
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="y")
            y_ = Int(y, variable_name_suffix=suffix)
        self._y = y_

    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_y_snapshots",
            value=int(self._y._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._y._value = self._y_snapshots[snapshot_name]
