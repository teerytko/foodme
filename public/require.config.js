(function() {
  require.config({
    baseUrl: '/static/',
    paths: {
      jquery:     'vendor/jquery/dist/jquery',
      bootstrap:  'vendor/bootstrap/dist/js/bootstrap',
      },
    shim: {
      bootstrap: ['jquery'],
    }
  });
}).call(this);
