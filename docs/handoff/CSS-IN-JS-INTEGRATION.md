# CSS-in-JS Framework Integration

**Companion Guide:** Framework Integration Guide (`FRAMEWORK-INTEGRATION.md`)

---

## Overview

While Nordover is optimized for native CSS, it works seamlessly with CSS-in-JS frameworks. This guide covers best practices for:

- Emotion
- Styled Components
- Vanilla Extract
- CSS Modules

---

## Emotion

Emotion is a lightweight CSS-in-JS library that pairs well with React.

### Setup

```bash
npm install @emotion/react @emotion/styled
npm install @xxnamae/nordover-ui
```

### Import Nordover CSS

```typescript
// app.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';

export default function App() {
  return <Dashboard />;
}
```

### Use Emotion for Custom Styles

```typescript
// components/Card.tsx
import { css } from '@emotion/react';

const cardStyle = css`
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  
  @media (prefers-color-scheme: dark) {
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  }
`;

export function Card({ children }) {
  return <div css={cardStyle}>{children}</div>;
}
```

### Emotion + Nordover Classes

```typescript
// components/Button.tsx
import { css } from '@emotion/react';

interface CustomButtonProps {
  variant?: 'primary' | 'secondary';
  children: React.ReactNode;
}

export function CustomButton({ variant = 'primary', children }: CustomButtonProps) {
  const customStyle = css`
    font-weight: 600;
    letter-spacing: 0.5px;
    
    &:hover {
      transform: translateY(-2px);
    }
  `;

  return (
    <button className={`btn btn-${variant}`} css={customStyle}>
      {children}
    </button>
  );
}
```

---

## Styled Components

Styled Components is popular in React applications for component-scoped styling.

### Setup

```bash
npm install styled-components
npm install @xxnamae/nordover-ui
```

### Import Nordover CSS

```typescript
// app.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';
import { StyledApp } from './App.styled';

export default function App() {
  return <StyledApp><Dashboard /></StyledApp>;
}
```

### Create Styled Components

```typescript
// components/Card.styled.ts
import styled from 'styled-components';

export const StyledCard = styled.div`
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  transition: all var(--duration-moderate);

  &:hover {
    border-color: var(--color-accent);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
`;
```

### Use Styled Components with Nordover

```typescript
// components/Card.tsx
import React from 'react';
import { StyledCard } from './Card.styled';

export function Card({ children }) {
  return <StyledCard>{children}</StyledCard>;
}
```

### Composing Nordover Classes with Styled Components

```typescript
// components/Button.tsx
import styled from 'styled-components';

export const StyledButton = styled.button`
  /* Inherit base button styles from Nordover */
  /* Add custom Styled Components styles on top */
  
  font-weight: var(--fw-semibold);
  transition: all var(--duration-base);
  
  &:active {
    transform: scale(0.95);
  }
`;

export function Button({ variant = 'primary', children }) {
  return (
    <StyledButton className={`btn btn-${variant}`}>
      {children}
    </StyledButton>
  );
}
```

---

## CSS Modules

CSS Modules are great for locally-scoped CSS alongside Nordover globals.

### Setup

```bash
npm install @xxnamae/nordover-ui
# CSS Modules support is built into most modern bundlers
```

### Import Nordover Globally

```typescript
// app.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';

export default function App() {
  return <Dashboard />;
}
```

### Create CSS Module

```css
/* Card.module.css */
.card {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  transition: all var(--duration-moderate);
}

.card:hover {
  border-color: var(--color-accent);
  box-shadow: 0 4px 12px color-mix(in oklch, var(--color-fg) 15%, transparent);
}

.cardTitle {
  font-size: var(--text-lg);
  font-weight: var(--fw-semibold);
  margin: 0 0 var(--space-2) 0;
}
```

### Use CSS Module with Nordover

```typescript
// Card.tsx
import React from 'react';
import styles from './Card.module.css';

interface CardProps {
  title: string;
  children: React.ReactNode;
}

export function Card({ title, children }: CardProps) {
  return (
    <div className={styles.card}>
      <h3 className={styles.cardTitle}>{title}</h3>
      {children}
    </div>
  );
}
```

### Compose Classes

```typescript
// Button.tsx
import styles from './Button.module.css';

export function Button({ variant = 'primary', children }) {
  return (
    <button className={`btn btn-${variant} ${styles.customButton}`}>
      {children}
    </button>
  );
}
```

---

## Vanilla Extract

Vanilla Extract is a zero-runtime CSS-in-TS solution for static styling.

### Setup

```bash
npm install @vanilla-extract/css
npm install @vanilla-extract/recipes
npm install @xxnamae/nordover-ui
```

### Create Vanilla Extract Styles

```typescript
// styles/card.css.ts
import { style } from '@vanilla-extract/css';

export const cardStyle = style({
  padding: 'var(--space-4)',
  borderRadius: 'var(--radius-md)',
  background: 'var(--color-surface)',
  border: '1px solid var(--color-border)',
  transition: 'all var(--duration-moderate)',

  ':hover': {
    borderColor: 'var(--color-accent)',
    boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
  },
});

export const cardTitle = style({
  fontSize: 'var(--text-lg)',
  fontWeight: 'var(--fw-semibold)',
  margin: 0,
  marginBottom: 'var(--space-2)',
});
```

### Use Vanilla Extract with Nordover

```typescript
// Card.tsx
import React from 'react';
import { cardStyle, cardTitle } from './styles/card.css';

export function Card({ title, children }) {
  return (
    <div className={cardStyle}>
      <h3 className={cardTitle}>{title}</h3>
      {children}
    </div>
  );
}
```

---

## Best Practices

### 1. Keep Nordover as Foundation

Always import Nordover as a global foundation:

```typescript
// app.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';

// Then use your CSS-in-JS for custom component styling
```

### 2. Use CSS Custom Properties

```typescript
const customCard = css`
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  /* These automatically update with dark mode */
`;
```

### 3. Leverage CSS Layers

If your CSS-in-JS framework supports `@layer`, use it:

```css
@layer components {
  /* Your styled components inherit Nordover's layer order */
}
```

### 4. Dark Mode Considerations

CSS-in-JS frameworks automatically inherit dark mode from Nordover:

```typescript
const darkModeAwareCard = css`
  background: var(--color-surface);
  
  /* Dark mode? Nordover variables automatically update */
  /* No additional dark mode CSS needed here */
`;
```

### 5. Performance Optimization

CSS-in-JS adds runtime overhead. Minimize by:

- Using static styles where possible
- Extracting animation timing to CSS custom properties
- Keeping component-specific styles minimal
- Let Nordover handle complex components (cards, forms, etc.)

---

## Example: Complete App with Emotion

```typescript
// app.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';
import { css } from '@emotion/react';
import { Header } from './components/Header';
import { Dashboard } from './pages/Dashboard';

const appStyle = css`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: var(--color-bg);
  color: var(--color-fg);
  transition: background-color var(--duration-slow), color var(--duration-slow);
`;

export default function App() {
  return (
    <div css={appStyle}>
      <Header />
      <Dashboard />
    </div>
  );
}
```

```typescript
// components/Header.tsx
import { css } from '@emotion/react';

const headerStyle = css`
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  padding: var(--space-4);
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

export function Header() {
  return (
    <header css={headerStyle}>
      <h1 className="t-heading-lg">My App</h1>
      <button className="btn btn-ghost">Menu</button>
    </header>
  );
}
```

---

## Resources

- **Emotion Docs:** https://emotion.sh/docs/introduction
- **Styled Components Docs:** https://styled-components.com/docs
- **Vanilla Extract Docs:** https://vanilla-extract.style/
- **CSS Modules Docs:** https://github.com/css-modules/css-modules
- **Nordover Tokens:** `docs/visual/tokens/tokens-web.css`

---

**License:** MIT  
**Last Updated:** 2026-06-01
