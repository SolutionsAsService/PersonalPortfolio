# Carry-Forward Ledger (facts about the medium, measured in this run)

- With `html { scroll-behavior: smooth }`, every `scrollTo(0, y)` in a capture script animates. A final `scrollTo({top: 0, behavior: 'instant'})` still left `scrollY = 39` because earlier animations were still running, so the full-page shot painted the sticky header part-way down the page. Fix in the capture tool: inject `html { scroll-behavior: auto !important }` before scrolling.
- A `display: grid` list item turns loose text and an inline `<code>` into separate anonymous grid items, so `<code>` drops to a new row. `&nbsp;` before it was inert ("from" at y=5362, `main` at y=5398). Fix: wrap the value in one element.
- `grid-template-columns: 1fr` has an automatic minimum. A tile containing a `white-space: nowrap` domain refused to shrink (page 323px at 320). Fix: `minmax(0, 1fr)` plus `min-width: 0` on the flex child.
- Absolutely positioned sr-only spans inside a horizontally scrolling strip escape its scroll box unless the slice is `position: relative` (page 2123px wide at 390).
- See also `UGC-site/CARRY-FORWARD.md` and `tulsa-plumbing-site/CARRY-FORWARD.md`.
