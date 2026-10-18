      const htmlEl = document.documentElement;
      const themeToggle = document.getElementById('themeToggle');
      const themeIcon = document.getElementById('themeIcon');

      // Load saved theme preference
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

      // Live Filter for Tool Cards
      const searchInput = document.getElementById('toolSearch');
      const toolItems = document.querySelectorAll('.tool-item');

      searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        toolItems.forEach((item) => {
          const text = item.innerText.toLowerCase();
          item.style.display = text.includes(query) ? '' : 'none';
        });
      });
