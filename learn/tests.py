import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from learn.models import Language, Course, Lesson, Game, Badge, UserProfile, UserProgress, MicroTask, Certificate, Contest, ContestSubmission


class CodeQuestCoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testlearner", password="password123")
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)

        self.lang = Language.objects.create(
            name="HTML5",
            slug="html",
            short_code="HTML",
            category="Frontend",
            summary="Markup language",
            order=1,
            is_active=True,
        )
        self.course = Course.objects.create(
            language=self.lang,
            title="HTML5 Foundations",
            slug="html-core",
            description="Core HTML",
            level="Beginner",
            order=1,
        )
        self.lesson1 = Lesson.objects.create(
            course=self.course,
            title="01. First Heading",
            slug="01-heading",
            order=1,
            est_minutes=4,
            xp=40,
            body_md="Use `<h1>` for headers.",
            task_prompt="Create an h1 tag.",
            starter_code="<!-- Code here -->",
            solution="<h1>Hello World</h1>",
            tests_json=[{"id": "t1", "desc": "Has h1", "type": "dom_exists", "query": "h1"}],
            hints_json=["Hint 1: wrap in <h1>"],
        )
        self.lesson2 = Lesson.objects.create(
            course=self.course,
            title="02. Paragraph",
            slug="02-paragraph",
            order=2,
            est_minutes=5,
            xp=50,
            body_md="Use `<p>` for paragraphs.",
            task_prompt="Create a p tag.",
            starter_code="<!-- Code here -->",
            solution="<p>Some text</p>",
            tests_json=[{"id": "t2", "desc": "Has p", "type": "dom_exists", "query": "p"}],
            hints_json=[],
        )
        self.game = Game.objects.create(
            slug="tag-match",
            title="Tag Match",
            tagline="Match tags",
            description="Semantic HTML drill",
            xp_per_win=30,
        )
        self.badge = Badge.objects.create(
            name="First Code",
            slug="first-code",
            description="Earned 100 XP",
            xp_required=100,
        )

    def test_landing_page(self):
        res = self.client.get(reverse("landing"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "CodeQuest")
        self.assertContains(res, "HTML5 Foundations")

    def test_catalogue_page(self):
        res = self.client.get(reverse("catalogue"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "HTML5")

    def test_catalogue_alias_route(self):
        res = self.client.get("/catalogue/")
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "HTML5")

    def test_landing_page_track_links_valid(self):
        res = self.client.get(reverse("landing"))
        self.assertEqual(res.status_code, 200)
        self.assertNotContains(res, "link: '/catalogue/'")

    def test_course_detail(self):
        res = self.client.get(reverse("course_detail", args=[self.course.slug]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "01. First Heading")
        self.assertContains(res, "02. Paragraph")

    def test_lesson_detail(self):
        res = self.client.get(reverse("lesson_detail", args=[self.course.slug, self.lesson1.slug]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "First Heading")
        self.assertContains(res, "codeEditor")
        self.assertContains(res, "previewIframe")
        self.assertContains(res, "Software Models")
        self.assertContains(res, "software_models.js")
        self.assertContains(res, "CSS Box Model")
        self.assertContains(res, "AST &amp; State")
        self.assertContains(res, "Relational Schema")

    def test_decoy_admin_returns_404(self):
        res = self.client.get("/admin/")
        self.assertEqual(res.status_code, 404)

    def test_api_check_lesson_authenticated(self):
        self.client.login(username="testlearner", password="password123")
        payload = json.dumps({"passed": True})
        res = self.client.post(
            reverse("api_check_lesson", args=[self.lesson1.id]),
            data=payload,
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["ok"])
        self.assertTrue(data["passed"])
        self.assertEqual(data["xp_awarded"], 40)

        # Profile updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.xp, 40)
        self.assertTrue(UserProgress.objects.filter(user=self.user, lesson=self.lesson1, status="COMPLETED").exists())

    def test_playground(self):
        res = self.client.get(reverse("playground"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "editorHtml")

    def test_games_hub_and_game_play(self):
        hub_res = self.client.get(reverse("games_hub"))
        self.assertEqual(hub_res.status_code, 200)
        self.assertContains(hub_res, "Tag Match")

        game_res = self.client.get(reverse("game_play", args=[self.game.slug]))
        self.assertEqual(game_res.status_code, 200)
        self.assertContains(game_res, "Tag Match")

    def test_game_score_api(self):
        self.client.login(username="testlearner", password="password123")
        res = self.client.post(reverse("api_record_game_score", args=[self.game.slug]))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["xp_earned"], 30)

        self.profile.refresh_from_db()
        self.assertEqual(self.profile.xp, 30)

    def test_catalogue_authenticated_dashboard(self):
        self.client.login(username="testlearner", password="password123")
        # Mark lesson 1 completed
        UserProgress.objects.create(
            user=self.user,
            lesson=self.lesson1,
            status="COMPLETED"
        )
        res = self.client.get(reverse("catalogue"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Welcome back, testlearner!")
        self.assertContains(res, "PICK UP WHERE YOU LEFT OFF")
        self.assertContains(res, "Resume Lesson")
        self.assertContains(res, "Practice Arena")
        self.assertContains(res, "Arcade Drills")
        self.assertContains(res, "1 / 2 Lessons Completed")
        self.assertContains(res, "50%")

    def test_catalogue_guest_view(self):
        res = self.client.get(reverse("catalogue"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "1-Click Instant Demo")
        self.assertContains(res, "Practice Arena")
        self.assertContains(res, "Playground Studio")

    def test_cloud_db_status_endpoint(self):
        res = self.client.get(reverse("api_cloud_db_status"))
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("status", data)
        self.assertIn("persistence_mode", data)
        self.assertIn("tables_count", data)

    def test_contests_hub_and_detail(self):
        from django.utils import timezone
        import datetime
        contest = Contest.objects.create(
            title="Weekly Syntax Battle #1",
            slug="syntax-battle-1",
            description="Algorithmic problem solving",
            category="ALGO_SPRINT",
            duration_minutes=30,
            xp_reward=200,
            starts_at=timezone.now(),
            ends_at=timezone.now() + datetime.timedelta(days=7),
            is_active=True
        )
        res = self.client.get(reverse("contests_hub"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Weekly Coding")
        self.assertContains(res, "Weekly Syntax Battle #1")

        detail_res = self.client.get(reverse("contest_detail", args=[contest.slug]))
        self.assertEqual(detail_res.status_code, 200)
        self.assertContains(detail_res, "Weekly Syntax Battle #1")

    def test_contest_submission_api(self):
        from django.utils import timezone
        import datetime
        contest = Contest.objects.create(
            title="Speed Sorting Challenge",
            slug="speed-sort",
            duration_minutes=25,
            xp_reward=150,
            starts_at=timezone.now(),
            ends_at=timezone.now() + datetime.timedelta(days=7),
            is_active=True
        )
        self.client.login(username="testlearner", password="password123")
        payload = {"code": "def solve(data): return sorted(data)"}
        res = self.client.post(
            reverse("api_submit_contest", args=[contest.slug]),
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "PASSED")
        self.assertEqual(data["score"], 100)
        self.assertEqual(data["xp_awarded"], 150)

    def test_certificates_hub_and_verify(self):
        cert = Certificate.objects.create(
            credential_id="CQ-BD-2026-TEST-1119003",
            user=self.user,
            student_name="Test Learner",
            track_slug="python",
            track_title="Python 3 Foundations",
            mastery_score=95,
            is_verified=True,
            qr_data="https://codequest-bd.vercel.app/verify/CQ-BD-2026-TEST-1119003"
        )
        res = self.client.get(reverse("certificates_hub"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Verifiable Professional")

        verify_res = self.client.get(reverse("verify_certificate_view", args=[cert.credential_id]))
        self.assertEqual(verify_res.status_code, 200)
        self.assertContains(verify_res, "CQ-BD-2026-TEST-1119003")
        self.assertContains(verify_res, "Test Learner")
        self.assertContains(verify_res, "95%")

    def test_claim_certificate_api(self):
        self.client.login(username="testlearner", password="password123")
        payload = {
            "student_name": "Md Najmus Sakib",
            "student_id": "1119003",
            "track_slug": "python"
        }
        res = self.client.post(
            reverse("api_claim_certificate"),
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["success"])
        self.assertIn("credential_id", data)

    def test_micro_task_check_api(self):
        mt = MicroTask.objects.create(
            lesson=self.lesson1,
            task_type="CORE_SYNTAX",
            task_number=1,
            title="Micro Task: Heading Attributes",
            instructions="Add class attribute to heading",
            xp_reward=30
        )
        self.client.login(username="testlearner", password="password123")
        payload = {"task_id": mt.id, "code": "<h1 class='title'>Hello</h1>"}
        res = self.client.post(
            reverse("api_check_micro_task"),
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["passed"])
        self.assertEqual(data["xp_awarded"], 30)

    def test_admin_panel_view(self):
        res = self.client.get(reverse("admin_panel"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Command Center")
        self.assertContains(res, "Active Tracks")

        stats_res = self.client.get(reverse("api_admin_stats"))
        self.assertEqual(stats_res.status_code, 200)
        data = stats_res.json()
        self.assertIn("languages", data)
        self.assertIn("courses", data)
        self.assertIn("certificates", data)
