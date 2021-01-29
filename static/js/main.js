/*
	Typify by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

(function($) {

	skel.breakpoints({
		xlarge:	'(max-width: 1680px)',
		large:	'(max-width: 1280px)',
		medium:	'(max-width: 980px)',
		small:	'(max-width: 736px)',
		xsmall:	'(max-width: 480px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

	});

var wrapper_div = document.getElementById('input_set');
var btn = document.getElementById('btn');

btn.addEventListener('click', function() {
  var n = document.getElementById("no_of_fields").value;
  var fieldset = document.createElement('div'),
    newInput;
  for (var k = 0; k < n; k++) {

    newInput = document.createElement('input');
    newInput.value = '';
    newInput.type = 'text';
    newInput.placeholder = "Textfield no. " + k;
    fieldset.appendChild(newInput);
    fieldset.appendChild(document.createElement('br'));
  }

  wrapper_div.insertBefore(fieldset, this);

}, false);

})(jQuery);