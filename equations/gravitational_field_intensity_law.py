from scipy.constants import G

from ..drivers.axes import Axes
from ..drivers.equation import Equation
from ..utils import distance


class GravitationalFieldIntensityLaw:
    
    def __init__(self, field):

        self.field = field
        self.axes = Axes(self.field.dimensions)

    def _equation(self, point):

        foo = 0.0

        # equation to solve is g_t + G*Sum_i m_i/d_i**2  = 0
        
        for body in self.field.bodies:
                
            dist = distance(body.position.value, point)
            foo += G*body.mass.value/dist**2

        foo += body.gravitational_field_intensity.value
        
        return Equation(foo)
    
    def solve(self, point, unknown):

        equation = self._equation(point)

        return equation.solve(unknown)