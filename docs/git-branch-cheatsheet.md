
# 🧠 Git Branch Discipline Guide – Datastrike Standard

**For backend engineers building sovereignty, not spaghetti.**
This guide defines **exact branching, commit, and PR protocols** — no chaos, no cowboy coding.

---

## 🧭 Branch Strategy Overview

| Branch    | Purpose                               | Rules                                                                            |
| --------- | ------------------------------------- | -------------------------------------------------------------------------------- |
| `main`    | 🔒 Production-ready, stable code only | Protected. Only merge via PRs from `develop`. All tests **must** pass.           |
| `develop` | 🚧 Active development zone            | All features and fixes branch off here. Must be tested before merging to `main`. |

---

## 🔧 Branch Prefixes

| Prefix                | Use Case                              | Example                       |
| --------------------- | ------------------------------------- | ----------------------------- |
| `feature/`            | 🚀 New features                       | `feature/search-endpoint`     |
| `bugfix/`             | 🐛 Fixing bugs                        | `bugfix/fix-price-parsing`    |
| `hotfix/`             | 🔥 Emergency production fixes         | `hotfix/fix-login-crash-prod` |
| `docs/`               | 📚 Docs-only changes                  | `docs/contributing-guide`     |
| `chore/`              | 🧹 Non-functional dev tasks           | `chore/update-dependencies`   |
| `refactor/`           | 🔄 Code cleanups (no behavior change) | `refactor/extract-exporter`   |
| `spike/` *(optional)* | ⚗️ Experimental/prototype branches    | `spike/test-new-parser`       |

---

## 🌈 Naming Style Rules

* Use **kebab-case**: `feature/add-user-auth`
* Be descriptive and short (max 5 words)
* 1 branch = 1 purpose. No multipurpose mega-branches.

---

## ✍️ Commit Message Format

```bash
<type> #<issue_number>: <module>: <short summary>
```

### ✅ Examples:

```
feat #12: search: add Amazon scraping logic
fix #18: captcha: handle token timeout fallback
refactor #21: exporter: extract Excel logic
docs #5: contribution-guide: add PR checklist
```

### 📘 Allowed types:

* `feat`: New feature
* `fix`: Bug fix
* `docs`: Markdown or docstring changes
* `refactor`: Code cleanup, no logic change
* `chore`: Config/tools/deps
* `test`: Add/update tests
* `hotfix`: Emergency production bug

---

## 🔗 Issue Linking Rules

* Every branch **must** have an open issue (use GitHub Issues or Projects)
* In commits and PRs:

  * ✅ `Closes #42` → auto-closes the issue when merged
  * ✅ `fix #42` in commit links the task

---

## 📤 Pull Request Protocol

| Step | Requirement                                             |
| ---- | ------------------------------------------------------- |
| 🔗   | PR must link to a GitHub Issue (`Closes #xx`)           |
| ✅    | All tests and lint checks must pass                     |
| 👀   | At least 1 reviewer approval before merge               |
| 📋   | Use PR template with checklist                          |
| 🧹   | Delete branch after merge (enforce via GitHub settings) |

---

## 🛡️ Branch Protection Rules (enforced on GitHub)

* `main` is protected:

  * No direct commits
  * PRs only
  * Tests + linters must pass
  * Require PR review
* `develop` is semi-protected (optional)

[🔗 GitHub: Managing Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule)

---

## ⚗️ Spike Branches (optional)

* Used for unstable, throwaway experiments
* Never merge into `develop` or `main` directly
* If valuable, convert into a `feature/` branch with proper review

---

## 💡 Pro Tips

* Rebase before pushing large changes: `git pull --rebase origin develop`
* Use `draft PRs` to get feedback early
* Keep PRs focused: <300 lines changed is ideal
* Never commit `.env`, `.db`, or local `.log` files
* Enforce `.gitignore` hygiene — protect your repo from noise

---

## 🧠 Summary

| Rule                     | Reason                    |
| ------------------------ | ------------------------- |
| No direct `main` commits | Prevents production leaks |
| Prefix all branches      | Instant readability       |
| Use kebab-case           | Consistency               |
| Link issues in commits   | Full traceability         |
| Protect `main`           | CI/CD readiness           |
| Spike branches ≠ prod    | Keep experiments isolated |

---

