# Review of the solo and team candidates

The author drafted both candidates after Zach requested a single-agent variant, a variant using independent exploration and critique, and a less prescriptive evaluation prompt. The original skill and six websites were preserved.

An independent reviewer using the author's inherited model and reasoning inspected both draft skills. It confirmed that solo prohibits delegation, team implements the proposed workflow, and both share visual criteria. It recommended three changes to team, all accepted:

- Give builders the same visual criteria available to the solo designer.
- Bound builder tasks, keep critics read-only, and prohibit subagents from delegating further.
- Use separate preview ports as well as working folders.

The author reread both variants after applying the changes. Remaining hypothesis: independent builders may still converge on similar ideas; rendered trials must establish whether the workflow produces a noticeable benefit. Both variants remain experimental and have not been tested through website generation.

The [round-two protocol](../evaluation/round-2.md) controls the total allowance across agents and separates document validation from outcome evidence.

Both final files passed the bundled `quick_validate.py` skill validator. Word counts include frontmatter and headings.

| Candidate | Words | SHA-256 |
| --- | ---: | --- |
| `design-solo` | 362 | `a890443daa7205713636653a3b22929097c8da8131484fb96eb03aba3da65ce9` |
| `design-team` | 463 | `8ba4032b8611c91708d4eece79d024f847171cde7968ff4c911c0e1c240270e4` |

The original skill still matches `fd9e161e7849cdf8276175c5fa648c35b3112d892d6e7dc5ece662f69cfcf22b`. Candidates are local files; no global installation or discovery configuration was changed.

Historical note: these candidates were retired after design 5. Exact reviewed files remain available as [solo v2](../evaluation/skill-snapshots/design-solo-v2.md) and [team v2](../evaluation/skill-snapshots/design-team-v2.md). See the [design 5 revision](../evaluation/design-5-review.md) for the current candidate.
