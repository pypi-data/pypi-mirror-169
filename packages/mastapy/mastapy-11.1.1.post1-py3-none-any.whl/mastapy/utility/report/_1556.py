'''_1556.py

DynamicCustomReportItem
'''


from mastapy._internal import constructor
from mastapy.utility.report import (
    _1537, _1519, _1525, _1526,
    _1527, _1528, _1529, _1530,
    _1532, _1533, _1534, _1535,
    _1536, _1538, _1540, _1541,
    _1544, _1545, _1546, _1548,
    _1549, _1550, _1551, _1553,
    _1554
)
from mastapy.shafts import _20
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _990
from mastapy.utility_gui.charts import _1621, _1622
from mastapy.bearings.bearing_results import (
    _1703, _1704, _1707, _1715
)
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2587
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4120
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4448, _4452
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'DynamicCustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicCustomReportItem',)


class DynamicCustomReportItem(_1545.CustomReportNameableItem):
    '''DynamicCustomReportItem

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicCustomReportItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self) -> 'bool':
        '''bool: 'IsMainReportItem' is the original name of this property.'''

        return self.wrapped.IsMainReportItem

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value else False

    @property
    def inner_item(self) -> '_1537.CustomReportItem':
        '''CustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1537.CustomReportItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_shaft_damage_results_table_and_chart(self) -> '_20.ShaftDamageResultsTableAndChart':
        '''ShaftDamageResultsTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _20.ShaftDamageResultsTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftDamageResultsTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_cylindrical_gear_table_with_mg_charts(self) -> '_990.CylindricalGearTableWithMGCharts':
        '''CylindricalGearTableWithMGCharts: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _990.CylindricalGearTableWithMGCharts.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CylindricalGearTableWithMGCharts. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_ad_hoc_custom_table(self) -> '_1519.AdHocCustomTable':
        '''AdHocCustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1519.AdHocCustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to AdHocCustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_chart(self) -> '_1525.CustomChart':
        '''CustomChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1525.CustomChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_graphic(self) -> '_1526.CustomGraphic':
        '''CustomGraphic: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1526.CustomGraphic.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomGraphic. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_image(self) -> '_1527.CustomImage':
        '''CustomImage: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1527.CustomImage.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomImage. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report(self) -> '_1528.CustomReport':
        '''CustomReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1528.CustomReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_cad_drawing(self) -> '_1529.CustomReportCadDrawing':
        '''CustomReportCadDrawing: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1529.CustomReportCadDrawing.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportCadDrawing. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_chart(self) -> '_1530.CustomReportChart':
        '''CustomReportChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1530.CustomReportChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_column(self) -> '_1532.CustomReportColumn':
        '''CustomReportColumn: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1532.CustomReportColumn.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumn. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_columns(self) -> '_1533.CustomReportColumns':
        '''CustomReportColumns: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1533.CustomReportColumns.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumns. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_definition_item(self) -> '_1534.CustomReportDefinitionItem':
        '''CustomReportDefinitionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1534.CustomReportDefinitionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportDefinitionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_horizontal_line(self) -> '_1535.CustomReportHorizontalLine':
        '''CustomReportHorizontalLine: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1535.CustomReportHorizontalLine.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHorizontalLine. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_html_item(self) -> '_1536.CustomReportHtmlItem':
        '''CustomReportHtmlItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1536.CustomReportHtmlItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHtmlItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_item_container(self) -> '_1538.CustomReportItemContainer':
        '''CustomReportItemContainer: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1538.CustomReportItemContainer.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainer. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_base(self) -> '_1540.CustomReportItemContainerCollectionBase':
        '''CustomReportItemContainerCollectionBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1540.CustomReportItemContainerCollectionBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_item(self) -> '_1541.CustomReportItemContainerCollectionItem':
        '''CustomReportItemContainerCollectionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1541.CustomReportItemContainerCollectionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_multi_property_item_base(self) -> '_1544.CustomReportMultiPropertyItemBase':
        '''CustomReportMultiPropertyItemBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1544.CustomReportMultiPropertyItemBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportMultiPropertyItemBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_nameable_item(self) -> '_1545.CustomReportNameableItem':
        '''CustomReportNameableItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1545.CustomReportNameableItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNameableItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_named_item(self) -> '_1546.CustomReportNamedItem':
        '''CustomReportNamedItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1546.CustomReportNamedItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNamedItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_status_item(self) -> '_1548.CustomReportStatusItem':
        '''CustomReportStatusItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1548.CustomReportStatusItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportStatusItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_tab(self) -> '_1549.CustomReportTab':
        '''CustomReportTab: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1549.CustomReportTab.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTab. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_tabs(self) -> '_1550.CustomReportTabs':
        '''CustomReportTabs: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1550.CustomReportTabs.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTabs. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_report_text(self) -> '_1551.CustomReportText':
        '''CustomReportText: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1551.CustomReportText.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportText. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_sub_report(self) -> '_1553.CustomSubReport':
        '''CustomSubReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1553.CustomSubReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomSubReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_table(self) -> '_1554.CustomTable':
        '''CustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1554.CustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_dynamic_custom_report_item(self) -> 'DynamicCustomReportItem':
        '''DynamicCustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if DynamicCustomReportItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to DynamicCustomReportItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_line_chart(self) -> '_1621.CustomLineChart':
        '''CustomLineChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1621.CustomLineChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomLineChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_custom_table_and_chart(self) -> '_1622.CustomTableAndChart':
        '''CustomTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1622.CustomTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_loaded_ball_element_chart_reporter(self) -> '_1703.LoadedBallElementChartReporter':
        '''LoadedBallElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1703.LoadedBallElementChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBallElementChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_loaded_bearing_chart_reporter(self) -> '_1704.LoadedBearingChartReporter':
        '''LoadedBearingChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1704.LoadedBearingChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_loaded_bearing_temperature_chart(self) -> '_1707.LoadedBearingTemperatureChart':
        '''LoadedBearingTemperatureChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1707.LoadedBearingTemperatureChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingTemperatureChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_loaded_roller_element_chart_reporter(self) -> '_1715.LoadedRollerElementChartReporter':
        '''LoadedRollerElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1715.LoadedRollerElementChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedRollerElementChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_shaft_system_deflection_sections_report(self) -> '_2587.ShaftSystemDeflectionSectionsReport':
        '''ShaftSystemDeflectionSectionsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2587.ShaftSystemDeflectionSectionsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftSystemDeflectionSectionsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_parametric_study_histogram(self) -> '_4120.ParametricStudyHistogram':
        '''ParametricStudyHistogram: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4120.ParametricStudyHistogram.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ParametricStudyHistogram. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_campbell_diagram_report(self) -> '_4448.CampbellDiagramReport':
        '''CampbellDiagramReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4448.CampbellDiagramReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CampbellDiagramReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None

    @property
    def inner_item_of_type_per_mode_results_report(self) -> '_4452.PerModeResultsReport':
        '''PerModeResultsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4452.PerModeResultsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to PerModeResultsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new_override(self.wrapped.InnerItem.__class__)(self.wrapped.InnerItem) if self.wrapped.InnerItem is not None else None
