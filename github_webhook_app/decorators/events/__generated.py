
# Webhook event decorators
# DO NOT EDIT
# Generated on 2023-10-16T22:54:00Z

import github_webhook_app.models
from .abstract_handler import abstract_webhook_handler

              
class handle_label_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("label-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookLabelDeleted)

class handle_member_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("member-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMemberEdited)

class handle_project_card_converted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-card-converted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCardConverted)

class handle_project_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectDeleted)

class handle_meta_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("meta-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMetaDeleted)

class handle_member_removed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("member-removed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMemberRemoved)

class handle_milestone_closed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("milestone-closed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMilestoneClosed)

class handle_milestone_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("milestone-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMilestoneCreated)

class handle_milestone_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("milestone-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMilestoneDeleted)

class handle_milestone_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("milestone-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMilestoneEdited)

class handle_milestone_opened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("milestone-opened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMilestoneOpened)

class handle_package_published(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("package-published", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPackagePublished)

class handle_package_updated(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("package-updated", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPackageUpdated)

class handle_repository_vulnerability_alert_dismiss(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-vulnerability-alert-dismiss", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryVulnerabilityAlertDismiss)

class handle_project_card_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-card-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCardCreated)

class handle_project_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectEdited)

class handle_page_build(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("page-build", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPageBuild)

class handle_project_column_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-column-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectColumnCreated)

class handle_pull_request_locked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-locked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestLocked)

class handle_project_column_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-column-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectColumnDeleted)

class handle_project_card_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-card-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCardDeleted)

class handle_project_card_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-card-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCardEdited)

class handle_project_card_moved(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-card-moved", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCardMoved)

class handle_watch_started(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("watch-started", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWatchStarted)

class handle_project_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectReopened)

class handle_project_closed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-closed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectClosed)

class handle_project_column_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-column-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectColumnEdited)

class handle_project_column_moved(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-column-moved", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectColumnMoved)

class handle_pull_request_auto_merge_disabled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-auto-merge-disabled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestAutoMergeDisabled)

class handle_project_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("project-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookProjectCreated)

class handle_pull_request_review_comment_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-comment-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewCommentDeleted)

class handle_pull_request_assigned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-assigned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestAssigned)

class handle_pull_request_ready_for_review(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-ready-for-review", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReadyForReview)

class handle_pull_request_converted_to_draft(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-converted-to-draft", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestConvertedToDraft)

class handle_registry_package_updated(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("registry-package-updated", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRegistryPackageUpdated)

class handle_pull_request_opened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-opened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestOpened)

class handle_pull_request_milestoned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-milestoned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestMilestoned)

class handle_pull_request_review_thread_resolved(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-thread-resolved", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewThreadResolved)

class handle_pull_request_unlabeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-unlabeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestUnlabeled)

class handle_pull_request_labeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-labeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestLabeled)

class handle_pull_request_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestEdited)

class handle_pull_request_closed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-closed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestClosed)

class handle_pull_request_demilestoned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-demilestoned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestDemilestoned)

class handle_pull_request_review_thread_unresolved(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-thread-unresolved", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewThreadUnresolved)

class handle_push(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("push", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPush)

class handle_pull_request_unlocked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-unlocked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestUnlocked)

class handle_pull_request_review_comment_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-comment-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewCommentCreated)

class handle_status(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("status", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookStatus)

class handle_pull_request_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReopened)

class handle_pull_request_synchronize(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-synchronize", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestSynchronize)

class handle_pull_request_review_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewEdited)

class handle_issue_comment_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issue-comment-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssueCommentDeleted)

class handle_pull_request_review_comment_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-comment-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewCommentEdited)

class handle_label_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("label-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookLabelEdited)

class handle_pull_request_review_request_removed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-request-removed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewRequestRemoved)

class handle_code_scanning_alert_reopened_by_user(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-reopened-by-user", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertReopenedByUser)

class handle_pull_request_review_dismissed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-dismissed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewDismissed)

class handle_code_scanning_alert_fixed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-fixed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertFixed)

class handle_pull_request_unassigned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-unassigned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestUnassigned)

class handle_check_suite_completed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("check-suite-completed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCheckSuiteCompleted)

class handle_pull_request_review_submitted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-submitted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewSubmitted)

class handle_pull_request_review_requested(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-review-requested", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestReviewRequested)

class handle_branch_protection_rule_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("branch-protection-rule-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookBranchProtectionRuleDeleted)

class handle_repository_vulnerability_alert_create(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-vulnerability-alert-create", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryVulnerabilityAlertCreate)

class handle_branch_protection_rule_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("branch-protection-rule-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookBranchProtectionRuleCreated)

class handle_registry_package_published(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("registry-package-published", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRegistryPackagePublished)

class handle_code_scanning_alert_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertCreated)

class handle_release_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleaseDeleted)

class handle_code_scanning_alert_appeared_in_branch(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-appeared-in-branch", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertAppearedInBranch)

class handle_release_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleaseEdited)

class handle_code_scanning_alert_closed_by_user(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-closed-by-user", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertClosedByUser)

class handle_release_prereleased(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-prereleased", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleasePrereleased)

class handle_check_run_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("check-run-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCheckRunCreated)

class handle_secret_scanning_alert_location_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("secret-scanning-alert-location-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecretScanningAlertLocationCreated)

class handle_branch_protection_rule_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("branch-protection-rule-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookBranchProtectionRuleEdited)

class handle_release_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleaseCreated)

class handle_release_published(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-published", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleasePublished)

class handle_check_run_completed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("check-run-completed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCheckRunCompleted)

class handle_release_released(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-released", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleaseReleased)

class handle_dependabot_alert_dismissed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("dependabot-alert-dismissed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDependabotAlertDismissed)

class handle_release_unpublished(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("release-unpublished", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookReleaseUnpublished)

class handle_deployment_status_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("deployment-status-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDeploymentStatusCreated)

class handle_repository_archived(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-archived", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryArchived)

class handle_code_scanning_alert_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("code-scanning-alert-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCodeScanningAlertReopened)

class handle_repository_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryCreated)

class handle_dependabot_alert_fixed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("dependabot-alert-fixed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDependabotAlertFixed)

class handle_repository_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryDeleted)

class handle_discussion_category_changed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-category-changed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionCategoryChanged)

class handle_repository_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryEdited)

class handle_discussion_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionDeleted)

class handle_repository_import(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-import", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryImport)

class handle_dependabot_alert_reintroduced(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("dependabot-alert-reintroduced", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDependabotAlertReintroduced)

class handle_repository_privatized(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-privatized", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryPrivatized)

class handle_dependabot_alert_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("dependabot-alert-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDependabotAlertCreated)

class handle_repository_publicized(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-publicized", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryPublicized)

class handle_repository_renamed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-renamed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryRenamed)

class handle_commit_comment_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("commit-comment-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCommitCommentCreated)

class handle_repository_transferred(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-transferred", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryTransferred)

class handle_delete(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("delete", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDelete)

class handle_repository_unarchived(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-unarchived", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryUnarchived)

class handle_pull_request_auto_merge_enabled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("pull-request-auto-merge-enabled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPullRequestAutoMergeEnabled)

class handle_repository_vulnerability_alert_resolve(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-vulnerability-alert-resolve", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryVulnerabilityAlertResolve)

class handle_create(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("create", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookCreate)

class handle_star_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("star-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookStarDeleted)

class handle_deploy_key_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("deploy-key-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDeployKeyCreated)

class handle_deploy_key_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("deploy-key-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDeployKeyDeleted)

class handle_team_add(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("team-add", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookTeamAdd)

class handle_dependabot_alert_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("dependabot-alert-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDependabotAlertReopened)

class handle_secret_scanning_alert_revoked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("secret-scanning-alert-revoked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecretScanningAlertRevoked)

class handle_discussion_answered(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-answered", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionAnswered)

class handle_repository_vulnerability_alert_reopen(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("repository-vulnerability-alert-reopen", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookRepositoryVulnerabilityAlertReopen)

class handle_gollum(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("gollum", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookGollum)

class handle_secret_scanning_alert_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("secret-scanning-alert-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecretScanningAlertCreated)

class handle_deployment_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("deployment-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDeploymentCreated)

class handle_fork(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("fork", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookFork)

class handle_workflow_job_completed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-job-completed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowJobCompleted)

class handle_discussion_comment_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-comment-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionCommentCreated)

class handle_star_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("star-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookStarCreated)

class handle_discussion_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionEdited)

class handle_security_and_analysis(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("security-and-analysis", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecurityAndAnalysis)

class handle_discussion_labeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-labeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionLabeled)

class handle_secret_scanning_alert_resolved(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("secret-scanning-alert-resolved", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecretScanningAlertResolved)

class handle_discussion_comment_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-comment-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionCommentDeleted)

class handle_discussion_comment_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-comment-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionCommentEdited)

class handle_secret_scanning_alert_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("secret-scanning-alert-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookSecretScanningAlertReopened)

class handle_public(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("public", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPublic)

class handle_workflow_job_in_progress(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-job-in-progress", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowJobInProgress)

class handle_discussion_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionCreated)

class handle_discussion_locked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-locked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionLocked)

class handle_workflow_run_in_progress(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-run-in-progress", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowRunInProgress)

class handle_discussion_pinned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-pinned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionPinned)

class handle_discussion_transferred(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-transferred", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionTransferred)

class handle_discussion_unanswered(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-unanswered", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionUnanswered)

class handle_discussion_unlabeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-unlabeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionUnlabeled)

class handle_discussion_unlocked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-unlocked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionUnlocked)

class handle_discussion_unpinned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("discussion-unpinned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookDiscussionUnpinned)

class handle_workflow_run_completed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-run-completed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowRunCompleted)

class handle_workflow_job_queued(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-job-queued", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowJobQueued)

class handle_issues_demilestoned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-demilestoned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesDemilestoned)

class handle_issues_deleted(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-deleted", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesDeleted)

class handle_issue_comment_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issue-comment-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssueCommentCreated)

class handle_workflow_run_requested(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("workflow-run-requested", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookWorkflowRunRequested)

class handle_ping(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("ping", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPing)

class handle_member_added(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("member-added", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookMemberAdded)

class handle_issues_closed(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-closed", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesClosed)

class handle_issue_comment_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issue-comment-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssueCommentEdited)

class handle_package_v2_create(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("package-v2-create", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookPackageV2Create)

class handle_issues_assigned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-assigned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesAssigned)

class handle_issues_edited(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-edited", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesEdited)

class handle_issues_labeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-labeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesLabeled)

class handle_issues_locked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-locked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesLocked)

class handle_issues_milestoned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-milestoned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesMilestoned)

class handle_issues_opened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-opened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesOpened)

class handle_issues_pinned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-pinned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesPinned)

class handle_issues_reopened(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-reopened", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesReopened)

class handle_issues_transferred(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-transferred", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesTransferred)

class handle_issues_unassigned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-unassigned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesUnassigned)

class handle_issues_unlabeled(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-unlabeled", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesUnlabeled)

class handle_issues_unlocked(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-unlocked", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesUnlocked)

class handle_issues_unpinned(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("issues-unpinned", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookIssuesUnpinned)

class handle_label_created(abstract_webhook_handler):
  def __init__(self, func):
    super(self, func)
    self._set_targets("label-created", {"X-GitHub-Delivery", "X-Github-Hook-Installation-Target-Id", "X-Github-Hook-Id", "X-Github-Hook-Installation-Target-Type", "User-Agent", "X-Hub-Signature-256", "X-Github-Event"}, github_webhook_app.models.WebhookLabelCreated)
