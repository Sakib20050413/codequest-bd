/**
 * CodeQuest BD - Mode 4: Bug-Hunter & Output Blitz Engine
 * 60-Second rapid fire MCQ and output prediction trainer for CSE 324 Lab quizzes.
 */

class BlitzQuizEngine {
    constructor(questions, options = {}) {
        this.questions = questions || [];
        this.currentIndex = 0;
        this.score = 0;
        this.streak = 0;
        this.maxStreak = 0;
        this.multiplier = 1;
        this.correctCount = 0;
        this.timeLeft = 60;
        this.timerId = null;
        this.isGameActive = false;
        this.csrfToken = options.csrfToken || '';

        this.initDOM();
    }

    initDOM() {
        this.timerEl = document.getElementById('blitz-timer');
        this.scoreEl = document.getElementById('blitz-score');
        this.streakEl = document.getElementById('blitz-streak');
        this.multiplierEl = document.getElementById('blitz-multiplier');
        this.questionCard = document.getElementById('blitz-question-card');
        this.progressBar = document.getElementById('blitz-progress-bar');
        this.explanationBox = document.getElementById('blitz-explanation-box');
    }

    start() {
        if (this.questions.length === 0) {
            alert('No quiz questions loaded in bank!');
            return;
        }

        this.currentIndex = 0;
        this.score = 0;
        this.streak = 0;
        this.maxStreak = 0;
        this.multiplier = 1;
        this.correctCount = 0;
        this.timeLeft = 60;
        this.isGameActive = true;

        document.getElementById('blitz-start-screen')?.classList.add('hidden');
        document.getElementById('blitz-game-screen')?.classList.remove('hidden');
        document.getElementById('blitz-end-screen')?.classList.add('hidden');

        this.updateHUD();
        this.renderQuestion();

        if (this.timerId) clearInterval(this.timerId);
        this.timerId = setInterval(() => {
            this.timeLeft--;
            this.updateHUD();

            if (this.timeLeft <= 0) {
                this.endGame();
            }
        }, 1000);
    }

    updateHUD() {
        if (this.timerEl) {
            this.timerEl.textContent = `${this.timeLeft}s`;
            if (this.timeLeft <= 10) {
                this.timerEl.classList.add('text-rose-400', 'animate-pulse');
            } else {
                this.timerEl.classList.remove('text-rose-400', 'animate-pulse');
            }
        }
        if (this.scoreEl) this.scoreEl.textContent = this.score;
        if (this.streakEl) this.streakEl.textContent = `${this.streak}🔥`;
        if (this.multiplierEl) this.multiplierEl.textContent = `${this.multiplier}x`;

        if (this.progressBar) {
            const pct = (this.timeLeft / 60) * 100;
            this.progressBar.style.width = `${pct}%`;
        }
    }

    renderQuestion() {
        if (this.currentIndex >= this.questions.length) {
            this.endGame();
            return;
        }

        const q = this.questions[this.currentIndex];
        const categoryBadge = document.getElementById('blitz-category-badge');
        const questionText = document.getElementById('blitz-question-text');
        const codeBlock = document.getElementById('blitz-code-block');
        const codePre = document.getElementById('blitz-code-content');
        const optionsContainer = document.getElementById('blitz-options-container');

        if (categoryBadge) categoryBadge.textContent = q.category;
        if (questionText) questionText.textContent = q.question;

        if (q.code && q.code.trim()) {
            codeBlock?.classList.remove('hidden');
            if (codePre) codePre.textContent = q.code;
        } else {
            codeBlock?.classList.add('hidden');
        }

        if (optionsContainer) {
            optionsContainer.innerHTML = '';
            const opts = q.options;
            ['A', 'B', 'C', 'D'].forEach(letter => {
                if (!opts[letter]) return;
                const btn = document.createElement('button');
                btn.className = 'w-full text-left p-4 rounded-xl border border-slate-700 bg-slate-900/80 hover:bg-slate-800 hover:border-indigo-500 font-medium text-sm transition flex items-center gap-3 text-slate-200 group';
                btn.innerHTML = `
                    <span class="w-8 h-8 rounded-lg bg-slate-800 group-hover:bg-indigo-600 text-slate-300 group-hover:text-white font-mono font-bold flex items-center justify-center text-xs border border-slate-700 transition">
                        ${letter}
                    </span>
                    <span class="flex-1">${opts[letter]}</span>
                `;
                btn.onclick = () => this.handleAnswer(letter, btn);
                optionsContainer.appendChild(btn);
            });
        }

        // Hide explanation for next question
        if (this.explanationBox) {
            this.explanationBox.classList.add('hidden');
        }
    }

    handleAnswer(chosenLetter, buttonEl) {
        if (!this.isGameActive) return;

        const q = this.questions[this.currentIndex];
        const isCorrect = (chosenLetter === q.correct);

        // Disable all buttons in container
        const allBtns = document.querySelectorAll('#blitz-options-container button');
        allBtns.forEach(b => b.disabled = true);

        if (isCorrect) {
            buttonEl.classList.remove('bg-slate-900/80', 'border-slate-700');
            buttonEl.classList.add('bg-emerald-950/60', 'border-emerald-500', 'text-emerald-200');

            this.streak++;
            if (this.streak > this.maxStreak) this.maxStreak = this.streak;
            this.correctCount++;

            // Update Multiplier
            if (this.streak >= 8) this.multiplier = 5;
            else if (this.streak >= 5) this.multiplier = 3;
            else if (this.streak >= 3) this.multiplier = 2;
            else this.multiplier = 1;

            const addedPoints = q.points * this.multiplier;
            this.score += addedPoints;

            if (window.soundEngine) {
                if (this.streak >= 3) window.soundEngine.playCombo();
                else window.soundEngine.playTone(880, 'sine', 0.1);
            }
        } else {
            buttonEl.classList.remove('bg-slate-900/80', 'border-slate-700');
            buttonEl.classList.add('bg-rose-950/60', 'border-rose-500', 'text-rose-200');

            // Highlight the correct answer
            allBtns.forEach(b => {
                if (b.textContent.includes(q.options[q.correct])) {
                    b.classList.add('border-emerald-500/70', 'bg-emerald-950/30');
                }
            });

            this.streak = 0;
            this.multiplier = 1;
            if (window.soundEngine) window.soundEngine.playError();
        }

        this.updateHUD();

        // Show instant pedagogical explanation
        if (this.explanationBox) {
            const expText = document.getElementById('blitz-explanation-text');
            if (expText) expText.textContent = q.explanation;
            this.explanationBox.classList.remove('hidden');
        }

        // Advance question after delay
        setTimeout(() => {
            this.currentIndex++;
            this.renderQuestion();
        }, 1200);
    }

    endGame() {
        if (!this.isGameActive) return;
        this.isGameActive = false;
        clearInterval(this.timerId);

        if (window.soundEngine) window.soundEngine.playSuccess();

        document.getElementById('blitz-game-screen')?.classList.add('hidden');
        document.getElementById('blitz-end-screen')?.classList.remove('hidden');

        document.getElementById('final-blitz-score').textContent = this.score;
        document.getElementById('final-correct-count').textContent = `${this.correctCount} / ${this.questions.length}`;
        document.getElementById('final-max-streak').textContent = `${this.maxStreak} Combo 🔥`;

        // Submit to API
        this.submitBlitzResults();
    }

    async submitBlitzResults() {
        try {
            const res = await fetch('/api/submit-blitz/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrfToken,
                },
                body: JSON.stringify({
                    score: this.score,
                    correct_count: this.correctCount,
                })
            });
            const data = await res.json();
            if (data.status === 'ok' && data.awarded_xp > 0) {
                const awardBanner = document.getElementById('blitz-xp-awarded-banner');
                if (awardBanner) {
                    awardBanner.textContent = `+${data.awarded_xp} XP Added to your BAIUST Profile! Current Total: ${data.total_xp} XP`;
                    awardBanner.classList.remove('hidden');
                }
            }
        } catch (e) {
            console.error('Blitz score submit failed', e);
        }
    }
}

window.BlitzQuizEngine = BlitzQuizEngine;
