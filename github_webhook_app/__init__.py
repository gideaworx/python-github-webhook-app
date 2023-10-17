
# Webhook event decorators
#   DO NOT EDIT
#   Generated on 2023-10-17T20:42:59Z

import github_webhook_app.models
from .abc_service import ABCWebhookService

class WebhookService(ABCWebhookService):
  def __init__(self):
    ABCWebhookService.__init__(self)

  def handle_branch_protection_rule_created(self, func):
    return self._wrap(func, event_name="branch-protection-rule-created", request_body=github_webhook_app.models.WebhookBranchProtectionRuleCreated)

  def handle_branch_protection_rule_deleted(self, func):
    return self._wrap(func, event_name="branch-protection-rule-deleted", request_body=github_webhook_app.models.WebhookBranchProtectionRuleDeleted)

  def handle_branch_protection_rule_edited(self, func):
    return self._wrap(func, event_name="branch-protection-rule-edited", request_body=github_webhook_app.models.WebhookBranchProtectionRuleEdited)

  def handle_check_run_completed(self, func):
    return self._wrap(func, event_name="check-run-completed", request_body=github_webhook_app.models.WebhookCheckRunCompleted)

  def handle_check_run_created(self, func):
    return self._wrap(func, event_name="check-run-created", request_body=github_webhook_app.models.WebhookCheckRunCreated)

  def handle_check_suite_completed(self, func):
    return self._wrap(func, event_name="check-suite-completed", request_body=github_webhook_app.models.WebhookCheckSuiteCompleted)

  def handle_code_scanning_alert_appeared_in_branch(self, func):
    return self._wrap(func, event_name="code-scanning-alert-appeared-in-branch", request_body=github_webhook_app.models.WebhookCodeScanningAlertAppearedInBranch)

  def handle_code_scanning_alert_closed_by_user(self, func):
    return self._wrap(func, event_name="code-scanning-alert-closed-by-user", request_body=github_webhook_app.models.WebhookCodeScanningAlertClosedByUser)

  def handle_code_scanning_alert_created(self, func):
    return self._wrap(func, event_name="code-scanning-alert-created", request_body=github_webhook_app.models.WebhookCodeScanningAlertCreated)

  def handle_code_scanning_alert_fixed(self, func):
    return self._wrap(func, event_name="code-scanning-alert-fixed", request_body=github_webhook_app.models.WebhookCodeScanningAlertFixed)

  def handle_code_scanning_alert_reopened(self, func):
    return self._wrap(func, event_name="code-scanning-alert-reopened", request_body=github_webhook_app.models.WebhookCodeScanningAlertReopened)

  def handle_code_scanning_alert_reopened_by_user(self, func):
    return self._wrap(func, event_name="code-scanning-alert-reopened-by-user", request_body=github_webhook_app.models.WebhookCodeScanningAlertReopenedByUser)

  def handle_commit_comment_created(self, func):
    return self._wrap(func, event_name="commit-comment-created", request_body=github_webhook_app.models.WebhookCommitCommentCreated)

  def handle_create(self, func):
    return self._wrap(func, event_name="create", request_body=github_webhook_app.models.WebhookCreate)

  def handle_delete(self, func):
    return self._wrap(func, event_name="delete", request_body=github_webhook_app.models.WebhookDelete)

  def handle_dependabot_alert_created(self, func):
    return self._wrap(func, event_name="dependabot-alert-created", request_body=github_webhook_app.models.WebhookDependabotAlertCreated)

  def handle_dependabot_alert_dismissed(self, func):
    return self._wrap(func, event_name="dependabot-alert-dismissed", request_body=github_webhook_app.models.WebhookDependabotAlertDismissed)

  def handle_dependabot_alert_fixed(self, func):
    return self._wrap(func, event_name="dependabot-alert-fixed", request_body=github_webhook_app.models.WebhookDependabotAlertFixed)

  def handle_dependabot_alert_reintroduced(self, func):
    return self._wrap(func, event_name="dependabot-alert-reintroduced", request_body=github_webhook_app.models.WebhookDependabotAlertReintroduced)

  def handle_dependabot_alert_reopened(self, func):
    return self._wrap(func, event_name="dependabot-alert-reopened", request_body=github_webhook_app.models.WebhookDependabotAlertReopened)

  def handle_deploy_key_created(self, func):
    return self._wrap(func, event_name="deploy-key-created", request_body=github_webhook_app.models.WebhookDeployKeyCreated)

  def handle_deploy_key_deleted(self, func):
    return self._wrap(func, event_name="deploy-key-deleted", request_body=github_webhook_app.models.WebhookDeployKeyDeleted)

  def handle_deployment_created(self, func):
    return self._wrap(func, event_name="deployment-created", request_body=github_webhook_app.models.WebhookDeploymentCreated)

  def handle_deployment_status_created(self, func):
    return self._wrap(func, event_name="deployment-status-created", request_body=github_webhook_app.models.WebhookDeploymentStatusCreated)

  def handle_discussion_answered(self, func):
    return self._wrap(func, event_name="discussion-answered", request_body=github_webhook_app.models.WebhookDiscussionAnswered)

  def handle_discussion_category_changed(self, func):
    return self._wrap(func, event_name="discussion-category-changed", request_body=github_webhook_app.models.WebhookDiscussionCategoryChanged)

  def handle_discussion_comment_created(self, func):
    return self._wrap(func, event_name="discussion-comment-created", request_body=github_webhook_app.models.WebhookDiscussionCommentCreated)

  def handle_discussion_comment_deleted(self, func):
    return self._wrap(func, event_name="discussion-comment-deleted", request_body=github_webhook_app.models.WebhookDiscussionCommentDeleted)

  def handle_discussion_comment_edited(self, func):
    return self._wrap(func, event_name="discussion-comment-edited", request_body=github_webhook_app.models.WebhookDiscussionCommentEdited)

  def handle_discussion_created(self, func):
    return self._wrap(func, event_name="discussion-created", request_body=github_webhook_app.models.WebhookDiscussionCreated)

  def handle_discussion_deleted(self, func):
    return self._wrap(func, event_name="discussion-deleted", request_body=github_webhook_app.models.WebhookDiscussionDeleted)

  def handle_discussion_edited(self, func):
    return self._wrap(func, event_name="discussion-edited", request_body=github_webhook_app.models.WebhookDiscussionEdited)

  def handle_discussion_labeled(self, func):
    return self._wrap(func, event_name="discussion-labeled", request_body=github_webhook_app.models.WebhookDiscussionLabeled)

  def handle_discussion_locked(self, func):
    return self._wrap(func, event_name="discussion-locked", request_body=github_webhook_app.models.WebhookDiscussionLocked)

  def handle_discussion_pinned(self, func):
    return self._wrap(func, event_name="discussion-pinned", request_body=github_webhook_app.models.WebhookDiscussionPinned)

  def handle_discussion_transferred(self, func):
    return self._wrap(func, event_name="discussion-transferred", request_body=github_webhook_app.models.WebhookDiscussionTransferred)

  def handle_discussion_unanswered(self, func):
    return self._wrap(func, event_name="discussion-unanswered", request_body=github_webhook_app.models.WebhookDiscussionUnanswered)

  def handle_discussion_unlabeled(self, func):
    return self._wrap(func, event_name="discussion-unlabeled", request_body=github_webhook_app.models.WebhookDiscussionUnlabeled)

  def handle_discussion_unlocked(self, func):
    return self._wrap(func, event_name="discussion-unlocked", request_body=github_webhook_app.models.WebhookDiscussionUnlocked)

  def handle_discussion_unpinned(self, func):
    return self._wrap(func, event_name="discussion-unpinned", request_body=github_webhook_app.models.WebhookDiscussionUnpinned)

  def handle_fork(self, func):
    return self._wrap(func, event_name="fork", request_body=github_webhook_app.models.WebhookFork)

  def handle_gollum(self, func):
    return self._wrap(func, event_name="gollum", request_body=github_webhook_app.models.WebhookGollum)

  def handle_issue_comment_created(self, func):
    return self._wrap(func, event_name="issue-comment-created", request_body=github_webhook_app.models.WebhookIssueCommentCreated)

  def handle_issue_comment_deleted(self, func):
    return self._wrap(func, event_name="issue-comment-deleted", request_body=github_webhook_app.models.WebhookIssueCommentDeleted)

  def handle_issue_comment_edited(self, func):
    return self._wrap(func, event_name="issue-comment-edited", request_body=github_webhook_app.models.WebhookIssueCommentEdited)

  def handle_issues_assigned(self, func):
    return self._wrap(func, event_name="issues-assigned", request_body=github_webhook_app.models.WebhookIssuesAssigned)

  def handle_issues_closed(self, func):
    return self._wrap(func, event_name="issues-closed", request_body=github_webhook_app.models.WebhookIssuesClosed)

  def handle_issues_deleted(self, func):
    return self._wrap(func, event_name="issues-deleted", request_body=github_webhook_app.models.WebhookIssuesDeleted)

  def handle_issues_demilestoned(self, func):
    return self._wrap(func, event_name="issues-demilestoned", request_body=github_webhook_app.models.WebhookIssuesDemilestoned)

  def handle_issues_edited(self, func):
    return self._wrap(func, event_name="issues-edited", request_body=github_webhook_app.models.WebhookIssuesEdited)

  def handle_issues_labeled(self, func):
    return self._wrap(func, event_name="issues-labeled", request_body=github_webhook_app.models.WebhookIssuesLabeled)

  def handle_issues_locked(self, func):
    return self._wrap(func, event_name="issues-locked", request_body=github_webhook_app.models.WebhookIssuesLocked)

  def handle_issues_milestoned(self, func):
    return self._wrap(func, event_name="issues-milestoned", request_body=github_webhook_app.models.WebhookIssuesMilestoned)

  def handle_issues_opened(self, func):
    return self._wrap(func, event_name="issues-opened", request_body=github_webhook_app.models.WebhookIssuesOpened)

  def handle_issues_pinned(self, func):
    return self._wrap(func, event_name="issues-pinned", request_body=github_webhook_app.models.WebhookIssuesPinned)

  def handle_issues_reopened(self, func):
    return self._wrap(func, event_name="issues-reopened", request_body=github_webhook_app.models.WebhookIssuesReopened)

  def handle_issues_transferred(self, func):
    return self._wrap(func, event_name="issues-transferred", request_body=github_webhook_app.models.WebhookIssuesTransferred)

  def handle_issues_unassigned(self, func):
    return self._wrap(func, event_name="issues-unassigned", request_body=github_webhook_app.models.WebhookIssuesUnassigned)

  def handle_issues_unlabeled(self, func):
    return self._wrap(func, event_name="issues-unlabeled", request_body=github_webhook_app.models.WebhookIssuesUnlabeled)

  def handle_issues_unlocked(self, func):
    return self._wrap(func, event_name="issues-unlocked", request_body=github_webhook_app.models.WebhookIssuesUnlocked)

  def handle_issues_unpinned(self, func):
    return self._wrap(func, event_name="issues-unpinned", request_body=github_webhook_app.models.WebhookIssuesUnpinned)

  def handle_label_created(self, func):
    return self._wrap(func, event_name="label-created", request_body=github_webhook_app.models.WebhookLabelCreated)

  def handle_label_deleted(self, func):
    return self._wrap(func, event_name="label-deleted", request_body=github_webhook_app.models.WebhookLabelDeleted)

  def handle_label_edited(self, func):
    return self._wrap(func, event_name="label-edited", request_body=github_webhook_app.models.WebhookLabelEdited)

  def handle_member_added(self, func):
    return self._wrap(func, event_name="member-added", request_body=github_webhook_app.models.WebhookMemberAdded)

  def handle_member_edited(self, func):
    return self._wrap(func, event_name="member-edited", request_body=github_webhook_app.models.WebhookMemberEdited)

  def handle_member_removed(self, func):
    return self._wrap(func, event_name="member-removed", request_body=github_webhook_app.models.WebhookMemberRemoved)

  def handle_meta_deleted(self, func):
    return self._wrap(func, event_name="meta-deleted", request_body=github_webhook_app.models.WebhookMetaDeleted)

  def handle_milestone_closed(self, func):
    return self._wrap(func, event_name="milestone-closed", request_body=github_webhook_app.models.WebhookMilestoneClosed)

  def handle_milestone_created(self, func):
    return self._wrap(func, event_name="milestone-created", request_body=github_webhook_app.models.WebhookMilestoneCreated)

  def handle_milestone_deleted(self, func):
    return self._wrap(func, event_name="milestone-deleted", request_body=github_webhook_app.models.WebhookMilestoneDeleted)

  def handle_milestone_edited(self, func):
    return self._wrap(func, event_name="milestone-edited", request_body=github_webhook_app.models.WebhookMilestoneEdited)

  def handle_milestone_opened(self, func):
    return self._wrap(func, event_name="milestone-opened", request_body=github_webhook_app.models.WebhookMilestoneOpened)

  def handle_package_published(self, func):
    return self._wrap(func, event_name="package-published", request_body=github_webhook_app.models.WebhookPackagePublished)

  def handle_package_updated(self, func):
    return self._wrap(func, event_name="package-updated", request_body=github_webhook_app.models.WebhookPackageUpdated)

  def handle_package_v2_create(self, func):
    return self._wrap(func, event_name="package-v2-create", request_body=github_webhook_app.models.WebhookPackageV2Create)

  def handle_page_build(self, func):
    return self._wrap(func, event_name="page-build", request_body=github_webhook_app.models.WebhookPageBuild)

  def handle_ping(self, func):
    return self._wrap(func, event_name="ping", request_body=github_webhook_app.models.WebhookPing)

  def handle_project_card_converted(self, func):
    return self._wrap(func, event_name="project-card-converted", request_body=github_webhook_app.models.WebhookProjectCardConverted)

  def handle_project_card_created(self, func):
    return self._wrap(func, event_name="project-card-created", request_body=github_webhook_app.models.WebhookProjectCardCreated)

  def handle_project_card_deleted(self, func):
    return self._wrap(func, event_name="project-card-deleted", request_body=github_webhook_app.models.WebhookProjectCardDeleted)

  def handle_project_card_edited(self, func):
    return self._wrap(func, event_name="project-card-edited", request_body=github_webhook_app.models.WebhookProjectCardEdited)

  def handle_project_card_moved(self, func):
    return self._wrap(func, event_name="project-card-moved", request_body=github_webhook_app.models.WebhookProjectCardMoved)

  def handle_project_closed(self, func):
    return self._wrap(func, event_name="project-closed", request_body=github_webhook_app.models.WebhookProjectClosed)

  def handle_project_column_created(self, func):
    return self._wrap(func, event_name="project-column-created", request_body=github_webhook_app.models.WebhookProjectColumnCreated)

  def handle_project_column_deleted(self, func):
    return self._wrap(func, event_name="project-column-deleted", request_body=github_webhook_app.models.WebhookProjectColumnDeleted)

  def handle_project_column_edited(self, func):
    return self._wrap(func, event_name="project-column-edited", request_body=github_webhook_app.models.WebhookProjectColumnEdited)

  def handle_project_column_moved(self, func):
    return self._wrap(func, event_name="project-column-moved", request_body=github_webhook_app.models.WebhookProjectColumnMoved)

  def handle_project_created(self, func):
    return self._wrap(func, event_name="project-created", request_body=github_webhook_app.models.WebhookProjectCreated)

  def handle_project_deleted(self, func):
    return self._wrap(func, event_name="project-deleted", request_body=github_webhook_app.models.WebhookProjectDeleted)

  def handle_project_edited(self, func):
    return self._wrap(func, event_name="project-edited", request_body=github_webhook_app.models.WebhookProjectEdited)

  def handle_project_reopened(self, func):
    return self._wrap(func, event_name="project-reopened", request_body=github_webhook_app.models.WebhookProjectReopened)

  def handle_public(self, func):
    return self._wrap(func, event_name="public", request_body=github_webhook_app.models.WebhookPublic)

  def handle_pull_request_assigned(self, func):
    return self._wrap(func, event_name="pull-request-assigned", request_body=github_webhook_app.models.WebhookPullRequestAssigned)

  def handle_pull_request_auto_merge_disabled(self, func):
    return self._wrap(func, event_name="pull-request-auto-merge-disabled", request_body=github_webhook_app.models.WebhookPullRequestAutoMergeDisabled)

  def handle_pull_request_auto_merge_enabled(self, func):
    return self._wrap(func, event_name="pull-request-auto-merge-enabled", request_body=github_webhook_app.models.WebhookPullRequestAutoMergeEnabled)

  def handle_pull_request_closed(self, func):
    return self._wrap(func, event_name="pull-request-closed", request_body=github_webhook_app.models.WebhookPullRequestClosed)

  def handle_pull_request_converted_to_draft(self, func):
    return self._wrap(func, event_name="pull-request-converted-to-draft", request_body=github_webhook_app.models.WebhookPullRequestConvertedToDraft)

  def handle_pull_request_demilestoned(self, func):
    return self._wrap(func, event_name="pull-request-demilestoned", request_body=github_webhook_app.models.WebhookPullRequestDemilestoned)

  def handle_pull_request_edited(self, func):
    return self._wrap(func, event_name="pull-request-edited", request_body=github_webhook_app.models.WebhookPullRequestEdited)

  def handle_pull_request_labeled(self, func):
    return self._wrap(func, event_name="pull-request-labeled", request_body=github_webhook_app.models.WebhookPullRequestLabeled)

  def handle_pull_request_locked(self, func):
    return self._wrap(func, event_name="pull-request-locked", request_body=github_webhook_app.models.WebhookPullRequestLocked)

  def handle_pull_request_milestoned(self, func):
    return self._wrap(func, event_name="pull-request-milestoned", request_body=github_webhook_app.models.WebhookPullRequestMilestoned)

  def handle_pull_request_opened(self, func):
    return self._wrap(func, event_name="pull-request-opened", request_body=github_webhook_app.models.WebhookPullRequestOpened)

  def handle_pull_request_ready_for_review(self, func):
    return self._wrap(func, event_name="pull-request-ready-for-review", request_body=github_webhook_app.models.WebhookPullRequestReadyForReview)

  def handle_pull_request_reopened(self, func):
    return self._wrap(func, event_name="pull-request-reopened", request_body=github_webhook_app.models.WebhookPullRequestReopened)

  def handle_pull_request_review_comment_created(self, func):
    return self._wrap(func, event_name="pull-request-review-comment-created", request_body=github_webhook_app.models.WebhookPullRequestReviewCommentCreated)

  def handle_pull_request_review_comment_deleted(self, func):
    return self._wrap(func, event_name="pull-request-review-comment-deleted", request_body=github_webhook_app.models.WebhookPullRequestReviewCommentDeleted)

  def handle_pull_request_review_comment_edited(self, func):
    return self._wrap(func, event_name="pull-request-review-comment-edited", request_body=github_webhook_app.models.WebhookPullRequestReviewCommentEdited)

  def handle_pull_request_review_dismissed(self, func):
    return self._wrap(func, event_name="pull-request-review-dismissed", request_body=github_webhook_app.models.WebhookPullRequestReviewDismissed)

  def handle_pull_request_review_edited(self, func):
    return self._wrap(func, event_name="pull-request-review-edited", request_body=github_webhook_app.models.WebhookPullRequestReviewEdited)

  def handle_pull_request_review_request_removed(self, func):
    return self._wrap(func, event_name="pull-request-review-request-removed", request_body=github_webhook_app.models.WebhookPullRequestReviewRequestRemoved)

  def handle_pull_request_review_requested(self, func):
    return self._wrap(func, event_name="pull-request-review-requested", request_body=github_webhook_app.models.WebhookPullRequestReviewRequested)

  def handle_pull_request_review_submitted(self, func):
    return self._wrap(func, event_name="pull-request-review-submitted", request_body=github_webhook_app.models.WebhookPullRequestReviewSubmitted)

  def handle_pull_request_review_thread_resolved(self, func):
    return self._wrap(func, event_name="pull-request-review-thread-resolved", request_body=github_webhook_app.models.WebhookPullRequestReviewThreadResolved)

  def handle_pull_request_review_thread_unresolved(self, func):
    return self._wrap(func, event_name="pull-request-review-thread-unresolved", request_body=github_webhook_app.models.WebhookPullRequestReviewThreadUnresolved)

  def handle_pull_request_synchronize(self, func):
    return self._wrap(func, event_name="pull-request-synchronize", request_body=github_webhook_app.models.WebhookPullRequestSynchronize)

  def handle_pull_request_unassigned(self, func):
    return self._wrap(func, event_name="pull-request-unassigned", request_body=github_webhook_app.models.WebhookPullRequestUnassigned)

  def handle_pull_request_unlabeled(self, func):
    return self._wrap(func, event_name="pull-request-unlabeled", request_body=github_webhook_app.models.WebhookPullRequestUnlabeled)

  def handle_pull_request_unlocked(self, func):
    return self._wrap(func, event_name="pull-request-unlocked", request_body=github_webhook_app.models.WebhookPullRequestUnlocked)

  def handle_push(self, func):
    return self._wrap(func, event_name="push", request_body=github_webhook_app.models.WebhookPush)

  def handle_registry_package_published(self, func):
    return self._wrap(func, event_name="registry-package-published", request_body=github_webhook_app.models.WebhookRegistryPackagePublished)

  def handle_registry_package_updated(self, func):
    return self._wrap(func, event_name="registry-package-updated", request_body=github_webhook_app.models.WebhookRegistryPackageUpdated)

  def handle_release_created(self, func):
    return self._wrap(func, event_name="release-created", request_body=github_webhook_app.models.WebhookReleaseCreated)

  def handle_release_deleted(self, func):
    return self._wrap(func, event_name="release-deleted", request_body=github_webhook_app.models.WebhookReleaseDeleted)

  def handle_release_edited(self, func):
    return self._wrap(func, event_name="release-edited", request_body=github_webhook_app.models.WebhookReleaseEdited)

  def handle_release_prereleased(self, func):
    return self._wrap(func, event_name="release-prereleased", request_body=github_webhook_app.models.WebhookReleasePrereleased)

  def handle_release_published(self, func):
    return self._wrap(func, event_name="release-published", request_body=github_webhook_app.models.WebhookReleasePublished)

  def handle_release_released(self, func):
    return self._wrap(func, event_name="release-released", request_body=github_webhook_app.models.WebhookReleaseReleased)

  def handle_release_unpublished(self, func):
    return self._wrap(func, event_name="release-unpublished", request_body=github_webhook_app.models.WebhookReleaseUnpublished)

  def handle_repository_archived(self, func):
    return self._wrap(func, event_name="repository-archived", request_body=github_webhook_app.models.WebhookRepositoryArchived)

  def handle_repository_created(self, func):
    return self._wrap(func, event_name="repository-created", request_body=github_webhook_app.models.WebhookRepositoryCreated)

  def handle_repository_deleted(self, func):
    return self._wrap(func, event_name="repository-deleted", request_body=github_webhook_app.models.WebhookRepositoryDeleted)

  def handle_repository_edited(self, func):
    return self._wrap(func, event_name="repository-edited", request_body=github_webhook_app.models.WebhookRepositoryEdited)

  def handle_repository_import(self, func):
    return self._wrap(func, event_name="repository-import", request_body=github_webhook_app.models.WebhookRepositoryImport)

  def handle_repository_privatized(self, func):
    return self._wrap(func, event_name="repository-privatized", request_body=github_webhook_app.models.WebhookRepositoryPrivatized)

  def handle_repository_publicized(self, func):
    return self._wrap(func, event_name="repository-publicized", request_body=github_webhook_app.models.WebhookRepositoryPublicized)

  def handle_repository_renamed(self, func):
    return self._wrap(func, event_name="repository-renamed", request_body=github_webhook_app.models.WebhookRepositoryRenamed)

  def handle_repository_transferred(self, func):
    return self._wrap(func, event_name="repository-transferred", request_body=github_webhook_app.models.WebhookRepositoryTransferred)

  def handle_repository_unarchived(self, func):
    return self._wrap(func, event_name="repository-unarchived", request_body=github_webhook_app.models.WebhookRepositoryUnarchived)

  def handle_repository_vulnerability_alert_create(self, func):
    return self._wrap(func, event_name="repository-vulnerability-alert-create", request_body=github_webhook_app.models.WebhookRepositoryVulnerabilityAlertCreate)

  def handle_repository_vulnerability_alert_dismiss(self, func):
    return self._wrap(func, event_name="repository-vulnerability-alert-dismiss", request_body=github_webhook_app.models.WebhookRepositoryVulnerabilityAlertDismiss)

  def handle_repository_vulnerability_alert_reopen(self, func):
    return self._wrap(func, event_name="repository-vulnerability-alert-reopen", request_body=github_webhook_app.models.WebhookRepositoryVulnerabilityAlertReopen)

  def handle_repository_vulnerability_alert_resolve(self, func):
    return self._wrap(func, event_name="repository-vulnerability-alert-resolve", request_body=github_webhook_app.models.WebhookRepositoryVulnerabilityAlertResolve)

  def handle_secret_scanning_alert_created(self, func):
    return self._wrap(func, event_name="secret-scanning-alert-created", request_body=github_webhook_app.models.WebhookSecretScanningAlertCreated)

  def handle_secret_scanning_alert_location_created(self, func):
    return self._wrap(func, event_name="secret-scanning-alert-location-created", request_body=github_webhook_app.models.WebhookSecretScanningAlertLocationCreated)

  def handle_secret_scanning_alert_reopened(self, func):
    return self._wrap(func, event_name="secret-scanning-alert-reopened", request_body=github_webhook_app.models.WebhookSecretScanningAlertReopened)

  def handle_secret_scanning_alert_resolved(self, func):
    return self._wrap(func, event_name="secret-scanning-alert-resolved", request_body=github_webhook_app.models.WebhookSecretScanningAlertResolved)

  def handle_secret_scanning_alert_revoked(self, func):
    return self._wrap(func, event_name="secret-scanning-alert-revoked", request_body=github_webhook_app.models.WebhookSecretScanningAlertRevoked)

  def handle_security_and_analysis(self, func):
    return self._wrap(func, event_name="security-and-analysis", request_body=github_webhook_app.models.WebhookSecurityAndAnalysis)

  def handle_star_created(self, func):
    return self._wrap(func, event_name="star-created", request_body=github_webhook_app.models.WebhookStarCreated)

  def handle_star_deleted(self, func):
    return self._wrap(func, event_name="star-deleted", request_body=github_webhook_app.models.WebhookStarDeleted)

  def handle_status(self, func):
    return self._wrap(func, event_name="status", request_body=github_webhook_app.models.WebhookStatus)

  def handle_team_add(self, func):
    return self._wrap(func, event_name="team-add", request_body=github_webhook_app.models.WebhookTeamAdd)

  def handle_watch_started(self, func):
    return self._wrap(func, event_name="watch-started", request_body=github_webhook_app.models.WebhookWatchStarted)

  def handle_workflow_job_completed(self, func):
    return self._wrap(func, event_name="workflow-job-completed", request_body=github_webhook_app.models.WebhookWorkflowJobCompleted)

  def handle_workflow_job_in_progress(self, func):
    return self._wrap(func, event_name="workflow-job-in-progress", request_body=github_webhook_app.models.WebhookWorkflowJobInProgress)

  def handle_workflow_job_queued(self, func):
    return self._wrap(func, event_name="workflow-job-queued", request_body=github_webhook_app.models.WebhookWorkflowJobQueued)

  def handle_workflow_run_completed(self, func):
    return self._wrap(func, event_name="workflow-run-completed", request_body=github_webhook_app.models.WebhookWorkflowRunCompleted)

  def handle_workflow_run_in_progress(self, func):
    return self._wrap(func, event_name="workflow-run-in-progress", request_body=github_webhook_app.models.WebhookWorkflowRunInProgress)

  def handle_workflow_run_requested(self, func):
    return self._wrap(func, event_name="workflow-run-requested", request_body=github_webhook_app.models.WebhookWorkflowRunRequested)

name = "github_webhook_app"