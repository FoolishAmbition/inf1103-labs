# INF1103 Lab 8 Inventory Management System

Python 3.11 or newer is required. Run commands from this folder.

```text
python -B main.py
python -B -m unittest -v
python -B lab8_demonstrations.py
```

Docker workflow:

```text
docker build -t inf1103-lab8 .
docker run --rm inf1103-lab8 python -B -m unittest -v
docker run --rm -it inf1103-lab8
```

## Included evidence

- `Lab8_Predict_First_Notes.docx`: four proposed predictions, actual observations/comparisons, LSP diagnosis and UML review notes. Matching Markdown is included for editing.
- `uml/`: editable Mermaid, SVG and high-resolution PNG class diagram.
- `Lab8_UML_Design.md`: relationship/type explanations and record-label definitions.
- `evidence/`: actual command logs and labelled browser captures of saved output.
- `SUBMISSION_CHECKLIST.md`: verification details and remaining review points.
- `SUBMISSION_MANIFEST.sha256`: hashes for every included file except the manifest itself.

Final verification on 13 November 2026: Week8 60/60 tests passed in Docker; host combined Week7/Week8 regression 76/76 passed; no skipped tests. Production sample inventory is unchanged. Tests use temporary storage. The duplicate-ID error printed during the suite is an expected rejection test, not a suite failure.

Predictions were prepared in-session before the remaining demonstrations; observations were added after actual runs. Review the notes before submission. Evidence PNGs show saved log views, not native terminal windows; capture terminal screenshots yourself if the instructor requires that exact format. Final Git commit/push of this evidence still requires separate approval.
