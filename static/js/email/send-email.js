document.addEventListener('DOMContentLoaded', () => {
  const fields = document.querySelectorAll(
    '.email-card input.form-control, .email-card select.form-select'
  );

  fields.forEach((field) => {
    if (field.type === 'hidden' || field.closest('.crispy-field-box')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'crispy-field-box';
    field.parentNode.insertBefore(wrapper, field);
    wrapper.appendChild(field);

    const icon = document.createElement('i');
    const name = field.name.toLowerCase();

    if (name.includes('email_list') || field.tagName === 'SELECT') {
      icon.className = 'bi bi-people-fill crispy-left-icon';
    } else if (name.includes('subject')) {
      icon.className = 'bi bi-chat-quote-fill crispy-left-icon';
      field.placeholder = 'Enter email campaign subject...';
    } else if (name.includes('attachment') || field.type === 'file') {
      icon.className = 'bi bi-paperclip crispy-left-icon';
    } else {
      icon.className = 'bi bi-envelope-fill crispy-left-icon';
    }

    wrapper.appendChild(icon);
  });

  // مزامنة ألوان منطقة الكتابة داخل CKEditor مع وضع الصفحة (Dark / Light)
  const syncCKEditorTheme = () => {
    if (typeof CKEDITOR === 'undefined') return;

    const isLight = document.documentElement.getAttribute('data-bs-theme') === 'light';
    const bgColor = isLight ? '#f8fafc' : '#0f172a';
    const textColor = isLight ? '#0f172a' : '#f8fafc';

    Object.values(CKEDITOR.instances).forEach((instance) => {
      if (instance.document && instance.document.getBody()) {
        const body = instance.document.getBody();
        body.setStyle('background-color', bgColor);
        body.setStyle('color', textColor);
        body.setStyle('font-family', "'Plus Jakarta Sans', sans-serif");
        body.setStyle('font-size', '15px');
        body.setStyle('line-height', '1.6');
        body.setStyle('padding', '14px 16px');
      }
    });
  };

  if (typeof CKEDITOR !== 'undefined') {
    CKEDITOR.on('instanceReady', (evt) => {
      syncCKEditorTheme();

      const editor = evt.editor;
      const container = editor.container ? editor.container.$ : null;

      editor.on('focus', () => {
        if (container) container.classList.add('editor-focused');
      });

      editor.on('blur', () => {
        if (container) container.classList.remove('editor-focused');
      });
    });
  }

  const themeObserver = new MutationObserver(() => {
    syncCKEditorTheme();
  });

  themeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-bs-theme'],
  });
});

