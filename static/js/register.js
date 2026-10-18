
  document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.auth-card .form-control');

    inputs.forEach((input) => {
      // إنشاء غلاف للحقل لوضع الأيقونات بداخله
      const wrapper = document.createElement('div');
      wrapper.className = 'crispy-field-box';
      input.parentNode.insertBefore(wrapper, input);
      wrapper.appendChild(input);

      // تحديد الأيقونة المناسبة حسب اسم الحقل
      const icon = document.createElement('i');
      const name = input.name.toLowerCase();
    if (name.includes('user')) {
        icon.className = 'bi bi-person-fill crispy-left-icon';
        input.placeholder = 'Enter your username';
      } else if (name.includes('email')) {
        icon.className = 'bi bi-envelope-fill crispy-left-icon';
        input.placeholder = 'you@example.com';
      } else if (name.includes('password2')) {
        icon.className = 'bi bi-shield-check crispy-left-icon';
        input.placeholder = 'Repeat your password';
      } else if (name.includes('password')) {
        // يشمل password في تسجيل الدخول و password1 في التسجيل
        icon.className = 'bi bi-lock-fill crispy-left-icon';
        input.placeholder = 'Enter your password';
      } else {
        icon.className = 'bi bi-input-cursor-text crispy-left-icon';
      }
      wrapper.appendChild(icon);

      // إذا كان الحقل كلمة مرور، أضف زر إظهار/إخفاء ومؤشر قوة الباسورد
      if (input.type === 'password') {
        const toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.className = 'toggle-pass-btn';
        toggleBtn.innerHTML = '<i class="bi bi-eye"></i>';
        toggleBtn.addEventListener('click', () => {
          const isPass = input.type === 'password';
          input.type = isPass ? 'text' : 'password';
          toggleBtn.innerHTML = isPass ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
        });
        wrapper.appendChild(toggleBtn);

        // إضافة شريط قياس قوة كلمة المرور لحقل الباسورد الأول
        if (name.includes('password1')) {
          const strengthWrap = document.createElement('div');
          strengthWrap.className = 'strength-wrapper';
          const strengthBar = document.createElement('div');
          strengthBar.className = 'strength-bar';
          strengthWrap.appendChild(strengthBar);
          wrapper.parentNode.insertBefore(strengthWrap, wrapper.nextSibling);

          input.addEventListener('input', () => {
            const val = input.value;
            strengthWrap.style.display = val.length > 0 ? 'block' : 'none';
            let score = 0;
            if (val.length >= 8) score += 35;
            if (/[A-Z]/.test(val) && /[a-z]/.test(val)) score += 30;
            if (/[0-9]/.test(val) || /[^A-Za-z0-9]/.test(val)) score += 35;

            strengthBar.style.width = `${score}%`;
            if (score < 40) strengthBar.style.backgroundColor = '#f43f5e';
            else if (score < 80) strengthBar.style.backgroundColor = '#f59e0b';
            else strengthBar.style.backgroundColor = '#10b981';
          });
        }
      }
    });
  });
