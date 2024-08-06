function toggleDetail(projectId) {
    var detail = document.getElementById(projectId);
    if (detail.style.display === 'block') {
        detail.style.display = 'none';
    } else {
        detail.style.display = 'block';
    }
}
