# Design 4: quality, cost, and possible skill tweaks

Review complete. **No skill or trial-site files were changed.** Design 5 is still running and was not inspected. This is an unblinded review of the existing outputs, not another generation trial.

Shared brief: “Build a jaw-dropping interactive landing page. You choose the subject, visual style, and interactions.”

Zach reports a decent improvement with the skills, little quality difference between solo and agents, and an improvement that still falls short of his retention bar. My rendered inspection broadly agrees: the skill outputs have stronger coherence and integration of controls, but the full agent workflow does not show a clear quality advantage over solo in this trial.

## Cost is the strongest finding

These are Zach's approximate generation costs, not independently audited billing records. Ratios use those estimates.

| Condition | Product | Approximate cost | Relative to baseline |
| --- | --- | ---: | ---: |
| No skill | PELAGIC ocean expeditions | $2.68 | 1.00× |
| Solo | Elsewhere ambient listening | $3.50 | 1.31× |
| Agents | SOL solar observatory | $10.00 | 3.73× |

Solo added about **$0.82 / 31%**. Agents added about **$6.50 over solo**, for **2.86× its cost**, without a comparable visible improvement. Solo currently offers the better quality/cost tradeoff among the skill variants. That does not yet establish that it meets Zach's required improvement over baseline.

The files document two team concept builders, a selection critic, main-agent implementation, and a fresh final critic. The extra stages are real. There is no per-stage billing or timing evidence here, so I cannot assign the cost increase to a particular stage or claim an exact saving from removing it. This trial measures the workflows at their actual reported costs; it is not an equal-cost causal comparison.

## What improved, and what still limits the result

**PELAGIC:** A strong cinematic submarine image provides an immediate identity. The depth control works, but the main visual response is a darker, slightly enlarged and recolored version of the same scene. The opening's outlined title, image, coordinates, depth labels, and supporting microcopy create more competing detail. On mobile, the submarine is heavily cropped and the text lies over its image. The rest of the page follows a conventional mission, experience, journal, and closing structure.

**Elsewhere:** The type hierarchy is calmer and easier to read; the planet has room to breathe, and the player, world selection, mixer, and color system belong to the same experience. The phone opening gives copy and artwork separate space. It also delivers actual synthesized audio and working controls. This is a more cohesive product experience. Its spatial metaphor is attractive, but most of the visual interaction remains planet rotation and palette changes around a familiar landing-page structure.

**SOL:** The solar imagery has rich detail and a strong crop. Changing wavelength changes the actual observation as well as labels and color; the field guide stays synchronized, and the exported poster works. The mobile opening keeps the wavelength control visible. The secondary light journey is clear and functional. These are useful strengths, but I do not see a decisive overall quality advantage over Elsewhere. Both use large left-hand sans-serif headlines with italic emphasis, a dominant object to the right, restrained instrument-like labels, and controls beneath.

The remaining gap is between a polished interactive page and the requested extraordinary experience. Increasing visual polish has helped. The current outputs still rely heavily on familiar compositions and simple control-driven changes. This is specific to the “jaw-dropping” brief; it is not a reason to require spectacle in ordinary application interfaces.

| Evidence | No skill | Solo | Agents |
| --- | --- | --- | --- |
| Desktop opening | [PELAGIC](design-4-evidence/no-skill-desktop-hero.png) | [Elsewhere](design-4-evidence/solo-desktop-hero.png) | [SOL](design-4-evidence/team-desktop-hero.png) |
| Complete desktop page | [PELAGIC](design-4-evidence/no-skill-desktop-full.png) | [Elsewhere](design-4-evidence/solo-desktop-full.png) | [SOL](design-4-evidence/team-desktop-full.png) |
| Phone opening | [PELAGIC](design-4-evidence/no-skill-mobile-hero.png) | [Elsewhere](design-4-evidence/solo-mobile-hero.png) | [SOL](design-4-evidence/team-mobile-hero.png) |

## What the retained concepts reveal

Solo's [Orbital](design-4-evidence/solo-orbital-concept.png) and [Observatory](design-4-evidence/solo-observatory-concept.png) share the planet, text/art arrangement, world selection, and central interaction. The meaningful differences are mainly the background, framing, scale, and headline wording. The shared [concept implementation](../../design-4-skill-solo/src/concept.js) confirms this. Shared code is efficient; the issue is the narrow range of rendered ideas being compared.

The solo concepts also omit the eventual listening experience: their controls change the planet palette and annotation, while the audio engine is introduced in the final application. Selection therefore judged visual framing without testing the product's eventual primary action. The final audio works; this is a weakness in the concept-selection method, not a claim that the delivered audio is missing.

The team did explore different subjects: [a lamp](design-4-evidence/team-a-concept.png) and [the Sun](design-4-evidence/team-b-concept.png). However, both still use a large left headline, a large right object, and a slider below. Its [selection critic](../../design-4-skill-agents/artifacts/selection-critic/selection.md) gives concrete reasons to choose SOL, including richer imagery and more immediate phone controls, and identifies actionable contrast and labeling issues. The [worklog](../../design-4-skill-agents/WORKLOG.md) also records a final critic's reduced-motion replay finding and fix. These are useful contributions. They establish that critique did work, but not that the complete team process was worth nearly three times solo's cost.

## Tweak candidates — notes only, not applied

1. **Make alternatives test different experiences.** Before investing in two implementations, identify the compositional or interaction decision they are comparing. For an open creative brief, require a meaningful difference in spatial structure or the visitor's core action. This addresses solo's palette/frame comparison and the similar structure of both team candidates. Preserve code and asset reuse where it saves effort.

2. **Prototype the actual primary action.** The small concept should include the interaction that makes the finished experience worth choosing. In Elsewhere, that means a minimal working listening experience, not only switching planet colors. The check should be whether the central user action and its feedback were genuinely compared; it should not require completing secondary features in both concepts.

3. **Keep the original ambition in the selection criteria.** Judge whether the candidate achieves the user's requested impact before judging how well it fits the subject the builder invented. A plausible hypothesis is that choosing a calm listening product made it easier to accept an attractive but familiar result. A calm subject can still support an extraordinary interaction. The critic should identify the specific moment that earns the brief's ambition, or name that gap. Avoid turning this into a universal palette, typography, or effects rule.

4. **Test a cheaper, selective use of agents.** A future cost experiment could start with solo exploration plus one focused critic, and add another builder only for a concrete unresolved design problem. Keep model/reasoning stable while testing the workflow change. The present evidence supports questioning unconditional agent stages; it does not establish which reduced workflow will retain the benefit.

5. **Direct expansion effort toward the defining experience.** The outputs add useful features, but also conventional supporting sections: PELAGIC's journal/wish list, Elsewhere's ritual copy/timer, SOL's FAQ/poster/journey. Before adding more surface area, compare its contribution with improving the central interaction. Do not remove requested functionality or assume all supporting content is waste. There is no cost breakdown proving these additions caused the team premium.

6. **Distinguish quality improvement from creative separation.** Continue scoring both: “Does this look and work better?” and “Is the difference substantial enough to justify using the skill?” These outputs suggest progress on the former, with insufficient evidence on the latter. For open-ended prompts, differences in subject and asset quality also introduce variation; the upcoming shared music-app brief will provide another useful comparison.

Keep both skills frozen until the next running comparison is reviewed. These candidates are hypotheses for a later revision, not accumulated requirements to paste wholesale into the skills.

## Fresh inspection and limits

Reviewed production previews at ports 4176 (baseline), 4174 (solo), and 4177 (team). Captured matching 1440 × 900 desktop and 390 × 844 phone views in Chromium. Inspected the four retained concepts from development previews at ports 5174 and 5177, plus source and project records.

- Baseline: completed the first descent, selected the deepest zone with the keyboard and phone control, toggled the sound state, changed the experience panel, opened/closed a journal article, and saved a local fixture wish list.
- Solo: started playback and measured a nonzero Web Audio signal, selected another world, dispatched a planet drag, adjusted a mix layer with the keyboard, closed the mixer, and verified the master gain faded near zero after pause. Phone play and mixer controls worked. Audio signal was checked; sound quality was not evaluated by listening.
- Team: changed wavelength using keyboard and phone controls, verified synchronized field-guide imagery, saved and visually inspected a [PNG poster](design-4-evidence/team-exported-poster.png), opened/closed information, and tested light-journey playback, pause, and scrub-to-arrival.
- No page-level JavaScript errors or failed requests were observed in the recorded desktop journeys. All three sampled phone layouts had document width equal to viewport width. Initial premature samples of PELAGIC's animated values were corrected by waiting for completion; SOL's phone interaction screenshot was recaptured after its image crossfade.

[Recorded interaction observations](design-4-evidence/interaction-observations.json). This was not a complete accessibility audit, a fresh run of every existing test, or a hardware/browser performance comparison. Existing project verification claims are distinguished above from checks performed during this review.

Skill hashes remain the same as before inspection:

- `design-solo`: `a890443daa7205713636653a3b22929097c8da8131484fb96eb03aba3da65ce9`
- `design-team`: `8ba4032b8611c91708d4eece79d024f847171cde7968ff4c911c0e1c240270e4`
- Original `design`: `fd9e161e7849cdf8276175c5fa648c35b3112d892d6e7dc5ece662f69cfcf22b`
