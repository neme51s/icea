// JavaScript для выпадающих меню по наведению на мобильных устройствах

document.addEventListener('DOMContentLoaded', function() {
    const dropdownHovers = document.querySelectorAll('.dropdown-hover');
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    
    // Для десктопов - по наведению, для мобильных - по клику
    if (!isTouchDevice) {
        // Десктоп: активация по наведению
        dropdownHovers.forEach(dropdown => {
            const link = dropdown.querySelector('.nav-link');
            const menu = dropdown.querySelector('.dropdown-menu');
            
            link.addEventListener('mouseenter', function() {
                menu.style.display = 'block';
                setTimeout(() => {
                    menu.style.opacity = '1';
                    menu.style.visibility = 'visible';
                    menu.style.transform = 'translateY(0)';
                }, 10);
            });
            
            dropdown.addEventListener('mouseleave', function() {
                menu.style.opacity = '0';
                menu.style.visibility = 'hidden';
                menu.style.transform = 'translateY(10px)';
                setTimeout(() => {
                    menu.style.display = 'none';
                }, 300);
            });
        });
    } else {
        // Мобильные: переключаем класс по клику
        dropdownHovers.forEach(dropdown => {
            const link = dropdown.querySelector('.nav-link');
            
            link.addEventListener('click', function(e) {
                if (window.innerWidth < 992) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    // Закрываем другие открытые меню
                    dropdownHovers.forEach(otherDropdown => {
                        if (otherDropdown !== dropdown && otherDropdown.classList.contains('show')) {
                            otherDropdown.classList.remove('show');
                        }
                    });
                    
                    // Переключаем текущее меню
                    dropdown.classList.toggle('show');
                }
            });
        });
        
        // Закрываем меню при клике вне его
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.dropdown-hover') && window.innerWidth < 992) {
                dropdownHovers.forEach(dropdown => {
                    dropdown.classList.remove('show');
                });
            }
        });
    }
    
    // Адаптация при изменении размера окна
    window.addEventListener('resize', function() {
        if (window.innerWidth >= 992) {
            // На десктопе показываем все меню
            dropdownHovers.forEach(dropdown => {
                dropdown.classList.remove('show');
                const menu = dropdown.querySelector('.dropdown-menu');
                if (menu) {
                    menu.style.display = 'block';
                }
            });
        } else {
            // На мобильных скрываем все меню
            dropdownHovers.forEach(dropdown => {
                const menu = dropdown.querySelector('.dropdown-menu');
                if (menu) {
                    menu.style.display = 'none';
                    menu.style.opacity = '1';
                    menu.style.visibility = 'visible';
                    menu.style.transform = 'none';
                }
            });
        }
    });
});