 const htmlEl = document.documentElement;
      const themeToggle = document.getElementById('themeToggle');
      const themeIcon = document.getElementById('themeIcon');

      const savedTheme = localStorage.getItem('django_auto_theme') || 'dark';
      setTheme(savedTheme);

      themeToggle.addEventListener('click', () => {
        const currentTheme = htmlEl.getAttribute('data-bs-theme');
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(nextTheme);
      });

      function setTheme(theme) {
        htmlEl.setAttribute('data-bs-theme', theme);
        localStorage.setItem('django_auto_theme', theme);
        themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
      }

      const fileInput = document.getElementById('form-control');
      const dropZone = document.getElementById('dropZone');
      const fileBadge = document.getElementById('fileBadge');
      const fileNameText = document.getElementById('fileNameText');

      fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
          const file = fileInput.files[0];
          const sizeKB = (file.size / 1024).toFixed(1);
          fileNameText.textContent = `${file.name} (${sizeKB} KB)`;
          fileBadge.style.display = 'inline-flex';
        }
      });

      ['dragenter', 'dragover'].forEach((evt) => {
        dropZone.addEventListener(evt, () => dropZone.classList.add('dragover'));
      });
      ['dragleave', 'drop'].forEach((evt) => {
        dropZone.addEventListener(evt, () => dropZone.classList.remove('dragover'));
      });