
''' This module contains the url conf for the nemi search pages.
'''

from django.conf.urls import patterns, url
import views

urlpatterns = patterns("", 
        url(r'^general/$',
            views.GeneralSearchView.as_view(),
            name='methods-general'),
        url(r'^general_tsv/$',
            views.ExportGeneralSearchView.as_view(),
            {'export' : 'tsv'},
            name='methods-general_export_tsv'),
        url(r'^general_xls/$',
            views.ExportGeneralSearchView.as_view(),
            {'export' : 'xls'},
            name='methods-general_export_xls'),
        url(r'^method_summary/(?P<method_id>\d+)/$',
            views.MethodSummaryView.as_view(),
            name='methods-method_summary'),
        url(r'^method_analyte_export/(?P<method_id>\w+)/$',
            views.ExportMethodAnalyte.as_view(),
            name='methods-method_analyte_export'),
        url(r'^analyte/$', 
            views.AnalyteSearchView.as_view(),
            name='methods-analyte'),
        url(r'^analyte_tsv/$',
            views.ExportAnalyteSearchView.as_view(),
            {'export' : 'tsv'},
            name='methods-analyte_export_tsv'),
        url(r'^analyte_xls/$',
            views.ExportAnalyteSearchView.as_view(),
            {'export' : 'xls'},
            name='methods-analyte_export_xls'),
        url(r'^keyword/$',
            views.KeywordSearchView.as_view(),
            name='methods-keyword'),
        url(r'^microbiological/$',
            views.MicrobiologicalSearchView.as_view(),
            name='methods-microbiological'),
        url(r'^biological/$',
            views.BiologicalSearchView.as_view(),
            name='methods-biological'),
        url(r'^biological_method_summary/(?P<method_id>\d+)/$',
            views.BiologicalMethodSummaryView.as_view(),
            name='methods-biological_method_summary'),
        url(r'^toxicity/$',
            views.ToxicitySearchView.as_view(),
            name='methods-toxicity'),
        url(r'^toxicity_method_summary/(?P<method_id>\d+)/$',
            views.ToxicityMethodSummaryView.as_view(),
            name='methods-toxicity_method_summary'),
        url(r'^physical/$',
            views.PhysicalSearchView.as_view(),
            name='methods-physical'),
        url(r'^stream_physical/$',
            views.StreamPhysicalSearchView.as_view(),
            name='methods-stream_physical'),
        url(r'^stream_physical_method_summary/(?P<method_id>\d+)/$',
            views.StreamPhysicalMethodSummaryView.as_view(),
            name='methods-stream_physical_method_summary'),
        url(r'^regulatory/$', 
            views.RegulatorySearchView.as_view(),
            name='methods-regulatory'),
        url(r'^regulatory_tsv/$',
            views.ExportRegulatorySearchView.as_view(),
            {'export' : 'tsv'},
            name='methods-regulatory_export_tsv'),
        url(r'^regulatory_xls/$',
            views.ExportRegulatorySearchView.as_view(),
            {'export' : 'xls'},
            name='methods-regulatory_export_xls'),
        url(r'^tabular_regulatory/$',
            views.TabularRegulatorySearchView.as_view(),
            name='methods-tabular_reg'),
        url(r'^method_summary_reg/(?P<rev_id>\d+)/$',
            views.RegulatoryMethodSummaryView.as_view(),
            name='methods-method_summary_reg'),
        url(r'^browse_methods/$',
            views.BrowseMethodsView.as_view(),
            name='methods-browse'),
        url(r'^method_pdf/(?P<method_id>\d+)/$',
            views.MethodPdfView.as_view(),
            name='methods-pdf'),
                       
        ## Ajax urls which return json objects
        url(r'^analyte_select/$',
            views.AnalyteSelectView.as_view(),
            name='methods-analyte_select'),
        url(r'^method_count/$',
            views.MethodCountView.as_view(),
            name='methods-method_count'),
        url(r'^media_name/$',
            views.MediaNameView.as_view(),
            name='methods-media_name'),
        url(r'^method_source/$',
            views.SourceView.as_view(),
            name='methods-source'),
        url(r'^instrumentation/$',
            views.InstrumentationView.as_view(),
            name='methods-instrumentation'),
        url(r'^regulations/$',
            views.RegulationView.as_view(),
            name='methods-regulations'),
        url(r'^method_types/$',
            views.MethodTypeView.as_view(),
            name='methods-method_types'),
        url(r'^subcategories/$',
            views.SubcategoryView.as_view(),
            name='methods-subcategories'),
        url(r'^gear_types/$',
            views.GearTypeView.as_view(),
            name='methods-gear_types'),
        url(r'^stat_objectives/$',
            views.StatObjectiveView.as_view(),
            name='methods-stat_objectives'),
        url(r'^stat_item_types/$',
            views.StatItemTypeView.as_view(),
            name='methods-stat_item_types'),
        url(r'^stat_analysis_types/$',
            views.StatAnalysisTypeView.as_view(),
            name='methods-stat_analysis_types'),
        url(r'^stat_source_type/$',
            views.StatSourceTypeView.as_view(),
            name='methods-stat_publication_source'),
        url(r'^stat_media_emphasized/$',
            views.StatMediaNameView.as_view(),
            name='methods-stat_media_emphasized'),
        url(r'^stat_special_topics/$',
            views.StatSpecialTopicseView.as_view(),
            name='methods-stat_special_topics'),
        )
