# Nordover — Forms & Inputs Specification

## Overview

Nordover provides a comprehensive form control system with standardized styling, validation states, and accessibility features. All form elements use consistent sizing and token-based theming.

## Form Structure

### Basic Field Group
```html
<div class="field">
  <label class="field-label" for="email">Email Address</label>
  <input type="email" id="email" class="form-input" required>
  <span class="field-help">We'll never share your email</span>
</div>
```

**Components:**
- `.field`: Container for label + input + help text
- `.field-label`: Label text, bold weight
- `.form-input`: Standard input field
- `.field-help`: Help text below input, muted color
- `.field-error`: Error message, red color

## Input Types

All inputs support:
- Focus: 3px `--color-focus` ring with 15% opacity
- Disabled: 50% opacity, `--color-subtle` background
- Placeholder: muted color

### Text Input
```html
<input type="text" class="form-input" placeholder="Enter text">
```

### Email Input
```html
<input type="email" class="form-input" required>
```

### Password Input
```html
<input type="password" class="form-input" minlength="8">
```

### Number Input
```html
<input type="number" class="form-input" min="0" max="100">
```

### Textarea
```html
<textarea class="form-textarea" rows="4" placeholder="Enter message"></textarea>
```

**Styling:**
- Minimum height: 6rem
- Resizable: vertical only
- Same focus/disabled states as input

## Checkboxes & Radios

### Checkbox
```html
<label class="cluster gap-2">
  <input type="checkbox" class="form-checkbox">
  <span>I agree to the terms</span>
</label>
```

**States:**
- Unchecked: bordered, empty
- Checked: filled with accent color, checkmark icon
- Disabled: 50% opacity
- Focus: 3px focus ring

### Radio
```html
<fieldset class="stack">
  <legend>Choose an option</legend>
  <label class="cluster gap-2">
    <input type="radio" name="choice" class="form-radio" value="a">
    <span>Option A</span>
  </label>
  <label class="cluster gap-2">
    <input type="radio" name="choice" class="form-radio" value="b">
    <span>Option B</span>
  </label>
</fieldset>
```

**Styling:**
- Circular, same sizing as checkbox
- Custom radio dot appears when checked
- Group with `<fieldset>` and `<legend>`

### Checkbox Groups
```html
<fieldset class="stack">
  <legend>Preferences</legend>
  <label class="cluster gap-2">
    <input type="checkbox" class="form-checkbox" name="prefs" value="email">
    <span>Email notifications</span>
  </label>
  <label class="cluster gap-2">
    <input type="checkbox" class="form-checkbox" name="prefs" value="sms">
    <span>SMS notifications</span>
  </label>
</fieldset>
```

## Select & Dropdown

### Select List
```html
<div class="field">
  <label class="field-label" for="country">Country</label>
  <select id="country" class="form-select">
    <option value="">Select a country</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
  </select>
</div>
```

**Styling:**
- CSS-only arrow overlay
- Hover state on background
- Same focus ring as input

### Multi-select
For multiple selections, use checkboxes grouped in a fieldset or consider a custom component:

```html
<fieldset class="form-group">
  <legend class="field-label">Interests</legend>
  <div class="form-group-item">
    <input type="checkbox" id="design" class="form-checkbox" value="design">
    <label for="design">Design</label>
  </div>
  <div class="form-group-item">
    <input type="checkbox" id="code" class="form-checkbox" value="code">
    <label for="code">Code</label>
  </div>
</fieldset>
```

## Toggles & Switches

### Toggle (Binary State)
```html
<label class="cluster gap-2">
  <input type="checkbox" class="form-toggle">
  <span>Enable notifications</span>
</label>
```

**Styling:**
- Pill-shaped toggle switch
- Width: 2.5rem, height: 1.5rem
- Animated transition on check

### Switch (App-specific)
```html
<label class="cluster gap-2">
  <input type="checkbox" class="form-switch">
  <span>Dark mode</span>
</label>
```

**Styling:**
- Similar to toggle but with app-specific colors
- Success color when active

## Range Slider

```html
<div class="field">
  <label class="field-label" for="volume">Volume</label>
  <input type="range" id="volume" class="form-input" min="0" max="100">
</div>
```

**Note:** Browser-native range styling varies. Custom styling planned for Fase 2.

## Form Validation

### Valid State
```html
<input type="email" class="form-input" value="user@example.com">
```

### Invalid State
```html
<div class="field">
  <input type="email" class="form-input" value="not-an-email">
  <span class="field-error">Please enter a valid email</span>
</div>
```

**Styling:**
- Error text in `--color-error`
- Add red border (optional, via custom style)
- Inline error message below input

## Form Layouts

### Vertical Stack
```html
<form class="stack">
  <div class="field">
    <label class="field-label">First Name</label>
    <input type="text" class="form-input">
  </div>
  <div class="field">
    <label class="field-label">Last Name</label>
    <input type="text" class="form-input">
  </div>
  <button class="btn btn-primary w-full">Submit</button>
</form>
```

### Two-Column Layout
```html
<form class="grid" style="grid-template-columns: 1fr 1fr; gap: var(--gap-component)">
  <div class="field">
    <label class="field-label">First Name</label>
    <input type="text" class="form-input">
  </div>
  <div class="field">
    <label class="field-label">Last Name</label>
    <input type="text" class="form-input">
  </div>
</form>
```

### Inline Form
```html
<form class="cluster gap-2">
  <input type="text" class="form-input" placeholder="Search">
  <button class="btn btn-primary">Search</button>
</form>
```

## Accessibility

### Label Association
Every input must have an associated label:
```html
<label for="email" class="field-label">Email</label>
<input type="email" id="email" class="form-input">
```

### Required Fields
```html
<label class="field-label">Email <span aria-label="required">*</span></label>
<input type="email" class="form-input" required aria-required="true">
```

### Error Association
```html
<input 
  type="email" 
  class="form-input" 
  aria-describedby="email-error"
  aria-invalid="true"
>
<span id="email-error" class="field-error">Invalid email format</span>
```

### Focus Management
- All inputs support `:focus-visible` with clear focus indicator
- Tab order follows document flow
- Form can be submitted with Enter key

### ARIA Attributes
- `aria-label`: For unlabeled inputs
- `aria-describedby`: Links to help/error text
- `aria-required="true"`: For required fields
- `aria-invalid="true"`: For validation errors

## Disabled & Read-only States

### Disabled Input
```html
<input type="text" class="form-input" disabled>
```
- 50% opacity
- `not-allowed` cursor
- Cannot be focused

### Read-only Input
```html
<input type="text" class="form-input" readonly value="Fixed value">
```
- Appears editable but cannot change
- Can be focused and tabbed
- Use for display of computed/auto-filled values

## Custom Styling

Override form element colors:

```css
@layer brand {
  :root {
    --input-radius: var(--radius-md);
    --color-focus: #0066FF;
  }
}
```

## Do's and Don'ts

✅ **Do:**
- Always use `<label>` with `for` attribute
- Group related checkboxes with `<fieldset>`
- Show required field indicator clearly
- Provide help text for complex fields
- Use appropriate input type (email, number, etc.)
- Show validation errors inline and clearly
- Ensure labels are visible, not just placeholders

❌ **Don't:**
- Rely on placeholder as label
- Disable form submission button without feedback
- Submit forms on blur
- Use all-caps for form labels
- Hide required field indicators
- Change focus order from document flow
- Assume all browsers support all input types

## Examples

### Login Form
```html
<form class="stack" style="max-width: 24rem">
  <div class="field">
    <label for="username" class="field-label">Username</label>
    <input type="text" id="username" class="form-input" required>
  </div>
  <div class="field">
    <label for="password" class="field-label">Password</label>
    <input type="password" id="password" class="form-input" required>
  </div>
  <label class="cluster gap-2">
    <input type="checkbox" class="form-checkbox">
    <span>Remember me</span>
  </label>
  <button class="btn btn-primary w-full">Sign In</button>
</form>
```

### Contact Form
```html
<form class="stack">
  <div class="field">
    <label for="name" class="field-label">Full Name</label>
    <input type="text" id="name" class="form-input" required>
  </div>
  <div class="field">
    <label for="email" class="field-label">Email Address</label>
    <input type="email" id="email" class="form-input" required>
  </div>
  <div class="field">
    <label for="message" class="field-label">Message</label>
    <textarea id="message" class="form-textarea" required></textarea>
    <span class="field-help">Min 10 characters</span>
  </div>
  <div class="cluster gap-2">
    <button type="submit" class="btn btn-primary">Send</button>
    <button type="reset" class="btn btn-secondary">Clear</button>
  </div>
</form>
```
