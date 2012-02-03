
''' This module contains the url conf for the nemi search pages.
'''

from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns("", 
        url(r'^general/$',
            views.GeneralSearchView.as_view(),
            name='search-general'),
        url(r'^general_tsv/$',
            views.ExportGeneralSearchView.as_view(),
            {'export' : 'tsv'},
            name='search-general_export_tsv'),
        url(r'^general_xls/$',
            views.ExportGeneralSearchView.as_view(),
            {'export' : 'xls'},
            name='search-general_export_xls'),
        url(r'^method_summary/(?P<method_id>\d+)/$',
            views.MethodSummaryView.as_view(),
            name='search-method_summary'),
        url(r'^method_analyte_export/(?P<method_id>\w+)/$',
            views.ExportMethodAnalyte.as_view(),
            name='search-method_analyte_export'),
        url(r'^analyte/$', 
            views.AnalyteSearchView.as_view(),
            name='search-analyte'),
        url(r'^analyte_tsv/$',
            views.ExportAnalyteSearchView.as_view(),
            {'export' : 'tsv'},
            name='search-analyte_export_tsv'),
        url(r'^analyte_xls/$',
            views.ExportAnalyteSearchView.as_view(),
            {'export' : 'xls'},
            name='search-analyte_export_xls'),
        url(r'^analyte_select/$',
            views.AnalyteSelectView.as_view(),
            name='search-analyte_select'),
        url(r'^keyword/$',
            views.KeywordSearchView.as_view(),
            name='search-keyword'),
        url(r'^microbiological/$',
            views.MicrobiologicalSearchView.as_view(),
            name='search-microbiological'),
        url(r'^biological/$',
            views.BiologicalSearchView.as_view(),
            name='search-biological'),
        url(r'^biological_method_summary/(?P<method_id>\d+)/$',
            views.BiologicalMethodSummaryView.as_view(),
            name='search-biological_method_summary'),
        url(r'^toxicity/$',
            views.ToxicitySearchView.as_view(),
            name='search-toxicity'),
        url(r'^toxicity_method_summary/(?P<method_id>\d+)/$',
            views.ToxicityMethodSummaryView.as_view(),
            name='search-toxicity_method_summary'),
        url(r'^physical/$',
            views.PhysicalSearchView.as_view(),
            name='search-physical'),
        url(r'^stream_physical/$',
            views.StreamPhysicalSearchView.as_view(),
            name='search-stream_physical'),
        url(r'^stream_physical_method_summayr/(?P<pk>\d+)/$',
            views.StreamPhysicalMethodSummaryView.as_view(),
            name='search-stream_physical_method_summary'),
        url(r'^statistic_search/$',
            views.StatisticSearchView.as_view(),
            name='search-statistics'),
        url(r'^statistical_search_summary/(?P<pk>\d+)/$',
            views.StatisticalSourceSummaryView.as_view(),
            name='search-statistical_source_summary'),
        url(r'^create_statistical_source/$',
            views.AddStatisticalSourceView.as_view(),
            name='search-create_statistical_source'),
        url(r'^statistical_search_detail/(?P<pk>\d+)/$',
            views.StatisticalSourceDetailView.as_view(),
            name='search-statistical_source_detail'),
        url(r'^update_statistical_source/(?P<pk>\d+)/$',
            views.UpdateStatisticalSourceView.as_view(),
            name='search-update_statistical_source')
        )
