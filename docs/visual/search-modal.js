/**
 * Search Modal Dialog
 * Professional search modal implementation with keyboard navigation and accessibility
 */

class SearchModal {
  constructor() {
    this.modal = null;
    this.searchInput = null;
    this.resultsContainer = null;
    this.results = [];
    this.selectedIndex = -1;
    this.init();
  }

  init() {
    this.createModal();
    this.setupEventListeners();
  }

  createModal() {
    // Create dialog element
    this.modal = document.createElement('dialog');
    this.modal.id = 'search-modal';
    this.modal.className = 'search-dialog';
    this.modal.setAttribute('role', 'dialog');
    this.modal.setAttribute('aria-labelledby', 'search-title');
    this.modal.setAttribute('aria-modal', 'true');

    // Create modal structure
    const modalContent = document.createElement('div');
    modalContent.className = 'search-dialog-content';

    // Header with title and close button
    const header = document.createElement('div');
    header.className = 'search-dialog-header';
    header.innerHTML = `
      <h2 id="search-title" class="search-dialog-title">Søk i styleguide</h2>
      <button class="search-dialog-close" aria-label="Lukk søk (ESC)" data-testid="search-close">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="1.5" fill="none">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    `;

    // Search input
    const inputWrapper = document.createElement('div');
    inputWrapper.className = 'search-dialog-input-wrapper';
    this.searchInput = document.createElement('input');
    this.searchInput.type = 'search';
    this.searchInput.id = 'search-input';
    this.searchInput.className = 'search-dialog-input';
    this.searchInput.placeholder = 'Søk etter komponenter, tokens, patterns...';
    this.searchInput.setAttribute('aria-label', 'Søk i styleguide');
    this.searchInput.setAttribute('aria-autocomplete', 'list');
    this.searchInput.setAttribute('aria-controls', 'search-results-container');
    inputWrapper.appendChild(this.searchInput);

    // Results container
    this.resultsContainer = document.createElement('div');
    this.resultsContainer.id = 'search-results-container';
    this.resultsContainer.className = 'search-dialog-results';
    this.resultsContainer.setAttribute('role', 'listbox');
    this.resultsContainer.setAttribute('aria-live', 'polite');
    this.resultsContainer.setAttribute('aria-label', 'Søkeresultater');

    // Empty state
    const emptyState = document.createElement('div');
    emptyState.className = 'search-dialog-empty';
    emptyState.innerHTML = `
      <p>Skriv for å søke etter komponenter og tokens</p>
      <div class="search-dialog-shortcuts">
        <div class="shortcut"><kbd>↑↓</kbd> Navigér</div>
        <div class="shortcut"><kbd>Enter</kbd> Velg</div>
        <div class="shortcut"><kbd>ESC</kbd> Lukk</div>
      </div>
    `;
    this.resultsContainer.appendChild(emptyState);

    // Assemble modal
    modalContent.appendChild(header);
    modalContent.appendChild(inputWrapper);
    modalContent.appendChild(this.resultsContainer);
    this.modal.appendChild(modalContent);

    // Add backdrop click handler and append to body
    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) {
        this.close();
      }
    });

    document.body.appendChild(this.modal);
  }

  setupEventListeners() {
    // Ctrl+K and Cmd+K to open
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        this.open();
      }
    });

    // Close button
    const closeBtn = this.modal.querySelector('.search-dialog-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => this.close());
    }

    // Search input
    this.searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim();
      if (query.length > 0) {
        this.search(query);
      } else {
        this.showEmpty();
      }
      this.selectedIndex = -1; // Reset selection on new search
    });

    // Keyboard navigation
    this.searchInput.addEventListener('keydown', (e) => {
      const resultElements = this.resultsContainer.querySelectorAll('[role="option"]');

      switch (e.key) {
        case 'Escape':
          this.close();
          break;

        case 'ArrowDown':
          e.preventDefault();
          this.selectedIndex = Math.min(this.selectedIndex + 1, resultElements.length - 1);
          this.updateSelection(resultElements);
          break;

        case 'ArrowUp':
          e.preventDefault();
          this.selectedIndex = Math.max(this.selectedIndex - 1, -1);
          this.updateSelection(resultElements);
          break;

        case 'Enter':
          e.preventDefault();
          if (this.selectedIndex >= 0 && resultElements[this.selectedIndex]) {
            resultElements[this.selectedIndex].click();
          }
          break;
      }
    });

    // Focus trap - keep focus within modal when open
    this.modal.addEventListener('keydown', (e) => {
      if (e.key === 'Tab') {
        const focusableElements = this.modal.querySelectorAll(
          'input, button, [role="option"]'
        );
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (e.shiftKey) {
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement.focus();
          }
        } else {
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement.focus();
          }
        }
      }
    });
  }

  open() {
    this.modal.showModal();
    this.searchInput.focus();
    this.searchInput.select();
    this.showEmpty();
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.modal.close();
    document.body.style.overflow = '';
    this.searchInput.value = '';
    this.selectedIndex = -1;
  }

  search(query) {
    const sections = document.querySelectorAll('.doc-section[id]');
    this.results = [];

    sections.forEach((section) => {
      const title = section.querySelector('h2')?.textContent || '';
      const desc = section.querySelector('p')?.textContent || '';
      const combinedText = (title + ' ' + desc).toLowerCase();

      if (combinedText.includes(query.toLowerCase())) {
        this.results.push({
          id: section.id,
          title: title.trim(),
          desc: desc.substring(0, 100).trim(),
        });
      }
    });

    this.renderResults();
  }

  renderResults() {
    const container = this.resultsContainer;
    container.innerHTML = '';

    if (this.results.length === 0) {
      const noResults = document.createElement('div');
      noResults.className = 'search-dialog-no-results';
      noResults.textContent = 'Ingen resultater funnet';
      container.appendChild(noResults);
      return;
    }

    this.results.forEach((result, index) => {
      const resultEl = document.createElement('div');
      resultEl.setAttribute('role', 'option');
      resultEl.setAttribute('data-index', index);
      resultEl.className = 'search-dialog-result';

      resultEl.innerHTML = `
        <div class="search-result-title">${this.escapeHtml(result.title)}</div>
        <div class="search-result-desc">${this.escapeHtml(result.desc)}${result.desc.length >= 100 ? '...' : ''}</div>
      `;

      resultEl.addEventListener('click', () => {
        window.location.hash = result.id;
        this.close();
      });

      resultEl.addEventListener('mouseenter', () => {
        this.selectedIndex = index;
        this.updateSelection(container.querySelectorAll('[role="option"]'));
      });

      container.appendChild(resultEl);
    });
  }

  updateSelection(elements) {
    elements.forEach((el, idx) => {
      if (idx === this.selectedIndex) {
        el.classList.add('selected');
        el.setAttribute('aria-selected', 'true');
        el.scrollIntoView({ block: 'nearest' });
      } else {
        el.classList.remove('selected');
        el.setAttribute('aria-selected', 'false');
      }
    });
  }

  showEmpty() {
    this.resultsContainer.innerHTML = `
      <div class="search-dialog-empty">
        <p>Skriv for å søke etter komponenter og tokens</p>
        <div class="search-dialog-shortcuts">
          <div class="shortcut"><kbd>↑↓</kbd> Navigér</div>
          <div class="shortcut"><kbd>Enter</kbd> Velg</div>
          <div class="shortcut"><kbd>ESC</kbd> Lukk</div>
        </div>
      </div>
    `;
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

// Initialize search modal when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new SearchModal();
  });
} else {
  new SearchModal();
}
