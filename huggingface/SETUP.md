# Weekly dataset update setup

ACCESSIBILITY PROGRAMME RUNBOOKS — WEEKLY HUGGING FACE UPDATES

GitHub source: https://github.com/Double-FW/Accessibility_Programme_Runbooks
Hugging Face destination: https://huggingface.co/datasets/GarethFW/Accessibility_Programme_Runbooks
Dataset ID (already filled in): GarethFW/Accessibility_Programme_Runbooks
Secret name: HF_TOKEN (underscore; no hyphen)
No HF_DATASET_ID repository variable is needed for this package.

Work through one stage at a time. You can return to the chat after each stage.
Do not upload this whole setup folder or ZIP to either website.

STAGE 1 — OPEN THE DOWNLOAD
1. Download the ZIP from the chat.
2. Find it in Downloads on your Mac.
3. Double-click the ZIP to open it.
4. Open Accessibility_Programme_Runbooks_Weekly_Update_Setup.
5. You should see UPLOAD_TO_GITHUB, WORKFLOW_TO_COPY.txt,
   START_HERE.txt and CHECKS_AND_SOURCE_INVENTORY.md.
Stop here if following the chat one step at a time. Reply: done.

STAGE 2 — UPLOAD THREE ORDINARY FOLDERS TO GITHUB
1. Open https://github.com/Double-FW/Accessibility_Programme_Runbooks
2. Select the Code tab. Use the default branch (currently main).
3. Choose Add file, then Upload files.
4. On your Mac, open UPLOAD_TO_GITHUB.
5. Drag its THREE folders — huggingface, scripts and tests — together into
   the GitHub upload area. Drag the folders themselves to preserve paths.
   Do not upload the enclosing UPLOAD_TO_GITHUB folder.
6. Check the paths include huggingface/export-config.json,
   scripts/export_huggingface.py and tests/test_runbooks_huggingface.py.
   They must not start with UPLOAD_TO_GITHUB/.
7. Enter the commit message: Add weekly Hugging Face dataset update files
8. Choose Commit changes, directly to main if offered and permitted.
   If GitHub requires a pull request, create it and merge it before proceeding.

STAGE 3 — ADD THE WORKFLOW WITHOUT UPLOADING A HIDDEN FOLDER
1. Open https://github.com/Double-FW/Accessibility_Programme_Runbooks
2. Choose Add file, then Create new file.
3. In Name your file, type exactly:
   .github/workflows/huggingface-sync.yml
   Keep the dot at the beginning. GitHub creates the folders automatically.
4. On your Mac, open WORKFLOW_TO_COPY.txt in TextEdit or another text editor.
5. Use Command+A, then Command+C to copy ALL its contents.
6. Click inside the large GitHub file editor and use Command+V.
7. Check the first line says:
   name: Update Accessibility Programme Runbooks Hugging Face dataset
8. Choose Commit changes. Use: Add weekly Hugging Face workflow
9. Commit directly to main if permitted, or merge the required pull request.
   You do not need to reveal or upload any hidden Mac folder.

STAGE 4 — GIVE THE WORKFLOW ACCESS TO THIS HUGGING FACE DATASET
Never put a token in a public file, screenshot or this chat.
1. Open https://huggingface.co/settings/tokens
2. If reusing your existing fine-grained sync token, edit its permissions so
   the selected repositories include GarethFW/Accessibility_Programme_Runbooks.
   Enable Read contents and Write contents/settings for this selected repo.
   A gated-access permission selected automatically by the interface may remain.
   If the original token value is no longer available, create a new Custom /
   fine-grained token for this dataset instead. Copy its value privately.
3. Open https://github.com/Double-FW/Accessibility_Programme_Runbooks/settings/secrets/actions
4. In Repository secrets, choose New repository secret.
5. Name: HF_TOKEN
6. Secret: paste the actual Hugging Face token value.
7. Choose Add secret. If HF_TOKEN already exists, use its edit button to update
   it when necessary. GitHub will not show the saved value again.
8. Confirm HF_TOKEN appears in the Repository secrets list.
   Secrets are separate from Variables. This package needs no destination variable.

STAGE 5 — RUN THE FIRST UPDATE
1. Open https://github.com/Double-FW/Accessibility_Programme_Runbooks/actions
2. Select Update Accessibility Programme Runbooks Hugging Face dataset.
3. If GitHub asks you to enable Actions/workflows, enable them for this repo.
4. Choose Run workflow. Select main and choose the Run workflow button.
5. Refresh the page if the new run does not appear immediately.
6. Open the newest run and wait for it to finish.
7. A green tick means all workflow steps completed. If it fails, copy the run
   page's link into the chat. Do not send the token.
8. Open https://huggingface.co/datasets/GarethFW/Accessibility_Programme_Runbooks/tree/main
9. Look for README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl,
   synthetic_examples.jsonl, provenance.json, record_schema.json and
   validation_report.json. .gitattributes is expected and is left in place.
10. On the dataset card/viewer, select knowledge_chunks, documents or
    synthetic_examples. The viewer may take time to refresh.

AFTER THE FIRST SUCCESSFUL RUN
The workflow is configured for Mondays at 07:23 UTC (07:23 UK winter time,
08:23 UK summer time). GitHub may delay scheduled runs and may disable them
in public repositories after 60 days of inactivity. Manual Run workflow is
available whenever needed. There is no dependency on this chat staying open.

Edit the GitHub source documents as usual. Only the approved files listed in
huggingface/export-config.json are exported. A newly added document will not
be included automatically: return to the chat to update and review the list.
Do not add live or confidential records to public source files. Existing raw
Hugging Face copies outside the eight generated filenames are preserved but
are not kept in sync. This workflow does not change dataset visibility.

LICENCE AND DRAFT STATUS
The MIT LICENSE and updated RIGHTS.md agree. The licence text is preserved.
A changed LICENSE or RIGHTS.md no longer confirming MIT stops publication
for review. This is still draft guidance for local review/pilot adoption;
weekly publication does not turn it into an approved operational programme.

IF SOMETHING LOOKS DIFFERENT
Stop at the screen you are on and tell the chat what you can see. Screenshots
should exclude any token value. We can work through one action at a time.
