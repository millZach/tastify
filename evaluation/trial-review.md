# Review of Zach's first three design comparisons

Reviewed 2026-09-11. Zach confirmed that the model and reasoning setting were the same within each comparison. The six sibling projects were inspected as provided; neither the sites nor the skill were edited. This is an unblinded qualitative review, not a set of independent preference scores.

**Conclusion: this version of the skill has not demonstrated a useful, consistent improvement. Design 3 without the skill is the strongest evidence against retaining it unchanged.**

Zach's follow-up: he slightly preferred Northline with the skill, differing from my preference below. His central finding was that the design difference was barely noticeable. His retention bar requires noticeable improvement; a tally of slight wins is insufficient.

| Pair | My preference | Reasons and counterpoints |
| --- | --- | --- |
| 1 — Northline | Small no-skill edge | Its opening has a more compact headline, stronger product lighting and material detail, and a better balance between copy, product, and buying information. The skill version has clearer finish labels, a useful lifestyle image lower down, and puts the product before the controls on mobile. Those are real improvements, but the overall quality is close. |
| 2 — Playframe | Small skill edge | The pixel art is more consistent across the game and supporting illustrations. The surrounding design feels connected to the demo. Both use essentially the same headline/CTA/editor composition, and both deliver the main editing and playback loop. This is a modest preference, not a substantial jump in quality. |
| 3 — RIFT | Clear no-skill edge | Stronger material treatment, spatial depth, composition, and staging of the portal experience. The difference persists across the opening, project worlds, and mobile views. |

## What makes design 3 better without the skill

The no-skill portal has irregular surface detail, warm internal light, a visible membrane, and a grounding shadow. Its headline and sculpture occupy distinct areas while forming one composition. The skill version's purple metal ring is competently rendered, but the extremely large headline competes with it, particularly where the pale lettering overlaps the object on mobile.

The orange typography world is the clearest comparison. The no-skill version uses perspective, foreshortening, and fading edges to make the type feel like a surface extending through the scene. Its title and explanation frame that artwork. The skill version presents a more frontal rectangular mesh alongside another oversized title. On desktop, the mesh extends beyond the viewport and crosses the manipulation hint; on mobile, it reads as a smaller demonstration underneath the heading. Both bend typography, but the resulting experiences have different visual impact.

The third world shows a similar difference. The no-skill object's bright, warm reflections and overlapping loops give it convincing volume. The skill version repeats the large title-left/object-right arrangement. Reusing a type system is useful; repeatedly giving the title so much visual weight makes the artwork less dominant.

Entry also differs in implementation: the no-skill version coordinates copy withdrawal, an expanding portal, a full-screen transition layer, and the destination reveal. The skill version connects native smooth scrolling to portal enlargement and particle transformation. The former more closely supports the invitation to travel through a portal. This assessment comes from the rendered entry states and source inspection; the screenshot filenames are nominal capture targets, not measured animation timings.

These observations do not establish that light backgrounds or any particular font are inherently better. The skill version also uses bold color and real 3D. The deciding differences are relationships between elements and how thoroughly the visual idea is developed.

| View | Without skill | With skill |
| --- | --- | --- |
| RIFT opening | [Desktop](review-2026-09-11/design-3-noskill-desktop-hero.png) · [Mobile](review-2026-09-11/design-3-noskill-mobile-hero.png) | [Desktop](review-2026-09-11/design-3-skill-desktop-hero.png) · [Mobile](review-2026-09-11/design-3-skill-mobile-hero.png) |
| RIFT typography world | [Desktop](review-2026-09-11/design-3-noskill-desktop-world-2.png) · [Mobile](review-2026-09-11/design-3-noskill-mobile-world-2.png) | [Desktop](review-2026-09-11/design-3-skill-desktop-world-2.png) · [Mobile](review-2026-09-11/design-3-skill-mobile-world-2.png) |
| RIFT object world | [Desktop](review-2026-09-11/design-3-noskill-desktop-world-3.png) | [Desktop](review-2026-09-11/design-3-skill-desktop-world-3.png) |
| Northline | [Full page](review-2026-09-11/design-1-noskill-desktop-full.png) · [Mobile opening](review-2026-09-11/design-1-noskill-mobile-hero.png) | [Full page](review-2026-09-11/design-1-skill-desktop-full.png) · [Mobile opening](review-2026-09-11/design-1-skill-mobile-hero.png) |
| Playframe | [Full page](review-2026-09-11/design-2-noskill-desktop-full.png) · [Mobile editor](review-2026-09-11/design-2-noskill-mobile-demo.png) | [Full page](review-2026-09-11/design-2-skill-desktop-full.png) · [Mobile editor](review-2026-09-11/design-2-skill-mobile-demo.png) |

## What this says about the skill

The [tested skill](skill-snapshots/design-v1.md) spends much of its 524 words restating desirable outcomes: hierarchy, spacing, consistency, meaningful imagery, working states, and visual inspection. Several of those requirements already appear in Zach's working instructions. Both RIFT project records describe visual inspection and independent critique; both finished sites contain procedural artwork and working interactions. The baseline already performs much of the workflow the skill requests.

The missing contribution is a concrete method for making and rejecting visual choices. “Establish a clear focal area” does not tell the builder how to recognize when the headline and sculpture compete. “Inspect imagery” does not establish a sufficient bar for lighting, material quality, crop, and spatial composition. A requirement to inspect the result can be satisfied without making a strong enough judgment about it.

My hypothesis is that the skill adds little new decision-making ability and can direct attention toward satisfying general rules. Its wording about keeping motion subordinate and prioritizing usability deserves reconsideration for a brief where spectacle is itself the purpose. However, these three pairs cannot identify a particular sentence as the cause of the weaker output. They do support withholding any claim that this draft improves design.

My drafting mistake was treating a concise summary of sound advice as though it would reliably change the model's design decisions. Structural validation and a document review never established that it would work.

## Next experiment

Preserve this version and the six outputs. Test a short replacement that changes the process: identify the intended experience; render two meaningfully different opening compositions before committing; compare their focal hierarchy, image/material quality, and signature interaction against the brief and a relevant visual reference; then carry the chosen direction through the page and revise its largest visible weakness.

Use RIFT as a diagnostic case and add a fresh, different brief to check against copying its winning aesthetic. Hold model, reasoning, prompt, tools, and total build allowance constant across conditions; concept exploration must fit inside that allowance. Use fresh runs and conceal condition labels from the final comparison. Judge visual impact and required behavior separately, with Zach's preference as the primary result. Repeated comparisons are needed before calling the replacement reliable.

## Inspection scope

- Compared all six sites at 1440 × 900 and 390 × 844 in Chromium, with fonts loaded. Reviewed full desktop pages for Northline and Playframe, plus RIFT's individual worlds and contact views. Phone captures emulate a touch device; they are not physical-phone tests.
- Northline: all three finish controls worked; Graphite carried into the inquiry; empty submission identified two invalid fields; a fixture submission showed local success; Escape closed the dialog. Mobile inquiry/validation also worked. No POST request occurred in the desktop form journeys.
- Playframe: moved a platform, ran the edited level, paused and verified the character held position, resumed to the checkpoint, reset playback, and confirmed the edit remained. Both mobile editors accepted a touch control edit. The no-skill run collected five coins; the skill run collected three, matching their respective level designs.
- RIFT: dragged each portal, entered the first world, exercised all three world action buttons, opened the secret state and dismissed it with Escape, and inspected contact. Fresh mobile contexts were used for the final opening/first-two-world captures.
- No page-level JavaScript errors were observed in the recorded desktop journeys. All six sampled mobile layouts had document width equal to viewport width. This was not a full accessibility audit, cross-browser test, or hardware performance benchmark; prior project test reports were not counted as fresh results.

Recorded interaction observations: [Northline and Playframe](review-2026-09-11/remaining-interactions.json), [RIFT](review-2026-09-11/rift-interactions.json).
