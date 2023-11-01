// JavaScript script that fetches and prints how to say “Hello” depending on the language
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
// You script must work when it is imported from the HEAD tag

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      const langCode = $('INPUT#language_code').val();
      $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (response) {
        $('DIV#hello').text(response.hello);
      });
    }
  });
});
