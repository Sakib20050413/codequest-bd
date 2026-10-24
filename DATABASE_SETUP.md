# CodeQuest BD — Vercel Persistent Database & Auth Integrity Guide

## 1. সমস্যাটির মূল কারণ (Root Cause Analysis)
Vercel একটি **Serverless Stateless Platform**। Vercel-এর প্রতিটি ফাংশন (Lambda) একটি অস্থায়ী (ephemeral) কন্টেইনারে চলে।
- যখন আপনি লোকাল `db.sqlite3` ফাইল Vercel-এ ব্যবহার করেন, তখন Vercel এটিকে `/tmp/db.sqlite3`-এ কপি করে রাখে।
- প্রতিবার যখন ফাংশন ইনঅ্যাক্টিভ হয়ে স্লিপে যায় (কোল্ড স্টার্ট) বা নতুন কন্টেইনার তৈরি হয়, তখন `/tmp` ফাইলটি সম্পূর্ণরূপে মুছে যায় বা ডিফল্ট স্টেট-এ ফিরে আসে।
- ফলস্বরূপ:
  1. নতুন সাইন-আপ করা ইউজার অ্যাকাউন্ট মুছে যায়।
  2. ব্রাউজারের সেশন কুকি ডাটাবেজের সাথে মিল পায় না, যার কারণে ইউজার বারবার লগআউট হয়ে যায়।
  3. স্ট্রিক, অর্জিত XP এবং লেসন প্রোগ্রেস স্থায়ী থাকে না।

---

## 2. স্থায়ী সমাধান (Permanent Solution: Cloud PostgreSQL)
Django-এর সমস্ত ইউজার ডাটা, সেশন এবং প্রোগ্রেস স্থায়ী রাখতে একটি ফ্রি ক্লাউড PostgreSQL ডাটাবেজ (যেমন **Neon Serverless Postgres** বা **Supabase**) যুক্ত করতে হবে।

CodeQuest BD ইতিমধ্যে সম্পূর্ণ রেডি:
- `dj-database-url` ও `psycopg2-binary` ইনস্টল করা আছে।
- `config/settings.py`-তে `DATABASE_URL` বা `POSTGRES_URL` পেলেই স্বয়ংক্রিয়ভাবে ক্লাউড ডাটাবেজ যুক্ত হয়।
- `config/wsgi.py`-তে **Self-Healing Cloud Auto-Migrate Engine** যুক্ত করা হয়েছে, যা নতুন ক্লাউড ডাটাবেজ পাওয়ার সাথে সাথে স্বয়ংক্রিয়ভাবে টেবিল মাইগ্রেট ও কোর্স/লেসন ডাটা সিড করে নেয়।

---

## 3. কিভাবে সেটআপ করবেন (৩ মিনিটের গাইড)

### পদ্ধতি ১: Vercel Dashboard-এর ভেতর ১-ক্লিকে Neon Postgres (সবচেয়ে সহজ)
1. আপনার [Vercel Dashboard](https://vercel.com/)-এ যান এবং `codequest-bd` প্রজেক্টে ক্লিক করুন।
2. উপরের মেনু থেকে **Storage** ট্যাবে যান।
3. **Create Database** বাটনে ক্লিক করে **Postgres (Powered by Neon)** নির্বাচন করুন।
4. Region নির্বাচন করুন (যেমন: `Singapore (sin1)`) এবং **Create & Continue** দিন।
5. আপনার `codequest-bd` প্রজেক্ট সিলেক্ট করে **Connect** করুন।
6. Vercel স্বয়ংক্রিয়ভাবে `POSTGRES_URL` ও `DATABASE_URL` পরিবেশ ভেরিয়েবল সেট করে দেবে।
7. প্রজেক্টটি একবার Redeploy করুন। ব্যস! সব ইউজার ও সেশন এখন থেকে স্থায়ীভাবে ক্লাউডে সংরক্ষিত থাকবে।

---

### পদ্ধতি ২: সরাসরি Neon.tech থেকে ফ্রি ডাটাবেজ নেওয়া
1. [Neon.tech](https://neon.tech/)-এ গিয়ে GitHub দিয়ে সাইন-ইন করুন (সম্পূর্ণ ফ্রি)।
2. **Create Project** দিন (নাম দিন `codequest-db`, Region দিন `Singapore (ap-southeast-1)` বা কাছের কোনো রিজিয়ন)।
3. ড্যাশবোর্ডে **Connection Details** থেকে **PostgreSQL** কানেকশন স্ট্রিং কপি করুন:
   ```text
   postgresql://neondb_owner:npg_xxxx@ep-xyz-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require
   ```
4. Vercel Dashboard-এ যান:
   - `codequest-bd` প্রজেক্ট -> **Settings** -> **Environment Variables**
   - **Key**: `DATABASE_URL`
   - **Value**: আপনার কপি করা Neon কানেকশন স্ট্রিং
   - Environment: `Production`, `Preview`, `Development` (সবগুলো টিক দিন)
   - **Save** ক্লিক করুন।
5. Vercel-এর **Deployments** ট্যাবে গিয়ে সর্বশেষ ডেপ্লয়মেন্টে **Redeploy** বাটনে ক্লিক করুন।

---

## 4. লোকাল টেস্ট ও মাইগ্রেশন টুল (Optional CLI Tool)
আপনি চাইলে আপনার লোকাল কম্পিউটার থেকেই এক ক্লিকে ক্লাউড ডাটাবেজ যাচাই ও মাইগ্রেট করতে পারেন:
```bash
python setup_cloud_db.py "আপনার_কানেকশন_স্ট্রিং"
```
এটি নিজে থেকেই:
1. ক্লাউড ডাটাবেজে কানেক্ট করবে।
2. `migrate` রান করবে।
3. সমস্ত কোর্স, গেম এবং এডমিন ইউজার (`sakib_admin`) সিড করবে।
4. একটি সুন্দর ভেরিফিকেশন রিপোর্ট প্রিন্ট করবে।

---

## 5. লাইভ স্ট্যাটাস চেক (Live Database Status Endpoint)
আপনার সাইট এখন ক্লাউড ডাটাবেজে চলছে কিনা তা সরাসরি ব্রাউজারে দেখতে পারবেন:
[https://codequest-bd.vercel.app/api/cloud-db-status/](https://codequest-bd.vercel.app/api/cloud-db-status/)

এই এন্ডপয়েন্টটি জানাবে:
- ডাটাবেজ ইঞ্জিন (`postgresql` নাকি `sqlite3`)
- পারসিসটেন্স মোড (`Persistent Cloud Storage` নাকি `Ephemeral`)
- মোট ইউজার, কোর্স ও লেসন সংখ্যা।
