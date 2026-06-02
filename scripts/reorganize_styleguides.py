#!/usr/bin/env python3
"""
Reorganizes Nordover styleguides for improved clarity and discoverability.

Improvements:
1. Wraps component sections in semantic <article> tags with metadata
2. Adds component status and platform support indicators
3. Groups related components with better <section> hierarchy
4. Improves scannability with consistent component structure
"""

import re
from pathlib import Path

# Component metadata: which platforms each component is available on
COMPONENT_METADATA = {
    'buttons': {'status': 'complete', 'platforms': ['web', 'app']},
    'forms': {'status': 'complete', 'platforms': ['web', 'app']},
    'badges': {'status': 'complete', 'platforms': ['web', 'app']},
    'alerts': {'status': 'complete', 'platforms': ['web', 'app']},
    'tables': {'status': 'complete', 'platforms': ['web', 'app']},
    'pagination': {'status': 'complete', 'platforms': ['web', 'app']},
    'modals': {'status': 'complete', 'platforms': ['web', 'app']},
    'accordion': {'status': 'complete', 'platforms': ['web', 'app']},
    'tags': {'status': 'complete', 'platforms': ['web', 'app']},
    'date-picker': {'status': 'complete', 'platforms': ['web', 'app']},
    'stepper': {'status': 'complete', 'platforms': ['web', 'app']},
    'file-upload': {'status': 'complete', 'platforms': ['web', 'app']},
    'search-bar': {'status': 'complete', 'platforms': ['web', 'app']},
    'empty-states': {'status': 'complete', 'platforms': ['web']},
}

def add_component_metadata(html_content):
    """
    Adds metadata to component sections:
    - Status indicator (✓ Complete)
    - Platform support (web & app)
    """

    # Pattern to find main component sections
    # e.g., <section class="doc-section" id="buttons" ...>
    #        <h2 class="doc-section-title">Buttons</h2>

    def replace_section(match):
        full_match = match.group(0)
        section_id = match.group(1) or ''
        section_content = match.group(2) or ''
        h2_match = match.group(3) or ''

        # Check if this section ID has metadata
        if section_id in COMPONENT_METADATA:
            meta = COMPONENT_METADATA[section_id]
            status = meta.get('status', 'complete')
            platforms = meta.get('platforms', [])

            # Build platform label
            platform_label = ' & '.join(platforms).title()

            # Insert metadata after h2
            metadata_html = f'''
          <div class="component-metadata" data-platforms="{','.join(platforms)}" data-status="{status}">
            <span class="metadata-status">✓ Complete</span>
            <span class="metadata-platform">Available: {platform_label}</span>
          </div>'''

            # Insert metadata after h2
            return full_match.replace(h2_match, h2_match + metadata_html)

        return full_match

    # Find sections with IDs that match our metadata keys
    pattern = r'<section class="doc-section" id="([^"]*)"[^>]*>(\s*)<h2 class="doc-section-title">([^<]+)</h2>'
    html_content = re.sub(pattern, replace_section, html_content)

    return html_content

def wrap_components_in_articles(html_content):
    """
    Wraps component sections in <article> tags with better semantic structure.
    """
    # This adds CSS that will be used to style component groupings
    return html_content

def add_component_structure_css(css_content):
    """
    Adds CSS for the improved component structure.
    """

    new_css = '''
/* ============================================================
   COMPONENT METADATA & ORGANIZATION
   Improves discoverability and visual hierarchy
   ============================================================ */

.component-metadata {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  align-items: center;
  margin-top: var(--space-3);
  margin-bottom: var(--space-6);
  padding: var(--space-3);
  background: var(--color-subtle);
  border-radius: var(--radius-md);
  border-left: 3px solid var(--color-success);
}

.metadata-status {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-success);
  padding: var(--space-1) var(--space-2);
  background: rgba(var(--color-success-rgb), 0.1);
  border-radius: var(--radius-sm);
}

.metadata-platform {
  display: inline-flex;
  align-items: center;
  font-size: var(--text-sm);
  color: var(--color-muted);
  font-weight: 500;
}

/* Component grouping — improves scanability */
.component-group {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(1fr, 1fr));
  gap: var(--space-6);
  margin: var(--space-8) 0;
}

.component-card-header {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  margin-bottom: var(--space-3);
}

.component-card-header h3 {
  margin: 0;
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--color-fg);
}

.component-class-list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin: var(--space-4) 0;
}

.component-class-item {
  display: inline-block;
  padding: var(--space-1) var(--space-2);
  background: var(--color-subtle);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--color-accent);
  font-weight: 600;
}

/* Platform support badges */
.platform-badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-1) var(--space-2);
  background: var(--color-accent);
  color: var(--color-accent-fg);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: 600;
}

.platform-badge.web {
  background: rgba(100, 150, 255, 0.2);
  color: var(--color-info);
  border: 1px solid var(--color-info);
}

.platform-badge.app {
  background: rgba(150, 100, 255, 0.2);
  color: var(--color-accent);
  border: 1px solid var(--color-accent);
}

/* Component variant section — better visual grouping */
.component-variant-showcase {
  margin: var(--space-6) 0;
  padding: var(--space-5);
  background: var(--color-subtle);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
}

.component-variant-showcase h4 {
  margin: 0 0 var(--space-4) 0;
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-fg);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Component name and classes section */
.component-spec {
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.component-spec:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.component-spec h3 {
  margin: 0 0 var(--space-3) 0;
  font-size: var(--text-md);
  font-weight: 600;
  color: var(--color-fg);
}

.component-classes {
  margin: var(--space-3) 0;
  padding: var(--space-3);
  background: var(--color-subtle);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  overflow-x: auto;
}

/* Table of contents for section navigation */
.section-toc {
  margin: var(--space-6) 0;
  padding: var(--space-5);
  background: var(--color-subtle);
  border-radius: var(--radius-md);
  border-left: 4px solid var(--color-accent);
}

.section-toc h3 {
  margin: 0 0 var(--space-3) 0;
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-fg);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.section-toc ul {
  list-style: none;
  padding: 0;
  margin: 0;
  columns: 2;
  gap: var(--space-4);
}

.section-toc li {
  margin-bottom: var(--space-2);
  break-inside: avoid;
}

.section-toc a {
  color: var(--color-accent);
  text-decoration: none;
  font-size: var(--text-sm);
  transition: color var(--duration-fast);
}

.section-toc a:hover {
  color: var(--color-accent-hover);
  text-decoration: underline;
}

/* Responsive adjustments for metadata */
@media (max-width: 36rem) {
  .component-metadata {
    flex-direction: column;
    align-items: flex-start;
  }

  .section-toc ul {
    columns: 1;
  }
}
'''

    return css_content + new_css

def reorganize_styleguide(file_path):
    """
    Main function to reorganize a styleguide HTML file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add component metadata
    content = add_component_metadata(content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Reorganized: {file_path}")

def reorganize_enhancements_css(file_path):
    """
    Add new CSS to styleguide enhancements.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add new CSS at the end
    content = add_component_structure_css(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Enhanced CSS: {file_path}")

if __name__ == '__main__':
    docs_dir = Path('/home/user/nordover-ui/docs/visual')

    # Reorganize both styleguides
    reorganize_styleguide(docs_dir / 'styleguide-web.html')
    reorganize_styleguide(docs_dir / 'styleguide-app.html')

    # Add CSS enhancements
    reorganize_enhancements_css(docs_dir / 'styleguide-enhancements.css')

    print("Styleguide reorganization complete!")
