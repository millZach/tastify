# Product interface observations

Observed 2026-09-11 in a live Chromium preview, unauthenticated, at 1280 × 800 and 390 × 844 CSS pixels. These are visual and interaction observations of two public task flows, not claims about their usability metrics or all versions of these products.

## GitHub: find an issue, then inspect it

Primary pages: [VS Code issues](https://github.com/microsoft/vscode/issues) and [issue #335832](https://github.com/microsoft/vscode/issues/335832).

Observed desktop:

- The hierarchy separates global navigation, repository navigation, issue navigation, and the working list. The main region starts at roughly x=280 after a 256-pixel sidebar. Search and filters sit immediately above results; the user does not need to visit a settings page to narrow the list.
- Three pinned issues receive bounded cards. Ordinary issues share one bordered list with thin row dividers, approximately 64 pixels per ordinary row. The different containers communicate different importance rather than decorating every item identically.
- Semibold issue titles lead; smaller, muted author/time/number metadata sits below. Green or purple status icons and restrained label pills provide additional scan cues. The page is information-dense without giving every datum equal contrast.
- On the detail page, the title grows substantially and the open state becomes a labeled green pill. The conversation occupies the wide column; assignments and other metadata occupy a narrower right column. Horizontal rules, labels, and alignment group metadata without separate cards for each property. Empty metadata explicitly reads “No labels,” “No type,” etc.
- The issue description and timeline preserve authorship and sequence. The signed-out participation prompt sits where participation would happen, below the content.

Observed narrow layout:

- Global navigation collapses to a hamburger; repository navigation exposes Code and Issues plus overflow. The issue sidebar disappears behind an icon near “All issues.”
- Pinned issues stack. Ordinary issues remain a divided list with wrapping titles, rather than becoming a new card grid. Only some filtering controls remain directly visible; overflow takes others.
- Detail content becomes one column; assignee appears above the discussion. This is a meaningful reorder. At this width, three stacked pinned issues consume much of the first screen before ordinary results; the open/closed counts also appear truncated. These are tradeoffs visible in the specimen, not patterns to reproduce uncritically.

Interaction: activated the issue-title anchor from the list and verified the resulting URL and rendered detail. Preview locator clicks initially scrolled without activating reliably; executing the actual DOM anchor’s `click()` completed navigation. Opening the label filter was attempted, but its open state was not verified and is not evidence for a filter-behavior claim.

Evidence: [desktop list](screenshots/product-github-desktop.png), [desktop detail](screenshots/product-github-detail-desktop.png), [narrow list](screenshots/product-github-list-mobile.png), [narrow detail](screenshots/product-github-detail-mobile.png).

## Airbnb: compare places, then refine the search

Primary page: [Portland homes search](https://www.airbnb.com/s/Portland--OR/homes).

Observed desktop:

- A compact, segmented search summary keeps location, dates, and guest count together. A second horizontal band groups Filters with common amenity shortcuts. Brand/account controls occupy the edges.
- Results use two image-led columns beside a large map. Each result is a coherent image-and-text unit without an enclosing panel border. Large photos serve the comparison task. Property type/name, rating, descriptive line, capacity, dates, trip price, and discount/cancellation information form a repeatable order.
- The strongest visual weight goes to photography, titles, prices, and ratings. Descriptions are quieter. Image-corner badges and wishlist affordances attach to the object they affect. Map price markers supply a spatial comparison of the same inventory.
- Filter activation opens one centered, scrollable modal with a fixed title/close row and fixed footer actions. Related choices are grouped under headings and separated with whitespace and light rules: type of place, trip price, rooms and beds, amenities, neighborhoods, and booking options. Less common sections and “Show more” controls defer detail.
- The price histogram gives context for the range control. Numeric minimum/maximum fields are also present. The footer action says “Show 1,000+ places,” expressing the next result. It remains available while the long filter content scrolls.

Observed narrow layout:

- Location/dates/guests combine into one stacked search-summary control, with a separate filter icon. Quick filters scroll horizontally. The desktop result/map split changes to a map above sheet-like, single-column results, with Explore/Wishlists/Log in navigation at the bottom.
- The filter modal becomes almost viewport-wide and tall, retains clear section boundaries, and keeps its result action fixed at the bottom. Three recommended filters fit where desktop shows four. This is recomposition, not uniform shrinking.
- Typography is a rounded sans-serif; computed font-family lists Airbnb Cereal VF and fallbacks. Heading weight and spacing establish hierarchy without oversized editorial headings inside this search task.

Interaction: dismissed the informational all-fees announcement, opened and closed Filters on desktop, then opened Filters at narrow width. The modal’s rendered open states were inspected. No reservation, account action, saved wishlist, or search-filter application was submitted.

Evidence: [desktop results](screenshots/product-airbnb-desktop.png), [desktop filters](screenshots/product-airbnb-filters-desktop.png), [narrow results](screenshots/product-airbnb-mobile.png), [narrow filters](screenshots/product-airbnb-filters-mobile.png).

## Transferable recommendations for a short design skill

These are inferences from the observations, to test against each project:

1. Start from what users must notice, compare, and do. Choose the information structure before its surface styling. A dense issue queue and a visual lodging search need different densities and containers.
2. Give repeated content a stable scan order. Align the fields users compare and reduce the emphasis of secondary metadata. Use spacing within a group more tightly than spacing between groups.
3. Choose rows, tables, image-led units, or cards because the content needs them. “Avoid excessive cards” should not become “never use cards”: GitHub’s pinned issues and Airbnb’s photographs have defensible boundaries.
4. Keep frequent controls close to the content they affect; disclose infrequent detail in one coherent place. Preserve scope, current state, and an obvious next action when opening that place.
5. Design narrow layouts by priority: move, collapse, scroll, or defer elements deliberately. Recheck the first useful content, long titles, counts, and fixed controls; mechanical stacking can bury the task.
6. Use typography, alignment, contrast, and content before decoration. Permit product-specific personality where it supports recognition or the task, without prescribing one font, corner radius, palette, or visual genre.
7. Validate one real journey through at least two states at desktop and narrow widths. A good initial screenshot cannot establish that navigation, filtering, feedback, and reflow work.

## Limits

- Narrow captures use desktop Chromium at a narrow CSS viewport, not a physical touch device or mobile user agent. Keyboard navigation, touch dragging, screen readers, reduced motion, contrast ratios, and full accessibility conformance were not audited.
- Some snapshots raced asynchronous image/map loading or dialog animation; final saved Airbnb captures were retaken after the real content appeared. This inspection does not support an animation-quality claim.
- No authentication, private data, submission, transaction, or saved preference change was performed. Dynamic result counts, issue titles, prices, and inventory describe the observed session only.
- GitHub inherited dark appearance and Airbnb rendered light. These examples show different appropriate visual systems; they do not establish a preferred theme.
