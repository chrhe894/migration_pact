// Auto-resize <object> elements containing SVGs to match their intrinsic aspect ratio
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('object[type="image/svg+xml"]').forEach(function (obj) {
    obj.addEventListener('load', function () {
      try {
        var svg = obj.contentDocument.querySelector('svg');
        if (!svg) return;
        var vb = svg.getAttribute('viewBox');
        if (!vb) return;
        var parts = vb.split(/[\s,]+/);
        var w = parseFloat(parts[2]);
        var h = parseFloat(parts[3]);
        if (!w || !h) return;
        // Set object height based on its rendered width and SVG aspect ratio
        var ratio = h / w;
        obj.style.height = (obj.offsetWidth * ratio) + 'px';
        // Also handle window resize
        window.addEventListener('resize', function () {
          obj.style.height = (obj.offsetWidth * ratio) + 'px';
        });
      } catch (e) {
        // Cross-origin or other error — ignore
      }
    });
  });
});
