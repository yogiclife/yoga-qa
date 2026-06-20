# Maintainers Guide

## Project purpose

This repository hosts the Yogic Life Q&A website. It collects question-answer pairs from teachers and publishes them as a searchable MkDocs website.

## Website

https://yogiclife.github.io/yoga-qa/

## Repository

https://github.com/yogiclife/yoga-qa

## Main components

1. **Google Form**
   Teachers submit Q&A pairs.

2. **Google Sheet**
   Stores form responses.

3. **Google Apps Script**
   Validates submitter email addresses, creates Markdown files, saves a backup copy to Google Drive, and uploads the file to GitHub.

4. **GitHub repository**
   Stores the Markdown files and website source.

5. **GitHub Actions**
   Regenerates topic index pages, builds the MkDocs site, and deploys it to GitHub Pages.

## Content flow

```text
Google Form submission
→ Apps Script validation
→ Markdown file created
→ Google Drive backup saved
→ Markdown file uploaded to GitHub
→ GitHub Action runs
→ Topic README files regenerated
→ MkDocs website rebuilt
→ GitHub Pages website updated
```

## Topic folders

**Q&A files are stored under:**

```text
docs/food/
docs/philosophy/
docs/mind/
docs/mind-body-connection/
docs/sadhana/
docs/yogic-life/
docs/ethics/
docs/creation-cycle/
docs/miscellaneous/
```

Each topic folder has a `README.md` generated automatically by:

```text
scripts/generate_indices.py
```

**Do not manually edit topic `README.md` files unless necessary**, because they may be overwritten automatically.

## Adding approved contributors

Approved contributor emails are listed in the Google Apps Script inside the `trustedEmails` array.

To add a new teacher:

1. Open the Apps Script project.
2. Open `Code.gs`.
3. Add the teacher's email to `trustedEmails`.
4. Save the script.
5. Test with one submission.

## GitHub token

The Apps Script uses a GitHub fine-grained personal access token stored in Script Properties:

**`GITHUB_TOKEN`**

The token should have access only to this repository:

**`yogiclife/yoga-qa`**

Required permissions:

* **Contents:** Read and write
* **Metadata:** Read

If GitHub uploads stop working, check whether the token has expired or been revoked.

## If GitHub upload fails

The Q&A file is still saved in Google Drive under:

```text
Yoga QA Review/
```

The submitter receives an email saying that the submission was saved but not published.

To republish manually:

1. Find the `.md` file in Google Drive.
2. Upload it to the appropriate folder under `docs/`.
3. Commit the change.
4. GitHub Actions will rebuild the site automatically.

## Important maintenance files

* `mkdocs.yml`
* `.github/workflows/mkdocs.yml`
* `scripts/generate_indices.py`
* `docs/index.md`
* `Code.gs`
* `GitHub.gs`

## Website homepage

The homepage text is stored in:

```text
docs/index.md
```

## Succession

The repository owner has designated a GitHub successor.

At least one trusted teacher should also have:

* collaborator access to the GitHub repository;
* editor access to the Google Form;
* editor access to the Google Sheet;
* editor access to the Google Apps Script project.

## Routine checks

Occasionally verify that:

1. A form submission creates a Google Drive backup.
2. A Markdown file appears in GitHub.
3. GitHub Actions complete successfully.
4. The website updates.
5. Search works correctly on the website.

## Recovery procedure

If the website stops updating:

1. Verify that GitHub Actions are succeeding.
2. Check whether `GITHUB_TOKEN` has expired.
3. Verify that the Apps Script trigger is enabled.
4. Confirm that form submissions are reaching the Google Sheet.
5. Look in `Yoga QA Review/` for backup copies.
6. Upload any missing `.md` files manually to GitHub.
7. Commit the changes to trigger a rebuild.

No Q&A content should be lost, because all submissions are backed up in Google Drive.
