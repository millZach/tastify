---
name: tastify
description: Use before writing or restyling any user-facing interface. Triggers on landing pages, websites, app screens, dashboards, components, redesigns, "make it look better", and any task that produces HTML, CSS, or UI code. Covers concept, composition, typography, imagery, color, copy, motion, and the rendered review.
---

# Tastify

## Choose the target

On invocation, ask once per design task: “Should this design be optimized for desktop browsers, phones, or both?” Offer **Both**, **Desktop browser only**, and **Phone only**. If the user has already specified the target in this task, use that answer without asking again.

Record the answer in the acceptance checks and carry it through the task:

- **Both:** follow the full skill across desktop and phone. Design for pointer, keyboard, and touch; review desktop, phone, and an intermediate width.
- **Desktop browser only:** prioritize desktop composition, information density, pointer interaction, and keyboard use. Review a typical desktop viewport and a narrower desktop window. Phone optimization and phone review are outside scope.
- **Phone only:** prioritize phone composition, touch interaction, readable content, and controls within comfortable reach. Review a typical phone viewport and a narrower phone viewport. Desktop optimization and desktop review are outside scope.

Wait for the answer before making target-dependent layout decisions. Continue independent inspection and preparation while waiting; silence does not select an option. Preserve the chosen target until the user changes it. Apply the remaining design principles at the selected target's sizes and input methods.

## Inspect the context

Inspect the existing interface and supplied references first. For a scoped edit, work inside the established identity and behavior. For a new direction, inspect one real reference of comparable craft and relevant interaction or information density. Record the specific qualities you will carry into the work, such as hierarchy, typography, data treatment, or interaction feedback. Keep the reference available for the final visual comparison. A factual source qualifies as a design reference only when its rendered design also provides the standard the task needs. Match its finish, not its layout or branding. Match the brief's ambition: when it asks for spectacle, the signature moment is the spectacle.

## Carry the requirements through the task

Before writing interface code, add Tastify acceptance checks to the task's existing notes. Cover concept and reference, composition, type and color, copy, motion, and rendered review. Combine related requirements into concise checks without dropping individual constraints. For a scoped edit, limit the checks to the affected interface and relevant states.

Make each check observable: name what must be present in the rendered result and how you will verify it. Record numerical limits explicitly. Keep the checks with the implementation notes through interruptions and scope changes. Task correctness and Tastify acceptance both determine whether the interface is finished.

Mark a requirement inapplicable only with a concrete reason tied to its scope or an explicit user instruction. A preferred implementation is not a reason to waive a requirement. Resolve routine applicability decisions within the authorized task; ask the user only when their intent is needed.

## Decide what the page is

Write one sentence: what this is, and the single moment that proves it. Then write three one-line concepts that differ in where the visitor's attention lives and what they do first. Choose one.

Derive the composition from the subject's own nature. A threshold is entered, so it sits on the axis the visitor moves along. An instrument is played, so it is under the hands on the first screen. A night sky is looked up at, so the type gets out of its way. A working tool is used, so the work and its controls lead, and everything below applies to the active task or selected object.

Test the result: swap in a different subject. If the layout, headline pattern, and object placement still fit, they came from habit and the subject has not designed the page yet. Derive again.

## Compose

Squint at the first screen. One element dominates; decide whether that is the artwork or the words, and size the other down until it clearly follows. Every remaining element is subordinate or gone. Ask of each: what breaks if this is removed? Figure numbers, coordinates, corner marks, section indices, scroll cues, and slogans the visitor never uses are the layout apologizing for empty space. Grow the focal element into that space or close the space up.

The focal asset earns most of the iterations. Judge it at displayed size for light, material, edge, and grounding shadow. A clean but flat render is a placeholder; keep developing it until it looks like something that exists in a real place. Compose the artwork and the type as one picture: the type can sit inside, behind, or across it, or be the artwork itself.

**Type.** Two sizes carry the first screen, a third for controls. Display type is sized to be read in a glance rather than to fill the width, tracked tight, with leading tighter than body. Choose the family from the subject: one family with weight contrast, or one deliberate pair. Body 16–18px, controls and meaningful labels at least 14px, secondary text at least 12px; when space is tight, recompose before shrinking.

**Color.** Take the palette from the subject's material or light: one field, one ink, one accent, in large uninterrupted areas. The accent belongs to the action and the focal glow.

**Copy.** The headline names the specific thing. If it could head a different product it is a slogan; rewrite it with this subject's nouns. Text stands alone. Each element carries one line and no companion line: a control has one label, a button has one verb and carries its own price, the headline speaks for the opening by itself. The next line of text on the screen belongs to a different element. A fact appears once on the page, so a line that repeats a neighbor is deleted rather than moved. Budget the first screen to five text elements: the headline, one sentence, one action, and the labels its controls need. Above five, delete until five. Keep units, the instruction a visitor needs to operate something, and state feedback.

Count text elements by distinct communicative purpose, not by DOM container. A headline, explanatory sentence, metric value, metric label, control label, and legend entry are separate elements. Wrapping one sentence onto multiple lines does not create additional elements. Count the visible first screen at normal zoom at each reviewed width. Identify essential units, operating instructions, and state feedback separately under the existing exception; do not use that exception to exempt an entire component.

## Motion

Choose one signature motion and choreograph it as a sequence: the invitation, the response, and the arrival, each with a stage of its own. Build it early and finish it before decorating anything. Smaller motions inherit its easing and tempo. Make it understandable with the selected target's input methods, retaining keyboard accessibility and a coherent reduced-motion state. Keep controls beside the content they affect.

Fit animated artwork to both dimensions of its drawing area, with room for its motion and interaction extremes. Watch the silhouette through rotation, pointer movement, playback, and transitions; correct accidental cropping at the canvas, SVG, camera, or container that causes it.

## Build the page

The page has as many sections as it has distinct things to show. Expansion effort goes to the focal experience first. A supporting section shows something the visitor has not yet seen, or it merges into the one above. A section opens with its content; the content is the heading. Reserve a heading for a section the visitor scans as a list, such as specifications, levels, or prices.

## Review the render

Inspect the complete page at normal zoom using the viewport coverage selected under “Choose the target”; for scoped edits, inspect the affected components and states. Exercise the main journey and relevant failure states with the selected input methods. Read every visible line, including text inside scaled SVGs and canvases at its displayed size. For each line, name the element it belongs to and any other line that already says it; delete companions and repeats, and count the first screen against its budget of five. Then fix small type, weak contrast, awkward wrapping, and competing emphasis. Check control target sizes for the selected input methods.

Repeat the squint test and the subject-swap test on the finished page. Observe animated elements through a complete cycle or at their extreme states, checking their own drawing bounds as well as page overflow. Compare the focal experience with the concept sentence and the reference; it should keep its impact as details are simplified.

Return to the Tastify acceptance checks before delivery. For each check, record the rendered view or interaction inspected and the observed result. For the copy budget, list the first-screen text elements and their count. For repeated facts, identify where they were removed or why a repetition is required by the task. For hierarchy and the reference comparison, describe the visible result rather than assigning a general quality score.

Fix the largest unmet requirement, then repeat the affected check. Finish when the applicable checks pass and the rendered result supports those judgments. If access, capability, or an explicit task constraint prevents a required check or correction, record the evidence and report the limitation.

Describe skill compliance according to these results. Reading the skill, producing screenshots, or passing functional tests alone does not establish that Tastify was followed. Keep the evidence in task notes and give the user a concise account of the outcome and material limitations.
