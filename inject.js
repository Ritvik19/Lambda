// this is the code which will be injected into a given page...

(function() {

	// just place a div at top right
	var div = document.createElement('div');
	div.style.position = 'fixed';
	div.style.top = 0;
	div.style.right = 0;
	div.textContent = 'Access Obtained!';
	document.body.appendChild(div);

	var css_ = window.prompt('Enter the css selector for the elements to be scrapped')
	var att_ = window.prompt('Enter the attribute to be scrapped', 'text')
	var elems = document.querySelectorAll(css_)
	for(var i=0; i<elems.length; i++)
	{
			if(att_ == 'text')
				console.log(elems[i].innerHTML)
			else
				console.log(elems[i].getAttribute(att_))
	}
})();
