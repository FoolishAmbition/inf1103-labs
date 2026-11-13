# GitHub Copilot Instructions — INF1103 Lab 8

## Read project context

Read `AI_Coding_Background.md`, `CODEBASE_MAP_Lab8.md`, `PRD_Lab8.md` and `Lab8_Project_Plan_and_Progress.md` from `Week8/Background/`. Read the original Lab 8 handout when available. Inspect the relevant source, tests, Git status and history before choosing the next single milestone. Use the handout for course requirements and actual source and Git output for baseline and progress. Surface discrepancies before edits.

## Required workflow for every Git milestone

1. **Work one milestone at a time.** Use an implementation-first workflow. Skip teaching sessions, quizzes and understanding checks unless requested. The user's workflow change on 13 November 2026 supersedes the earlier teach/quiz/assess sequence.
2. **Preserve the prediction sequence.** Do not run official demonstrations before recording their predictions. On 13 November 2026 the user explicitly requested assistant-prepared notes in natural student-level wording. Proposed predictions may therefore be prepared in-session before execution, with actual observations added afterwards. Do not claim these were independent or earlier personal predictions. Leave the text available for user review before submission.
3. **Explain briefly.** Report what changed and why after implementation. Understanding checks are not a prerequisite for proposing or implementing an approved change.
4. **Propose and stop.** Show the exact files, methods, intended behavior, risks, regression tests, expected evidence and focused Git boundary. Wait for explicit approval of the proposed edits. If scope changes materially, ask again before widening it.
5. **Implement and verify.** Make only the approved edits. Run the focused tests and full regression suite, inspect the diff and report actual commands, results and any blocked checks. After each prediction experiment, have me record what happened and why I changed my view if it differed. Update progress with verified facts only, within the approved scope.
6. **Suggest a commit.** Present one meaningful message and the intended staged files after verification. Ask separately before staging, committing and pushing. A coding approval does not authorize Git actions. Verify the actual commit with `git log` and capture its hash. Never switch branches, merge, or rewrite history without approval.

## Project constraints

- Keep Python beginner-readable and responsibilities local. Reuse the existing application, tests and Docker workflow.
- Type and retain a separately created Supplier object in each Product. Inventory manages references to existing Products. Order creates and manages OrderLines, and each line references an independent Product. Verify multiplicities against implementation.
- Preserve the existing stock-update contract and demonstrate both Product subtypes through one Product-typed consumer and mixed Inventory. Use direct common-method calls for polymorphism. Keep subtype selection at construction boundaries such as JSON load.
- Preserve CLI and valid Week 7 JSON behavior through a reviewed supplier migration strategy. Keep the rejection test for untyped legacy rows. Review real sample data and update all affected constructor sites.
- Keep my Predict First answers, LSP diagnosis and optional reflection in my own words. Help me document observed results, review the UML against Section 1, and record one AI suggestion accepted and one changed if AI was used for the diagram.
- Treat Docker output, Git log, test results and screenshots as evidence only after they exist. Use the tracker to resume from the first open milestone.

Adapted from the EventWise Copilot example's context, scope, verification and continuation sections.
