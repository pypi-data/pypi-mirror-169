"""Class implementation for the animation_y interface
(using center-y coordinate internally).
"""

from typing import Union

from typing_extensions import final

from apysc._animation.animation_cy import AnimationCy
from apysc._animation.animation_interface_base import AnimationInterfaceBase
from apysc._animation.easing import Easing
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class AnimationCyInterface(AnimationInterfaceBase):
    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.num_is_gt_zero(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.is_easing(arg_position_index=4)
    def animation_y(
        self,
        *,
        y: Union[int, Int],
        duration: Union[int, Int] = 3000,
        delay: Union[int, Int] = 0,
        easing: Easing = Easing.LINEAR
    ) -> AnimationCy:
        """
        Set the center-y coordinate animation setting.

        Notes
        -----
        To start this animation, you need to call the `start` method of
        the returned instance.

        Parameters
        ----------
        y : Int or int
            Destination of the center-y coordinate.
        duration : Int or int, default 3000
            Milliseconds before an animation ends.
        delay : Int or int, default 0
            Milliseconds before an animation starts.
        easing : Easing, default Easing.LINEAR
            Easing setting.

        Returns
        -------
        animation_cy : AnimationCx
            Created animation setting instance.

        References
        ----------
        - animation_y interface
            - https://simon-ritchie.github.io/apysc/en/animation_y.html
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
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> _ = circle.animation_y(
        ...     y=100,
        ...     duration=1500,
        ...     easing=ap.Easing.EASE_OUT_QUINT,
        ... ).start()
        """
        animation_cy: AnimationCy = AnimationCy(
            target=self, y=y, duration=duration, delay=delay, easing=easing
        )
        return animation_cy
