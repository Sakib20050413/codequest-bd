import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from learn.models import Language, Course, Lesson, Game, Badge, UserProfile, UserProgress


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
        self.assertContains(res, "playgroundCode")

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
