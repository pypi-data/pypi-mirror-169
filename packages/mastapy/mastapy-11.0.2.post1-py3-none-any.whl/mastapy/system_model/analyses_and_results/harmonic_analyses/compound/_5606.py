'''_5606.py

AssemblyCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2179, _2218
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5414
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
    _5607, _5609, _5612, _5618,
    _5619, _5620, _5625, _5630,
    _5640, _5642, _5644, _5648,
    _5654, _5655, _5656, _5663,
    _5670, _5673, _5674, _5675,
    _5677, _5679, _5684, _5685,
    _5686, _5695, _5688, _5690,
    _5694, _5700, _5701, _5706,
    _5709, _5712, _5716, _5720,
    _5724, _5727, _5599
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'AssemblyCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundHarmonicAnalysis',)


class AssemblyCompoundHarmonicAnalysis(_5599.AbstractAssemblyCompoundHarmonicAnalysis):
    '''AssemblyCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundHarmonicAnalysis.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_5414.AssemblyHarmonicAnalysis]':
        '''List[AssemblyHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_5414.AssemblyHarmonicAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5607.BearingCompoundHarmonicAnalysis]':
        '''List[BearingCompoundHarmonicAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5607.BearingCompoundHarmonicAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5609.BeltDriveCompoundHarmonicAnalysis]':
        '''List[BeltDriveCompoundHarmonicAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5609.BeltDriveCompoundHarmonicAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5612.BevelDifferentialGearSetCompoundHarmonicAnalysis]':
        '''List[BevelDifferentialGearSetCompoundHarmonicAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5612.BevelDifferentialGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5618.BoltCompoundHarmonicAnalysis]':
        '''List[BoltCompoundHarmonicAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5618.BoltCompoundHarmonicAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5619.BoltedJointCompoundHarmonicAnalysis]':
        '''List[BoltedJointCompoundHarmonicAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5619.BoltedJointCompoundHarmonicAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5620.ClutchCompoundHarmonicAnalysis]':
        '''List[ClutchCompoundHarmonicAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5620.ClutchCompoundHarmonicAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5625.ConceptCouplingCompoundHarmonicAnalysis]':
        '''List[ConceptCouplingCompoundHarmonicAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5625.ConceptCouplingCompoundHarmonicAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5630.ConceptGearSetCompoundHarmonicAnalysis]':
        '''List[ConceptGearSetCompoundHarmonicAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5630.ConceptGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5640.CVTCompoundHarmonicAnalysis]':
        '''List[CVTCompoundHarmonicAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5640.CVTCompoundHarmonicAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_5642.CycloidalAssemblyCompoundHarmonicAnalysis]':
        '''List[CycloidalAssemblyCompoundHarmonicAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_5642.CycloidalAssemblyCompoundHarmonicAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_5644.CycloidalDiscCompoundHarmonicAnalysis]':
        '''List[CycloidalDiscCompoundHarmonicAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_5644.CycloidalDiscCompoundHarmonicAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5648.CylindricalGearSetCompoundHarmonicAnalysis]':
        '''List[CylindricalGearSetCompoundHarmonicAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5648.CylindricalGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5654.FaceGearSetCompoundHarmonicAnalysis]':
        '''List[FaceGearSetCompoundHarmonicAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5654.FaceGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_5655.FEPartCompoundHarmonicAnalysis]':
        '''List[FEPartCompoundHarmonicAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_5655.FEPartCompoundHarmonicAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5656.FlexiblePinAssemblyCompoundHarmonicAnalysis]':
        '''List[FlexiblePinAssemblyCompoundHarmonicAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5656.FlexiblePinAssemblyCompoundHarmonicAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5663.HypoidGearSetCompoundHarmonicAnalysis]':
        '''List[HypoidGearSetCompoundHarmonicAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5663.HypoidGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5670.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5670.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5673.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5673.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5674.MassDiscCompoundHarmonicAnalysis]':
        '''List[MassDiscCompoundHarmonicAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5674.MassDiscCompoundHarmonicAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5675.MeasurementComponentCompoundHarmonicAnalysis]':
        '''List[MeasurementComponentCompoundHarmonicAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5675.MeasurementComponentCompoundHarmonicAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5677.OilSealCompoundHarmonicAnalysis]':
        '''List[OilSealCompoundHarmonicAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5677.OilSealCompoundHarmonicAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5679.PartToPartShearCouplingCompoundHarmonicAnalysis]':
        '''List[PartToPartShearCouplingCompoundHarmonicAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5679.PartToPartShearCouplingCompoundHarmonicAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5684.PlanetCarrierCompoundHarmonicAnalysis]':
        '''List[PlanetCarrierCompoundHarmonicAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5684.PlanetCarrierCompoundHarmonicAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5685.PointLoadCompoundHarmonicAnalysis]':
        '''List[PointLoadCompoundHarmonicAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5685.PointLoadCompoundHarmonicAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5686.PowerLoadCompoundHarmonicAnalysis]':
        '''List[PowerLoadCompoundHarmonicAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5686.PowerLoadCompoundHarmonicAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5695.ShaftHubConnectionCompoundHarmonicAnalysis]':
        '''List[ShaftHubConnectionCompoundHarmonicAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5695.ShaftHubConnectionCompoundHarmonicAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_5688.RingPinsCompoundHarmonicAnalysis]':
        '''List[RingPinsCompoundHarmonicAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_5688.RingPinsCompoundHarmonicAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5690.RollingRingAssemblyCompoundHarmonicAnalysis]':
        '''List[RollingRingAssemblyCompoundHarmonicAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5690.RollingRingAssemblyCompoundHarmonicAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5694.ShaftCompoundHarmonicAnalysis]':
        '''List[ShaftCompoundHarmonicAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5694.ShaftCompoundHarmonicAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5700.SpiralBevelGearSetCompoundHarmonicAnalysis]':
        '''List[SpiralBevelGearSetCompoundHarmonicAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5700.SpiralBevelGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5701.SpringDamperCompoundHarmonicAnalysis]':
        '''List[SpringDamperCompoundHarmonicAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5701.SpringDamperCompoundHarmonicAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5706.StraightBevelDiffGearSetCompoundHarmonicAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundHarmonicAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5706.StraightBevelDiffGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5709.StraightBevelGearSetCompoundHarmonicAnalysis]':
        '''List[StraightBevelGearSetCompoundHarmonicAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5709.StraightBevelGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5712.SynchroniserCompoundHarmonicAnalysis]':
        '''List[SynchroniserCompoundHarmonicAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5712.SynchroniserCompoundHarmonicAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5716.TorqueConverterCompoundHarmonicAnalysis]':
        '''List[TorqueConverterCompoundHarmonicAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5716.TorqueConverterCompoundHarmonicAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5720.UnbalancedMassCompoundHarmonicAnalysis]':
        '''List[UnbalancedMassCompoundHarmonicAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5720.UnbalancedMassCompoundHarmonicAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5724.WormGearSetCompoundHarmonicAnalysis]':
        '''List[WormGearSetCompoundHarmonicAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5724.WormGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5727.ZerolBevelGearSetCompoundHarmonicAnalysis]':
        '''List[ZerolBevelGearSetCompoundHarmonicAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5727.ZerolBevelGearSetCompoundHarmonicAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5414.AssemblyHarmonicAnalysis]':
        '''List[AssemblyHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_5414.AssemblyHarmonicAnalysis))
        return value
