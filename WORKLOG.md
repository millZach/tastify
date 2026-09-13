# Design skill worklog

## Outcome and acceptance

Create a compact, usable design skill for GPT-6-Astra, informed by current skills, primary X/Reddit complaints, rendered website inspection, and Zach's preferences. Preserve design variety rather than prescribing one visual template. Research remains outside the runtime skill.

- [x] Research existing design skills (Astra, low reasoning).
- [x] Research X and Reddit criticism with source/access limitations (Astra, low reasoning).
- [x] Inspect Apple and other strong sites visually (Astra, high reasoning).
- [x] Record supplied preferences and subsequent trial feedback; optional aesthetic questions remain unanswered.
- [x] Write a concise skill and validate its structure.
- [x] Independent review at the author's inherited reasoning; simplify and resolve findings.
- [x] Prepare matched prompts, isolated conditions, blind evaluation, and honest test reporting.
- [x] Compare the final artifacts with the requested outcome; distinguish drafted, tested, and installed states.

Latest state: design 6 (Ember stove, v4) is the first trial Zach called a large improvement. His annotated capture still showed the companion-line habit (eyebrow, button reassurance, control caption, scroll cue), so v5 adds mechanical text rules. The skill was renamed `tastify` on 2026-09-11 and now lives at `skills/tastify/SKILL.md`. v3 and v4 are frozen in `evaluation/skill-snapshots/`. v5 is structurally valid and untested. See [design 6 and v5 below](#design-6-result-and-v5--2026-09-11).

## Initial drafting state

2026-09-11: Existing-skill research (eight examples) and community research (nine entries with explicit evidence limitations) complete. Two high-reasoning agents inspected Apple, Stripe, Linear, Aesop, GitHub, and Airbnb. The author also inspected GOV.UK on desktop/mobile and checked selected website/product screenshots. All 30 local screenshot links resolve.

The reviewed skill is 524 words including YAML/headings and passes the bundled validator. The author read the final revision and accepted the scope, faithful-recreation, and responsive-recomposition fixes. Skill SHA-256: `fd9e161e7849cdf8276175c5fa648c35b3112d892d6e7dc5ece662f69cfcf22b`.

At the end of drafting, three matched A/B prompts and a blind evaluation protocol were prepared. Zach subsequently chose Northline, Playframe, and RIFT and built the six sibling projects. See the review below. This remains a provisional skill, not a proven design improvement. No global skill installation or configuration changes were made in this workspace; files are saved locally and no commit/push/deployment was requested or performed.

## Known preferences from Zach's instructions

Clean, modern interfaces; clear hierarchy; focused interactions; breathing room; meaningful animation; avoid crowded pages, excessive cards, scattered controls, and decorative prose. Visual inspection and the actual user journey are required before product handoff. These are existing preferences, not answers to today's questions.

## Open questions

Broader preferred visual character and specific reference preferences remain open. Zach chose the first three comparison prompts and explicitly preferred design-3-noskill to design-3-skill; this does not establish a universal palette or typography preference.

## User trial review — 2026-09-11

Zach built six sibling projects: design-1/2/3 × skill/noskill. He reports no significant improvement and particularly prefers design-3-noskill. Current request is inspection and an assessment, not edits to the sites or skill.

- [x] Inspect all three pairs at matched desktop/mobile sizes.
- [x] Exercise central interactions, especially RIFT entry and project worlds.
- [x] Compare observed choices with the runtime skill and project records; separate evidence from hypotheses.
- [x] Record conclusions and useful next experiment.

The original proposed prompts were superseded in the actual trials by Northline, Playframe, and RIFT. Zach confirmed that model and reasoning were the same within each pair. The review did not reconstruct complete generation logs or independently verify every other condition.

Review saved in `evaluation/trial-review.md`, with matched screenshots and interaction observations in `evaluation/review-2026-09-11/`. Author preference: small no-skill edge for Northline, small skill edge for Playframe, clear no-skill edge for RIFT. The current skill has not demonstrated consistent value. Source websites and `skills/design/SKILL.md` are unchanged. Review is complete; a replacement skill and new generation trials are recommendations, not completed work.

Follow-up: Zach slightly preferred Northline with the skill, but emphasized that the difference was barely noticeable. Updated evaluation acceptance to require a noticeable improvement worth using the skill, beyond counting marginal wins. He suggested subagents as a possible ingredient and requested discussion. No new agent runs or skill revision have been started.

## Two revised candidates — 2026-09-11

Zach requested a skill without subagents, a skill using the proposed independent exploration/critique workflow, and a short open-ended landing-page prompt. The original skill and first-round websites must remain available for comparison. Do not generate new websites as part of this drafting request.

- [x] Draft short, self-contained `design-solo` and `design-team` skills with shared visual criteria.
- [x] Obtain an independent review at the author's inherited model/reasoning and resolve useful findings.
- [x] Prepare one minimal shared prompt and a three-condition comparison protocol.
- [x] Validate both final skills and record hashes, lengths, and remaining limitations.

Candidates: `skills/design-solo/SKILL.md` (362 words), `skills/design-team/SKILL.md` (463 words). Both passed the bundled skill validator. Protocol: `evaluation/round-2.md`. Independent review, accepted fixes, and final hashes: `research/skill-variants-review.md`. The original skill hash is unchanged. Creation and review are complete; no global installation or new website trial has been performed.

## Design 4 review

Zach reports a visible improvement with the revised skills, little difference between solo and team, and approximate generation costs of $2.68 baseline, $3.50 solo, and $10 team. He requests rendered/source review and notes for future tweaks, explicitly no skill changes. Design 5 is still running and is outside this review.

- [x] Inspect the three final pages at matched desktop/mobile sizes and exercise defining interactions.
- [x] Inspect retained concepts and selection records to assess what the workflow contributed.
- [x] Record cost/value conclusions and evidence-based tweak candidates, without editing skills or trial sites.
- [x] Verify skill hashes are unchanged and distinguish fresh checks from prior project reports.

Review saved at `evaluation/design-4-review.md`; new screenshots and interaction observations are in `evaluation/design-4-evidence/`. Finding: improved visual cohesion, no clear team advantage over solo commensurate with its 2.86× reported cost. Notes cover concept divergence, testing the actual primary interaction during selection, retaining the brief's ambition, selective agent use, and allocation of expansion effort. None are applied to the skills. No subagents were used for this review; design 5 and existing trial artifacts were left untouched.

Review complete. All 18 evidence/source links resolve, interaction records contain no driver failures, and all three skill hashes match their pre-review values. The report separates current checks from prior project claims and labels cost figures as Zach's estimates. Broader efficacy remains open pending further trials.

## Design 5 review and consolidation

Zach requests review of all three music-app pages and his annotated screenshots, correcting excessive supporting text, tiny type, and animation clipping in the skill. Retire the team variant and remove the solo workflow guidance. Preserve trial websites and historical skill snapshots.

- [x] Inspect matching desktop/phone renders and main play/edit/pause actions.
- [x] Investigate the reported spiral clipping and record review findings.
- [x] Consolidate into one concise design skill with concrete quality criteria.
- [x] Review and validate the skill; archive old variants and update evaluation references.

Review and revision complete. Fresh desktop/phone checks covered play, first-step editing, and pause in all three versions; solo canvas clipping was reproduced at four widths. The independent document reviewer found no material gaps; its annotation wording was adopted. The final skill contains 458 words including frontmatter/headings and passes `quick_validate.py`. SHA-256: `3862f1c9c37a136a14fde872c6322e3c6aa295d81c7f84e30121f92c7bf6bde2`. Exact v1/solo-v2/team-v2 snapshots retain their original hashes. Only `skills/design/SKILL.md` remains active; the retired folders are removed. Trial source files, global configuration, and installed skills were not modified. No new generation trial, commit, push, or deployment was performed.

## Taste rewrite (v4) — 2026-09-11

Zach asked for a review of the skill with the goal of giving Astra taste closer to a Claude model's. The author reread all research and evaluation records, then viewed the five hero captures side by side (RIFT pair, design 4 solo, design 5 baseline and solo).

Finding: every opening, including the winning no-skill RIFT, is the same template. Small logo left, nav right, mono uppercase eyebrow with a colored dot, giant two-line headline with an accented or italic second line, two lines of body, one pill button with a reassurance line, a 3D or wireframe object on the right, and scattered tiny annotations (figure numbers, coordinates, corner marks, section indices, scroll hints). Headlines are interchangeable mood slogans. v1–v3 never confronted this pattern; v3 in particular reads as a QA checklist with almost no content about choosing well.

- [x] Snapshot v3 exactly (`design-v3.md`, SHA-256 `3862f1c9…bde2`, 458 words).
- [x] Rewrite around checkable taste tests rather than adjectives: a one-sentence concept plus three divergent one-line concepts; composition derived from the subject with worked examples; a subject-swap test for layout and for headline copy; a squint test for dominance; a "what breaks if removed" test for every element, naming the recurring ornament as the layout apologizing for empty space; focal-asset development judged on light, material, edge, and grounding shadow; type, color, and copy rules that pull from the subject rather than prescribe a look; one choreographed signature motion; section economy tied to the focal experience.
- [x] Retain v3's concrete corrections from design 5: type floors, copy pruning that keeps useful labels, motion-extreme and drawing-bounds checks, three-width review, touch targets, and the working-tool branch.
- [x] Validate with `quick_validate.py` ("Skill is valid!"). A colon in the description broke YAML on the first pass and was reworded.

v4: 826 words including frontmatter and headings, SHA-256 `1e90170513335f031701a5c7004ef983d9732d95655cba37fe4ca7b2699bc7e0`. This is longer than the 400–700 range proposed in the existing-skills research; that range was a hypothesis, and the added length is the taste content that earlier versions lacked. Length is a variable to watch if the next trial regresses.

Not done: no generation trial, no global installation, no commit, no changes to trial sites or preference records. The subject-swap and squint tests are the main new hypotheses; the next matched baseline/skill run should check first whether the opening escapes the template above, and second whether Zach finds the difference noticeable.

## Design 6 — running 2026-09-11

Matched baseline/skill trial of v4 (SHA-256 `1e90170513335f031701a5c7004ef983d9732d95655cba37fe4ca7b2699bc7e0`), started by Zach in sibling `design-6-*` projects. Shared brief: Ember, a hand-built cast-iron wood stove; visitors see the fire, adjust airflow and watch the flame respond, and request a $2,400 quote with a local success state. Style, composition, and interactions left to the builder. The skill condition was directed at the file by path; the skill is not installed globally.

Review order once both finish: (1) does the skill opening escape the shared template observed in designs 3–5, (2) is the headline stove-specific or a slogan, (3) annotation count on the first screen, (4) is the airflow response choreographed, then overall preference, behavior, and cost. Zach's noticeable-improvement bar still applies.

## Design 6 result and v5 — 2026-09-11

Both Ember builds completed. Zach reports a huge difference in favor of the skill version, the first trial to clear his noticeable-improvement bar. Isolation check at the six-minute mark: baseline never left its folder; the skill agent read only SKILL.md outside its folder but listed `/home/zach/projects` once, exposing sibling folder names. Full-run recheck is pending the formal review. Recommendation recorded: neutral folder names for future trials.

Zach's annotated capture of the skill version (served on port 5180; baseline was 5179) marks four remaining defects, all one habit: every element gets a companion line. "HAND-BUILT IN VERMONT" above the headline, "Made by hand. Priced at $2,400." beneath a button that already shows $2,400, "A little more air. A little more life." under the control heading "Tend the fire", and a "Meet your stove" scroll cue. The v4 rule (each line exists because the visitor learns or can do something) is satisfiable by rationalization, so it did not bite.

v5 changes, all in `skills/design/SKILL.md`:

- Copy: "Text stands alone." One line per element and no companion line; a fact appears once, so repeats are deleted rather than moved; a hard budget of five text elements on the first screen (headline, one sentence, one action, control labels), with "above five, delete until five."
- Ornament list gains scroll cues.
- Sections open with their content; a heading is reserved for sections the visitor scans as a list.
- Review: for every visible line, name its element and any line that already says it; delete companions and repeats; count the first screen against the budget.

v4 frozen at `evaluation/skill-snapshots/design-v4.md` (SHA-256 `1e90170513335f031701a5c7004ef983d9732d95655cba37fe4ca7b2699bc7e0`). v5: 960 words, passes `quick_validate.py`, SHA-256 `109a2db497ff441fc4da5007ce0b7f61972473ad49687e3f2dbaaa5133eee706`. Untested in generation; the next trial (Foldline paper-puzzle brief, proposed as design 7) should count first-screen text elements and page headings in both conditions before judging anything else.

## Rename to tastify — 2026-09-11

Zach named the skill `tastify`. Folder moved from `skills/design` to `skills/tastify`; frontmatter `name` and title updated; content otherwise identical to v5. Live links in the evaluation files point at the new path; historical review text that names the old path is left as written. Validator passes. SHA-256 after rename: `327c6182b25e34be79d2217dc12ada2493e81159aa575ce6e5eab6a8cd2bfc2b`.

## Open item: publish before/after pages — added 2026-09-11

Once trials are finished, add the rendered trial pages to the public repo and link them from the README as before-skill and after-skill pairs. Plan: for each trial, copy the production build (`dist/`, including generated images and self-hosted fonts) into `examples/design-N/baseline/` and `examples/design-N/tastify/`, keep each pair's brief beside it, and serve them through GitHub Pages so visitors can open the live pages instead of reading source. Confirm each build still runs from a subfolder path before publishing. Not started.

## Designs 8 and 9, Ember rerun, and the examples folder — 2026-09-11

Zach ran three v5 pairs: Ember rerun (`design-6-noskill` vs `design-6as`), Foldline (`design-8-a` vs `design-8-as`), Orrery (`design-9a` vs `design-9as`). Transcript check: all three skill sessions read v5 from the pre-rename path before the folder became `tastify`; the design-9as "No such file" entries are a Playwright results file, unrelated. Zach judged the skill versions decisively better; the author agrees on all three first screens. Baselines reproduced the template on every subject (eyebrow with glyph, accent last line, three-line body, reassurance under the button, object right, handwritten aside).

Remaining defects in skill outputs, noted in the README: section subtitles and footer slogans below the fold in Foldline and Orrery; Orrery keeps the planets right of the headline.

Added `examples/`: `capture.mjs` (Playwright, 1440×900 and 390×844, 2× scale, 2.5 s settle after fonts) and `composite.py` (PIL pair images and the 2×3 grid). Raw captures in `examples/captures/`. README rewritten with the Foldline pair at the top, the grid, all pairs, briefs, and the updated trial table. Live HTML pages are still the open item above. Design 7 was not run.

## Auto-invocation and global install — 2026-09-11

Description rewritten as a trigger pointer (fires on landing pages, websites, app screens, dashboards, components, redesigns, "make it look better", and any HTML/CSS/UI code). Pushed to `main` on GitHub. Installed globally by copying `skills/tastify` into `~/Fleet/managed/agents/skills/tastify` and running Fleet sync; live links exist at `~/.agents/skills/tastify` (Codex/Astra) and `~/.claude/skills/tastify` (Claude Code). The Fleet copy is a copy, not a link: after editing the skill here, re-copy it into Fleet and sync.

## PR #1 (v6) regression and v7 — 2026-09-12

PR #1 merged on GitHub: a blocking device-target question at the top of the skill, mandatory acceptance checks and compliance evidence, and a stricter first-screen counting rule (value and label count separately). 1,591 words. Zach reports a significant regression: pages came out too sparse, with almost no information. Cause, from the text: every rule in v5 and v6 removes (budget, "delete until five", companion lines, a fact appears once, what-breaks, merge sections), nothing requires information to be present, and v6's evidence step rewards deletion because deletions are what it asks the agent to report. The strict counting rule also made dashboards and data-heavy openings impossible to pass.

v7 starts from v5 and keeps three v6 ideas: the counting rule by communicative purpose, writing down what the reference contributes, and an explicit finish condition. Changes:

- Device target is inferred from the brief or existing interface; no signal means desktop and phone. No blocking question.
- Visitor questions: before building, list what a visitor needs answered before acting; each gets a specific answer on the page. Removing an answer counts as breaking in the what-breaks test.
- Companion line is defined (restates, introduces, captions, or reassures about a neighbor); a line that adds a new fact is content.
- The five-element budget applies to a landing page's opening; in a working tool, the data is content and outside the budget.
- Build the page: the first screen is spare, the page below is substantial, list-like sections get real density.
- Review writes two lists: first-screen text with count, and each visitor question with its answering section.

Snapshots: `evaluation/skill-snapshots/tastify-v5.md` (SHA-256 `8f576a1982c50723c74c1c1fdf8465bb766a114e4910a6ee586da53bf291313b`), `tastify-v6-pr1.md` (`4b779fd3a416725acc6d9d37c782801e1f39de40857b871b9401fb16679ca056`). v7: 1330 words, passes `quick_validate.py`, SHA-256 `8f9044dcc6f1dd50b66153c57dbe3fc8a302e7001ff73dd2adf1af2b00fbd036`. Untested in generation; next trial should rerun Foldline and check the opening budget, then whether all three levels, the release date and platforms, and the mailing list have real content below the fold.
