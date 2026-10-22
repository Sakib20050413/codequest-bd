from django.test import TestCase, Client
from django.contrib.auth.models import User
from arena.models import LanguageTrack, ChallengeLevel, QuizQuestion, LabAnnouncement
from accounts.models import StudentProfile
from arena.piston_service import execute_code, evaluate_level_submission


class CodeQuestCoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_student',
            password='password123',
            first_name='Test',
            last_name='Student'
        )
        self.profile = self.user.profile
        self.profile.student_id = '1119999'
        self.profile.xp = 300
        self.profile.save()

        self.track = LanguageTrack.objects.create(
            title='Test C Track',
            slug='test-c-track',
            description='Test track description',
            difficulty='Beginner',
            order=1
        )

        self.level = ChallengeLevel.objects.create(
            track=self.track,
            title='Test Print',
            slug='test-print-level',
            level_number=1,
            engine='CODE_JUDGE',
            story_brief='Story brief',
            instructions_markdown='Instructions',
            starter_code_c='#include <stdio.h>\nint main() { printf("HELLO_CODEQUEST\\n"); return 0; }',
            test_cases=[{'input': '', 'expected_output': 'HELLO_CODEQUEST', 'is_hidden': False}],
            xp_reward=100
        )

    def test_pages_load_successfully(self):
        # 1. Landing Hub
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

        # 2. Tracks Listing
        res = self.client.get('/tracks/')
        self.assertEqual(res.status_code, 200)

        # 3. Track Detail
        res = self.client.get(f'/tracks/{self.track.slug}/')
        self.assertEqual(res.status_code, 200)

        # 4. Level Play Arena
        res = self.client.get(f'/play/{self.level.slug}/')
        self.assertEqual(res.status_code, 200)

        # 5. Blitz Game
        res = self.client.get('/blitz/')
        self.assertEqual(res.status_code, 200)

        # 6. Leaderboard
        res = self.client.get('/leaderboard/')
        self.assertEqual(res.status_code, 200)

        # 7. Formal Proposal
        res = self.client.get('/proposal/')
        self.assertEqual(res.status_code, 200)

    def test_student_level_progression(self):
        self.assertEqual(self.profile.rank_name, "Level 2: DOM Explorer 🚀")
        self.profile.add_xp(400)
        self.assertEqual(self.profile.rank_name, "Level 3: Logic Knight ⚔️")
        self.profile.add_xp(500)
        self.assertEqual(self.profile.rank_name, "Level 4: Full-Stack Samurai 🥷")
        self.profile.add_xp(500)
        self.assertEqual(self.profile.rank_name, "Level 5: BAIUST Grandmaster 👑")

    def test_piston_and_offline_evaluator(self):
        code = '#include <stdio.h>\nint main() {\n    printf("HELLO_CODEQUEST\\n");\n    return 0;\n}'
        eval_res = evaluate_level_submission(self.level, 'c', code)
        self.assertTrue(eval_res['all_passed'])
        self.assertEqual(eval_res['status'], 'ACCEPTED')

    def test_submission_api(self):
        self.client.login(username='test_student', password='password123')
        payload = {
            'level_id': self.level.id,
            'language': 'c',
            'code': '#include <stdio.h>\nint main() {\n    printf("HELLO_CODEQUEST\\n");\n    return 0;\n}'
        }
        res = self.client.post('/api/submit-level/', data=payload, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data['status'], 'ok')
        self.assertTrue(data['evaluation']['all_passed'])
        self.assertEqual(data['earned_xp'], 100)
