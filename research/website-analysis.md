# Website observation notes for a frontend design skill

Inspected 2026-09-11 in the collaborative Chromium/Electron browser. This is a visual comparison of first-party pages, not a claim that their current marketing treatment is appropriate for every application. All observations below came from rendered screenshots and direct browser interaction; DOM inspection supplemented them. No account, purchase, or sales conversation was started.

## Inspection record and evidence

Desktop CSS viewports: Apple and Stripe **1440×900**; Linear and Aesop **1280×800**. Mobile CSS viewport: **390×844** for all four. The browser resize tool changes layout width but retains a desktop user agent. Its desktop screenshot output was scaled to 1280×800 for the 1440×900 viewports; those screenshots do not imply a different CSS viewport. These were viewport captures, not full-page screenshots.

| Primary source | Actually inspected | Evidence |
|---|---|---|
| [Apple](https://www.apple.com/) | Desktop launch hero; scroll to product section at y≈590; mobile hero and first product text; opened and closed mobile navigation | [Desktop hero](screenshots/website-apple-desktop-hero.png), [mobile hero](screenshots/website-apple-mobile-hero.png), [mobile menu](screenshots/website-apple-mobile-menu.png) |
| [Stripe](https://stripe.com/) | Desktop hero and product demonstration grid at y≈740; mobile hero and product demonstration at y=650; opened mobile navigation, drilled into Products, closed it | [Desktop hero](screenshots/website-stripe-desktop-hero.png), [desktop products](screenshots/website-stripe-desktop-products-settled.png), [mobile hero](screenshots/website-stripe-mobile-hero.png), [mobile products](screenshots/website-stripe-mobile-scroll-settled.png), [menu](screenshots/website-stripe-mobile-menu.png), [nested menu](screenshots/website-stripe-mobile-products-menu.png) |
| [Linear](https://linear.app/) | Desktop hero and product UI demonstration; scrolled to y=900 showing demo activity, customer logos and following statement; mobile hero and opened navigation | [Desktop hero](screenshots/website-linear-desktop-hero.png), [desktop scroll](screenshots/website-linear-desktop-scroll.png), [mobile hero](screenshots/website-linear-mobile-hero.png), [mobile menu](screenshots/website-linear-mobile-menu.png) |
| [Aesop](https://www.aesop.com/) | Requested https://www.aesop.com/us/, redirected to https://www.aesop.com/; desktop hero before/after rejecting cookies; attempted carousel next; reloaded; desktop catalog at y=700; mobile hero and two-column catalog | [Initial overlay](screenshots/website-aesop-desktop-initial.png), [desktop hero](screenshots/website-aesop-desktop-hero.png), [desktop catalog](screenshots/website-aesop-desktop-catalog-settled.png), [mobile hero](screenshots/website-aesop-mobile-hero-settled.png), [mobile catalog](screenshots/website-aesop-mobile-catalog.png) |

### Important limits

- Apple’s desktop product section stayed visually blank in this session even after subsequent captures; mobile product text rendered. The browser reported renderer errors, so I do not interpret the blank section as intentional whitespace or claim to have inspected its intended product imagery/animation. [Failure capture](screenshots/website-apple-desktop-product-settled.png).
- Linear’s first snapshot showed only navigation, but a later untouched capture showed the complete hero. Initial screenshots can precede animation/rendering completion even when navigation reports loaded.
- Stripe’s desktop Products click changed navigation styling, but its dropdown content was not verified in a stable screenshot. Mobile navigation and its nested Products view were verified. A black/transparent patch appeared behind parts of the desktop/mobile header in this renderer; it is not treated as intended visual design.
- Aesop’s next-slide attempt left a horizontally cropped page in this session; reload recovered it. Its carousel interaction was attempted, but successful slide completion is unverified. [Cropped state](screenshots/website-aesop-carousel-cropped.png).
- These were selected homepage sections, not authenticated applications, full sites, accessibility audits, performance measurements, touch-device tests, or purchase journeys. No continuous motion recording was reviewed. State changes and changing demonstration content were observed; timing, easing, smoothness, reduced-motion support and general motion quality remain unverified.

## What each reference teaches

### Apple: stage one decision, then repeat a clear content grammar

The launch hero uses a full-width blue image field, a centered visual subject, compact centered announcement copy and one prominent event action. The global navigation is a narrow, dense horizontal strip above a spacious hero. In the mobile capture, that strip becomes a logo plus search, bag and menu controls. The opened menu replaces the underlying content with a large, single-column destination list. [Apple](https://www.apple.com/)

The first mobile product section uses a clear sequence: large dark product name, smaller muted explanation, quieter availability text, then adjacent filled and outlined actions. It achieves grouping through shared alignment and spacing, without enclosing every text element in a card. Its visual simplicity does not mean every region has the same density: navigation is compact, presentation is spacious. [Apple](https://www.apple.com/)

**Transfer:** Decide what a region is for, give its primary content visibly greater emphasis, keep related actions adjacent, and maintain consistent grammar across similar items. An engineering tool can use the same logic for equipment title → live state → relevant reading → action.

**Marketing-specific:** A viewport-sized brand image and launch announcement assume a visitor exploring a product. They should not displace alarms, measurements or the working surface of an application. The failed desktop product rendering is also a reminder to verify that essential content survives asset or animation trouble.

### Stripe: a coherent grid can support expressive imagery and unequal density

Stripe’s desktop hero is left aligned within a ruled page grid. The leading proposition is dark; its longer explanation is a quieter blue-gray at a similar large scale. A vivid diagonal orange/pink/purple image occupies the right side and passes behind some text. The saturated primary action and bordered alternative sit together. A thin horizontal customer-logo strip separates the hero from the next section. [Stripe](https://stripe.com/)

The product section uses unequal columns: the payments demonstration occupies about twice the width of the adjacent billing demonstration. Both combine a short heading with recognizable working UI. Their frames earn their place by bounding separate demonstrations; the content is not a collection of empty decorative boxes. Mobile stacks these demonstrations. The hero is also edited, not merely scaled: the long desktop explanation is omitted, the proposition wraps in two lines, and the two actions become wide stacked controls. [Stripe](https://stripe.com/)

Mobile navigation uses a full-height destination list, clear separators, and persistent bottom actions. Products opens a deeper list with a Back control, group headings, product names and compact descriptions. This is progressive disclosure of a large taxonomy. A sales chat prompt visibly covered substantial lower-page content on the initial mobile capture; that is a useful counterexample to copying every element of a reference. [Stripe](https://stripe.com/)

**Transfer:** Use a common alignment system while allowing important work to occupy more space. Show a realistic result or operation where it teaches faster than prose. On narrow screens, reprioritize secondary copy, stack controls and give deep navigation a clear way back.

**Marketing-specific:** Animated brand ribbons, rotating logos and sales overlays are promotional choices. The changing payments demo communicates a range of payment contexts; an actual operational screen would need stable values and deliberate update behavior instead of a cycling presentation.

### Linear: show the product, and distinguish presentation density from working density

The desktop composition uses near-black surfaces, restrained gray rules, a large two-line left-aligned heading and a short muted description. The actual product demonstration occupies a wide surface below. Inside that demonstration, navigation, issue title, activity, status and review material are relatively dense, organized with alignment, dividers and tonal surface changes. It is not a sparse dashboard made from oversized metric cards. The subsequent section separates customer logos and a large explanatory statement through whitespace. [Linear](https://linear.app/)

On mobile, the headline reflows into four lines, the announcement moves below the description, and the product demonstration remains visibly cropped/scaled as an illustration. It is not proof of a usable mobile version of the full product UI. The header retains login/sign-up actions beside a menu trigger. The opened menu groups destinations under small category labels and provides large, vertically arranged links. [Linear](https://linear.app/)

**Transfer:** Present actual working content early; use typography, alignment and restrained dividers to organize high information density. Reserve spaciousness around major groups while keeping repeated working rows efficient. Give navigation a taxonomy rather than scattering unrelated controls.

**Marketing-specific:** Huge headlines, muted decorative text and an illustrative miniature UI should not become mandatory application styling. A real engineering display needs readable data at the size shown, sufficient contrast and a responsive arrangement of its controls; a cropped marketing demonstration does not establish those properties.

### Aesop: visual restraint can be warm, photographic and editorial

The desktop hero is dominated by a warm, full-bleed interior photograph/video frame. Navigation overlays the top; a headline and wide outlined action sit near the bottom over a darkened area. The catalog changes to a pale cream field with an editorial serif heading, sans-serif supporting text and three open product columns. Large isolated product images carry the visual identity; names, descriptions and prices align beneath them without an enclosing card around each item. Computed styles confirmed the catalog heading’s Zapf-Humanist family and the hero’s SuisseIntl family. [Aesop](https://www.aesop.com/)

On mobile, the hero image is recropped vertically around its subject; text becomes left aligned and the action spans most of the width. The catalog shows two columns with smaller product imagery, brief truncated copy, aligned prices and full-width per-item actions. It therefore preserves comparison across two items rather than blindly converting every desktop collection into one column. [Aesop](https://www.aesop.com/)

**Transfer:** Let meaningful imagery define character; create separation with alignment and space before adding boxes. Choose mobile column count according to what must be compared and what remains legible. Use editorial typography when the subject and content support it.

**Marketing-specific:** Lifestyle film, very large packshots and a slow browsing rhythm serve brand discovery. They should not occupy the majority of a production control screen. The observed mobile truncation should not be copied for critical equipment names or alarm descriptions.

## Observable decision rules worth carrying into a short skill

These are design inferences from the comparison, not claims of measured conversion or usability improvements.

1. **Choose the page’s dominant job before styling.** A product launch, catalog, working editor and alarm overview need different density and composition. The first viewport should expose the content or action that serves that job.
2. **Establish a visible order of attention.** Point to the primary subject, supporting information and next action in a screenshot. If all have equal visual weight, adjust scale, placement, contrast or space before adding decoration.
3. **Group by meaning with alignment and spacing.** Related labels, values and controls should read as a unit. Use containers when they establish a real boundary—an independently actionable item, separate workflow or contrasting surface—not automatically around every datum.
4. **Spend space according to importance.** Calm does not require low density everywhere. Give major groups breathing room, keep repeated working rows compact, and allow the primary chart/editor/demo more space than supporting content.
5. **Use imagery that contributes information or character.** A product in use, real interface, relevant photograph or clear diagram can replace explanation. A generic gradient or ornamental dashboard screenshot cannot establish usefulness by itself.
6. **Treat responsive design as recomposition.** Recheck reading order, text length, image crop, column count, action placement and navigation depth at narrow widths. Never assume shrinking the desktop composition is sufficient.
7. **Keep behavior and state understandable.** Menus need visible close/back paths; selected or expanded content should be apparent. Add motion when it explains a transition or demonstrates a process, then inspect its actual completion and reduced-motion behavior. The latter was not tested on these references.
8. **Borrow a principle, not a brand costume.** Apple’s centered staging, Stripe’s expressive grid, Linear’s dark product focus and Aesop’s warm editorial imagery are alternatives. Select colors, typography, surfaces and density from the project’s purpose and identity.
9. **Inspect the result, including failures.** Capture settled desktop and mobile states, scroll beyond the hero, exercise important controls, and look for blocked content, broken assets, accidental cropping and unreadable real data. A famous reference is evidence to examine, not a quality exemption.

For engineering dashboards specifically: prioritize live state, anomalies, readable units, comparison and direct actions. Transfer disciplined grouping and attention management. Treat cinematic heroes, promotional carousels, miniature screenshots and intrusive sales prompts as context-specific reference material.
