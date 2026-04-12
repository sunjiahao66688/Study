// 简单的JavaScript功能

document.addEventListener('DOMContentLoaded', function() {
    console.log('网站已加载完成！');
    
    // 更新页面访问时间
    updateVisitTime();
    
    // 添加点击效果到卡片
    addCardClickEffects();
    
    // 添加滚动效果
    addScrollEffects();
    
    // 显示当前时间
    updateCurrentTime();
    
    // 添加一些交互功能
    addInteractiveFeatures();
});

// 更新访问时间
function updateVisitTime() {
    const visitTime = new Date().toLocaleString('zh-CN');
    const visitElement = document.getElementById('visit-time');
    if (visitElement) {
        visitElement.textContent = visitTime;
    }
}

// 添加卡片点击效果
function addCardClickEffects() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
}

// 添加滚动效果
function addScrollEffects() {
    let lastScrollTop = 0;
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // 向下滚动
            if (header) {
                header.style.transform = 'translateY(-100%)';
            }
        } else {
            // 向上滚动
            if (header) {
                header.style.transform = 'translateY(0)';
            }
        }
        
        lastScrollTop = scrollTop;
    });
}

// 更新当前时间
function updateCurrentTime() {
    const timeElement = document.getElementById('current-time');
    if (timeElement) {
        function updateTime() {
            const now = new Date();
            timeElement.textContent = now.toLocaleTimeString('zh-CN');
        }
        
        updateTime();
        setInterval(updateTime, 1000);
    }
}

// 添加交互功能
function addInteractiveFeatures() {
    // 主题切换按钮
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            this.textContent = document.body.classList.contains('dark-theme') 
                ? '切换到亮色主题' 
                : '切换到暗色主题';
        });
    }
    
    // 复制代码功能
    const codeBlocks = document.querySelectorAll('.code');
    codeBlocks.forEach(block => {
        block.addEventListener('click', function() {
            const text = this.textContent;
            navigator.clipboard.writeText(text).then(() => {
                const originalText = this.textContent;
                this.textContent = '已复制到剪贴板！';
                setTimeout(() => {
                    this.textContent = originalText;
                }, 1500);
            });
        });
    });
    
    // 显示/隐藏内容
    const toggleButtons = document.querySelectorAll('.toggle-content');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const target = document.getElementById(targetId);
            if (target) {
                target.classList.toggle('hidden');
                this.textContent = target.classList.contains('hidden') 
                    ? '显示更多' 
                    : '显示更少';
            }
        });
    });
}

// 简单的表单验证示例
function validateForm(form) {
    const email = form.querySelector('input[type="email"]');
    const message = form.querySelector('textarea');
    
    if (email && !email.value.includes('@')) {
        alert('请输入有效的电子邮件地址');
        email.focus();
        return false;
    }
    
    if (message && message.value.trim().length < 10) {
        alert('消息内容至少需要10个字符');
        message.focus();
        return false;
    }
    
    return true;
}

// AJAX请求示例
function fetchData(url, callback) {
    fetch(url)
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.error('请求失败:', error));
}

// 工具函数：防抖
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 工具函数：节流
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}