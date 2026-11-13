# INF1103 Lab 8 — Project Plan and Progress

**Baseline:** Active `inf1103-labs` checkout on branch `lab8`, based on `b6aedc0` (Week 7 copied into Week 8). Milestone 0 documentation committed and pushed through `b42fc99`. **Working folder for Lab 8:** `Week8/`; current background documents are in `Week8/Background/`. **Status:** Milestone 0 complete. Milestone 1 Supplier implementation verified: 13 focused tests and 45 total regression tests passed. PF-1 remains deferred; final UML alignment, later features, Docker execution and submission evidence remain pending.

## Milestone rules

Follow the [Copilot instructions](.github/copilot-instructions.md) for every milestone. Use an implementation-first workflow: no teaching sessions, quizzes or understanding gates unless requested. Present the exact files, minimal change, test plan and commit boundary, then wait for explicit edit approval. Implement, verify and briefly explain what changed and why. Record actual hashes only after verification. Ask separately before staging, committing and pushing. Preserve student-authored official Predict First entries before their demonstrations; defer those demonstrations while continuing unrelated implementation if needed.

The boundaries below are proposed. Verify the active repository and existing conventions before using the sample commit messages. The teaching topics and quiz starters below are retained as optional reference material only; do not present them as required steps under the updated workflow.

## Milestones

| Status | Step and teaching topic | Quiz starter | Proposed scope and verification | Suggested commit |
|---|---|---|---|---|
| Complete | 0. Baseline and design. Teach is-a, collaboration, whole–part and lifecycle. Handout §1 is thinking only. | How would you distinguish a reference between collaborators from a reference to an owned part? | Baseline inspected and tested; ownership, multiplicity and types checked. Provisional design recorded in `Week8/Lab8_UML_Design.md`; open decisions remain for their implementation milestones. Docker execution is deferred to Milestone 7. | `docs(lab8): outline typed relationship design` |
| Implementation verified; PF-1 deferred | 1. Supplier association. Object identity, references, annotations and constructor chaining. | Optional reference only under updated workflow. | Supplier injection, CLI creation/reuse, nested JSON, old typed-record migration and fixtures implemented. 13 focused tests and 45 full regression tests pass. Sample JSON unchanged. PF-1 awaits the student's prediction; do not run its deletion demonstration yet. | `feat(lab8): associate products with suppliers` |
| Pending | 2. Inventory aggregation. Teach collections of a base type and object identity during transfer. | What would you compare to prove a transfer used the original object rather than a copy? | `main.py`, `test_products.py`. Annotate collection and operations, preserve duplicate behavior, test present/missing IDs and transfer A → B. Run PF-2 after prediction. | `feat(lab8): add typed inventory transfer operations` |
| Pending | 3. Order composition. Teach lifecycle ownership, delegated totals and encapsulated price access. | Who should create the entries in a shopping basket if they belong to only one basket? Explain your design. | `main.py`, `test_products.py`. Expose price as approved, implement Order and OrderLine, exercise subtotals, a multi-line total and line/order removal. Run PF-3 after prediction. | `feat(lab8): compose orders from order lines` |
| Pending | 4. Type and UML review. Teach multiplicity, optional lookup and the purpose of annotations. | How would you show a lookup that can return zero or one Product in UML and in Python? | Review all Lab 8 attributes and signatures against the draft UML. Close type gaps in `main.py` and update the diagram. Verify relationships, labels and types by inspection and run regression tests after code edits. | `docs(lab8): align UML with typed relationships` |
| Pending | 5. LSP. Teach behavioral contracts, including accepted inputs, stock semantics and return values. | How would you test whether a caller typed as Product can safely use any subtype? | `test_products.py`, with `main.py` changes only if tests reveal a contract gap. Run the same typed detail function with both types, and check successful and rejected stock updates and normal inventory operations. Record the user's diagnosis of the digital override from §6.3. | `test(lab8): verify product substitutability` |
| Pending | 6. Polymorphism. Teach dynamic dispatch through the Product abstraction. | In a loop over Products, what determines which implementation runs for each item? | `test_products.py` and `main.py` only if needed. Run one mixed-inventory loop calling display and fulfilment. Capture both specialized outputs and compare them with PF-4 after prediction. | `test(lab8): demonstrate mixed product dispatch` |
| Pending | 7. Docker and submission. Rehearse ownership, typing and substitution by tracing the demo and explaining the UML. | Which screenshot or test would you use to demonstrate lifecycle ownership, and what does it show? | Verify final diagram against implementation, run full suite and CLI in Docker, collect evidence and check the submission package. Update `Dockerfile` only if the approved file layout requires it. If evidence is submitted separately, finish this step without a repository commit. | `docs(lab8): record final verification and submission evidence` |

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
