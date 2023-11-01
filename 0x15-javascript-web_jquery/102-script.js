// JavaScript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
