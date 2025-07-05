
# 🧠 Branch Management Guide — Datastrike Discipline

Built for backend ops where chaos is death.
Follow this flow to keep your Git branches lean, traceable, and deployment-ready under fire.

---

## 🔐 Branch Strategy & Protections

| Branch | Purpose                      | Protection Rules                                         |
| ------ | ---------------------------- | -------------------------------------------------------- |
| `main` | ✅ Production. Always stable. | 🔒 PR only. Mamun merges. All tests + 1 review required. |
| `dev`  | 🚧 Active integration branch | 🔐 PR only. Review + CI required. No direct commits.     |

**⚠️ No one pushes to `main` directly.** PRs to `main` happen **only after QA’d `dev`**.

---

## 🧩 Allowed Branch Types

| Prefix        | Purpose                                   | Example                          |
| ------------- | ----------------------------------------- | -------------------------------- |
| `feature/`    | 🚀 New features                           | `feature/add-search-endpoint`    |
| `bugfix/`     | 🐛 Bug fixes                              | `bugfix/fix-scraper-timeout`     |
| `hotfix/`     | 🔥 Urgent prod fix                        | `hotfix/fix-login-error`         |
| `refactor/`   | 🔄 Code cleanup, no behavior change       | `refactor/extract-logger`        |
| `chore/`      | 🧹 Maintenance (deps, CI, config)         | `chore/update-pydantic`          |
| `docs/`       | 📚 Documentation updates                  | `docs/update-contribution-guide` |
| `experiment/` | ⚗️ Prototyping/spike work                 | `experiment/async-task-runner`   |
| `backup/`     | 🧯 Temp backup branch (local if possible) | `backup/old-price-watcher`       |

---

## 🧱 Naming Rules (Strict)

* Format: `prefix/short-kebab-case-description`
* Only use approved prefixes (see above)
* Max 5–6 words per branch name

✅ Examples:

```
feature/add-csv-exporter
bugfix/handle-missing-prices
docs/refresh-api-readme
refactor/unify-logger
```

---

## ✍️ Commit Message Format

```bash
<type> #<issue>: <module>: short summary
```

✅ Examples:

```bash
feat #22: api: add /search endpoint
fix #18: captcha: handle token expiration
refactor #11: exporter: split Excel writer
docs #31: readme: add install steps
```

> 🔗 Always reference an issue with `#id` and use precise modules.

---

## ✅ Pull Request Rules

| Rule            | Description                                              |
| --------------- | -------------------------------------------------------- |
| 🔗 Issue Linked | Every PR must close/fix/refer to an issue (`Closes #xx`) |
| ✅ CI Passed     | Tests + lint must pass before merge                      |
| 👀 Reviewed     | At least **1 reviewer** must approve                     |
| 🧹 Clean        | No `.env`, `.db`, `.log`, or temp files committed        |
| 🧱 Naming       | Branch name must follow format                           |
| 🔒 Merge        | Only Mamun merges into `main`                            |

> PRs must be opened **against `dev`** unless it’s an emergency `hotfix`.

---

## 🧼 Branch Lifecycle

| Branch Type    | Delete After Merge? | Notes                          |
| -------------- | ------------------- | ------------------------------ |
| `feature/*`    | ✅ Yes               | 1 feature per branch           |
| `bugfix/*`     | ✅ Yes               | Small and scoped               |
| `refactor/*`   | ✅ Yes               | Keep clean post-merge          |
| `chore/*`      | ✅ Yes               | Maintenance only               |
| `docs/*`       | ✅ Yes               | Markdown/docstring only        |
| `hotfix/*`     | ✅ Yes               | Merge into both `main` + `dev` |
| `experiment/*` | ⚠️ Maybe            | Delete if not promoted         |
| `backup/*`     | ❌ Local only        | Never long-term in remote      |

---

## 📆 Stale Branch Protocol

* ⏱ Any branch inactive >30 days = flag for review
* ❌ Inactive >60 days = delete unless archived with purpose
* Use `git branch --merged` regularly to check for cleanup

---

## 🛠 Git Commands for Cleanup

```bash
# View branches already merged (safe to delete)
git branch --merged

# Delete local branch (safe)
git branch -d branch-name

# Force delete local branch (unsafe)
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

---

## 🌟 Branching Pro Tips

* Always branch off latest `dev`
* Pull `dev` before branching: `git checkout dev && git pull`
* Rebase before pushing: `git pull --rebase origin dev`
* Keep branches <300 lines of diff to ease PR review
* Open PRs early — feedback is fuel, not failure
* Delete branches after merge — don’t litter the repo

---

## 🔥 Summary Checklist

✅ Use only allowed prefixes
✅ Follow kebab-case naming
✅ Delete branches post-merge
✅ PRs must link issues
✅ No direct `main` pushes
✅ Pass CI before merge
✅ Keep feature branches scoped
✅ Document everything in `docs/`

---

> 📎 Pin this file in `docs/branch-management.md`
> 📘 Reference it in `README.md` and `CONTRIBUTING.md`
> 🔒 Enforce via GitHub branch protection + PR templates

---

🧠 Discipline isn't a suggestion — it's a weapon.
This isn’t just a branching strategy.
This is backend architecture enforcement at the team level.

---

