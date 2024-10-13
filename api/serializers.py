from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import (
    UserProfile, Payment, Goal, Workout, WorkoutLesson,
    Notification, UserNotification, Insight, UserStatistic,
    Post, Food, Exercise, MealPlan, UserProgress,
    HealthTips, ExternalAuth, UserGoal, DailyStatistic,
    PaymentMethod, UsageDays, SomeModel, UserActivityLog,
User
)

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


from django.contrib.auth import authenticate
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Foydalanuvchini autentifikatsiya qilish
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Login yoki parol noto'g'ri.")

        # `user` obyektini qaytarish
        data['user'] = user
        return data

# Change password serializer
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()


# Password reset request serializer
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value
class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate(self, attrs):
        return attrs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"

class WorkoutLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLesson
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = "__all__"




class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = "__all__"





class UserStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistic
        fields = "__all__"





class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"  # Qo'shimcha maydonlar qo'shilishi mumkin

    def update(self, instance, validated_data):
        # Faqat 'is_eaten' maydonini yangilash
        instance.is_eaten = validated_data.get('is_eaten', instance.is_eaten)
        instance.save()
        return instance



class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = "__all__"


class HealthTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTips
        fields = "__all__"



class ExternalAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalAuth
        fields = "__all__"


class UserGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGoal
        fields = "__all__"



class DailyStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStatistic
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class UsageDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageDays
        fields = "__all__"



class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = "__all__"
class UserActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivityLog
        fields = "__all__"
