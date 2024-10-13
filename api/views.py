from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout
from django.conf import settings
from django.db.models import Sum
import stripe
from datetime import date, timedelta
from .models import (
    User, UserProfile, ExternalAuth, Goal, UserGoal,
    Workout, WorkoutLesson, Notification, Insight,
    UserNotification, Post, Food, Exercise, MealPlan,
    UserProgress, HealthTips, PasswordResetRequest,
    UserActivityLog, Payment,SomeModel
)
import uuid
from rest_framework import generics
from .serializers import (
    UserSerializer, UserProfileSerializer, ExternalAuthSerializer,
    GoalSerializer, UserGoalSerializer, WorkoutSerializer,
    WorkoutLessonSerializer, NotificationSerializer, InsightSerializer,
    UserNotificationSerializer, PostSerializer, FoodSerializer,
    ExerciseSerializer, MealPlanSerializer, UserProgressSerializer,
    HealthTipsSerializer, UserRegistrationSerializer,
    UserLoginSerializer, ChangePasswordSerializer,
    PasswordResetRequestSerializer, PasswordResetSerializer,
    UserActivityLogSerializer, PaymentSerializer, SomeModelSerializer
)
from .serializers import (
    UserSerializer, UserProfileSerializer, ExternalAuthSerializer,
    GoalSerializer, UserGoalSerializer, WorkoutSerializer,
    WorkoutLessonSerializer, NotificationSerializer, InsightSerializer,
    UserNotificationSerializer, FoodSerializer, ExerciseSerializer,
    MealPlanSerializer, UserProgressSerializer, HealthTipsSerializer,
    UserRegistrationSerializer, UserLoginSerializer,
    ChangePasswordSerializer, PasswordResetRequestSerializer, PasswordResetSerializer,
    UserActivityLogSerializer, PaymentSerializer
)

stripe.api_key = settings.STRIPE_SECRET_KEY

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Faqat tizimga kirgan foydalanuvchilar tahrir qilishga ruxsat

    def get_queryset(self):
        return User.objects.all()

    @action(detail=True, methods=['put', 'patch'])
    def edit(self, request, pk=None):
        user = self.get_object()

        jwt_authenticator = JWTAuthentication()
        auth_header = jwt_authenticator.get_header(request)
        if auth_header:
            validated_token = jwt_authenticator.get_raw_token(auth_header)
            if validated_token:
                token_user = jwt_authenticator.get_user(validated_token)

                if user != token_user:
                    return Response({'error': 'Siz faqat o\'z hisobingizni tahrirlashingiz mumkin.'},
                                    status=status.HTTP_403_FORBIDDEN)

        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return self.edit(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return self.edit(request, *args, **kwargs)




class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
#
# # User progress management
class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer


class HealthTipsViewSet(viewsets.ModelViewSet):
    queryset = HealthTips.objects.all()
    serializer_class = HealthTipsSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
#
class ExternalAuthViewSet(viewsets.ModelViewSet):
    queryset = ExternalAuth.objects.all()
    serializer_class = ExternalAuthSerializer
#
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
#
class UserGoalViewSet(viewsets.ModelViewSet):
    queryset = UserGoal.objects.all()
    serializer_class = UserGoalSerializer
#
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]  # Faqat tizimga kirgan foydalanuvchilar kirishi mumkin

    # Workout ma'lumotini tasdiqlash uchun PATCH yoki PUT so'rovlaridan foydalaniladi
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    # Workout-ni tasdiqlash uchun maxsus action
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def confirm_completion(self, request, pk=None):
        workout = self.get_object()

        # Tasdiqlash uchun True/False qiymatlari kirib keladi
        is_completed = request.data.get('is_completed', None)

        if is_completed is not None:
            workout.is_completed = is_completed
            workout.save()
            return Response({'status': 'Workout updated successfully', 'is_completed': workout.is_completed})
        else:
            return Response({'error': 'is_completed value is required'}, status=status.HTTP_400_BAD_REQUEST)

class WorkoutLessonViewSet(viewsets.ModelViewSet):
    queryset = WorkoutLesson.objects.all()
    serializer_class = WorkoutLessonSerializer
#
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
#
class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer


class UserRegistrationView(viewsets.ViewSet):
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserLoginViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']  # Adjusted to get the user from the validated data
#             login(request, user)
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.contrib.auth import login


class UserLoginViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Foydalanuvchini validatsiyadan o'tkazish

            # Foydalanuvchini tizimga kiritish
            login(request, user)

            # JWT tokenlarni yaratish
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Login successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "session_id": request.session.session_key  # Session ID ni olish
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestViewSet(viewsets.ModelViewSet):
    queryset = PasswordResetRequest.objects.all()
    serializer_class = PasswordResetRequestSerializer


class PasswordResetViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            reset_request = PasswordResetRequest.objects.filter(token=serializer.data.get("token"), is_used=False).first()
            if reset_request:
                user = reset_request.user
                user.set_password(serializer.data.get("new_password"))
                user.save()
                reset_request.is_used = True
                reset_request.save()
                return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid or used token."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    @action(detail=False, methods=['get'])
    def high_protein(self, request):
        high_protein_foods = self.queryset.filter(protein__gte=20)
        serializer = self.get_serializer(high_protein_foods, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def low_carb(self, request):
        low_carb_foods = self.queryset.filter(carbs__lte=10)
        serializer = self.get_serializer(low_carb_foods, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def vegetarian(self, request):
        vegetarian_foods = self.queryset.filter(is_vegetarian=True)
        serializer = self.get_serializer(vegetarian_foods, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def total_calories(self, request):
        food_ids = request.data.get('food_ids', [])
        selected_foods = self.queryset.filter(id__in=food_ids)
        total_calories = sum(food.calories for food in selected_foods)
        return Response({'total_calories': total_calories})

    # Ovqat yeyilganini tasdiqlash action
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def confirm_consumption(self, request, pk=None):
        food = self.get_object()

        # Tasdiqlash uchun True/False qiymati keladi
        is_consumed = request.data.get('is_consumed', None)

        if is_consumed is not None:
            food.is_consumed = is_consumed  # Tasdiqlangan qiymatni saqlash
            food.save()
            return Response({'status': 'Food consumption updated successfully', 'is_consumed': food.is_consumed})
        else:
            return Response({'error': 'is_consumed value is required'}, status=status.HTTP_400_BAD_REQUEST)



class UserActivityLogViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer


class PaymentCreateViewSet(viewsets.ViewSet):
    def create(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        amount = request.data.get('amount')
        try:
            amount_in_cents = int(float(amount) * 100)
        except ValueError:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            charge = stripe.Charge.create(
                amount=amount_in_cents,
                currency='usd',
                customer=user_profile.stripe_customer_id,
                description=f'Charge for {user_profile.user.email}'
            )

            payment = Payment.objects.create(
                user_profile=user_profile,
                stripe_charge_id=charge.id,
                amount=amount,
                success=True
            )
            return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SomeModelViewSet(viewsets.ModelViewSet):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]  # Foydalanuvchi tizimga kirgan bo'lishi kerak

    def get_queryset(self):
        queryset = super().get_queryset()
        min_calories = self.request.query_params.get('min_calories')
        if min_calories:
            queryset = queryset.filter(calories_burned__gte=min_calories)
        return queryset

    @action(detail=False, methods=['get'])
    def total_burned_calories(self, request):
        exercise_ids = request.query_params.getlist('exercise_ids', [])
        selected_exercises = self.queryset.filter(id__in=exercise_ids)
        total_burned = sum(exercise.calories_burned for exercise in selected_exercises)
        return Response({'total_burned_calories': total_burned})

    # Kunlik kaloriya sarfini hisoblash
    @action(detail=False, methods=['get'])
    def daily_calories(self, request):
        today = date.today()
        user = request.user

        total_calories = UserActivityLog.objects.filter(user=user, date=today).aggregate(Sum('calories_burned'))['calories_burned__sum']

        if total_calories is None:
            total_calories = 0

        return Response({'daily_calories_burned': total_calories})

    # Oylik kaloriya sarfini hisoblash
    @action(detail=False, methods=['get'])
    def monthly_calories(self, request):
        today = date.today()
        user = request.user
        start_of_month = today.replace(day=1)

        total_calories = UserActivityLog.objects.filter(user=user, date__gte=start_of_month).aggregate(Sum('calories_burned'))['calories_burned__sum']

        if total_calories is None:
            total_calories = 0

        return Response({'monthly_calories_burned': total_calories})

    @action(detail=False, methods=['get'])
    def burned_calories(self, request):
        user = request.user
        period = request.query_params.get('period', 'daily')  # kunlik, oylik yoki haftalik
        today = date.today()

        if period == 'daily':
            date_filter = today
        elif period == 'weekly':
            date_filter = today - timedelta(days=7)
        elif period == 'monthly':
            date_filter = today.replace(day=1)
        else:
            return Response({'error': 'Invalid period'}, status=status.HTTP_400_BAD_REQUEST)

        # Kaloriya yoqish bo'yicha loglar
        total_calories = UserActivityLog.objects.filter(
            user=user,
            date__gte=date_filter
        ).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

        return Response({'burned_calories': total_calories})

    # Haftalik kaloriya sarfini hisoblash
    @action(detail=False, methods=['get'])
    def weekly_calories(self, request):
        today = date.today()
        user = request.user
        start_of_week = today - timedelta(days=today.weekday())

        total_calories = UserActivityLog.objects.filter(user=user, date__gte=start_of_week).aggregate(Sum('calories_burned'))['calories_burned__sum']

        if total_calories is None:
            total_calories = 0

        return Response({'weekly_calories_burned': total_calories})

