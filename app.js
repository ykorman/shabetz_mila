(function() {
	$("#loginBtn").click(function() {
		username = $("#username").val();
		password = $("#password").val();
		$.post("shabetz_mila/login",
			{ username: username, password: password },
			function(response) {
			//alert("Data loaded: " + data); 
				if (response == "success")
					$.mobile.changePage($("#main"));
				else
					$("#loginError").popup("open");					
			});
	});
})();
