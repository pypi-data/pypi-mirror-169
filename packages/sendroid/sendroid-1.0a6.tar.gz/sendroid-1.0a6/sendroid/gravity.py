
from    plyer      import gravity
from    .sensor     import Sensor
import  logging


class Gravity(Sensor):
    """
        Management class for gyroscope sensor.
    """
    NO_GRAVITY_VALUE = (.0, .0, .0)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def on_disable(self) -> None:
        gravity.disable()

    def on_enable(self) -> None:
        try:
            gravity.enable()
        except Exception as e:
            logging.error('Failed to enable the gravity on device: %s', e)
            return False
        else:
            logging.info('Enabled gravity on device.')
            return True

    def gravity(self) -> tuple:
        """
            Returns gravity sensor value.
        """
        try:
            x, y, z = gravity.gravity
            return (x, y, z)
        except Exception as e:
            logging.error('Error occured when tried to read gravity sensor data: %s', e)
            return self.NO_GRAVITY_VALUE

