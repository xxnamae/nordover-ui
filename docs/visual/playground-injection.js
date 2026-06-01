/**
 * Playground Injection Script
 * Automatically adds "Open in Playground" buttons to component sections
 * in styleguides. Include this script in styleguide HTML files.
 */

(function() {
  const COMPONENT_PLAYGROUND_COMPONENTS = {
    'buttons': {
      label: 'Buttons',
      examples: ['btn-primary', 'btn-secondary', 'btn-ghost', 'btn-link', 'btn-sm', 'btn-lg', 'btn-touch', 'btn-elevated']
    },
    'forms': {
      label: 'Forms',
      examples: ['input-text', 'input-email', 'input-password', 'input-checkbox', 'input-radio', 'input-select', 'input-textarea']
    },
    'badges': {
      label: 'Badges',
      examples: ['badge-primary', 'badge-success', 'badge-error', 'badge-warning', 'badge-info']
    },
    'alerts': {
      label: 'Alerts',
      examples: ['alert-success', 'alert-error', 'alert-warning', 'alert-info']
    },
    'accordion': {
      label: 'Accordion',
      examples: ['accordion']
    },
    'data-patterns': {
      label: 'Data Tables',
      examples: ['data-table']
    },
    'pagination': {
      label: 'Pagination',
      examples: ['pagination']
    },
    'modals': {
      label: 'Modals',
      examples: ['modal-basic']
    }
  };

  function init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', addPlaygroundLinks);
    } else {
      addPlaygroundLinks();
    }
  }

  function addPlaygroundLinks() {
    Object.entries(COMPONENT_PLAYGROUND_COMPONENTS).forEach(([sectionId, config]) => {
      const section = document.getElementById(sectionId);
      if (section) {
        addLinkToSection(section, config);
      }
    });
  }

  function addLinkToSection(section, config) {
    // Find the section title
    const title = section.querySelector('.doc-section-title');
    if (!title) return;

    // Create a container for playground links
    const linkContainer = document.createElement('div');
    linkContainer.className = 'playground-link-container';
    linkContainer.style.cssText = `
      display: flex;
      gap: 0.5rem;
      margin-top: 0.75rem;
      flex-wrap: wrap;
    `;

    // Add link for each example
    config.examples.forEach(component => {
      const link = document.createElement('a');
      link.href = `./playground.html?component=${component}`;
      link.className = 'playground-link';
      link.textContent = `→ ${component}`;
      link.title = `Open ${component} in playground`;
      link.style.cssText = `
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.375rem 0.75rem;
        background: var(--color-accent, #0066cc);
        color: white;
        text-decoration: none;
        border-radius: var(--radius-sm, 4px);
        font-size: var(--text-xs, 0.75rem);
        font-weight: 500;
        transition: opacity var(--duration-fast, 150ms);
      `;
      link.onmouseover = () => link.style.opacity = '0.9';
      link.onmouseout = () => link.style.opacity = '1';

      linkContainer.appendChild(link);
    });

    // Insert after title
    title.parentNode.insertBefore(linkContainer, title.nextSibling);
  }

  // Initialize when script loads
  init();
})();
