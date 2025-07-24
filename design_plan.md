# Design Plan

This document outlines the plan for redesigning the City List website.

## Guiding Principles

*   **Pure HTML + CSS:** No CSS frameworks or JavaScript. SASS is an option if needed.
*   **Component-based:** Share as much page structure as possible to facilitate easy addition of new pages.
*   **Tunable:** Use variables for font sizes, colors, and responsive breakpoints to allow for easy adjustments.
*   **Responsive:** The design should work well on all screen sizes.

## Plan

1.  **[Done] Create `design_plan.md`:** This file will outline the design principles, color palette, typography, and reusable components.
2.  **[Done] Create a base template:** This will contain the common HTML structure (header, footer, navigation) that all other pages will inherit from. I'll create `src/templates/base.html`.
3.  **[Done] Create a static CSS file:** This will hold all the CSS rules. I'll create `src/static/css/style.css` and define CSS variables for colors, fonts, and breakpoints.
4.  **[Done] Update Django settings:** I'll configure Django to serve static files from the new `static` directory.
5.  **[Done] Refactor existing templates:** I'll update `business_list.html` and `business_detail.html` to extend the new `base.html` and use the new CSS classes.
6.  **[Done] Iterate and refine:** I'll review the changes and make adjustments to the CSS to ensure the pages look good and are responsive.
7.  **[In Progress] Make it prettier:** Experiment with colors, fonts, and layout to create a more modern and visually appealing design.

## Design System (Version 2)

### Colors

*   `--primary-color`: #2c3e50 (Midnight Blue)
*   `--secondary-color`: #ecf0f1 (Clouds)
*   `--accent-color`: #1abc9c (Turquoise)
*   `--text-color`: #34495e (Wet Asphalt)
*   `--background-color`: #fff
*   `--link-hover-color`: #2ecc71 (Emerald)

### Typography

*   `--font-family`: "Lato", "Helvetica Neue", Helvetica, Arial, sans-serif
*   `--font-size-base`: 16px
*   `--font-size-h1`: 2.5rem
*   `--font-size-h2`: 2rem
*   `--font-size-h3`: 1.75rem

### Breakpoints

*   `--breakpoint-sm`: 576px
*   `--breakpoint-md`: 768px
*   `--breakpoint-lg`: 992px
*   `--breakpoint-xl`: 1200px

## Design System (Version 1)

### Colors

*   `--primary-color`: #333
*   `--secondary-color`: #eee
*   `--accent-color`: #f4511e
*   `--text-color`: #333
*   `--background-color`: #fff

### Typography

*   `--font-family`: "Helvetica Neue", Helvetica, Arial, sans-serif
*   `--font-size-base`: 16px
*   `--font-size-h1`: 2.5rem
*   `--font-size-h2`: 2rem
*   `--font-size-h3`: 1.75rem

### Breakpoints

*   `--breakpoint-sm`: 576px
*   `--breakpoint-md`: 768px
*   `--breakpoint-lg`: 992px
*   `--breakpoint-xl`: 1200px
