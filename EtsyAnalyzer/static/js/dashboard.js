// EtsyAnalyzer Workflow Dashboard JavaScript

// Global state
let workflowState = {
    currentStage: 'analysis',
    loading: false,
    data: {}
};

// Utility functions
function showLoading(element, message = 'Loading...') {
    if (typeof element === 'string') {
        element = document.getElementById(element);
    }
    if (element) {
        element.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${message}`;
        element.disabled = true;
        element.classList.add('loading');
    }
}

function hideLoading(element, originalText = '') {
    if (typeof element === 'string') {
        element = document.getElementById(element);
    }
    if (element) {
        element.innerHTML = originalText;
        element.disabled = false;
        element.classList.remove('loading');
    }
}

function showAlert(message, type = 'info', autoHide = true) {
    const alertContainer = document.querySelector('.container-fluid');
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    // Insert at the top
    alertContainer.insertBefore(alertDiv, alertContainer.firstChild);

    // Auto-hide after 5 seconds
    if (autoHide) {
        setTimeout(() => {
            const alert = bootstrap.Alert.getOrCreateInstance(alertDiv);
            alert.close();
        }, 5000);
    }
}

function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString();
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Copied to clipboard!', 'success');
    }).catch(() => {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showAlert('Copied to clipboard!', 'success');
    });
}

// API functions
async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    };

    if (data && method !== 'GET') {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(endpoint, options);
        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || `HTTP ${response.status}`);
        }

        return result;
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

// Workflow management
function updateWorkflowStatus() {
    fetch('/api/workflow-status')
        .then(response => response.json())
        .then(data => {
            workflowState.data = data;
            // Update UI elements that show status
            updateStatusCards(data);
        })
        .catch(error => {
            console.error('Failed to update workflow status:', error);
        });
}

function updateStatusCards(data) {
    // Update status cards if they exist on the page
    const pendingElement = document.querySelector('[data-status="pending-briefs"]');
    if (pendingElement) {
        pendingElement.textContent = data.pending_briefs || 0;
    }

    const approvedElement = document.querySelector('[data-status="approved-briefs"]');
    if (approvedElement) {
        approvedElement.textContent = data.approved_briefs || 0;
    }

    const assetsElement = document.querySelector('[data-status="total-assets"]');
    if (assetsElement) {
        assetsElement.textContent = data.total_assets || 0;
    }

    const printfulElement = document.querySelector('[data-status="printful-ready"]');
    if (printfulElement) {
        printfulElement.textContent = data.printful_ready || 0;
    }
}

// File upload handling
function handleFileUpload(fileInput, briefId) {
    const file = fileInput.files[0];
    if (!file) return;

    // Validate file
    if (!file.type.includes('png')) {
        showAlert('Please upload a PNG file only.', 'danger');
        return;
    }

    if (file.size > 20 * 1024 * 1024) { // 20MB
        showAlert('File size must be less than 20MB.', 'danger');
        return;
    }

    // Show progress
    const progressContainer = document.createElement('div');
    progressContainer.className = 'upload-progress mt-3';
    progressContainer.innerHTML = `
        <div class="progress">
            <div class="progress-bar progress-bar-striped progress-bar-animated"
                 role="progressbar" style="width: 0%"></div>
        </div>
        <small class="text-muted">Uploading...</small>
    `;

    fileInput.parentNode.appendChild(progressContainer);

    // Upload file
    const formData = new FormData();
    formData.append('file', file);
    formData.append('brief_id', briefId);

    const xhr = new XMLHttpRequest();
    const progressBar = progressContainer.querySelector('.progress-bar');
    const statusText = progressContainer.querySelector('small');

    xhr.upload.onprogress = function(e) {
        if (e.lengthComputable) {
            const percentComplete = (e.loaded / e.total) * 100;
            progressBar.style.width = percentComplete + '%';
            statusText.textContent = `Uploading... ${Math.round(percentComplete)}%`;
        }
    };

    xhr.onload = function() {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.success) {
                showAlert('Design uploaded successfully!', 'success');
                setTimeout(() => location.reload(), 1000);
            } else {
                showAlert('Upload failed: ' + response.error, 'danger');
                progressContainer.remove();
            }
        } else {
            showAlert('Upload failed. Please try again.', 'danger');
            progressContainer.remove();
        }
    };

    xhr.onerror = function() {
        showAlert('Network error. Please check your connection.', 'danger');
        progressContainer.remove();
    };

    xhr.open('POST', '/api/upload-design');
    xhr.send(formData);
}

// Drag and drop functionality
function initializeDragAndDrop() {
    const dropZones = document.querySelectorAll('.drop-zone');

    dropZones.forEach(zone => {
        zone.addEventListener('dragover', function(e) {
            e.preventDefault();
            zone.classList.add('drag-over');
        });

        zone.addEventListener('dragleave', function(e) {
            e.preventDefault();
            zone.classList.remove('drag-over');
        });

        zone.addEventListener('drop', function(e) {
            e.preventDefault();
            zone.classList.remove('drag-over');

            const files = e.dataTransfer.files;
            if (files.length > 0) {
                const form = zone.closest('.upload-form');
                const briefId = form ? form.dataset.briefId : null;
                if (briefId) {
                    const input = zone.querySelector('input[type="file"]');
                    input.files = files;
                    handleFileUpload(input, briefId);
                }
            }
        });
    });
}

// Form validation
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });

    return isValid;
}

// Export functions
function exportDesignPrompts() {
    const prompts = [];
    const promptElements = document.querySelectorAll('[data-prompt]');

    promptElements.forEach(element => {
        prompts.push({
            briefId: element.dataset.briefId,
            prompt: element.dataset.prompt
        });
    });

    if (prompts.length === 0) {
        showAlert('No prompts to export.', 'warning');
        return;
    }

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(prompts, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `design_prompts_${new Date().toISOString().split('T')[0]}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();

    showAlert('Prompts exported successfully!', 'success');
}

// Keyboard shortcuts
function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + R: Refresh status
        if ((e.ctrlKey || e.metaKey) && e.key === 'r' && !e.shiftKey) {
            e.preventDefault();
            updateWorkflowStatus();
            showAlert('Status refreshed', 'info');
        }

        // Ctrl/Cmd + E: Export
        if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
            e.preventDefault();
            exportDesignPrompts();
        }

        // Escape: Close modals
        if (e.key === 'Escape') {
            const openModals = document.querySelectorAll('.modal.show');
            openModals.forEach(modal => {
                const modalInstance = bootstrap.Modal.getInstance(modal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            });
        }
    });
}

// Auto-refresh functionality
let autoRefreshInterval;
function startAutoRefresh(intervalMs = 30000) { // 30 seconds
    if (autoRefreshInterval) {
        clearInterval(autoRefreshInterval);
    }

    autoRefreshInterval = setInterval(() => {
        updateWorkflowStatus();
    }, intervalMs);
}

function stopAutoRefresh() {
    if (autoRefreshInterval) {
        clearInterval(autoRefreshInterval);
        autoRefreshInterval = null;
    }
}

// Theme handling
function initializeTheme() {
    const theme = localStorage.getItem('dashboard-theme') || 'light';
    document.documentElement.setAttribute('data-theme', theme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('dashboard-theme', newTheme);
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    initializeDragAndDrop();
    initializeKeyboardShortcuts();

    // Start auto-refresh if on dashboard page
    if (window.location.pathname === '/' || window.location.pathname === '/dashboard') {
        startAutoRefresh();
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle page visibility change
    document.addEventListener('visibilitychange', function() {
        if (document.hidden) {
            stopAutoRefresh();
        } else {
            if (window.location.pathname === '/' || window.location.pathname === '/dashboard') {
                startAutoRefresh();
                updateWorkflowStatus();
            }
        }
    });

    console.log('EtsyAnalyzer Workflow Dashboard initialized');
});

// Clean up when page unloads
window.addEventListener('beforeunload', function() {
    stopAutoRefresh();
});