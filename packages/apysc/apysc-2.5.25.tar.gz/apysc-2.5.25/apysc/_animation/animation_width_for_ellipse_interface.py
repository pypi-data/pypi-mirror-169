"""Class implementation for the animation_width (for ellipse) interface.
"""

from typing import Union

from typing_extensions import final

from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.animation_width_for_ellipse import AnimationWidthForEllipse
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AnimationWidthForEllipseInterface(AnimationInterfaceBase):
    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.num_is_gt_zero(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_easing(arg_position_index=4)
    def animation_width(
        self,
        *,
        width: Union[int, Int],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR
    ) -> AnimationWidthForEllipse:
        """
        Set the ellipse-width animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        width : Int or int
            The final ellipse-width of the animation.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_width_for_ellipse : AnimationWidthForEllipse
            Created animation setting instance.

        References
        ----------
        - animation_width and animation_height interfaces
            - https://simon-ritchie.github.io/apysc/en/animation_width_and_height.html  # noqa
        - Animation interfaces duration setting
            - https://simon-ritchie.github.io/apysc/en/animation_duration.html
        - Animation interfaces delay setting
            - https://simon-ritchie.github.io/apysc/en/animation_delay.html
        - Each animation interface return value
            - https://simon-ritchie.github.io/apysc/en/animation_return_value.html  # noqa
        - Sequential animation setting
            - https://simon-ritchie.github.io/apysc/en/sequential_animation.html
        - animation_parallel interface
            - https://simon-ritchie.github.io/apysc/en/animation_parallel.html
        - Easing enum
            - https://simon-ritchie.github.io/apysc/en/easing_enum.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = ellipse.animation_width(
        ...     width=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_width_for_ellipse: AnimationWidthForEllipse = (
            AnimationWidthForEllipse(
                target=self, width=width, duration=duration, delay=delay, easing=easing
            )
        )
        return animation_width_for_ellipse
