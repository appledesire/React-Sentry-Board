"""
    This list is tracking old api endpoints that don't correctly implement pagination.
    The goal is to eventually add pagination for all and shrink this list.
    DO NOT ADD ANY NEW APIS
"""
SENTRY_API_PAGINATION_ALLOWLIST_DO_NOT_MODIFY = {
    "ApiTokensEndpoint",
    "AssistantEndpoint",
    "AuthenticatorIndexEndpoint",
    "BitbucketSearchEndpoint",
    "BroadcastIndexEndpoint",
    "BuiltinSymbolSourcesEndpoint",
    "DiscoverSavedQueriesEndpoint",
    "GithubSharedSearchEndpoint",
    "GitlabIssueSearchEndpoint",
    "GroupEventsEndpoint",
    "GroupIntegrationsEndpoint",
    "GroupParticipantsEndpoint",
    "GroupSimilarIssuesEmbeddingsEndpoint",
    "GroupStatsEndpoint",
    "GroupTagsEndpoint",
    "GroupingConfigsEndpoint",
    "IntegrationFeaturesEndpoint",
    "InternalQueueTasksEndpoint",
    "InternalStatsEndpoint",
    "JiraSearchEndpoint",
    "JiraServerSearchEndpoint",
    "KeyTransactionEndpoint",
    "OrgAuthTokensEndpoint",
    "OrganizationAccessRequestDetailsEndpoint",
    "OrganizationAlertRuleAvailableActionIndexEndpoint",
    "OrganizationApiKeyIndexEndpoint",
    "OrganizationAuthProvidersEndpoint",
    "OrganizationDeriveCodeMappingsEndpoint",
    "OrganizationEnvironmentsEndpoint",
    "OrganizationEventsFacetsEndpoint",
    "OrganizationEventsNewTrendsStatsEndpoint",
    "OrganizationEventsRelatedIssuesEndpoint",
    "OrganizationEventsRootCauseAnalysisEndpoint",
    "OrganizationEventsSpansHistogramEndpoint",
    "OrganizationEventsVitalsEndpoint",
    "OrganizationGroupIndexEndpoint",
    "OrganizationGroupIndexStatsEndpoint",
    "OrganizationIndexEndpoint",
    "OrganizationIntegrationServerlessFunctionsEndpoint",
    "OrganizationIssuesCountEndpoint",
    "OrganizationIssuesResolvedInReleaseEndpoint",
    "OrganizationMetricsDetailsEndpoint",
    "OrganizationMetricsTagDetailsEndpoint",
    "OrganizationMetricsTagsEndpoint",
    "OrganizationMissingMembersEndpoint",
    "OrganizationMonitorScheduleSampleDataEndpoint",
    "OrganizationMonitorStatsEndpoint",
    "OrganizationPluginsConfigsEndpoint",
    "OrganizationPluginsEndpoint",
    "OrganizationProcessingIssuesEndpoint",
    "OrganizationProfilingFiltersEndpoint",
    "OrganizationProjectsEndpoint",
    "OrganizationRecentSearchesEndpoint",
    "OrganizationRelayUsage",
    "OrganizationReleasesEndpoint",
    "OrganizationRepositoriesEndpoint",
    "OrganizationSdkUpdatesEndpoint",
    "OrganizationSearchesEndpoint",
    "OrganizationSentryFunctionEndpoint",
    "OrganizationStatsEndpoint",
    "OrganizationTagsEndpoint",
    "OrganizationUserDetailsEndpoint",
    "OrganizationUserReportsEndpoint",
    "OrganizationUserTeamsEndpoint",
    "OrganizationUsersEndpoint",
    "PluginGroupEndpoint",
    "ProjectAgnosticRuleConditionsEndpoint",
    "ProjectArtifactLookupEndpoint",
    "ProjectCodeOwnersEndpoint",
    "ProjectEnvironmentsEndpoint",
    "ProjectFiltersEndpoint",
    "ProjectGroupIndexEndpoint",
    "ProjectGroupingConfigsEndpoint",
    "ProjectIssuesResolvedInReleaseEndpoint",
    "ProjectMemberIndexEndpoint",
    "ProjectMonitorStatsEndpoint",
    "ProjectPlatformsEndpoint",
    "ProjectPluginsEndpoint",
    "ProjectReleaseSetupCompletionEndpoint",
    "ProjectRuleStatsIndexEndpoint",
    "ProjectServiceHookStatsEndpoint",
    "ProjectStatsEndpoint",
    "ProjectSymbolSourcesEndpoint",
    "ProjectTagsEndpoint",
    "ProjectUserStatsEndpoint",
    "ProjectUsersEndpoint",
    "ReleaseThresholdEndpoint",
    "SentryAppRequestsEndpoint",
    "SentryAppsStatsEndpoint",
    "SentryInternalAppTokensEndpoint",
    "TeamGroupsOldEndpoint",
    "TeamStatsEndpoint",
    "UserAuthenticatorIndexEndpoint",
    "UserEmailsEndpoint",
    "UserIdentityConfigEndpoint",
    "UserNotificationSettingsOptionsEndpoint",
    "UserNotificationSettingsProvidersEndpoint",
    "UserPermissionsConfigEndpoint",
    "UserPermissionsEndpoint",
    "UserRolesEndpoint",
    "UserSocialIdentitiesIndexEndpoint",
    "UserSubscriptionsEndpoint",
    "UserUserRolesEndpoint",
}
