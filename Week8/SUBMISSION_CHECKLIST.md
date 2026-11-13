# Lab 8 submission checklist

Verification date: 13 November 2026 (Asia/Singapore). Runtime source tested at commit `e02e14d`. This is a working checklist, not a declaration that the submission is complete.

| Requirement | Current evidence | Remaining work |
|---|---|---|
| Python source and type hints | `main.py`; source/type review in `Lab8_UML_Design.md` | Include the final verified version in the submission. |
| Automated relationship and LSP checks | `test_products.py`; host suites: 72 passed, 2 skipped | Complete the official deferred demonstrations and rerun affected tests. |
| Supplier association | Implementation and ordinary association tests verified | Record PF-1 prediction, then run the deletion experiment and record observation/comparison. |
| Inventory aggregation | Typed lookup/removal tests verified | Record PF-2 prediction before enabling the skipped transfer test; include post-removal Product-use evidence. |
| Order composition | Single-order subtotal, multi-line total, display and removal tests verified | Record PF-3 prediction, then run the official two-order identity experiment and record observation/comparison. |
| Polymorphism | Mixed-product test prepared but skipped | Record PF-4 prediction, then enable/run the mixed-loop test and record observation/comparison. |
| LSP written diagnosis | Executable stock/substitution checks verified | Student writes the handout's 2–3 sentence diagnosis in their own words. |
| Complete UML | Source-aligned Mermaid in `Lab8_UML_Design.md` | Export a legible diagram and inspect it. Include student-authored notes identifying one AI suggestion accepted and one changed. |
| Predict First Word document | No Lab 8 prediction document created | Include all four student-authored predictions, observations and comparisons, with predictions recorded before their respective demonstrations. `Week7Submission.docx` is a prior artifact, not the Lab 8 prediction document. |
| Docker build | [Build log](evidence/docker_build.txt), exit 0 | Capture the course-required screenshot showing command and result. |
| Docker tests | [Test log](evidence/docker_tests.txt): 58 discovered, 56 passed, 2 skipped, exit 0 | After deferred tests are enabled, rerun and capture final evidence. |
| Docker CLI | [CLI log](evidence/docker_cli.txt), exit 0 | Capture the course-required program-run screenshot. Scripted stdin verified the CLI; no manual TTY screenshot was produced. |
| Git history and push | Milestone pushes verified through `e02e14d` | Commit/push this evidence boundary after separate approvals; capture final Git history/status/push screenshots. |
| Final package | Existing root `Week8.zip` left untouched and not audited | Assemble/review a final package once outstanding evidence is complete. Do not assume the existing ZIP contains current changes. |

## Verified Docker workflow

Run from `Week8/`:

```text
docker build --progress=plain -t inf1103-lab8 .
docker run --rm inf1103-lab8 python -B -m unittest -v
docker run --rm -it inf1103-lab8
```

Docker Desktop initially had no running Linux engine. Starting it allowed the build to proceed. The saved build log is the confirmed successful run, with its actual exit code; it does not include the initial failed attempt. Console output was captured with trailing prompt whitespace removed. The Dockerfile needed no edits and uses Python 3.11.

The CLI verification used `docker run --rm -i inf1103-lab8` with scripted stdin and no host mounts. Actions were: display sample inventory; add physical P099 USB Adapter (25.00, stock 4, weight 0.2) with demo supplier S099; add digital D099 Demo Download (12.50, stock 10, size 100) reusing S099; search P099; update D099 stock to 7; search D099; save; exit with save. Supplier name/email were explicit test data, `Demo Supplier` / `demo@example.com`. The container was removed afterwards; host `inventory.json` was unchanged.

All four official demonstrations remain deferred. Logs verify the executed operations only; text logs do not replace the handout's screenshot requirements.
