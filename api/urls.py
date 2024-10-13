from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (
    FoodViewSet,
    UserRegistrationView,
    UserViewSet,
    ExerciseViewSet,
    MealPlanViewSet,
    UserProgressViewSet,
    HealthTipsViewSet,
    UserProfileViewSet,
    ExternalAuthViewSet,
    GoalViewSet,
    UserGoalViewSet,
    WorkoutViewSet,
    WorkoutLessonViewSet,
    NotificationViewSet,
    InsightViewSet,
    UserNotificationViewSet,
    PaymentCreateViewSet,
    UserLoginViewSet,
    UserLogoutViewSet,
    ChangePasswordViewSet,
    PasswordResetRequestViewSet,
    PasswordResetViewSet,
    SomeModelViewSet,
    UserActivityLogViewSet,
)

router = DefaultRouter()
router.register(r'user-activity-logs', UserActivityLogViewSet, basename='user-activity-log')
router.register(r'password-reset-requests', PasswordResetRequestViewSet, basename='password-reset-request')
router.register(r'users', UserViewSet, basename="users")
router.register(r'foods', FoodViewSet, basename='foods')
router.register(r'exercises', ExerciseViewSet, basename='exercises')  # faqat bir marta
router.register(r'meal-plans', MealPlanViewSet, basename='meal-plans')
router.register(r'user-progress', UserProgressViewSet, basename='user-progress')
router.register(r'health-tips', HealthTipsViewSet, basename='health-tips')
router.register(r'user-profiles', UserProfileViewSet, basename='user-profiles')
router.register(r'external-auth', ExternalAuthViewSet, basename='external-auth')
router.register(r'goals', GoalViewSet, basename='goals')
router.register(r'user-goals', UserGoalViewSet, basename='user-goals')
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'workout-lessons', WorkoutLessonViewSet, basename='workout-lessons')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'insights', InsightViewSet, basename='insights')
router.register(r'user-notifications', UserNotificationViewSet, basename='user-notifications')
router.register(r'some-models', SomeModelViewSet, basename='some-models')

urlpatterns = [
    path('', include(router.urls), name='api-root'),
    path('register/', UserRegistrationView.as_view({'post': 'create'}), name='user-registration'),
    path('login/', UserLoginViewSet.as_view({'post': 'create'}), name='user-login'),
    path('logout/', UserLogoutViewSet.as_view({'post': 'create'}), name='user-logout'),
    path('change-password/', ChangePasswordViewSet.as_view({'post': 'create'}), name='change-password'),
    path('password-reset-request/', PasswordResetRequestViewSet.as_view({'post': 'create'}), name='password-reset-request'),
    path('password-reset/', PasswordResetViewSet.as_view({'post': 'create'}), name='password-reset'),
    # Token olish yo'li
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Tokenni yangilash yo'li
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
