﻿'''_981.py

CylindricalGearPinionTypeCutterFlank
'''


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _980, _965
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearPinionTypeCutterFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPinionTypeCutterFlank',)


class CylindricalGearPinionTypeCutterFlank(_965.CylindricalGearAbstractRackFlank):
    '''CylindricalGearPinionTypeCutterFlank

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_PINION_TYPE_CUTTER_FLANK

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearPinionTypeCutterFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def residual_fillet_undercut(self) -> 'float':
        '''float: 'ResidualFilletUndercut' is the original name of this property.'''

        return self.wrapped.ResidualFilletUndercut

    @residual_fillet_undercut.setter
    def residual_fillet_undercut(self, value: 'float'):
        self.wrapped.ResidualFilletUndercut = float(value) if value else 0.0

    @property
    def cutter(self) -> '_980.CylindricalGearPinionTypeCutter':
        '''CylindricalGearPinionTypeCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_980.CylindricalGearPinionTypeCutter)(self.wrapped.Cutter) if self.wrapped.Cutter is not None else None
