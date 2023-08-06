﻿'''_471.py

CylindricalGearToothFatigueFractureResultsN1457
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import _1627
from mastapy.gears.rating.cylindrical.iso6336 import _492, _489
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457 = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'CylindricalGearToothFatigueFractureResultsN1457')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearToothFatigueFractureResultsN1457',)


class CylindricalGearToothFatigueFractureResultsN1457(_0.APIBase):
    '''CylindricalGearToothFatigueFractureResultsN1457

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearToothFatigueFractureResultsN1457.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_fatigue_damage(self) -> 'float':
        '''float: 'MaximumFatigueDamage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumFatigueDamage

    @property
    def fatigue_damage_chart(self) -> '_1627.ThreeDChartDefinition':
        '''ThreeDChartDefinition: 'FatigueDamageChart' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1627.ThreeDChartDefinition)(self.wrapped.FatigueDamageChart) if self.wrapped.FatigueDamageChart is not None else None

    @property
    def critical_section(self) -> '_492.ToothFlankFractureAnalysisRowN1457':
        '''ToothFlankFractureAnalysisRowN1457: 'CriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_492.ToothFlankFractureAnalysisRowN1457)(self.wrapped.CriticalSection) if self.wrapped.CriticalSection is not None else None

    @property
    def mesh_contact_point_a_section(self) -> '_492.ToothFlankFractureAnalysisRowN1457':
        '''ToothFlankFractureAnalysisRowN1457: 'MeshContactPointASection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_492.ToothFlankFractureAnalysisRowN1457)(self.wrapped.MeshContactPointASection) if self.wrapped.MeshContactPointASection is not None else None

    @property
    def mesh_contact_point_ab_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointABSection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointABSection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_ab_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointABSection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointABSection.__class__)(self.wrapped.MeshContactPointABSection) if self.wrapped.MeshContactPointABSection is not None else None

    @property
    def mesh_contact_point_b_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointBSection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointBSection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_b_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointBSection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointBSection.__class__)(self.wrapped.MeshContactPointBSection) if self.wrapped.MeshContactPointBSection is not None else None

    @property
    def mesh_contact_point_c_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointCSection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointCSection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_c_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointCSection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointCSection.__class__)(self.wrapped.MeshContactPointCSection) if self.wrapped.MeshContactPointCSection is not None else None

    @property
    def mesh_contact_point_d_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDSection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointDSection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_d_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointDSection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointDSection.__class__)(self.wrapped.MeshContactPointDSection) if self.wrapped.MeshContactPointDSection is not None else None

    @property
    def mesh_contact_point_de_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDESection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointDESection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_de_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointDESection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointDESection.__class__)(self.wrapped.MeshContactPointDESection) if self.wrapped.MeshContactPointDESection is not None else None

    @property
    def mesh_contact_point_e_section(self) -> '_489.ToothFlankFractureAnalysisContactPointN1457':
        '''ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointESection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.ToothFlankFractureAnalysisContactPointN1457.TYPE not in self.wrapped.MeshContactPointESection.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_e_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(self.wrapped.MeshContactPointESection.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MeshContactPointESection.__class__)(self.wrapped.MeshContactPointESection) if self.wrapped.MeshContactPointESection is not None else None

    @property
    def analysis_rows(self) -> 'List[_492.ToothFlankFractureAnalysisRowN1457]':
        '''List[ToothFlankFractureAnalysisRowN1457]: 'AnalysisRows' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AnalysisRows, constructor.new(_492.ToothFlankFractureAnalysisRowN1457))
        return value

    @property
    def contact_points(self) -> 'List[_489.ToothFlankFractureAnalysisContactPointN1457]':
        '''List[ToothFlankFractureAnalysisContactPointN1457]: 'ContactPoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ContactPoints, constructor.new(_489.ToothFlankFractureAnalysisContactPointN1457))
        return value
