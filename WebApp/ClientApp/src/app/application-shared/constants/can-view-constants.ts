export class CanViewConstants {
  // failures
  public static canReportFailure = ['admin','normal'];
  public static canViewFailures = ['admin'];
  public static canDoFailureReporting = ['admin', 'normal'];

  // reviews
  public static canDoReviewsReporting = ['admin'];
  public static canViewReviews = ['admin'];
  public static canCreateFailureReview = ['admin'];
  // user manager
  public static isNormalUser = ['admin'];
  public static isSystemManager = ['admin'];
  public static isUserManager = ['admin'];
  public static isSystemSettingsManager = ['admin'];
}
