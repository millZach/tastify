# Design skill A/B test

Status: Zach completed three pairs using Northline, Playframe, and RIFT, with the same model and reasoning within each comparison. See the [trial review](trial-review.md) for rendered evidence, interaction checks, and conclusions. The protocol and original suggested prompts below are retained as the initial proposal, not a claim that every proposed control was applied in these user-run trials. The tested candidate is preserved at [design v1](skill-snapshots/design-v1.md); no global installation was performed here.

Reviewed candidate: 524 words; SHA-256 `fd9e161e7849cdf8276175c5fa648c35b3112d892d6e7dc5ece662f69cfcf22b`. This hash identifies the frozen v1 snapshot; later revisions are separate candidates.

## What this tests

Does adding this skill improve Astra's output for Zach, beyond the same brief and his existing working instructions? The research and document review are inputs to this hypothesis, not evidence that it works.

## Matched conditions

1. Freeze the skill file and record its SHA-256 before a round. Use a fresh GPT-6-Astra context for every build. Hold reasoning, original prompt, user preferences, starter files, data/assets, tools, dependency versions, and resource allowance constant. Record actual runtime/tool usage and any deviations. Neither builder sees another output or this research conversation.
2. Baseline receives the original task. Treatment receives that identical task plus the exact frozen skill. Keep other available skills and instructions the same; keep the candidate out of automatic discovery in the baseline. Use separate working folders and direct access to the candidate only in the treatment. If skill exposure cannot be verified, report the trial as compromised and rerun with a controlled setup.
3. Let each builder complete its ordinary workflow within the same allowance. Save the untouched final output and its verification report. Do not coach only one side or repair artifacts after seeing which condition produced them. The skill's effect on workflow is part of the treatment.
4. Capture matching desktop and mobile views after fonts/assets settle, plus the same interaction states. Use 1440 × 900 and 390 × 844 by default. Check each prompt's required journey and relevant failure state under the same conditions. Record failures separately from appearance.
5. Randomize A/B labels independently for each pair. Keep the condition mapping out of the review page and critic context. Give Zach working previews and matching screenshots. A fresh critic may score the outputs using only the prompt, confirmed preferences, artifacts, and checks—not the skill, provenance, or builder explanations. Zach's preference is the primary outcome; critic ratings are supporting evidence.

## Suggested prompts

### 1. A distinctive website

> Build a responsive website for Northline, a small Oregon studio making modular desk lamps. Show the lamp, its adjustable configurations, three finishes, dimensions, and a $180 price. Let visitors choose a finish and open an inquiry form that retains their selection. Show clear validation and a local success state; do not send messages or process payments. Create a credible identity suited to the product and use supplied assets where available.

Before running, prepare one shared lamp asset set. Both conditions receive exactly those files; any additional asset-generation allowance must match. The first view, finish selection, and inquiry states are the required captures.

### 2. An everyday app

> Build a responsive daily planning app called Daymark. Users can add tasks with an estimated duration, choose today's priorities, complete tasks, and start or pause a focus timer on a selected task. Persist tasks locally. Include realistic sample tasks, a clear empty state, and feedback for invalid input. Focus on the experience of planning a day and doing the next task.

Check first use, adding/selecting/completing a task, timer start/pause, empty/invalid state, and reload persistence. Capture planning and active-focus views.

### 3. An engineering tool

> Build a responsive panel schedule review tool for a controls engineer. Use a local fixture of circuits with tag, description, voltage, current, assigned panel, and review status. Let the engineer search, filter to items needing review, inspect a circuit, edit its assignment, and mark it reviewed. Keep changes locally and show what is saved. Make units and missing data clear. This is a fixture-based review UI, not a live control or compliance calculator.

Prepare identical fixtures before running, including long labels and missing values. Check search/filter, detail/edit, saved feedback, empty results, and reload persistence. Capture list and detail views.

## Evaluation

For each pair, record a preferred option or tie, why, and 1–5 ratings for task clarity, composition/readability, visual consistency, product fit, and responsive/interaction quality. Keep a separate pass/fail record of required behavior; visual attractiveness cannot erase a broken flow. Note any accessibility or reference-preservation regression.

Updated retention rule following Zach's feedback: the skill must produce a noticeable improvement worth its added workflow and resource cost, with no material behavioral regression. The initial proposal to count preference wins in two of three pairs is insufficient when the differences are barely noticeable. Record preference strength alongside the winner. This is a small pilot, not a general model-performance claim. Ties or mixed results are useful findings. Revise demonstrated weaknesses and repeat affected pairs in fresh contexts. Report all pairs and skill versions, including losses.

Then use a held-out preservation task: make a narrow requested change to an existing branded page. Give both sides the same untouched source and reference screenshots. This checks whether the skill improves detail without gratuitous redesign. Repeated runs and additional domains are needed before claiming reliable general improvement.

## Results

Zach reports no significant improvement and particularly prefers RIFT without the skill. He subsequently clarified a slight preference for Northline with the skill, emphasizing that the difference was barely noticeable. The author's unblinded inspection found a small no-skill edge for Northline, a small skill edge for Playframe, and a clear no-skill edge for RIFT. Author preferences are separate from Zach's. The current draft has not demonstrated consistent improvement. No independent numerical or blinded preference scores were collected. See the [full review](trial-review.md); no revision or new generation trial has been performed.
