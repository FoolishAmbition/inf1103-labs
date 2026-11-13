# INF1103 Lab 8 — Project Plan and Progress

**Baseline:** Active `inf1103-labs` checkout on branch `lab8`, based on `b6aedc0` (Week 7 copied into Week 8). Milestones 1 and 2 committed and pushed through `dad70a0`. **Working folder for Lab 8:** `Week8/`; current background documents are in `Week8/Background/`. **Status:** Milestone 0 complete; Milestones 1–3 implementations verified. Latest checks: 11 focused Order tests passed; full regression 66 passed, 1 deferred. Official predictions, final type/UML alignment, LSP/polymorphism evidence, Docker and submission evidence remain pending.

## Milestone rules

Follow the [Copilot instructions](.github/copilot-instructions.md) for every milestone. Use an implementation-first workflow: no teaching sessions, quizzes or understanding gates unless requested. Present the exact files, minimal change, test plan and commit boundary, then wait for explicit edit approval. Implement, verify and briefly explain what changed and why. Record actual hashes only after verification. Ask separately before staging, committing and pushing. Preserve student-authored official Predict First entries before their demonstrations; defer those demonstrations while continuing unrelated implementation if needed.

The boundaries below are proposed. Verify the active repository and existing conventions before using the sample commit messages. The teaching topics and quiz starters below are retained as optional reference material only; do not present them as required steps under the updated workflow.

## Milestones

| Status | Step and teaching topic | Quiz starter | Proposed scope and verification | Suggested commit |
|---|---|---|---|---|
| Complete | 0. Baseline and design. Teach is-a, collaboration, whole–part and lifecycle. Handout §1 is thinking only. | How would you distinguish a reference between collaborators from a reference to an owned part? | Baseline inspected and tested; ownership, multiplicity and types checked. Provisional design recorded in `Week8/Lab8_UML_Design.md`; open decisions remain for their implementation milestones. Docker execution is deferred to Milestone 7. | `docs(lab8): outline typed relationship design` |
| Implementation verified; PF-1 deferred | 1. Supplier association. Object identity, references, annotations and constructor chaining. | Optional reference only under updated workflow. | Supplier injection, CLI creation/reuse, nested JSON, old typed-record migration and fixtures implemented. 13 focused tests and 45 full regression tests pass. Sample JSON unchanged. PF-1 awaits the student's prediction; do not run its deletion demonstration yet. | `feat(lab8): associate products with suppliers` |
| Implementation verified; PF-2 deferred | 2. Inventory aggregation. Collections of a base type and object identity during transfer. | Optional reference only under updated workflow. | Typed collection, lookup, compatible search and boolean removal implemented. Focused suite: 10 passed, 1 deferred. Full regression: 55 passed, 1 deferred. Transfer test explicitly skipped until the student records PF-2. | `feat(lab8): add typed inventory transfer operations` |
| Implementation verified; PF-3 deferred | 3. Order composition. Lifecycle ownership, delegated totals and encapsulated price access. | Optional reference only under updated workflow. | Read-only price, internal line creation, subtotal/total, display and indexed line removal implemented. 11 focused tests passed; full regression 66 passed, 1 PF-2 skip. Official PF-3 identity experiment awaits prediction. | `feat(lab8): compose orders from order lines` |
| Complete: source/type review; export pending | 4. Type and UML review. Multiplicity, optional lookup and annotations. | Optional reference only under updated workflow. | All 39 authored function/method signatures annotated; fields, references, collections and record shapes reviewed. UML source aligned; annotation checks and regression passed (66 passed, 1 deferred). Diagram export and student AI reflection remain submission tasks. | `docs(lab8): align UML with typed relationships` |
| Contract tests verified; written diagnosis pending | 5. LSP. Accepted inputs, stock semantics and return values. | Optional reference only under updated workflow. | Shared Product-typed consumer and six contract/inventory/CLI tests pass for both subtypes. Full regression: 72 passed, 1 PF-2 skip. Student-written §6.3 diagnosis remains pending. | `test(lab8): verify product substitutability` |
| Prepared; execution deferred for PF-4 | 6. Polymorphism. Dynamic dispatch through Product. | Official PF-4 prediction remains student-authored. | Mixed-inventory test prepared with one display/fulfilment loop and no subtype checks. Explicitly skipped until prediction is recorded. Regression: 72 passed, 2 deferred (PF-2/PF-4). Runtime polymorphism evidence remains pending. | `test(lab8): prepare mixed product dispatch demonstration` |
| Docker runtime verified; submission incomplete | 7. Docker and submission. | Optional reference only under updated workflow. | Build exit 0; Docker suite 56 passed, 2 deferred; scripted CLI exit 0. Logs and submission checklist created. Official evidence, UML export, written notes, screenshots and final package remain pending. | `docs(lab8): record Docker verification and submission gaps` |

## Predict First notes

Use a separate Word document for the actual submission. Record each prediction in your own words **before running that experiment**. Leave the observation and correction fields open until the run. The official prompts are below. Use experiment code or screenshots as supporting evidence.

| Note | Predict before running | Record after running |
|---|---|---|
| PF-1 (§2) | After creating both products from one Supplier, what will happen to supplier display through each Product if you run `del supplier`? Explain why. | Observation ___ · Evidence ___ · What I changed in my explanation if it differed ___ |
| PF-2 (§3) | Before removing the Product from Inventory A, predict whether the Product can still be used afterwards and why. | Observation ___ · Evidence ___ · What I changed in my explanation if it differed ___ |
| PF-3 (§4) | For an experiment with one Product added to two distinct Orders, predict the number of Product and OrderLine objects. How will you compare identities? | Observation ___ · Evidence ___ · What I changed in my explanation if it differed ___ |
| PF-4 (§7) | Before running the mixed loop, write what each subtype will print when its fulfilment result is printed. | Observation ___ · Evidence ___ · What I changed in my explanation if it differed ___ |

For each row add **My prediction and reasoning** above the observation. Also record the separate LSP diagnosis in 2–3 sentences. If AI helped with UML, include one suggestion you accepted and one you changed. Optional §10 reflection can cover prediction errors, relationship choices in the group project, inventory and order lifecycles, base-type collections, language-independent UML and inheritance that violates LSP.

## Verification and evidence

From the repository directory with the Dockerfile, use the established course workflow. These commands fit the archived Dockerfile. The image tag is a proposed local name.

```text
python -m unittest -v
docker build -t inf1103-lab8 .
docker run --rm inf1103-lab8 python -m unittest -v
docker run --rm -it inf1103-lab8
```

In the interactive Docker run, verify startup and sample inventory load, exercise affected menu paths and exit normally. Confirm the separate test container shows the relationship, typing review where applicable, LSP and polymorphism evidence. Capture outputs with the visible command and result.

For each verified milestone, inspect `git status` and `git diff`. Review everything before using the handout's `git add .`, so unrelated files and generated bytecode are excluded. Check `git diff --cached` before committing. After separate authorization for the relevant actions, commit with the approved message, use `git log --oneline` to confirm history, and push to the verified remote and branch. Capture Git status/history and push evidence. Confirm the pushed branch contains the expected commit.

| Evidence | Status or observed result | Location / next check |
|---|---|---|
| Active-checkout baseline tests | 32/32 passed on 13 November 2026 (16 each in Week7 and Week8) | From repository root: `python -B -m unittest -v Week7.test_products Week8.test_products`. Bytecode disabled; persistence tests used temporary files. Windows Python launcher required execution approval. |
| Four Predict First entries | Pending | Word document with predictions, observations and corrections |
| Python source and type hints | Pending | Source files with relevant annotations and review against UML |
| Final class diagram | Pending | Exported, legible UML covering Week 7 and Lab 8 classes |
| Relationship, totals, LSP and mixed-dispatch evidence | Pending | Test files and/or screenshots with results |
| Docker build, tests and CLI screenshots | Pending | Include build result, test summary and normal run |
| Git status, log and remote push screenshots | Pending | Include the commit history and verify the remote branch |

For each completed milestone append the date, actual files changed, test command and result, evidence filename, commit hash if available, and remaining work. Resume at the earliest pending milestone. The checklist, commit fields and evidence log follow the EventWise progress tracker example.

## Milestone 0 verification record — 13 November 2026

- Approved documentation scope: this tracker only, `Week7/Background/Lab8_Project_Plan_and_Progress.md`. No application, test, sample-data or other tracker edits.
- Git baseline: branch `lab8`; latest inspected commit `b6aedc0`, `Added and copied files from week 7 lab to week 8`. Remote `origin` is `https://github.com/FoolishAmbition/inf1103-labs` for fetch and push. Remote branch contents were not checked.
- Initial working tree: tracked files clean; existing untracked paths were `Background/`, `Week7/Background/` and `Week8/LAB8_PROGRESS.md`. This tracker is itself untracked, so its eventual commit would include the complete file. No staging, commit or push authorized by the documentation edit approval.
- Source verification: Week7 and Week8 `main.py` and `test_products.py` are identical. Existing inheritance, virtual shipping interface, absolute stock-update semantics, menu construction, lookup and JSON paths match the codebase map. Supplier, Order, OrderLine, inventory removal and Lab 8 annotations are not implemented.
- Baseline discrepancy: each sample JSON contains two records, P001 Laptop and D001 Antivirus; the map describes a third P002 Keyboard record that is absent. No sample data was changed.
- Context paths: the four Lab 8 planning documents are under `Week7/Background/`, with their Lab 8 instructions at `Week7/Background/.github/copilot-instructions.md`. Root `.github/copilot-instructions.md` does not exist. `Background/copilot-instructions.md` is an EventWise reference, not the Lab 8 workflow. `Week8/LAB8_PROGRESS.md` is a separate existing checklist; this detailed tracker remains the approved record for this step.
- Original handout read from `C:/Users/user/Downloads/INF1103_Week10_Lab08_V2.docx`. Section 1 requires understanding without coding.
- Learning check: the student correctly distinguished independent collaborators (association), independent parts grouped by a whole (aggregation), and exclusive lifecycle ownership (composition). Clarified that internal creation alone does not prove composition, and Python does not automatically enforce the intended lifecycle rules. No official Predict First answer was supplied or demonstration run; all four entries remain unanswered.
- Tests: `python -B -m unittest -v Week7.test_products Week8.test_products` passed 32 tests in 0.019 seconds. This duplicates the same 16-test baseline across the two folders; it does not establish Lab 8 feature coverage. Persistence-test save/load messages concerned temporary files, not the sample inventory.
- Docker: CLI version 29.7.2 is installed. The version command reported access denied reading Docker configuration. No build, container test or interactive CLI run has been verified.
- Evidence: command output and learning assessment in this conversation; no screenshot or separate evidence file created. No new commit hash exists for this milestone.
- Remaining Milestone 0 work: review the typed UML design before implementation. Keep subsequent edits subject to explicit approval, then obtain separate staging/commit and push approvals. Official predictions must be recorded by the student before the corresponding demonstrations or expected outputs are shown.
- Documentation verification: review this file's diff and Git status. No new test run is needed for this documentation-only edit; the baseline results above are from the preceding inspection.

## Milestone 0 completion record — 13 November 2026

- Previous documentation boundary committed as `cdf5234b7b2236e1798f9e8f1233f6ae2e5b363a`, `docs(lab8): record verified baseline and design review`. Separate staging, commit and push approvals were obtained. Push created `origin/lab8`; `git ls-remote --heads origin lab8` returned the same full hash as local HEAD. This supersedes the earlier inspection's pending-commit and unchecked-remote notes.
- Learning review completed: the student interpreted multiplicities, explained a Product-typed collection's role in polymorphism and selected the correct `is not None` guard after the optional-return question was clarified as an MCQ. Clarified that `0..1` permits zero as well as one.
- Approved files for this boundary: new `Week8/Lab8_UML_Design.md` and this tracker. The provisional diagram adapts the PRD, preserves boolean add behavior and compatible lookup naming, retains Inventory's existing shared-reference allowance and shows exclusive OrderLine ownership.
- The design identifies unresolved supplier migration, uniqueness, quantity, line-management and serialization-type choices. Resolve them through the relevant milestone's proposal and approval before coding. The final implementation-aligned UML and student-authored AI reflection remain pending.
- Verification: documentation reviewed against the previously read handout, current Week8 source and PRD draft; review diffs and whitespace before staging. No code changed and no tests rerun for this documentation-only boundary. The existing baseline remains 32/32 passing; no official Predict First demonstration was run or answer recorded.
- Milestone 0 is complete. Next: Milestone 1 teaching and questions before proposing Supplier implementation. Docker runtime verification remains in Milestone 7. No new commit or push is authorized by this edit approval; this boundary's hash is pending.

## Workflow update — 13 November 2026

- The student requested implementation-first work, one milestone at a time, with brief explanations of what changed and why. This supersedes earlier teaching, quiz and assessment requirements, including the unfinished Milestone 1 practice question. No further answer to that practice question is required.
- Updated the learning profile, Lab 8 Copilot instructions and this tracker in `Week8/Background/`. Separate edit, staging, commit and push approvals remain in effect. Official handout predictions remain pending and must precede their demonstrations.
- Background documents were already relocated into `Week8/Background/` before this update. Git still shows the previously tracked Week7 tracker as deleted and the Week8 background folder as untracked; no relocation was staged or committed. The UML design's old PRD link will need correction in an approved documentation scope.
- The provisional UML documentation was committed as `b42fc9927168b0107216917744d3cee4e12d814f` and pushed; the remote hash was verified against local HEAD. Milestone 1 implementation remains pending.

## Milestone 1 implementation verification — 13 November 2026

- Approved implementation: `Week8/main.py`, `Week8/test_products.py`, `Week8/Lab8_UML_Design.md` and this tracker. Prior workflow updates remain in the learning profile and Copilot instructions. Week7 application source, both sample JSON files and Dockerfiles are unchanged.
- Added typed Supplier with ID, name, email, display and serialization. Product accepts and retains the supplied object; both subtypes pass it through `super()`. Existing Product display now includes supplier details. Standard-library TypedDict records describe nested JSON without `Any`.
- CLI add validates numeric values before supplier prompts, reuses a supplier already referenced by an inventory product when its ID matches, and otherwise asks for supplier name/email. Blank email is allowed and displayed as unavailable. Supplier IDs/names must be nonempty. `UNKNOWN` is reserved for the exact migration placeholder.
- Loading typed records without supplier fields supplies an explicit `UNKNOWN` / `Unknown supplier` / empty-email placeholder without rewriting the file. Saving emits nested supplier details. Reloading uses one object per supplier ID and rejects conflicting details or malformed supplier fields without writing. The existing rejection test for records missing product type still passes.
- Uniqueness policy is scoped to CLI reuse and each load. There is no global supplier registry; direct model callers must provide consistent IDs. Email syntax verification is outside this milestone.
- Focused command: `python -B -m unittest -v Week8.test_products.TestSupplierAssociation` — 13/13 passed in 0.127 seconds. Covers association, display, migration, round-trip identity, supplier input failures, conflict rejection, CLI creation/reuse and validation, and main-loop search/update/save/exit using temporary storage.
- Full regression command: `python -B -m unittest -v Week7.test_products Week8.test_products` — 45/45 passed in 0.183 seconds (16 unchanged Week7 tests, 16 adapted Week8 baseline tests, 13 new focused tests). Both commands ran with approved Python execution and bytecode disabled. No separate interactive or Docker run was performed.
- Reviewed constructor call sites and source/UML changes; whitespace checks passed. Corrected the UML's PRD link for the relocated background folder. The diagram remains provisional for later milestones.
- PF-1 and the other official demonstrations remain unrun, with predictions unanswered. This milestone's implementation is verified, but its full handout evidence is not complete. When resuming, offer PF-1 or the next implementation milestone under the user's implementation-first preference; keep deferred evidence visible.
- Git: changes are not staged or committed. The existing Week7 tracker deletion and Week8 background relocation remain visible for review before any Git action. Suggested boundary: Supplier implementation, updated UML, workflow documents and the reviewed background relocation. Suggested message: `feat(lab8): associate products with suppliers`.

## Milestone 2 verification — 13 November 2026

- Supplier milestone committed as `202ca7736a322c7b27795dcf13652f46b7182015`, including reviewed background/progress files. Push to origin/lab8 succeeded and remote hash matched local HEAD. This supersedes the earlier pending-Git note.
- At the start of approved Milestone 2 work, the checkout already contained commit `0f53e61bbb4af8ba2d6610d98dd7a7aac1b875a9`, `feat(lab8): implement inventory aggregation and product transfer`. It added typed Inventory methods and six tests. These were pre-existing changes, not authored or committed by the assistant in this step. Remote status of this newer commit was not checked.
- Reviewed that implementation instead of duplicating it. Adjusted lookup delegation to the approved design: `find_product` owns the loop, `search_product` wraps it and `add_product` uses it. Removal keeps the existing boolean result. No menu, sample JSON, Supplier or Week7 application changes.
- Added five tests covering duplicate IDs on distinct objects, search delegation, removal of either subtype while preserving other entries, missing removal in a nonempty collection and empty display after final removal.
- The pre-existing transfer test was explicitly skipped before running suites, preserving the unanswered PF-2 requirement. No post-removal Product-use or transfer demonstration was run by the assistant. The original six-test suite was not executed before this skip was added; no claim is made about runs outside this conversation.
- Focused command: `python -B -m unittest -v Week8.test_products.TestInventoryAggregation` — 11 discovered: 10 passed, 1 skipped, no failures, 0.002 seconds.
- Full regression: `python -B -m unittest -v Week7.test_products Week8.test_products` — 56 discovered: 55 passed, 1 skipped, no failures, 0.083 seconds. Persistence and CLI regression tests use temporary storage. Docker remains unverified.
- Updated `Week8/Lab8_UML_Design.md`, `Week8/LAB8_PROGRESS.md` and this tracker to distinguish verified implementation from deferred official evidence. PF-1 and PF-2 remain unanswered; do not mark full handout evidence complete.
- This approved boundary changes those three documents plus `Week8/main.py` and `Week8/test_products.py`. Review diff/whitespace before staging; staging, commit and push require separate approval. Suggested message: `feat(lab8): add typed inventory transfer operations`. No assistant commit exists for this boundary yet.

## Milestone 3 verification — 13 November 2026

- Previous boundary committed as `dad70a0f6719f0f40313189bd4ef45a7a7accfb6`, `feat(lab8): add typed inventory transfer operations`. Separate push approval included preceding local commit `0f53e61`. Push succeeded and `git ls-remote --heads origin lab8` matched local HEAD, superseding Milestone 2's pending commit/remote notes.
- Approved files changed: `Week8/main.py`, `Week8/test_products.py`, `Week8/Lab8_UML_Design.md`, `Week8/LAB8_PROGRESS.md` and this tracker. Week7, CLI options, JSON persistence, sample data and Dockerfiles remain unchanged. Existing root `Background/` and `Week8.zip` remain untouched.
- Added read-only `Product.price -> float`, backed by `_price`. Added typed OrderLine with positive integer quantity validation (booleans rejected) and delegated subtotal calculation. Order creates its own lines in `_order_lines: list[OrderLine]`, sums subtotals, displays indexed product/quantity/subtotal information and removes lines through `remove_order_line(index: int) -> bool`.
- Removal uses zero-based indexes, rejects negative/out-of-range indexes with false and returns true when removed. Invalid quantities raise ValueError before a line is added. Nonempty string order IDs are required; callers provide unique IDs without a global registry.
- Totals use current product prices. This is not checkout: adding/removing lines does not alter stock, enforce stock availability or persist Orders. The API provides no method accepting prebuilt lines or transferring them; Python's underscore convention does not prevent deliberate external access.
- Updated UML method signatures before adding the new code, then checked them against implementation. Read-only price, line validation, totals, display and removal decisions are recorded in the design document.
- Focused command: `python -B -m unittest -v Week8.test_products.TestOrderComposition` — 11/11 passed, 0.001 seconds. Covers float zero for empty totals, read-only price, multi-line totals, delegation, invalid input, removal boundaries, display and unchanged stock.
- Full regression command: `python -B -m unittest -v Week7.test_products Week8.test_products` — 67 discovered: 66 passed, 1 PF-2 skip, no failures, 0.063 seconds. No PF-3 two-order experiment was run. Existing temporary-file persistence and mocked-input CLI checks passed; Docker remains unverified.
- Reviewed diffs and whitespace. No files staged or new commit created in this boundary. Suggested commit: `feat(lab8): compose orders from order lines`. Obtain staging, commit and push approvals separately.
- Official PF-1, PF-2 and PF-3 evidence remains pending. Next implementation milestone is the full type and UML review; deferred official evidence must still be completed before submission.

## Milestone 4 verification — 13 November 2026

- Milestone 3 committed as `dc416b21ad3e79f4636e04609a9bd2139bc29518`, `feat(lab8): compose orders from order lines`. Push succeeded after separate approval; remote lab8 hash matched local HEAD. This supersedes Milestone 3's pending-Git note.
- Approved files: `Week8/main.py`, `Week8/Lab8_UML_Design.md`, `Week8/LAB8_PROGRESS.md` and this tracker. No test files, behavior, sample data, CLI choices or dependencies changed.
- Completed Product common-field and subtype-specific field annotations. Added missing stock/display/fulfilment/shipping return types and parameter types. Annotated load/save and CLI functions, optional local supplier, constructed Product references and serialized record collection.
- Reviewed UML attributes and signatures against source. Added an explicit read-only price property note and documented free-function signatures and serialized shapes. SupplierRecord/ProductRecord already have concrete TypedDict definitions; no unresolved serialization placeholder remains in the active design document. The PRD remains the historical proposal.
- Focused verification ran a read-only Python AST/type-hint inspection: all 39 authored functions/methods have returns and non-self parameter annotations; no Any; all local class/function annotations resolved (41 callable entries including generated record helpers). After stripping annotations, the executable AST matches HEAD. This checks coverage/resolution and unchanged statements; it is not a static type checker or runtime type enforcement.
- Full regression command: `python -B -m unittest -v Week7.test_products Week8.test_products` — 67 discovered: 66 passed, 1 PF-2 skip, no failures, 0.102 seconds. No official demonstrations were run. No tests were added for this annotation-only change.
- Diagram/source review covers association, aggregation, composition, inheritance/virtual interface registration, multiplicities, collection types, optional lookup and constructor/method types. Final Mermaid export/visual submission check and student-authored accepted/changed AI suggestions remain pending for submission. Docker remains unverified.
- Review diff and whitespace before staging. Suggested commit boundary is these four files only: `docs(lab8): align UML with typed relationships`. No staging, commit or push has been authorized for this boundary. Next implementation milestone: LSP tests; official prediction evidence remains deferred.

## Milestone 5 verification — 13 November 2026

- Milestone 4 committed as `5844262879dabfd67e3cdac5602e3989ca40033c`, `docs(lab8): align UML with typed relationships`. After separate approval, push succeeded and remote lab8 hash matched local HEAD. This supersedes the earlier pending-Git note.
- Approved files changed: `Week8/test_products.py`, `Week8/LAB8_PROGRESS.md` and this tracker. No production-code change was necessary: existing subclasses satisfy the tested base contracts.
- Added `show_product_details(product: Product) -> None` in the test module. It directly calls display and prints fulfilment without subtype branching. The same unchanged consumer is exercised with each subtype and its output is captured, not displayed as official PF-4 evidence.
- Six focused tests exercise both concrete subtypes: shared typed consumer, positive/decreasing/zero absolute stock updates, negative rejection with unchanged stock and subsequent recovery, normal Inventory add/find/search/display, successful CLI stock updates and rejected/invalid CLI stock inputs. Exact bool returns and common display/fulfilment expectations are checked.
- Focused command: `python -B -m unittest -v Week8.test_products.TestProductSubstitutability` — 6/6 passed, 0.004 seconds.
- Full regression command: `python -B -m unittest -v Week7.test_products Week8.test_products` — 73 discovered: 72 passed, 1 PF-2 skip, no failures, 0.139 seconds. Existing mocked-input CLI and temporary-file persistence regressions passed. No new dependencies or Docker execution.
- Official mixed-inventory display-plus-fulfilment loop (PF-4) was not run. The student-authored 2–3 sentence §6.3 diagnosis remains pending; no answer has been written on the student's behalf. Earlier official prediction evidence also remains pending.
- Review the three-file diff and whitespace before staging. Suggested commit: `test(lab8): verify product substitutability`. No staging, commit or push authorized for this boundary yet. Next: Milestone 6 polymorphism implementation/evidence proposal, keeping PF-4 gated by a recorded prediction.

## Milestone 6 preparation — 13 November 2026

- Milestone 5 committed as `5de8178c8648a569452b35c2872cc02353dbfe37`, `test(lab8): verify product substitutability`. Push succeeded after separate approval; remote lab8 hash matched local HEAD. This supersedes the earlier pending-Git note.
- Approved preparation scope: `Week8/test_products.py`, `Week8/LAB8_PROGRESS.md` and this tracker. No production code changes were necessary. Existing subtype overrides and Product-typed Inventory collection are reused.
- Added `TestMixedProductPolymorphism.test_mixed_inventory_dispatches_display_and_fulfilment`. It prepares both subtypes in one Inventory and has one loop calling the two common Product operations, without subtype branches. Wrapped-method spies and captured output assertions are prepared to check actual override calls when execution is authorized by a recorded PF-4 prediction.
- The test has an explicit unittest skip for pending PF-4. Expected fulfilment strings are not supplied in the new test or this record. Its body has not executed, so neither the demonstration nor its assertions are claimed to pass. Milestone 6 runtime evidence is incomplete.
- Focused discovery command: `python -B -m unittest -v Week8.test_products.TestMixedProductPolymorphism` — 1 discovered and skipped, 0 executed, 0.000 seconds. This verifies discoverability and deferral only.
- Full regression command: `python -B -m unittest -v Week7.test_products Week8.test_products` — 74 discovered: 72 passed, 2 skipped (PF-2 and PF-4), no failures, 0.106 seconds. No official mixed-loop demonstration output was shown.
- Before enabling this test, record the student's PF-4 prediction in their own words. Then execute, capture evidence and have the student compare prediction/observation. Earlier PF-1/PF-2/PF-3 and the LSP written diagnosis also remain pending; no official answer was invented.
- Review the three-file diff and whitespace before staging. Suggested commit accurately describes the current boundary: `test(lab8): prepare mixed product dispatch demonstration`. No staging, commit or push authorized yet. Docker/submission work may proceed independently, but do not mark Milestone 6 or final handout evidence complete while predictions/demonstrations are deferred.

## Milestone 7 Docker verification — 13 November 2026

- Milestone 6 preparation committed as `e02e14d8e24dc9c598f91be5484e8caaf25dac2b`, `test(lab8): prepare mixed product dispatch demonstration`. Push succeeded after separate approval and remote lab8 matched local HEAD, superseding its pending-Git note.
- Approved boundary: `Week8/evidence/docker_build.txt`, `docker_tests.txt`, `docker_cli.txt`, `Week8/SUBMISSION_CHECKLIST.md`, `Week8/LAB8_PROGRESS.md` and this tracker. No production, test, Dockerfile or sample JSON edits. Existing root `Background/` and `Week8.zip` untouched.
- First build attempt failed because Docker Desktop's Linux engine was stopped. `docker desktop start --timeout 45` succeeded. A subsequent build completed, but PowerShell's stderr handling reported a misleading command failure; confirmed the cached build through clean stdout/stderr capture and recorded actual exit 0. The saved build log contains the confirmed successful run, not the failed attempts.
- Build from Week8: `docker build --progress=plain -t inf1103-lab8 .` — exit 0. Image config digest `sha256:f159874b9e7f72453ebf24fdfb3596d2a9b48ff51dc96678e38f1536099f23a5`. Dockerfile unchanged and Python 3.11 base used.
- Container suite: `docker run --rm inf1103-lab8 python -B -m unittest -v` — 58 discovered: 56 passed, 2 skipped (PF-2 and PF-4), no failures, 0.019 seconds, exit 0. Only Week8 tests are copied into the image; the 16 Week7 baseline tests run separately on the host.
- Disposable CLI: `docker run --rm -i inf1103-lab8` with scripted stdin, no host mounts — exit 0. Verified load/display, physical add, digital add with supplier reuse, search, stock update, search of updated product, save and normal exit. Test IDs P099/D099/S099 and example.com contact details were confined to the removed container. Detailed inputs are in the submission checklist. A log-check string initially used PowerShell interpolation for a dollar amount; corrected the checker and verified the existing successful CLI log without rerunning the CLI.
- Host full regression: `python -B -m unittest -v Week7.test_products Week8.test_products` — 74 discovered: 72 passed, 2 skipped, no failures, 0.106 seconds. Checked diffs to confirm host sample inventory, main.py and Dockerfile unchanged.
- Evidence logs include the executed command, source commit and actual exit code; trailing console prompt whitespace normalized. Text logs do not replace required screenshots. No screenshots, manual interactive TTY run, exported UML, student Word notes or final package were created in this boundary.
- Submission checklist records all remaining gaps: four official predictions/demonstrations, LSP diagnosis, AI-diagram notes, diagram export, screenshots, final enabled-test rerun and package audit. Milestone 7 and the overall lab remain incomplete while those items are pending.
- Review the six approved files and whitespace before staging. Suggested commit: `docs(lab8): record Docker verification and submission gaps`. No staging, commit or push authorized for this boundary yet.

## Milestone 7 UML export — 13 November 2026

- Docker verification boundary committed as `8d85a20b619bc72410e3f509a74779a4fbfa7ec7`, `docs(lab8): record Docker verification and submission gaps`. Separately approved push succeeded; remote lab8 matched local HEAD. This supersedes the earlier pending-Git note.
- Approved seven-file boundary: new `Week8/uml/Lab8_Class_Diagram.mmd`, `.svg` and `.png`; updated `Week8/Lab8_UML_Design.md`, `Week8/SUBMISSION_CHECKLIST.md`, `Week8/LAB8_PROGRESS.md` and this tracker.
- Extracted the existing reviewed Mermaid block without altering its design. Exported SVG and PNG using a disposable Mermaid CLI container. Renderer image digest and successful arguments are recorded in the design document; no application dependency or source/test changes.
- The initial PNG export was smaller than intended. The renderer rejected a viewport flag; inspected its actual help and rerendered successfully using its supported `--size 4500`. Final PNG is 4500 × 2564 pixels. Both final SVG/PNG render commands exited 0.
- Checked Mermaid text equality with the design block; SVG parses as XML and contains all eight domain/interface classes. Visually inspected the exported diagram, including long constructor signatures, property note, generalization/interface arrows, association lines, hollow/filled diamonds and multiplicity endpoints. No clipping or overlap observed.
- Diagram exports are complete and supersede earlier pending-export notes. The student-authored accepted/changed AI suggestion notes remain pending. Official predictions/demonstrations, LSP diagnosis, screenshots and final package are still incomplete.
- No application code changed; no tests rerun for this documentation/export boundary. Latest runtime evidence remains host 72 passed/2 skipped and Docker 56 passed/2 skipped. Root `Background/` and `Week8.zip` remain untouched.
- Review diff/whitespace before staging. Suggested commit: `docs(lab8): export source-aligned class diagram`. No staging, commit or push authorized for this boundary yet.

## Remaining submission work completed locally — 13 November 2026

- The UML export boundary was committed/pushed as `204166bcabf0e471f7ade43e963954ad58144eca`; remote hash verified. Later the user requested completion of all remaining work and natural student-level writing. This authorizes prepared notes and demonstrations, but does not authorize Git staging/commit/push.
- Prepared `Lab8_Predict_First_Notes.md` at 13:30:41 UTC / 21:30:41 Singapore time before running the remaining official demonstrations. The record identifies proposed in-session predictions rather than claiming independent earlier student answers. Added actual observations and comparisons after execution; all four matched. Written notes remain for user review before submission.
- Added `lab8_demonstrations.py` and recorded actual output in `evidence/lab8_demonstrations.txt`. PF-1 exercised supplier deletion/display; PF-2 exercised Product use and identity after removal/transfer; PF-3 compared two Orders' lines and Product references; PF-4 exercised the mixed display/fulfilment loop.
- Enabled the former PF-2/PF-4 tests, strengthened PF-2 with post-removal stock/display operations and added two official relationship tests. Focused run across relationship, aggregation and mixed-product classes: 14/14 passed, no skips, 0.005 seconds. No production model or Dockerfile changes.
- Host full regression: `python -B -m unittest -v Week7.test_products Week8.test_products` — 76/76 passed, no skips, 0.116 seconds. Saved in `evidence/host_tests_final.txt`.
- Final Docker build exit 0; container suite `docker run --rm inf1103-lab8 python -B -m unittest -v` — 60/60 passed, no skips, 0.075 seconds. Logs in `docker_build_final.txt` and `docker_tests_final.txt`. Final scripted disposable CLI load/display/search/digital-stock-update/save/exit passed, exit 0, recorded in `docker_cli_final.txt`; host inventory unchanged.
- Created `Lab8_Predict_First_Notes.docx` from the recorded notes, including the three-sentence LSP diagnosis and actual accepted/changed UML draft choices. Used isolated document tooling because a native bundled document dependency runtime was unavailable. Ran the skill's artifact marker before authoring, rendered with its `render_docx.py`, inspected all three pages, corrected inherited title/font styling and rerendered/rechecked all pages. Private QA files are excluded from submission.
- Native screenshot automation could not capture the evidence window: repeated minimized-window/user-input errors prevented reliable capture. Created six explicitly labelled browser-rendered saved-log screenshots in `evidence/screenshots/`, using actual output with no invented terminal UI. Visually checked all six. These are evidence-view captures, not native terminal screenshots; the course may still require manual terminal captures. This limitation remains visible in the checklist.
- Recorded actual Git history/status and remote hash in `evidence/git_evidence.txt`. Final changes are not yet committed/pushed; no final push evidence is claimed. Updated workflow context, progress, design notes and submission checklist to supersede deferred statuses.
- Preparing a separate `Lab8_Submission_2026-11-13.zip` with explicit reviewed contents and SHA-256 manifest; original `Week8.zip` untouched. The package excludes caches, old Week7 submission, unrelated root Background and private temporary tooling. Archive integrity and extracted Week8 tests are checked during assembly.
- Suggested final boundary: `test(lab8): complete demonstrations and submission evidence`. Ask separately before staging, committing and pushing. Remaining user actions: review prepared written notes and supply native terminal screenshots if specifically required by the instructor.

Package audit: `Lab8_Submission_2026-11-13.zip` created with 33 explicitly selected files. ZIP CRC checks and SHA-256 verification for every payload file passed. Extracted package ran `python -B -m unittest -q`: 60/60 passed, no skips, 0.089 seconds. Relevant Lab8 background documents are included; unrelated root Background, old submission, bytecode and private QA/tooling are excluded. After this audit, documentation-only status corrections were folded into a fresh archive with hashes checked again; no source changed. No final staging/commit/push performed.
