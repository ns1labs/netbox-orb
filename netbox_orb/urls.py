from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # Agents
    path('agent/', views.AgentListView.as_view(), name='agent_list'),
    path('agent/add/', views.AgentEditView.as_view(), name='agent_add'),
    path('agent/<int:pk>/', views.AgentView.as_view(), name='agent'),
    path('agent/<int:pk>/edit/', views.AgentEditView.as_view(), name='agent_edit'),
    path('agent/<int:pk>/delete/', views.AgentDeleteView.as_view(), name='agent_delete'),
    path('agent/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='agent_changelog',  kwargs={
        'model': models.Agent
    }),
    # Agent Groups
    path('agent-group/', views.AgentGroupListView.as_view(), name='agentgroup_list'),
    path('agent-group/add/', views.AgentGroupEditView.as_view(), name='agentgroup_add'),
    path('agent-group/<int:pk>/', views.AgentGroupView.as_view(), name='agentgroup'),
    path('agent-group/<int:pk>/edit/', views.AgentGroupEditView.as_view(), name='agentgroup_edit'),
    path('agent-group/<int:pk>/delete/', views.AgentGroupDeleteView.as_view(), name='agentgroup_delete'),
    path('agent-group/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='agentgroup_changelog',  kwargs={
        'model': models.AgentGroup
    }),
    # Policy Cloud Probers
    path('policy-cloud-prober/', views.PolicyCloudProberListView.as_view(), name='policycloudprober_list'),
    path('policy-cloud-prober/add/', views.PolicyCloudProberEditView.as_view(), name='policycloudprober_add'),
    path('policy-cloud-prober/<int:pk>/', views.PolicyCloudProberView.as_view(), name='policycloudprober'),
    path('policy-cloud-prober/<int:pk>/edit/', views.PolicyCloudProberEditView.as_view(), name='policycloudprober_edit'),
    path('policy-cloud-prober/<int:pk>/delete/', views.PolicyCloudProberDeleteView.as_view(), name='policycloudprober_delete'),
    path('policy-cloud-prober/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='policycloudprober_changelog',  kwargs={
        'model': models.PolicyCloudProber
    }),
    # Sinks
    path('sink/', views.SinkListView.as_view(), name='sink_list'),
    path('sink/add/', views.SinkEditView.as_view(), name='sink_add'),
    path('sink/<int:pk>/', views.SinkView.as_view(), name='sink'),
    path('sink/<int:pk>/edit/', views.SinkEditView.as_view(), name='sink_edit'),
    path('sink/<int:pk>/delete/', views.SinkDeleteView.as_view(), name='sink_delete'),
    path('sink/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sink_changelog',  kwargs={
        'model': models.Sink
    }),
    # Datasets
    path('dataset/', views.DatasetListView.as_view(), name='dataset_list'),
    path('dataset/add/', views.DatasetEditView.as_view(), name='dataset_add'),
    path('dataset/<int:pk>/', views.DatasetView.as_view(), name='dataset'),
    path('dataset/<int:pk>/edit/', views.DatasetEditView.as_view(), name='dataset_edit'),
    path('dataset/<int:pk>/delete/', views.DatasetDeleteView.as_view(), name='dataset_delete'),
    path('dataset/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='dataset_changelog',  kwargs={
        'model': models.Dataset
    }),
)