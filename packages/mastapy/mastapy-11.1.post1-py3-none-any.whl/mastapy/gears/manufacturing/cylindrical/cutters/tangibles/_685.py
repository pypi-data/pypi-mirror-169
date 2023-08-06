﻿'''_685.py

CylindricalGearFormedWheelGrinderTangible
'''


from mastapy.gears.manufacturing.cylindrical.cutters import _668
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _684
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearFormedWheelGrinderTangible')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFormedWheelGrinderTangible',)


class CylindricalGearFormedWheelGrinderTangible(_684.CutterShapeDefinition):
    '''CylindricalGearFormedWheelGrinderTangible

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_FORMED_WHEEL_GRINDER_TANGIBLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearFormedWheelGrinderTangible.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> '_668.CylindricalGearFormGrindingWheel':
        '''CylindricalGearFormGrindingWheel: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_668.CylindricalGearFormGrindingWheel)(self.wrapped.Design) if self.wrapped.Design is not None else None
