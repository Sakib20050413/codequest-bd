from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import StudentProfile


def login_view(request):
    if request.user.is_authenticated:
        return redirect('arena:home')

    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password = request.POST.get('password', '').strip()

        user = None
        # Try matching by username first
        user = authenticate(request, username=identifier, password=password)
        # If not, try matching by student_id
        if not user:
            try:
                profile = StudentProfile.objects.get(student_id=identifier)
                user = authenticate(request, username=profile.user.username, password=password)
            except StudentProfile.DoesNotExist:
                user = None

        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name or user.username}! Happy Questing 🚀")
            next_url = request.GET.get('next', 'arena:home')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid BAIUST Student ID / Username or Password.")

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('arena:home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip().lower()
        full_name = request.POST.get('full_name', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        batch_section = request.POST.get('batch_section', 'CSE 3-2 Section A').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()
        avatar = request.POST.get('avatar', 'cyber_rover')

        if not username or not password or not student_id:
            messages.error(request, "All core fields are required.")
            return render(request, 'accounts/register.html')

        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken.")
            return render(request, 'accounts/register.html')

        if StudentProfile.objects.filter(student_id=student_id).exists():
            messages.error(request, f"Student ID '{student_id}' is already registered.")
            return render(request, 'accounts/register.html')

        # Create user
        first_name = full_name.split()[0] if full_name else username
        last_name = " ".join(full_name.split()[1:]) if len(full_name.split()) > 1 else ""

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Configure profile
        profile = user.profile
        profile.student_id = student_id
        profile.batch_section = batch_section
        profile.avatar = avatar
        profile.badges = ["First Blood (1st Solve)"]
        profile.save()

        login(request, user)
        messages.success(request, f"Account successfully created for {full_name or username}! Level 1 Rookie Badge unlocked 🛡️")
        return redirect('arena:home')

    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out safely.")
    return redirect('arena:home')


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        batch_section = request.POST.get('batch_section', '').strip()
        avatar = request.POST.get('avatar', '').strip()
        preferred_track = request.POST.get('preferred_track', '').strip()

        if full_name:
            parts = full_name.split()
            request.user.first_name = parts[0]
            request.user.last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
            request.user.save()

        if batch_section:
            profile.batch_section = batch_section
        if avatar:
            profile.avatar = avatar
        if preferred_track:
            profile.preferred_track = preferred_track
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('accounts:profile')

    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def save_wizard_track_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            track_slug = data.get('track_slug')
            profile = request.user.profile
            profile.preferred_track = track_slug
            profile.save()
            return JsonResponse({'status': 'ok', 'message': 'Diagnostic wizard selection saved.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'POST required'}, status=405)
