// Main JavaScript for Portfolio Website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Check if new visitor
    fetch('/api/check-new-visitor')
        .then(response => response.json())
        .then(data => {
            if (data.is_new) {
                setTimeout(function() {
                    const welcomeToast = document.createElement('div');
                    welcomeToast.className = 'toast';
                    welcomeToast.setAttribute('role', 'alert');
                    welcomeToast.setAttribute('aria-live', 'assertive');
                    welcomeToast.setAttribute('aria-atomic', 'true');
                    welcomeToast.innerHTML = `
                        <div class="toast-header">
                            <strong class="me-auto">Welcome!</strong>
                            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                        </div>
                        <div class="toast-body">
                            Thanks for visiting my portfolio! Feel free to explore my projects and skills.
                        </div>
                    `;
                    
                    document.querySelector('.position-fixed').appendChild(welcomeToast);
                    const toast = new bootstrap.Toast(welcomeToast);
                    toast.show();
                }, 3000);
            }
        })
        .catch(error => console.error('Error checking if new visitor:', error));
    
    // Animate elements when they come into view
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    animateElements.forEach(element => {
        observer.observe(element);
    });
});