// this is the code which will be injected into a given page...

(function() {

	// just place a div at top right
	var div = document.createElement('div');
	div.style.position = 'fixed';
	div.style.top = 0;
	div.style.right = 0;
	div.innerHTML = '<h1>Access Obtained!</h1>';
	div.style.border = "1px solid #000000";
	div.style.boxShadow = "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)";
	div.style.height = "200px";
	div.style.width = "500px";
	div.style.backgroundColor = "white";
	div.style.overflowY = "scroll";
	div.style.overflowX = "scroll";
	div.style.textAlign = "center";
	div.style.fontFamily = "Courier New, monospace"
	div.style.zIndex = "100000";
	document.body.appendChild(div);
	div.innerHTML += '<table style="width:90%; margin:5%;" border="1"><tr><td>Iteration</td><td>Data</td></tr></table>'
	table = div.lastChild
	table.style.border = "1px solid #000000";
	var css_ = window.prompt('Enter the css selector for the elements to be scrapped')
	var att_ = window.prompt('Enter the attribute to be scrapped', 'text')
	var elems = document.querySelectorAll(css_)

	for(var i=0; i<elems.length; i++)
	{
			if(att_ == 'text')
				table.innerHTML += '<tr><td>'+i+'</td><td>'+elems[i].innerHTML+'</td></tr>'
			else
				table.innerHTML += '<tr><td>'+i+'</td><td>'+elems[i].getAttribute(att_)+'</td></tr>'
	}
})();
