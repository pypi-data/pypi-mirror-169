﻿'''_5472.py

AssemblyCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model import _2113, _2152
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5342
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _5473, _5475, _5478, _5484,
    _5485, _5486, _5491, _5496,
    _5506, _5508, _5510, _5514,
    _5520, _5521, _5522, _5529,
    _5536, _5539, _5540, _5541,
    _5543, _5545, _5550, _5551,
    _5552, _5561, _5554, _5556,
    _5560, _5566, _5567, _5572,
    _5575, _5578, _5582, _5586,
    _5590, _5593, _5465
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'AssemblyCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundHarmonicAnalysisOfSingleExcitation',)


class AssemblyCompoundHarmonicAnalysisOfSingleExcitation(_5465.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation):
    '''AssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2113.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2113.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2113.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5342.AssemblyHarmonicAnalysisOfSingleExcitation]':
        '''List[AssemblyHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5342.AssemblyHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bearings(self) -> 'List[_5473.BearingCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[BearingCompoundHarmonicAnalysisOfSingleExcitation]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5473.BearingCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def belt_drives(self) -> 'List[_5475.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[BeltDriveCompoundHarmonicAnalysisOfSingleExcitation]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5475.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5478.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5478.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bolts(self) -> 'List[_5484.BoltCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[BoltCompoundHarmonicAnalysisOfSingleExcitation]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5484.BoltCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def bolted_joints(self) -> 'List[_5485.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[BoltedJointCompoundHarmonicAnalysisOfSingleExcitation]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5485.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def clutches(self) -> 'List[_5486.ClutchCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ClutchCompoundHarmonicAnalysisOfSingleExcitation]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5486.ClutchCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def concept_couplings(self) -> 'List[_5491.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5491.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5496.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5496.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cv_ts(self) -> 'List[_5506.CVTCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[CVTCompoundHarmonicAnalysisOfSingleExcitation]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5506.CVTCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5508.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_5508.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5510.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_5510.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5514.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5514.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5520.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5520.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def fe_parts(self) -> 'List[_5521.FEPartCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[FEPartCompoundHarmonicAnalysisOfSingleExcitation]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5521.FEPartCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5522.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5522.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5529.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5529.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5536.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5536.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5539.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5539.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def mass_discs(self) -> 'List[_5540.MassDiscCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[MassDiscCompoundHarmonicAnalysisOfSingleExcitation]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5540.MassDiscCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def measurement_components(self) -> 'List[_5541.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5541.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def oil_seals(self) -> 'List[_5543.OilSealCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[OilSealCompoundHarmonicAnalysisOfSingleExcitation]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5543.OilSealCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5545.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5545.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def planet_carriers(self) -> 'List[_5550.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5550.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def point_loads(self) -> 'List[_5551.PointLoadCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[PointLoadCompoundHarmonicAnalysisOfSingleExcitation]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5551.PointLoadCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def power_loads(self) -> 'List[_5552.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[PowerLoadCompoundHarmonicAnalysisOfSingleExcitation]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5552.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5561.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5561.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def ring_pins(self) -> 'List[_5554.RingPinsCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[RingPinsCompoundHarmonicAnalysisOfSingleExcitation]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5554.RingPinsCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5556.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5556.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def shafts(self) -> 'List[_5560.ShaftCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ShaftCompoundHarmonicAnalysisOfSingleExcitation]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5560.ShaftCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5566.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5566.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def spring_dampers(self) -> 'List[_5567.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[SpringDamperCompoundHarmonicAnalysisOfSingleExcitation]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5567.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5572.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5572.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5575.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5575.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def synchronisers(self) -> 'List[_5578.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[SynchroniserCompoundHarmonicAnalysisOfSingleExcitation]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5578.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def torque_converters(self) -> 'List[_5582.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5582.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5586.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5586.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5590.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[WormGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5590.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5593.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]':
        '''List[ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5593.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5342.AssemblyHarmonicAnalysisOfSingleExcitation]':
        '''List[AssemblyHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5342.AssemblyHarmonicAnalysisOfSingleExcitation))
        return value
