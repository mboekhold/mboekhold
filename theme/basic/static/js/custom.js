function openInNewTab(url) {
  var win = window.open(url, '_blank');
  win.focus();
}

window.addEventListener('resize', function() {
  if (window.innerWidth > 768) {
    document.getElementById('mobile-nav-menu').style.display = 'none';
    document.getElementById('nav-menu').style.display = 'flex';
  } else {
    document.getElementById('nav-menu').style.display = 'none';
    document.getElementById('mobile-nav-menu').style.display = 'block';
  }
});