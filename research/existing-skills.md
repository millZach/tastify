# Existing frontend skills: what a short design skill should retain

Research date: 2026-09-11. Primary source files were fetched directly from GitHub; sizes below count whitespace-separated words in `SKILL.md`, including frontmatter and code. They are not model token counts or total package sizes. Observations describe instructions, not demonstrated effectiveness. Recommendations and failure predictions are inference; no comparative generation benchmark was run.

## Recommendation

Write an original, roughly 400–700-word skill organized around decisions and visual feedback. This length is a proposed experiment, not a proven optimum. Preserve the brief and existing identity; identify the surface's main user job; choose a coherent visual direction tied to its content; implement the actual workflow; inspect the rendered result; fix the largest mismatch. Keep optional references outside the core. Avoid importing aesthetic catalogs, fixed technology preferences, mandatory image generation, or exhaustive lists of forbidden trends.

The strongest transferable distinction is between persuasive pages and operational software. The strongest verification instruction is to compare the actual render with the actual reference and exercise the main flow. Neither depends on making every project visually extravagant.

## Compared examples

| Example | Root size | Observed approach | Transfer / likely limitation (inference) |
|---|---:|---|---|
| Anthropic frontend-design | 1,516 words | Subject-specific direction, small token plan, review before build, restraint and screenshot critique. Explicit brief overrides warnings about common looks. | Retain contextual choice and restrained emphasis. A long trend blacklist may become its own aesthetic bias. |
| Impeccable v4.3.1 | 1,562 words, plus scripts/playbooks | Product context, preservation versus replacement, surface modes, routed commands, bounded browser passes. | Retain surface mode and incumbent identity. Full package is much more than the root's word count suggests. |
| Taste v2 experimental | 12,853 words | Brief inference, aesthetic dials, design-system mappings, extensive technical/style appendices. Explicitly excludes dashboards and complex product UI. | Retain a one-sentence interpretation of the brief. Too broad and lengthy for this short general-purpose skill. |
| Taste v1 | 2,937 words | Default variance/motion/density 8/6/4, stack preferences, style bans, creative pattern catalog. | Useful contrasting baseline: fixed expressive defaults risk becoming a replacement template. |
| UI UX Pro Max | 2,118 words, plus searchable data | Prioritized quality categories, design-system search, narrow domain search for targeted work, persisted master/page overrides. | Retain task-sized retrieval and priorities. Database output is a candidate, not evidence that a design fits. |
| Vercel web-design-guidelines | 176 words, plus 1,012-word fetched command | Thin review wrapper that fetches current rules and returns file/line findings. | Keep detailed audits optional. Short entry point does not mean low total context cost or visual evaluation. |
| OpenAI frontend-app-builder | 4,467 words | Image-generated concepts, detailed spec extraction, faithful implementation, browser and image comparison. | Retain reference fidelity and real workflow checks. Mandatory concept generation is excessive for many ordinary changes. |
| Anthropic webapp-testing | 501 words, plus helper/examples | Inspect rendered state, discover selectors, act through Playwright; server lifecycle helper. | Retain inspection before action and functional checks. A testing toolkit alone does not supply visual judgment. |

### 1. Anthropic frontend-design

The current file grounds choices in subject, audience, and purpose. It asks for a compact palette/type/layout plan, reviews generic choices before coding, concentrates boldness, and checks responsive behavior, keyboard focus, reduced motion, and screenshots. Its explicit reference-precedence clause matters: familiar aesthetics are legitimate when requested. Copy guidance emphasizes clear actions and useful empty/error states. [Exact SKILL.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md).

**Inference:** retain the decision structure, not its full enumeration of currently fashionable looks. Its premise that a client rejected cliché proposals should not become an invented fact in every project. Existing operational interfaces often need continuity more than novelty.

### 2. Impeccable

The root distinguishes Persuade, Operate, Read, and Experience by the individual surface's user outcome. It says refinement preserves identity and behavior, while redesign replaces the visual world within product constraints. It loads project context through a launcher and routes into playbooks; inspection is bounded to a batched pass, batch fixes, and at most one confirmation. [Exact root](https://raw.githubusercontent.com/pbakaus/impeccable/cb56ed6c19a07329a9fa0cd4e657bee040156593/.agents/skills/impeccable/SKILL.md).

The separate 881-word craft floor contains both usability checks and aesthetic prescriptions, including type/radius limits and illustration constraints. [Exact craft floor](https://raw.githubusercontent.com/pbakaus/impeccable/cb56ed6c19a07329a9fa0cd4e657bee040156593/.agents/skills/impeccable/reference/craft-floor.md).

**Inference:** surface-specific priorities are more reusable than a global style. Borrow the distinction without imposing extra context files or launcher dependencies. A strict two-pass ceiling can conflict with fixing a known material defect; use evidence-driven stopping instead.

### 3–4. Taste v2 and v1

V2 starts with brief inference and an explicit design read, allows conversational dial overrides, maps briefs to systems, includes redesign preservation, and scopes itself to landing pages, portfolios, and redesigns. Its extensive appendices and implementation recipes make it the largest root examined. [Exact v2](https://raw.githubusercontent.com/Leonxlnx/taste-skill/ccbc15639c97057cbfcf32ecebc38ef716e4bb37/skills/taste-skill/SKILL.md).

V1 defaults to elevated variance and motion, prescribes React/Next and Tailwind, restricts icon libraries, and includes font/color prohibitions and animated bento recipes. Its header explicitly identifies it as the compatibility version. [Exact v1](https://raw.githubusercontent.com/Leonxlnx/taste-skill/ccbc15639c97057cbfcf32ecebc38ef716e4bb37/skills/taste-skill-v1/SKILL.md).

**Inference:** a short interpretation of the task is useful; numeric dials are less useful unless tied to observable acceptance criteria. A fixed animation increase during preservation work can alter the experience without solving a user problem. Replacing one default font and palette with another is not a reliable route to distinctiveness.

### 5. UI UX Pro Max

The current root instructs a full design-system search for new directions, one domain search for targeted concerns, and stack-specific retrieval when relevant. It prioritizes accessibility and interaction ahead of visual style and keeps fuller rules in references. The root advertises a substantial local dataset; those counts were read, not independently audited. [Exact SKILL.md](https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/7f69fed6a2717900085f1bc3b263721f8ba025e2/.claude/skills/ui-ux-pro-max/SKILL.md).

**Inference:** retrieve only the knowledge the decision needs. A product-category palette generator may accelerate ideation but cannot replace inspecting real content, brand assets, or user workflows. Do not reproduce its database or universal numeric heuristics in the short core.

### 6. Vercel web-design-guidelines

This is a review skill, not a design generator: it fetches a rules file, inspects specified source, and emits concise locations and findings. [Exact wrapper](https://raw.githubusercontent.com/vercel-labs/agent-skills/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md). Its retrieved rules cover semantics, focus, forms, motion, performance, and copy; they also prescribe title case. [Fetched command](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md).

**Inference:** useful example of keeping detailed audits out of the main skill. Static review cannot establish whether the rendered composition works. Its title-case preference conflicts with Anthropic's sentence-case preference, illustrating why brand voice should outrank borrowed house styles.

### 7. OpenAI frontend-app-builder

This public plugin skill defaults to Image Gen concepts, complete surface planning, extracted design tokens, working UI, and reference fidelity. It distinguishes requested concept review from ordinary execution, exempts small existing-system fixes from image generation, and demands browser plus image inspection before handoff. [Exact SKILL.md](https://raw.githubusercontent.com/openai/plugins/d416fd5a43426019986b1e489506db3db66dee3d/plugins/build-web-apps/skills/frontend-app-builder/SKILL.md).

**Inference:** retain the insistence that successful functionality does not prove visual fidelity. Do not import its full concept pipeline, repeated inventories, tool-specific gates, or subjective 10/10 stopping rule. They add work disproportionate to a narrow UI task and can privilege an image over responsive behavior if applied mechanically. No claim here establishes special effectiveness on GPT-6-Astra.

### 8. Anthropic webapp-testing

The skill supplies Playwright interaction guidance and a server helper, emphasizing rendered reconnaissance before choosing selectors. It is useful for distinguishing an inspected interface from code that merely compiled. [Exact SKILL.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/webapp-testing/SKILL.md).

**Inference:** the short design skill should demand the outcome (inspect, exercise, repair) while using the available browser tooling. Avoid embedding Python or network-idle recipes in a general design skill.

## License and reuse findings

These are observed repository declarations, not a legal clearance review. Original synthesis is preferable to copying expressive passages or bundling code/data.

- Anthropic frontend-design has a skill-local [Apache-2.0 license](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/LICENSE.txt). Impeccable has a root [Apache-2.0 license](https://raw.githubusercontent.com/pbakaus/impeccable/cb56ed6c19a07329a9fa0cd4e657bee040156593/LICENSE). For distributed adaptations, check license-copy, change-notice, attribution, and any applicable NOTICE requirements.
- Taste carries an [MIT license](https://raw.githubusercontent.com/Leonxlnx/taste-skill/ccbc15639c97057cbfcf32ecebc38ef716e4bb37/LICENSE); UI UX Pro Max also carries [MIT](https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/7f69fed6a2717900085f1bc3b263721f8ba025e2/LICENSE). Both require their copyright and permission notices with copies/substantial portions.
- Vercel agent-skills' [README declares MIT](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md#license), but root `LICENSE` returned 404. The separately fetched web-interface-guidelines file's reuse terms were not established here. Do not treat the wrapper's declaration as proof for every external dependency.
- OpenAI plugins' root `LICENSE` returned 404; no license in the `build-web-apps` subtree appeared in the recursive tree inspection. The [repository README](https://github.com/openai/plugins/blob/d416fd5a43426019986b1e489506db3db66dee3d/README.md) describes curated examples without supplying a blanket grant. Public availability alone is insufficient to assert unrestricted copying. Use its workflow as research evidence; verify terms before redistributing text.

## Candidate behaviors to test in a short skill

1. Identify the primary user action and surface type before choosing composition or density.
2. Inspect supplied references and existing UI; preserve their defining traits unless redesign is requested.
3. Make a few coherent, content-specific choices for hierarchy, type, spacing, color, and media. Do not add visual structure without a user-facing purpose.
4. Build the actual journey with realistic content and necessary interaction states. Let motion explain actions or direct attention deliberately.
5. Inspect desktop and mobile renders; exercise the main flow and relevant failure state. Fix the largest visible or functional mismatch before cosmetic refinements.
6. Stop when the requested experience and acceptance checks are satisfied; disclose concrete unverified gaps.

Test these against an unassisted baseline across at least a task-heavy tool, a distinctive marketing page, and a constrained existing-brand change. This recommendation is a proposed evaluation, not an assertion that shorter instructions always win.

## Availability and verification limits

All eight listed skill files and the additional references cited above were retrieved successfully. Root commits were recorded through GitHub's commits API immediately after reading `main`; pinned links identify those snapshots. `python` was unavailable locally, so retrieval used `python3`. No package was installed or executed. Impeccable's root `NOTICE` returned 404. The much-discussed older OpenAI frontend-skill/blog was not relied upon; the verified current plugin file supplies the OpenAI example. Effectiveness claims, repository popularity, dataset completeness, and model-specific performance were not validated.
