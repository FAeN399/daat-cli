# How to Run This Starter Template

## Prerequisites
- Git installed
- GitHub CLI (`gh`) or Git remote access
- Text editor
- Project board tool (GitHub Projects, Trello, Linear, etc.)

## Step-by-Step Launch

### 1. Clone or Copy (2 minutes)
```bash
# If using as template
cp -r /storage/emulated/0/projects/mystery /storage/emulated/0/projects/your-project-name
cd /storage/emulated/0/projects/your-project-name

# Or clone if forked
git clone <your-fork-url>
cd your-project-name
```

### 2. Fill Your Brief (8 minutes)
Open `PROJECT_BRIEF.md` and replace all `<placeholders>`:
- Define your problem statement
- Set clear outcome & definition of done
- Assign DACI roles
- List top 3 risks/unknowns
- Design your first 48-hour test
- Create 9-item backlog (3/3/3 structure)

### 3. Initialize Git (2 minutes)
```bash
git init
git add .
git commit -m "chore: init project from starter template"
git branch -M main
```

### 4. Create Remote & Push (3 minutes)
```bash
# Using GitHub CLI
gh repo create <org>/<project-name> --public --source=. --push

# OR manually
git remote add origin git@github.com:<org>/<project-name>.git
git push -u origin main
```

### 5. Set Up Project Board (5 minutes)
Create board with columns:
- **Backlog**
- **Ready**
- **In Progress** (WIP limit = 2)
- **Review**
- **Done**

Add your 9 backlog items from the brief.

### 6. Configure CI/Automation (5 minutes)
Edit `.github/workflows/ci.yml` to match your stack:
```yaml
# Update test/build commands for your language/framework
- run: npm test    # or pytest, cargo test, etc.
- run: npm build   # or your build command
```

### 7. Start Your 48-Hour Test (35 minutes)
- Assign first test from brief to team member
- Schedule T+24h check-in (10 minutes)
- Schedule T+48h decision meeting
- Share repo & board links with team
- Begin work on highest priority item

## Daily Operations

### Stand-up (10 minutes/day)
- What shipped yesterday?
- What's in progress? (max 2 items)
- Any blockers?

### 48-Hour Checkpoints
**T+24h**: Quick check - is test running? Any blockers?
**T+48h**: Decision time
- **Keep**: Scale if successful
- **Adjust**: Re-scope if learning indicates pivot
- **Stop**: Document why, move to next test

### Making Changes
1. Create feature branch
2. Make changes behind feature flag
3. Open PR using template
4. Get review (see CODEOWNERS)
5. Merge & deploy

### Recording Decisions
```bash
# Copy ADR template
cp DECISIONS/0001-example-adr.md DECISIONS/$(date +%Y%m%d)-your-decision.md
# Fill it out
# Commit it
```

## Customization

### Update forge.yaml
If using Master Forge MCP, update:
```yaml
project:
  name: your-project-name
  stacks: [your, stack]
  web: { framework: your-framework, language: your-lang }
```

### Update CODEOWNERS
```
# Add your team's GitHub handles
* @your-team
/docs/ @documentation-owner
```

## Success Criteria

By minute 60 you should have:
- ✅ Filled one-page brief
- ✅ Git repo initialized & pushed
- ✅ Project board with 9 items
- ✅ CI placeholder configured
- ✅ First 48h test assigned & started
- ✅ T+48h checkpoint scheduled

## Need Help?

- See `docs/60-minute-start-window.md` for detailed runbook
- Check `DECISIONS/0001-example-adr.md` for ADR format
- Review `.github/` templates for issue/PR formats

---

**Start the clock. Ship fast. Learn faster.**