﻿'''_3640.py

AssemblyCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.stability_analyses import _3508
from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
    _3641, _3643, _3646, _3652,
    _3653, _3654, _3659, _3664,
    _3674, _3676, _3678, _3682,
    _3688, _3689, _3690, _3697,
    _3704, _3707, _3708, _3709,
    _3711, _3713, _3718, _3719,
    _3720, _3729, _3722, _3724,
    _3728, _3734, _3735, _3740,
    _3743, _3746, _3750, _3754,
    _3758, _3761, _3633
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundStabilityAnalysis',)


class AssemblyCompoundStabilityAnalysis(_3633.AbstractAssemblyCompoundStabilityAnalysis):
    '''AssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2179.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2179.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3508.AssemblyStabilityAnalysis]':
        '''List[AssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3508.AssemblyStabilityAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_3641.BearingCompoundStabilityAnalysis]':
        '''List[BearingCompoundStabilityAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3641.BearingCompoundStabilityAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_3643.BeltDriveCompoundStabilityAnalysis]':
        '''List[BeltDriveCompoundStabilityAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3643.BeltDriveCompoundStabilityAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3646.BevelDifferentialGearSetCompoundStabilityAnalysis]':
        '''List[BevelDifferentialGearSetCompoundStabilityAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3646.BevelDifferentialGearSetCompoundStabilityAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_3652.BoltCompoundStabilityAnalysis]':
        '''List[BoltCompoundStabilityAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3652.BoltCompoundStabilityAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_3653.BoltedJointCompoundStabilityAnalysis]':
        '''List[BoltedJointCompoundStabilityAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3653.BoltedJointCompoundStabilityAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_3654.ClutchCompoundStabilityAnalysis]':
        '''List[ClutchCompoundStabilityAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3654.ClutchCompoundStabilityAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_3659.ConceptCouplingCompoundStabilityAnalysis]':
        '''List[ConceptCouplingCompoundStabilityAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3659.ConceptCouplingCompoundStabilityAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3664.ConceptGearSetCompoundStabilityAnalysis]':
        '''List[ConceptGearSetCompoundStabilityAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3664.ConceptGearSetCompoundStabilityAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_3674.CVTCompoundStabilityAnalysis]':
        '''List[CVTCompoundStabilityAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3674.CVTCompoundStabilityAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_3676.CycloidalAssemblyCompoundStabilityAnalysis]':
        '''List[CycloidalAssemblyCompoundStabilityAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_3676.CycloidalAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_3678.CycloidalDiscCompoundStabilityAnalysis]':
        '''List[CycloidalDiscCompoundStabilityAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_3678.CycloidalDiscCompoundStabilityAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3682.CylindricalGearSetCompoundStabilityAnalysis]':
        '''List[CylindricalGearSetCompoundStabilityAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3682.CylindricalGearSetCompoundStabilityAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3688.FaceGearSetCompoundStabilityAnalysis]':
        '''List[FaceGearSetCompoundStabilityAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3688.FaceGearSetCompoundStabilityAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_3689.FEPartCompoundStabilityAnalysis]':
        '''List[FEPartCompoundStabilityAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_3689.FEPartCompoundStabilityAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3690.FlexiblePinAssemblyCompoundStabilityAnalysis]':
        '''List[FlexiblePinAssemblyCompoundStabilityAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3690.FlexiblePinAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3697.HypoidGearSetCompoundStabilityAnalysis]':
        '''List[HypoidGearSetCompoundStabilityAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3697.HypoidGearSetCompoundStabilityAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3704.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3704.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3707.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3707.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_3708.MassDiscCompoundStabilityAnalysis]':
        '''List[MassDiscCompoundStabilityAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3708.MassDiscCompoundStabilityAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_3709.MeasurementComponentCompoundStabilityAnalysis]':
        '''List[MeasurementComponentCompoundStabilityAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3709.MeasurementComponentCompoundStabilityAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_3711.OilSealCompoundStabilityAnalysis]':
        '''List[OilSealCompoundStabilityAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3711.OilSealCompoundStabilityAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3713.PartToPartShearCouplingCompoundStabilityAnalysis]':
        '''List[PartToPartShearCouplingCompoundStabilityAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3713.PartToPartShearCouplingCompoundStabilityAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_3718.PlanetCarrierCompoundStabilityAnalysis]':
        '''List[PlanetCarrierCompoundStabilityAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3718.PlanetCarrierCompoundStabilityAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_3719.PointLoadCompoundStabilityAnalysis]':
        '''List[PointLoadCompoundStabilityAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3719.PointLoadCompoundStabilityAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_3720.PowerLoadCompoundStabilityAnalysis]':
        '''List[PowerLoadCompoundStabilityAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3720.PowerLoadCompoundStabilityAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3729.ShaftHubConnectionCompoundStabilityAnalysis]':
        '''List[ShaftHubConnectionCompoundStabilityAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3729.ShaftHubConnectionCompoundStabilityAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_3722.RingPinsCompoundStabilityAnalysis]':
        '''List[RingPinsCompoundStabilityAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_3722.RingPinsCompoundStabilityAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3724.RollingRingAssemblyCompoundStabilityAnalysis]':
        '''List[RollingRingAssemblyCompoundStabilityAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3724.RollingRingAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_3728.ShaftCompoundStabilityAnalysis]':
        '''List[ShaftCompoundStabilityAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3728.ShaftCompoundStabilityAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3734.SpiralBevelGearSetCompoundStabilityAnalysis]':
        '''List[SpiralBevelGearSetCompoundStabilityAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3734.SpiralBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_3735.SpringDamperCompoundStabilityAnalysis]':
        '''List[SpringDamperCompoundStabilityAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3735.SpringDamperCompoundStabilityAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3740.StraightBevelDiffGearSetCompoundStabilityAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundStabilityAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3740.StraightBevelDiffGearSetCompoundStabilityAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3743.StraightBevelGearSetCompoundStabilityAnalysis]':
        '''List[StraightBevelGearSetCompoundStabilityAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3743.StraightBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_3746.SynchroniserCompoundStabilityAnalysis]':
        '''List[SynchroniserCompoundStabilityAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3746.SynchroniserCompoundStabilityAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_3750.TorqueConverterCompoundStabilityAnalysis]':
        '''List[TorqueConverterCompoundStabilityAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3750.TorqueConverterCompoundStabilityAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3754.UnbalancedMassCompoundStabilityAnalysis]':
        '''List[UnbalancedMassCompoundStabilityAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3754.UnbalancedMassCompoundStabilityAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3758.WormGearSetCompoundStabilityAnalysis]':
        '''List[WormGearSetCompoundStabilityAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3758.WormGearSetCompoundStabilityAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3761.ZerolBevelGearSetCompoundStabilityAnalysis]':
        '''List[ZerolBevelGearSetCompoundStabilityAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3761.ZerolBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3508.AssemblyStabilityAnalysis]':
        '''List[AssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3508.AssemblyStabilityAnalysis))
        return value
