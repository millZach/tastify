# Tastify

A design skill for coding agents. It gives a model a small set of checkable tests for choosing a composition, cutting decoration, and finishing the one thing on the page that matters, instead of a list of adjectives about good design.

The skill is one file: [`skills/tastify/SKILL.md`](skills/tastify/SKILL.md).

## Why it exists

Coding agents are competent at implementing interfaces and weak at deciding what the interface should be. Left alone, the same model produces the same page for every subject: a small logo, a giant two-line headline with an accented second line, two lines of body copy, one pill button, a rendered object on the right, and a scattering of tiny annotations. Earlier versions of this skill restated good design principles and made no measurable difference. What worked was replacing principles with tests the model can actually run on its own output.

The core moves:

- **Subject-swap test.** Derive the composition from the subject's own nature, then swap in a different subject. If the layout still fits, it came from habit.
- **Squint test.** One element dominates the first screen. Everything else is subordinate or gone.
- **What breaks if this is removed?** Figure numbers, coordinates, corner marks, and scroll cues are the layout apologizing for empty space.
- **Text stands alone.** One line per element, a fact appears once, and the first screen is budgeted to five text elements.
- **The focal asset earns most of the iterations.** Judged at displayed size for light, material, edge, and grounding shadow.
- **One signature motion**, choreographed as invitation, response, and arrival.

It also keeps hard floors for type size, a review pass at three widths, and checks for animation clipping inside its own drawing bounds.

## Using it

Point the agent at the file at the start of the task:

```
Read /path/to/tastify/skills/tastify/SKILL.md and follow it throughout. Then:
<your brief>
```

Or copy `skills/tastify/` into whatever skills directory your agent discovers. The frontmatter is model-invocable, so an agent that reads skill descriptions will pick it up for interface work on its own.

It was developed against GPT-6 Astra running in Codex. Nothing in it is model-specific.

## Evidence

The skill was built through six matched trials: the same brief, model, and reasoning setting, with and without the skill, judged by rendered inspection and the author's preference. The record is honest about the misses.

| Trial | Skill version | Outcome |
| --- | --- | --- |
| 1–3, product page, game demo, studio portal | v1 | No consistent improvement. The baseline beat the skill on the most ambitious brief. |
| 4, open "jaw-dropping" brief | solo and team variants | Visible improvement in cohesion. Subagent workflow cost 2.9x solo for no gain and was retired. |
| 5, music playground | solo | Close to baseline. Exposed tiny type, decorative captions, and animation clipping. |
| 6, cast-iron stove | v4 | First trial the author called a large improvement. Remaining defect: companion lines on every element, which v5 addresses. |

Trial sites themselves are not in this repository. Captures, interaction records, and reviews are under [`evaluation/`](evaluation/). Research into existing skills, community complaints, and reference sites is under [`research/`](research/). [`WORKLOG.md`](WORKLOG.md) is the running record, including every skill hash.

Exact prior versions are frozen in [`evaluation/skill-snapshots/`](evaluation/skill-snapshots/).

## Testing it yourself

Use one brief in two fresh contexts with the same model and settings, one with the read-and-follow line above and one without. Give the folders neutral names; a folder called `noskill` tells the model it is the control. Before judging overall preference, count text elements on the first screen, count headings on the page, and check whether the opening escapes the template described above.

## License

MIT. See [LICENSE](LICENSE).
