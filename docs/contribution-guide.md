## 🧠 Refactored Final Additions (plug these into your doc)

---

### 🔐 Protected Branches

| Branch | Rule                                                 |
| ------ | ---------------------------------------------------- |
| `main` | Protected. PR only. Only Mamun can merge.            |
| `dev`  | Semi-protected. PR only. Reviewer approval required. |

Enable GitHub protection for both: tests must pass, reviews required.

---

### 🧱 Branch Naming Rules

* Format: `type/short-task-name`
* Use **kebab-case**
* 1 branch = 1 clear task

**✅ Examples**:

* `feature/add-search-endpoint`
* `bugfix/fix-json-parser`
* `docs/update-api-guide`

---

### ✍️ Commit Format (Strict)

Use:

```bash
<type> #<issue>: <module>: short summary
```

**✅ Examples:**

```
feat #12: api: add /search route
fix #33: captcha: handle timeout fallback
docs #21: logger: document rotating logs
```

---

### 🔍 PR Approval & Merge Rules

* All PRs target `dev`
* Must link issues: `Closes #xx`
* Must pass lint/tests
* Must be reviewed by at least 1 team member

---

### 🧹 Branch Cleanup

After merge:

* Delete the branch
* Use GitHub’s “auto-delete branch” setting

---

### ✅ CI & Linting

Every push must:

* Pass unit tests (`pytest`, etc.)
* Pass linting (`black`, `isort`, etc.)
* Failures = no merge

---

### 🧠 Add this at the very end:

```md
---
🧠 This guide is enforced by discipline, not suggestion.  
If you bypass the flow, you risk breaking the entire pipeline.  
Ship like it’s production. Always.
```

---

