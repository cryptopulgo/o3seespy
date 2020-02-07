from o3seespy.base_model import OpenSeesObject


class LayerBase(OpenSeesObject):
    op_base_type = "layer"


class Straight(LayerBase):
    """
    The Straight Layer Class
    
    The layer command is used to generate a number of fibers along a line or a circular arc.
    """
    op_type = 'straight'

    def __init__(self, osi, num_fiber, area_fiber, start, end):
        """
        Initial method for Straight

        Parameters
        ----------
        num_fiber: int
            Number of fibers along line
        area_fiber: float
            Area of each fiber
        start: listf
            Y & z-coordinates of first fiber in line (local coordinate system)
        end: listf
            Y & z-coordinates of last fiber in line (local coordinate system)
        """
        self.num_fiber = int(num_fiber)
        self.area_fiber = float(area_fiber)
        self.start = start
        self.end = end
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.num_fiber, self.area_fiber, *self.start, *self.end]
        self.to_process(osi)

class Circ(LayerBase):
    """
    The Circ Layer Class

    This command is used to construct a line of fibers along a circular arc
    """
    op_type = 'circ'

    def __init__(self, osi, num_fiber, area_fiber, center, radius, ang=None):
        """
        Initial method for Circ

        Parameters
        ----------
        num_fiber: int
            Number of fibers along line
        area_fiber: float
            Area of each fiber
        center: listf
            Y & z-coordinates of center of circular arc
        radius: float
            Radius of circlular arc
        ang: listf
            Starting and ending angle (optional) [0.0, 360.0-360/num_fibres]

        """
        self.num_fiber = int(num_fiber)
        self.area_fiber = float(area_fiber)
        self.center = center
        self.radius = float(radius)
        self.ang = ang
        osi.n_mat += 1
        self._tag = osi.n_mat
        self._parameters = [self.op_type, self._tag, self.num_fiber, self.area_fiber, *self.center, self.radius]
        if self.ang is not None:
            self._parameters += self.ang
        self.to_process(osi)
