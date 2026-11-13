# Lab 8 submission checklist

Final working-tree verification: 13 November 2026. Last committed/pushed boundary: 204166b; final evidence changes await separate Git approval.

| Requirement | Evidence and status |
|---|---|
| Source and types | main.py and test_products.py; source-aligned design in Lab8_UML_Design.md. |
| Four official demonstrations | lab8_demonstrations.py and evidence/lab8_demonstrations.txt. Proposed predictions recorded before these runs; observations added afterwards. |
| Written notes | Lab8_Predict_First_Notes.docx and matching Markdown. All three Word pages rendered and visually checked. Includes the LSP diagnosis and accepted/changed UML suggestions. User review remains required. |
| UML | uml/Lab8_Class_Diagram.mmd, .svg and .png. Source, XML and visual checks passed; PNG 4500 by 2564. |
| Host regression | evidence/host_tests_final.txt: 76/76 passed, no skips, including 16 Week7 tests. |
| Docker build | evidence/docker_build_final.txt: exit 0. Dockerfile unchanged. |
| Docker tests | evidence/docker_tests_final.txt: Week8 60/60 passed, no skips, exit 0. |
| Docker program | evidence/docker_cli_final.txt: display, search, digital stock update, save and normal exit passed; host inventory unchanged. Earlier add/reuse verification remains in evidence/docker_cli.txt. |
| Evidence images | Six PNGs in evidence/screenshots/ show browser-rendered views of actual saved output. They are explicitly labelled as log views, not native terminal screenshots. Native capture failed because the helper could not capture the minimized evidence window. |
| Git | evidence/git_evidence.txt records history/status and the verified remote hash. Final changes have not been staged, committed or pushed. |
| Package | New root Lab8_Submission_2026-11-13.zip: 33 files with a SHA-256 manifest. ZIP integrity and all payload hashes verified; extracted Week8 suite passed 60/60. Existing Week8.zip is unchanged. |

## Run the submitted project

From the extracted Week8 folder:

```text
python -B -m unittest -v
python -B lab8_demonstrations.py
docker build -t inf1103-lab8 .
docker run --rm inf1103-lab8 python -B -m unittest -v
docker run --rm -it inf1103-lab8
```

Docker copies the application, tests and inventory only. Run the standalone demonstration script with host Python; the corresponding relationship assertions also run in the container tests.

## Review before handing in

Read the prepared notes and ensure their explanations reflect your understanding. The record identifies in-session proposed predictions rather than claiming earlier independent answers. Optional reflection was not invented.

The labelled log-view images preserve actual output but are not native terminal screenshots. If the instructor requires a terminal window, capture the commands above and Git log/status/push in your own terminal. Final Git staging, committing and pushing remain separate approval steps.
