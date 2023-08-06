'''_5790.py

HarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5407, _5460, _5461, _5462,
    _5463, _5464, _5465, _5466,
    _5467, _5468, _5469, _5470,
    _5480, _5482, _5483, _5485,
    _5514, _5530, _5555
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.analysis_cases import _7270
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'HarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisOfSingleExcitation',)


class HarmonicAnalysisOfSingleExcitation(_7270.StaticLoadAnalysisCase):
    '''HarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_detail(self) -> '_5407.AbstractPeriodicExcitationDetail':
        '''AbstractPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5407.AbstractPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to AbstractPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_periodic_excitation_detail(self) -> '_5460.ElectricMachinePeriodicExcitationDetail':
        '''ElectricMachinePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5460.ElectricMachinePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachinePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_force_periodic_excitation_detail(self) -> '_5461.ElectricMachineRotorXForcePeriodicExcitationDetail':
        '''ElectricMachineRotorXForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5461.ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> '_5462.ElectricMachineRotorXMomentPeriodicExcitationDetail':
        '''ElectricMachineRotorXMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5462.ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorXMomentPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_force_periodic_excitation_detail(self) -> '_5463.ElectricMachineRotorYForcePeriodicExcitationDetail':
        '''ElectricMachineRotorYForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5463.ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> '_5464.ElectricMachineRotorYMomentPeriodicExcitationDetail':
        '''ElectricMachineRotorYMomentPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5464.ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorYMomentPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_rotor_z_force_periodic_excitation_detail(self) -> '_5465.ElectricMachineRotorZForcePeriodicExcitationDetail':
        '''ElectricMachineRotorZForcePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5465.ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineRotorZForcePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_axial_loads_excitation_detail(self) -> '_5466.ElectricMachineStatorToothAxialLoadsExcitationDetail':
        '''ElectricMachineStatorToothAxialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5466.ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothAxialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_loads_excitation_detail(self) -> '_5467.ElectricMachineStatorToothLoadsExcitationDetail':
        '''ElectricMachineStatorToothLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5467.ElectricMachineStatorToothLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_radial_loads_excitation_detail(self) -> '_5468.ElectricMachineStatorToothRadialLoadsExcitationDetail':
        '''ElectricMachineStatorToothRadialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5468.ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothRadialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> '_5469.ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        '''ElectricMachineStatorToothTangentialLoadsExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5469.ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineStatorToothTangentialLoadsExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_electric_machine_torque_ripple_periodic_excitation_detail(self) -> '_5470.ElectricMachineTorqueRipplePeriodicExcitationDetail':
        '''ElectricMachineTorqueRipplePeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5470.ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to ElectricMachineTorqueRipplePeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_excitation_detail(self) -> '_5480.GearMeshExcitationDetail':
        '''GearMeshExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5480.GearMeshExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_misalignment_excitation_detail(self) -> '_5482.GearMeshMisalignmentExcitationDetail':
        '''GearMeshMisalignmentExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5482.GearMeshMisalignmentExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshMisalignmentExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_gear_mesh_te_excitation_detail(self) -> '_5483.GearMeshTEExcitationDetail':
        '''GearMeshTEExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5483.GearMeshTEExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GearMeshTEExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_general_periodic_excitation_detail(self) -> '_5485.GeneralPeriodicExcitationDetail':
        '''GeneralPeriodicExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5485.GeneralPeriodicExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to GeneralPeriodicExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_periodic_excitation_with_reference_shaft(self) -> '_5514.PeriodicExcitationWithReferenceShaft':
        '''PeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5514.PeriodicExcitationWithReferenceShaft.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to PeriodicExcitationWithReferenceShaft. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_single_node_periodic_excitation_with_reference_shaft(self) -> '_5530.SingleNodePeriodicExcitationWithReferenceShaft':
        '''SingleNodePeriodicExcitationWithReferenceShaft: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5530.SingleNodePeriodicExcitationWithReferenceShaft.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to SingleNodePeriodicExcitationWithReferenceShaft. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None

    @property
    def excitation_detail_of_type_unbalanced_mass_excitation_detail(self) -> '_5555.UnbalancedMassExcitationDetail':
        '''UnbalancedMassExcitationDetail: 'ExcitationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _5555.UnbalancedMassExcitationDetail.TYPE not in self.wrapped.ExcitationDetail.__class__.__mro__:
            raise CastException('Failed to cast excitation_detail to UnbalancedMassExcitationDetail. Expected: {}.'.format(self.wrapped.ExcitationDetail.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ExcitationDetail.__class__)(self.wrapped.ExcitationDetail) if self.wrapped.ExcitationDetail is not None else None
